MathJax 3.2.2 - vendored browser runtime

Upstream: https://github.com/mathjax/MathJax
Documentation: https://docs.mathjax.org/en/v3.2/web/hosting.html
Source archive: https://registry.npmjs.org/mathjax/-/mathjax-3.2.2.tgz
Archive integrity (verified before extracting):
sha512-Bt+SSVU8eBG27zChVewOicYs7Xsdt40qm4+UpHyX7k0/O9NliPc+x77k1/FEsPsjKPZGJvtRZM1vO+geW0OhGw==

The upstream files have not been modified. See LICENSE for licensing,
package.json for the exact upstream package version, and SHA256SUMS.json
for SHA-256 checksums of all copied upstream files.

Selected paths from the upstream package:
  es5/tex-mml-chtml.js
  es5/input/tex/
  es5/input/mml/
  es5/output/chtml/fonts/
  es5/ui/
  es5/a11y/
  es5/sre/
  LICENSE
  package.json

The es5 directory contents are placed directly in this directory.
Other combined bundles, SVG output, development files and source maps
are not needed for the current site and are not included.

Keep the relative directory structure: MathJax locates its extensions,
CommonHTML web fonts, menus and accessibility resources relative to its
main script. Accessibility speech maps account for about 4 MB and are
loaded only when needed, rather than on every page visit.

MkDocs copies these assets into the generated site automatically.
No npm installation or external MathJax CDN is needed at build time
or by visitors. The original MathJax configuration is loaded first via
docs/javascripts/mathjax.js, followed by this pinned main script.

To upgrade: obtain an exact upstream version, verify the npm integrity,
copy the same runtime paths into a new version directory, regenerate
checksums, update mkdocs.yml, and verify nested-page resource paths.
