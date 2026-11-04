(() => {
  const originalTexts = new WeakMap();
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const segmenter = typeof Intl.Segmenter === "function"
    ? new Intl.Segmenter(undefined, { granularity: "grapheme" })
    : null;
  const pause = (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));
  let playback = 0;

  async function playCover() {
    const currentPlayback = ++playback;
    const cover = document.querySelector(".hero-content");
    if (!cover) return;

    const lines = Array.from(cover.querySelectorAll("[data-typewriter]"));
    const characters = lines.map((line) => {
      if (!originalTexts.has(line)) originalTexts.set(line, line.textContent);
      const text = originalTexts.get(line);
      line.textContent = text;
      if (reducedMotion.matches) return [];

      // Keep a complete accessible sentence, rather than announcing each letter.
      const accessible = document.createElement("span");
      accessible.className = "hero-typewriter-accessible";
      accessible.textContent = text;
      const visual = document.createElement("span");
      visual.setAttribute("aria-hidden", "true");
      const graphemes = segmenter
        ? Array.from(segmenter.segment(text), (entry) => entry.segment)
        : Array.from(text);
      const glyphs = graphemes.map((character) => {
        const glyph = document.createElement("span");
        glyph.className = "hero-typewriter-char";
        glyph.textContent = character;
        visual.appendChild(glyph);
        return glyph;
      });
      // Hidden characters still occupy their final positions, preventing jumps.
      line.replaceChildren(accessible, visual);
      return glyphs;
    });
    if (reducedMotion.matches) return;

    if (document.fonts) await document.fonts.ready;
    await pause(550);
    const isCurrent = () => currentPlayback === playback && cover.isConnected;
    for (const [lineIndex, glyphs] of characters.entries()) {
      if (!isCurrent()) return;
      let previous;
      for (const glyph of glyphs) {
        if (!isCurrent()) return;
        if (previous) previous.classList.remove("is-current");
        glyph.classList.add("is-revealed", "is-current");
        previous = glyph;
        await pause(lineIndex === 0 ? 180 : 120);
      }
      if (!isCurrent()) return;
      if (previous) previous.classList.remove("is-current");
      await pause(300);
    }
  }

  // Material's document$ also supports returning home with instant navigation.
  if (typeof document$ !== "undefined") {
    document$.subscribe(playCover);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", playCover, { once: true });
  } else {
    playCover();
  }
  window.addEventListener("pageshow", (event) => {
    if (event.persisted) playCover();
  });
  reducedMotion.addEventListener("change", playCover);
})();
