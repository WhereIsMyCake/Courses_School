"""Give mutable custom assets content-based URLs to avoid mixed cached releases."""

from hashlib import sha256
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


CUSTOM_ASSETS = {
    "stylesheets/extra.css",
    "javascripts/cover-typewriter.js",
    "javascripts/mathjax.js",
}


def on_config(config):
    def versioned(url):
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or parts.path not in CUSTOM_ASSETS:
            return url
        source = Path(config["docs_dir"]) / parts.path
        digest = sha256(source.read_bytes()).hexdigest()[:12]
        query = [(key, value) for key, value in parse_qsl(parts.query, keep_blank_values=True) if key != "v"]
        query.append(("v", digest))
        return urlunsplit(parts._replace(query=urlencode(query)))

    config["extra_css"] = [versioned(url) for url in config["extra_css"]]
    scripts = []
    for script in config["extra_javascript"]:
        if isinstance(script, str):
            scripts.append(versioned(script))
        else:
            script.path = versioned(script.path)
            scripts.append(script)
    config["extra_javascript"] = scripts
    return config
