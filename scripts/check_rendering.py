"""Build the site and check source math boundaries, rendered HTML, and TOCs.

Run: python scripts/check_rendering.py
Add --browser to typeset every Markdown page in a local Chromium browser.
Uses the site's existing Python dependencies; browser mode also needs Node 22+
and Chrome/Edge (or RENDER_BROWSER pointing to a Chromium executable).
"""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

from mkdocs.commands.build import build
from mkdocs.config import load_config


ROOT = Path(__file__).resolve().parents[1]
RAW_TEX = re.compile(r"\\(?:[A-Za-z]+|[\[\]()])|\$\$")
VOID_TAGS = set("area base br col embed hr img input link meta param source track wbr".split())


def unscoped_linebreak(tex: str) -> bool:
    """CHTML needs a multiline environment to honor TeX row separators."""
    environments = []
    for token in re.finditer(r"\\(begin|end)\{([^}]+)\}|\\\\", tex):
        if token[1] == "begin":
            environments.append(token[2])
        elif token[1] == "end":
            if environments and environments[-1] == token[2]:
                environments.pop()
        elif not environments:
            return True
    return False


def check_source(path: Path) -> tuple[int, list[str]]:
    """Count intended display blocks independently of Markdown's parser."""
    lines = path.read_text(encoding="utf-8").splitlines()
    errors = []
    count = 0
    fence = None
    active = None
    prose = []
    frontmatter = bool(lines and lines[0] == "---")

    def content(line):
        return re.sub(r"^(?:\s*>[ \t]?)+", "", line).strip()

    def margins(start, end):
        if start and content(lines[start - 1]):
            errors.append(f"line {start + 1}: display math needs a blank line before it")
        if end + 1 < len(lines) and content(lines[end + 1]):
            errors.append(f"line {end + 1}: display math needs a blank line after it")

    for index, line in enumerate(lines):
        if frontmatter:
            if index and line == "---":
                frontmatter = False
            continue
        text = content(line)
        marker = re.match(r"^(`{3,}|~{3,})(.*)$", text)
        if marker:
            if fence is None:
                fence = (marker[1][0], len(marker[1]), index)
            elif marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if fence:
            continue
        if active:
            close, start = active
            if text == close:
                count += 1
                margins(start, index)
                active = None
            elif not text:
                errors.append(f"line {index + 1}: blank line inside a display math block")
            continue
        if text in ("$$", r"\["):
            active = ("$$" if text == "$$" else r"\]", index)
        elif text.startswith("$$") and text.endswith("$$") and len(text) > 4:
            count += 1
            margins(index, index)
        elif text == r"\]":
            errors.append(f"line {index + 1}: unmatched display math closing marker")
        else:
            prose.append(re.sub(r"(`+).*?\1", "", line))
    if active:
        errors.append(f"line {active[1] + 1}: unclosed display math block")
    if fence:
        errors.append(f"line {fence[2] + 1}: unclosed code fence")
    prose = "\n".join(prose)
    if len(re.findall(r"(?<!\\)\\\(", prose)) != len(re.findall(r"(?<!\\)\\\)", prose)):
        errors.append("unpaired inline \\( ... \\) delimiters")
    return count, errors


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.formulas = []
        self.raw_text = []
        self.headings = []
        self.toc_links = set()
        self.toc_present = False
        self.toc_hidden = False
        self.image_sources = []
        self.errors = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        classes = attrs.get("class", "").split()
        parent = self.stack[-1] if self.stack else {}
        article = parent.get("article", False) or (tag == "article" and "md-content__inner" in classes)
        formula = parent.get("formula")
        if article and "arithmatex" in classes:
            if formula is not None:
                self.errors.append("nested .arithmatex wrappers")
            formula = len(self.formulas)
            self.formulas.append({"display": tag == "div", "text": []})
        toc = parent.get("toc", False) or "md-sidebar--secondary" in classes
        if "md-sidebar--secondary" in classes:
            self.toc_present = True
            self.toc_hidden = "hidden" in attrs
        if toc and tag == "a" and attrs.get("href", "").startswith("#"):
            self.toc_links.add(attrs["href"][1:])
        skip = parent.get("skip", False) or tag in {"pre", "code", "script", "style"} or formula is not None
        if article and re.fullmatch(r"h[1-6]", tag):
            self.headings.append((int(tag[1]), attrs.get("id")))
        if article and tag == "img":
            self.image_sources.append(attrs.get("src", ""))
        if tag not in VOID_TAGS:
            self.stack.append({"tag": tag, "article": article, "formula": formula, "toc": toc, "skip": skip})

    def handle_startendtag(self, tag, attributes):
        self.handle_starttag(tag, attributes)
        if tag not in VOID_TAGS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index]["tag"] == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        if not self.stack:
            return
        frame = self.stack[-1]
        if frame.get("formula") is not None:
            self.formulas[frame["formula"]]["text"].append(data)
        if frame["article"] and not frame["skip"]:
            self.raw_text.append(data)


