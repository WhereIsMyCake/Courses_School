# Learning at School

这是使用 MkDocs 和 Material 主题构建的 ZJU 课程笔记。

👉[网站](https://whereismycake.github.io/Courses_School/)

👉[仓库](https://github.com/WhereIsMyCake/Courses_School/)

## 项目结构

```text
mkdocs.yml                 全站配置、网址和课程导航
requirements.txt           固定版本的 Python 构建依赖
docs/
  index.md                 首页文字及封面结构
  ZJUcourse/               课程 Markdown、配图和 PDF
  stylesheets/extra.css    字体、封面、提示框等自定义样式
  stylesheets/backgroundXJ.jpg
  javascripts/
    mathjax.js             MathJax 配置
    cover-typewriter.js    首页逐字打印动画
  assets/vendor/           随站点发布的 MathJax 和字体
scripts/
  asset_versions.py        构建时为自定义 CSS / JS 自动添加内容版本号
  check_rendering.py       源文件、生成 HTML、目录检查
  check_rendering_browser.cjs
                           可选的逐页浏览器检查
```

## 安装与本地预览

建议使用 Python 3.12；当前构建依赖版本固定在 `requirements.txt`。在项目根目录执行以下 PowerShell 命令：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m mkdocs serve
```

打开 http://127.0.0.1:8000/，保存 Markdown 后预览会自动刷新。上述命令直接调用虚拟环境里的 Python，无需激活脚本或修改 PowerShell 执行策略。

macOS / Linux 将 `.\.venv\Scripts\python.exe` 换成 `.venv/bin/python`。如果已经在现有 Python 环境中安装了依赖，也可以直接使用 `python -m mkdocs serve`。

只构建、不启动预览：

```powershell
.\.venv\Scripts\python.exe -m mkdocs build
```

输出到 `site/`，可随时重新生成。请通过本地服务器预览，避免直接双击生成的 HTML，以免目录网址、搜索和资源加载行为不同。

## 配置和资源来源

主要配置均在 `mkdocs.yml`：

| 配置 | 用途 |
| --- | --- |
| `site_url` | 公开网站的完整网址，包含 `/Courses_School/` 项目路径；影响链接、站点地图和 404 页资源地址 |
| `nav` | 网站课程菜单；新增页面后，按需在这里添加导航项 |
| `theme.features` | 顶部课程标签、搜索、返回顶部和底部翻页等功能 |
| `theme.font: false` | 关闭主题自动请求 Google Fonts，改用项目内字体 |
| `markdown_extensions` | 提示框、折叠框、代码块、数学公式和目录支持 |
| `extra_css` | 加载 `docs/stylesheets/extra.css` |
| `extra_javascript` | 首页动画、MathJax 配置、MathJax 主脚本；MathJax 配置必须放在主脚本之前 |

网站运行所需的脚本、字体、图片和 PDF 均随站点发布。MathJax 和字体不需要访问 unpkg、Google Fonts 或 jsDelivr，也无需自动切换国内外 CDN。

| 本地资源 | 固定版本及来源 | 约占空间 |
| --- | --- | ---: |
| MathJax | [`mathjax@3.2.2`](https://registry.npmjs.org/mathjax/-/mathjax-3.2.2.tgz) | 7.3 MB |
| 霞鹜文楷屏幕阅读版 | [`lxgw-wenkai-screen-webfont@1.1.0`](https://registry.npmjs.org/lxgw-wenkai-screen-webfont/-/lxgw-wenkai-screen-webfont-1.1.0.tgz) | 4.6 MB |
| JetBrains Mono，400 正常字重 | [`@fontsource/jetbrains-mono@5.3.0`](https://registry.npmjs.org/@fontsource/jetbrains-mono/-/jetbrains-mono-5.3.0.tgz) | 0.1 MB |

字体按页面用到的字符分片加载；MathJax 扩展、数学字体和辅助功能资源按需加载，不会在每页一次下载上表全部文件。下载包已校验 npm 的 SHA-512 完整性；各资源目录内保留了版本、来源、许可证和 `SHA256SUMS.json`。这些第三方说明及许可证需要保留。

更新资源时，在 `docs/assets/vendor/` 中放入新版本，保留依赖目录结构和许可证，并同步修改配置或 CSS 中的版本路径。无需安装 npm 包来构建本项目。

## 页面样式和书写约定

- 每篇笔记保留一个 `#` 页面标题，下面用 `##`、`###` 分节。提示框内的“待补充”写普通文字，避免写成 `#待补充`，否则会被识别成一级标题并截断右侧目录。
- 段落与列表、表格、独立图片之间留一个空行；列表子项和提示框内容使用四个空格缩进。图片和说明分段，避免文字与图片底部对齐。
- 图片使用相对路径，如 `![图](image.png)`，不要写成站点根路径 `/image.png`。本项目默认使用目录网址，HTML iframe 的相对路径应以生成页面的位置为准，例如气候学复习页使用 `../notes.pdf`。
- 行内公式使用 `$x^2$` 或 `\(x^2\)`；显示公式使用独立的 `$$`，前后各留空行。`\[...\]` 也需要段落边界。

多行公式要使用数学环境，单写 `\\` 在 CommonHTML 中可能不会换行：

```markdown
$$
\begin{gathered}
a = b + c \\
d = e + f
\end{gathered}
$$
```

提示框沿用 Material 的类型，例如 `note`、`tip`、`warning`、`example`、`abstract`、`question`：

```markdown
!!! warning "易错点"

    普通的带标题提示框。

!!! abstract icon-only

    没有标题文字，但保留原生图标和顶部色条。

!!! tip ""

    标题栏和图标都不显示，仅保留内容框。

??? note "展开查看补充"

    默认折叠；使用 ???+ 可以默认展开。
```

`icon-only` 是项目在 `extra.css` 中定义的样式，不是 Material 的内置类型。不要用 `" "` 空格标题代替它，空白标题可能使图标和色条高度错位。

首页内容在 `docs/index.md`；打印动画由 `cover-typewriter.js` 控制，先标题后副标题，刷新或返回首页会重播。脚本中的 85 / 45 毫秒控制两行的打印间隔。用户选择减少动画时直接显示完整文字，禁用 JavaScript 时也保留文字。

`extra.css` 还控制右侧目录悬停显示、窄屏公式滚动，以及页脚“上一页／下一页”文字隐藏；页面名称、箭头和翻页链接保留。

## 线上与本地样式不一致时

GitHub Pages 的静态文件有浏览器缓存。新的 HTML / JavaScript 如果配上旧的 `extra.css`，可能出现封面文字重复、打印动画不显示、页脚方向文字仍在、`icon-only` 显示 `Abstract` / `Tip` 等现象。

`mkdocs.yml` 已注册 `scripts/asset_versions.py` 构建钩子，为自定义样式及脚本生成类似 `extra.css?v=内容哈希` 的加载地址。文件内容变化时，地址自动变化；普通构建和 `gh-deploy` 都会生效，无需手动改版本号，也不改变发布方式。已固定版本目录的字体和 MathJax 不受影响。

封面脚本还会确认配套样式已加载；缺少新样式时直接显示一份完整文字，避免生成重复文字。首次发布这项改动后，可以按 `Ctrl+F5` 强制刷新一次，确保浏览器连 HTML 也重新获取。

## 推送源码与发布网站

当前沿用 **`master` 保存源码，`gh-pages` 保存生成网页** 的方式。本地仓库没有自动发布工作流，所以只执行 `git push` 会更新源码，**不会自动把最新 Markdown 构建成公开网站**。

在确认本地预览和检查结果后：

```powershell
git add .
git commit -m "Update course notes"
git push origin master
.\.venv\Scripts\python.exe -m mkdocs gh-deploy
```

最后一条命令会构建当前文档并推送生成网页到 `gh-pages`，无需手动切换分支或复制 `site/`。GitHub Pages 应在仓库的 **Settings → Pages** 中使用 **Deploy from a branch → gh-pages → /(root)**。不要手工编辑 `gh-pages` 中的生成文件，下次发布会覆盖它们。[MkDocs 发布说明](https://www.mkdocs.org/user-guide/deploying-your-docs/#project-pages)

源码分支无需提交 `site/`，也不要提交 `.venv/`、`.tmp/` 或检查截图。它们已加入 `.gitignore`。如果以后希望只推送源码就自动发布，需要另外配置自动构建；本次整理没有更改发布方式。