def check_html(path: Path, expected_displays: int | None = None) -> tuple[PageParser, list[str]]:
    page = PageParser()
    page.feed(path.read_text(encoding="utf-8"))
    errors = list(page.errors)
    for text in page.raw_text:
        if RAW_TEX.search(text):
            errors.append("unrendered TeX outside math/code: " + repr(text.strip()[:180]))
    displays = sum(formula["display"] for formula in page.formulas)
    if expected_displays is not None and displays != expected_displays:
        errors.append(f"source has {expected_displays} display blocks, HTML has {displays}")
    for formula in page.formulas:
        text = "".join(formula["text"]).strip()
        delimiters = (r"\[", r"\]") if formula["display"] else (r"\(", r"\)")
        if not (text.startswith(delimiters[0]) and text.endswith(delimiters[1])):
            errors.append("malformed math wrapper: " + repr(text[:120]))
        if "$" in text:
            errors.append("unconsumed dollar delimiter inside a math wrapper")
        if unscoped_linebreak(text[2:-2]):
            errors.append("math rows use \\\\ outside a multiline environment; use gathered/aligned")
    if page.toc_present and not page.toc_hidden:
        expected = {identifier for level, identifier in page.headings if level > 1 and identifier}
        if expected != page.toc_links:
            errors.append(f"TOC misses headings: {sorted(expected - page.toc_links)}; extra: {sorted(page.toc_links - expected)}")
    return page, errors


def browser_executable() -> str:
    candidates = [os.environ.get("RENDER_BROWSER", "")]
    candidates.extend([
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ])
    candidates.extend(shutil.which(name) or "" for name in ["chromium", "chromium-browser", "google-chrome"])
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    raise RuntimeError("Chrome/Edge not found; set RENDER_BROWSER to a Chromium executable")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--browser", action="store_true")
    parser.add_argument("--report", type=Path, help="Optional JSON report path")
    args = parser.parse_args()
    temporary_root = ROOT / ".tmp"
    temporary_root.mkdir(exist_ok=True)
    report = {"pages": [], "errors": []}
    with tempfile.TemporaryDirectory(prefix="render-check-", dir=temporary_root) as temporary:
        site = Path(temporary) / "site"
        config = load_config(config_file=str(ROOT / "mkdocs.yml"), site_dir=str(site))
        build(config)
        from mkdocs.structure.files import get_files

        for source in get_files(config).documentation_pages():
            if not source.src_path.endswith(".md"):
                continue
            displays, errors = check_source(Path(source.abs_src_path))
            page, html_errors = check_html(site / source.dest_path, displays)
            errors.extend(html_errors)
            item = {"source": source.src_path, "html": source.dest_path, "formulas": len(page.formulas), "display_formulas": displays, "toc_links": len(page.toc_links), "errors": errors}
            report["pages"].append(item)
            report["errors"].extend(f"{source.src_path}: {error}" for error in errors)
        report["formula_count"] = sum(item["formulas"] for item in report["pages"])
        report["display_formula_count"] = sum(item["display_formulas"] for item in report["pages"])
        if args.browser and not report["errors"]:
            node = shutil.which("node")
            if not node:
                raise RuntimeError("Browser checks need Node.js 22+ with built-in WebSocket")
            manifest = Path(temporary) / "pages.json"
            manifest.write_text(json.dumps(report["pages"]), encoding="utf-8")
            result_path = Path(temporary) / "browser.json"
            env = dict(os.environ, RENDER_BROWSER=browser_executable())
            result = subprocess.run([node, str(ROOT / "scripts/check_rendering_browser.cjs"), str(site), str(manifest), str(result_path)], env=env, cwd=ROOT)
            if result_path.is_file():
                report["browser"] = json.loads(result_path.read_text(encoding="utf-8"))
            screenshot = Path(temporary) / "markov.png"
            if args.report and screenshot.is_file():
                args.report.parent.mkdir(parents=True, exist_ok=True)
                destination = args.report.with_suffix(".png")
                shutil.copyfile(screenshot, destination)
                report["screenshot"] = str(destination)
            if result.returncode:
                report["errors"].append("Browser verification failed; see browser results")
    # Leave no empty scratch directory behind after a normal check.
    try:
        temporary_root.rmdir()
    except OSError:
        pass
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for error in report["errors"]:
        print("FAIL:", error)
    print(f"{'FAIL' if report['errors'] else 'PASS'}: {len(report['pages'])} pages, {report['formula_count']} formulas, {report['display_formula_count']} source display blocks; {len(report['errors'])} errors")
    return int(bool(report["errors"]))


if __name__ == "__main__":
    raise SystemExit(main())
