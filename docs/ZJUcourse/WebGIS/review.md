# GIS 应用开发


## 1 绪论

### 1.1 Web 开发基础知识

#### Web 开发的概念

构建网站的主要非设计方面

#### Web 开发的发展阶段

1. 静态 web 页面

2. CGI
    - C / C++

3. ASP / JSP / PHP
    - 脚本语言

4. MVC
    - 分层：模型-视图-控制器

#### Browser / Server 结构

改进 Client / Server 结构，把客户端改成浏览器，开发和维护更简单，只要专注于服务器。

#### HTTP 协议

B / S 结构下的请求与响应需要遵循一定的协议，如超文本传输协议 HTTP 。

- **HTTP 的基本性质**：简单的、可扩展的、无状态而有会话的。

- HTTP 需要一个可靠的传输层协议，一般是 TCP 。

- **HTTP 会话的建立**：客户端建立连接 $\to$ 客户端发送请求并等待应答 $\to$ 服务器处理请求并送回应答
    - 以 TCP 连接为例，浏览器和服务器有三次握手
    - 服务器送回应答的内容格式为：
        - 状态行，包括 HTTP 协议版本、状态码、状态描述
        - HTTP首部，提供关于客户端发送数据的信息
        - 可选数据块，包含响应数据

- **HTTP 请求方法**：`GET`获取数据、`POST`提交数据、`PUT`创建/替换数据、`DELETE`删除数据。

- **HTTP 请求的内容**：统一称为资源，采用 URI 统一资源标识符进行标识。
    - URL 统一资源定位符（web 地址）：指定 web 资源位置
    - URN 统一资源名称：特定命名空间的唯一名称

### 1.2 WebGIS 介绍

#### WebGIS 定义

采用了 Web 技术的 GIS ，核心是在满足 HTTP 和 TCP/IP 标准的 Internet 应用体系中实现 Internet 环境下地理信息的有效管理与处理。

- 特点：
    - 空间数据与空间数据库
    - 数据量更大，结构更复杂
    - 数据展示要考虑坐标系、空间分析等

- 组成：
    - 客户端
        - web 浏览器客户端、桌面应用程序客户端、移动客户端
    - WebGIS 服务器
    - GIS 数据库

- 优点：
    - 传播广泛
    - 用户众多
    - 较好的跨平台性
    - 平均费用低廉
    - 易用性
    - 统一性
    - 应用广泛

#### 空间数据的存储与管理

1. 文件+关系数据库：空间几何属性与属性数据各自独立，使用特定内部标识连接。

2. 全关系型空间数据库：图形和属性数据用现有的一个关系数据库管理。

3. 对象-关系数据库：在关系数据库基础上，预定义空间数据对象的数据结构和 API 函数，直接存储和管理空间数据。

4. NoSQL 数据库：不同于关系数据库的管理系统。

### 1.3 云 GIS

#### 云计算的概念

基于互联网的计算方式

- 随需应变自助服务
- 随时随地用任何网络设备访问
- 资源池化
- 弹性使用
- 可度量服务

#### 云计算的服务模式

- IaaS 基础设施即服务

- PaaS 平台即服务

- SaaS 软件即服务

#### 云原生

一套指导软件架构设计的思想和技术，充分发挥云的能力。

#### 云 GIS

基于云计算扩展 GIS 的基本功能，实现海量空间数据的高性能存取与处理操作。

## 2 HTML 与 CSS

### 2.1 前端开发概述

#### 网页

构成网站的基本元素，通常是包含 HTML 标签的纯文本文件，通过浏览器解析、渲染。

#### HTML

HTML 超文本标记语言是一种描述网页的标记语言，但不是编程语言。

#### 浏览器

浏览器是网页运行、显示的平台，内核负责对网页语法进行解释并渲染。

#### Web 标准

由 W3C 组织和其他标准化组织制定的一系列标准的集合称为 Web 标准，统一了网页编写的标准，让不同浏览器的解析结果一致。

#### 网页的组成

- 结构 HTML ：描述页面结构组成

- 表现 CSS ：设置页面元素的样式

- 行为 JavaScript ：实现页面与用户的交互

### 2.2 HTML 介绍

#### 基本语法

HTML 标签由 `<>` 包裹，一般是成对的双标签，少数为单标签；标签之间有包含关系和并列关系。

HTML 标签可以设置属性，设置在双标签的开始标签或单标签中，之间以空格隔开。

#### 基本结构

```html
<!DOCTYPE html>
<html>

<head>
</head>

<body>
</body>

</html>
```

- `<html></html>` 页面根元素

- `<head></head>` 包含文档元数据与标题等信息

- `<body></body>` 包含可见的页面内容

#### 常用标签

- `<html></html>` 页面的根标签，包含页面的所有内容

    - `<head></head>` 定义关于文档的信息

        - `<title></title>` 设置网页标题

    - `<body></body>` 设置网页主体，是页面可见部分
        - `<h1></h1>` ~ `<h6></h6>` 正文标题，独占一行
        - `<p></p>` 表示一个段落，会自动换行，段落间有空隙 
        - `<br/>` 开始新的一行，但不会留空隙
        - `<img src="">` 定义图像
            - 必须填 `src` 属性设置图像来源
            - `alt` 属性可以设置图片加载失败时的文字
        - `<a></a>` 超链接
            - `href` 属性设置跳转目标
            - `target` 属性设置新页面打开方式，默认 `_self` 当前窗口，`_blank` 新窗口
        - `<ul></ul>` 无序列表， `<ol></ol>` 有序列表
            - 只能嵌套 `<li></li>` ，定义列表项
        - `<table></table>` 表格
            - `<tr></tr>` 定义表格行
                - `<td></td>` 定义表格数据
                - `<th></th>` 定义表格的表头单元格，加粗
        - `<form></form>` 表单，用于收集用户输入信息
            - `method` 设置表单提交时 HTML 方法为 `POST` 或 `GET`
            - `action` 指定表单提交的目标 URL
            - `name` 定义控件对应的变量名
            - `value` 存储控件当前的值
            - `required` 将当前控件标记为必填项
            - `<textarea></textarea>` 文本域控件
            - `<select></select>` 下拉列表控件
                - `<option></option>` 设置下拉列表的一个选项
            - `<input/>` 输入表单控件
                - `type` 设置控件类型，如按钮 `button` 、单选框 `radio` 、密码 `password` 、范围 `range` 、颜色 `color` 、文件 `file` 等
            - `<label></label>` 表单域中的提示信息
                - `for` 填入该标签所描述的表单控件的 `name` ，将两者相连
        - `<div></div>` 作为容器，块级元素，会以新行开始
            - `id` 或 `class` 进行标识
        - `<span></span>` 作为容器，内联元素，不会以新行开始
            - `id` 或 `class` 进行标识

#### 注释与特殊字符

- `<!---->`注释，但不能嵌套注释

- 特殊字符用代码替换，如：
    - `&lt` 小于
    - `&gt` 大于
    - `&nbsp` 空格

### 2.3 CSS 介绍

#### css 基本语法

css 是一种标记语言，由一个个样式组成，每个样式包括选择器和样式声明块。

用 `/* */` 注释。

- 行内样式：写在标签的 `style` 属性中
    - 例如 `<p style="color: red; font-size: 10px;"></p>`
- 内部样式：写在 HTML 文件的 `<style></style>` 标签中
- 外部样式：写在专门的 css 文件中，在 HTML 中通过 `<link>` 标签引入
    - `<link rel="stylesheet" type="css" href="index.css">`

#### css 基础选择器

- `*` 通配符选择器，用于页面中所有元素
    - `*{}`

- 标签/元素选择器：选中页面中某一类标签
    - 例如 `p{}`

- 类选择器：选中具有相同 `class` 属性的元素
    - 例如 `.classA{}`

- ID 选择器：选中一个元素（ID 唯一）
    - 例如 `#idA{}`

- 并集选择器：选择多组元素，多个选择器之间用 `,` 分隔
    - 例如 `p, .classA{}`

- 后代选择器：选中祖先的某个后代元素，选择器间用空格分隔
    - 例如 `select .items{}`

- 子元素选择器：选中父元素的直接子元素，选择器间用 `>` 分隔
    - 例如 `div > .titles{}`

- 伪类选择器：给某些选择器添加特殊效果，用 `:` 表示
    - 例如 `idA:hover{}`

#### 字体与文本相关属性

- 字体
    - （必需）`font-size` 指定大小

    - （必需）`font-family` 指定类型

    - `font-weight` 指定粗细

    - `font-style` 指定是否斜体

- 文本

    - `color` 颜色

    - `text-align` 元素内文本的对齐方式

    - `text-decoration` 修饰，如下划线、删除线等

    - `text-indent` 首行的缩进

    - `line-height` 行高


#### 元素背景相关属性

- `background-color` 背景颜色，默认透明

- `background-image` 背景图片，默认无，可用 `url()` 指定

- `background-size` 单位背景图片的尺寸

- `background-repeat` 背景图片重复方式

- `background-position` 背景图片位置

- `background-attachment` 背景图片是否随页面滚动



#### 元素显示模式与盒模型

根据元素显示方式不同，分为块元素、行内元素、行内块元素，可以通过 `display` 属性更改显示。

用 css 布局页面时，可以认为每个元素包含在一个盒子里：

- 盒子内容 content
    - `height` 和 `width` 设置内容区大小（仅用于块元素）

- 内边距 padding
    - `padding` 设置上、下、左、右的内边距/上、左右、下/上下、左右
    - `padding-top` 和 `padding-right` 和 `padding-bottom` 和 `padding-left` 分别设置 

- 边框 border
    - `border-width` 边框粗细
    - `border-style` 边框样式
    - `border-color` 边框颜色
    - `border-radius` 边框圆角

- 外边距 margin
    - `margin` 设置盒子边框与周围元素的距离，可以为负

#### 浮动与定位

网页布局方式有标准流、浮动和定位。

- `float` 设置浮动，默认不浮动

需要某个盒子固定在网页上特定位置，可以使用定位布局，包括

- 定位模式 `position` 属性
    - 静态定位 static 按标准流摆放，不偏移
    - 相对定位 relative 相对标准流位置偏移
    - 绝对定位 absolute 相对于离它最近的有定位的祖先元素进行定位
    - 固定定位 fixed 以浏览器的可视窗口为参照偏移
- 偏移量

#### css 三大特性

- 层叠性：相同选择器的设置，后写的覆盖前写的

- 继承性：子元素继承父元素的某些样式

- 优先级：行内样式 > ID 选择器 > 类选择器 > 元素选择器 > 通配选择器

## 3 JavaScript

### 3.1 概述

JavaScript 是一种运行在客户端的脚本语言，完整的实现由 ECMAScript 、DOM 文档对象模型、BOM 浏览器对象模型组成。

#### 基本特性

- 解释性语言
- 动态语言
- 基于原型的面向对象语言

#### 编写位置

- 行内
- 内嵌：包裹在 `<script></script>` 标签中
- 外部：`<script src="index.js"></script>`

#### 注释与输出

- `//` 单行注释，`/* */` 多行注释

输出方式有：

 - 控制台输出 `console.log()`
 - 浏览器提示框输出 `alert()`
 - 页面输出 `document.write()`

### 3.2 基本语法

#### 变量

- `let` 或 `var` 声明变量
- 变量名由字母、数组、下划线、美元符号组成，区分大小写，不能以数字开头
- `const` 声明常量，定义后不能修改

#### 数据类型

- 基本数据类型
    - 字符串
    - 数字
    - 布尔
    - 空值
    - 未定义
    - 任意精度的整数
    - symbol

- 此外都是引用数据类型，即对象 object

使用 `typeof` 操作符可以检查一个变量的数据类型。

使用 `instanceof` 操作符可以判断一个对象是否是某个特定类的实例。

#### 运算符/操作符

- 算数运算符
    - `+`
        - 也可以做字符串拼接
    - `-`
    - `*`
    - `/`
    - `%`
    - `++`
    - `--`

- 逻辑运算符：进行布尔值运算
    - `&&`
    - `||`
    - `!`

- 赋值运算符
    - `=`
    - `+=`
    - `-=`
    - `*=`
    - `/=`
    - `%=`

- 关系运算符：返回布尔值结果
    - `>`
    - `<`
    - `>=`
    - `<=`
    - `==` 可以根据一定规则进行类型转换
    - `!=` 不等
    - `===` 全等，不进行类型转换而直接比较
    - `!==` 不全等

- 条件运算符 `?:`

- 逗号运算符 `,`


### 3.3 面向对象

#### JavaScript 对象

可以分为：

- 内建对象：ES 标准定义
- 宿主对象：JS 运行环境提供，如 DOM 、BOM
- 自定义对象：开发人员自己创建


创建对象：

 - 用 `new` 关键字调用 `Object()` 构造函数
    - `var student = new Object(); student.name = 'x';`

 - 用对象字面量
    - `var student = {name: 'x'}`

删除对象属性：`delete student.name;`

#### 保存

JS 运行时，变量和基本类型保存到栈内存，对象保存到堆内存。

- 声明变量实际上是在栈内存中创建了一个空间来保存它
- 引用类型在堆内存中保存，变量里是对象在堆内存中的地址

#### JavaScript 函数

JS 中的函数也是一种对象，保存在堆内存中。

#### JavaScript 类

类是用于创建对象的蓝图，定义一类对象的属性和方法。

- `new` 可以创建类的实例，即对象。
- `extends` 可以创建子类，它能继承父类的属性和方法。
    - 子类定义中，可以用 `super` 调用父类方法。

#### JavaScript 数组

一种特殊的对象，其中元素可以是任意类型。

- 用 `Array` 类构建 `var a = new Array(1,2);`
    - 参数只有一个时表示数组长度
- 用字面量构建 `var a = [1, 2];`

#### JavaScript 常用类

- `Math`
- `Date`
- `String`

### 3.4 文档对象模型 DOM 与事件

文档指整个 HTML ，对象指每个部分转换成一个对象，使用模型表示对象之间的关系。JS 通过 DOM 来对 HTML 进行操作。

- 节点：构成网页的最基本组成部分
    - 文档节点：整个 HTML
    - 元素节点：HTML 中的各种标签
    - 文本节点：HTML 标签以外的文本内容
    - 属性节点：指标签中的一个个属性

- 事件：用户与浏览器发生的一些特定交互瞬间，帮助 HTML 和 JS 之间交互
    - 可以将元素对应事件绑定响应函数，触发事件时调用

#### DOM 操作 HTML

- 获取元素节点
    - `document.getElementById()` 通过 ID 获取一个元素节点对象
    - `document.getElementsByTagName()` 通过标签名获取一组元素节点对象
    - `document.getElementsByName()` 通过 name 属性获取一组元素节点对象

- 获取元素属性：`元素.属性名`

- 设置元素属性：`元素.属性名 = 新属性值`

- 获取和设置标签内部 HTML 代码：`innerHTML`

#### JavaScript 事件

常用的为元素绑定事件的方式：

- 通过 HTML 元素的指定事件属性
    - 例如 `<button onclick="console.log('点击确定')">确定</button>`
- 通过 DOM 对象指定的属性
- 通过事件监听器：使用 `addEventListener()` 函数监听
    - 可以为一个事件绑定多个程序

常用鼠标事件：

- `onclick` 单击
- `ondblclick` 双击
- `onmousedown` 按下
- `onmouseup` 松开
- `onmousemove` 移动
- `onmouseenter` 移到元素上

常用键盘事件：

- `onkeydown` 按下
- `onkeyup` 松开

#### 事件对象

某个事件被触发时，产生事件对象，包含所有相关信息，可以在处理程序中获取。

### 3.5 浏览器对象模型 BOM 与事件

JS 浏览器对象模型是操作浏览器的 api ，提供了很多用于访问浏览器功能的对象，使得能够通过 JS 来操作浏览器。

#### window 对象

window 对象是 BOM 的核心，表示一个浏览器的实例，是全局对象。

- 系统对话框
    - `alert()`
    - `confirm()`
    - `prompt()`

- 延时调用
    - `setTimeout()`

- 定时调用
    - `setInterval()`

#### 其他 BOM 对象

- Navigator

- History

- Location

### 3.6 异步编程

#### 异步模式

代码将不按照排列顺序执行，对于一个异步任务交由子线程执行，主线程继续执行后面的代码。

#### 常用方案

- 回调函数：将函数作为参数传递给其他函数
    - 同步的回调函数立即在主线程上执行
    - 异步的回调函数不会立即执行，而是放入回调队列以后执行

- Promise ：内置构造函数，它的实例对象用来封装一个异步操作，通过实例对象指定回调函数来获取异步结果

- async / await ：基于 Promise ，async 声明一个函数是异步的，await 等待一个 Promise 对象完成并返回结果

#### Ajax

组合了浏览器内建的 XMLHttpRequest 对象，和 JS 和 HTML DOM 。

允许通过与场景后面的 web 服务器交换数据来异步更新网络。

#### Axios

 Axios 是基于 Promise 的网络请求库。

## 4 空间数据发布与服务 

### 4.1 OGC 地图服务标准

OGC 开放地理空间信息联盟提出的一系列开放性标准被称为 OGC 标准，这些标准对接口定义、编码方式、功能描述、应用类型和实现方式进行了规范化的定义，并给出了相应的技术文档。目前已有基于 OGC 标准、涵盖地理空间信息发布、发现和连接的一整套服务接口，这些服务接口均符合 Open Web Service 的定义。

>网络服务是一种运行于 Web Server 上的程序，它们具有可以被别的程序通过互联网协议来调用的编程接口，是一种通过网络来调用资源、实现功能的方式。


#### WMS 与 WFS

WMS 与 WFS 是两个最常见的基于 OGC 标准的网络服务。

- Web Map Service 可用于对存储在服务器上的地理要素进行统一访问和渲染，例如制作地图、对数据进行非常简单的查询
    
- Web Feature Service 可用于对存储在服务器上的地理要素进行直接访问，例如查询一个数据集并检索要素、向数据集中添加或删除或更改要素

#### TMS / WMTS

Tile Map Service 瓦片地图服务是为了更高效快速的加载和渲染地图数据而设计的。如果海量的地图数据以矢量或者原始栅格图片的形式传输到客户端，在客户端渲染，不仅需要消耗大量的网络流量，而且对客户端的 CPU 和 GPU 也是很大的负荷。考虑到这些情况，TMS 将矢量和栅格数据在服务端预先渲染好，并根据比例尺分割成不同的图块，根据客户端的请求，传输这些图块，提供给客户端显示。

>所有数据发布为 TMS 服务时，需要投影到 Web-Mercator 坐标系。

### 4.2 GeoServer

GeoServer 是一个基于 Java 的服务器，允许用户查看和编辑地理空间数据。

 - 可以访问 MySQL、PostGIS、Oracle 等空间数据库并用其中的空间数据生成地图；
 - 支持 Shapefile、ArcSDE 和 MapInfo 等格式的地图数据；
支持多达上百种投影；

 - 能够将网络地图输出为多种格式(如 jpeg、gif、SVG、KML 等)，方便了不同浏览器用户对地图的查看。

### 4.3 其他开源空间数据发布与服务产品

#### OpenLayers

OpenLayers 是一个开源的 JavaScript 脚本框架，是一个专为 WebGlS 客户端开发提供的 JavaScript 类库包，可支持 WMS，GoogleMap，MSVirtualEarth 等地图来源。

#### PostgreSQL

#### PostGIS

## 5 主流前端地图框架

### 5.0

#### 基于 LBS 的地图 API

Location-based Service 基于位置的服务通常在连接互联网的场景中使用，基于 LBS 的地图 api 通过 JS 将地图嵌入到网页。

#### Charts

常用于业务页面、后台管理页面、地图非页面表达主体，有很强的图表可视化能力。

### 5.1 webGIS 架构

#### 基本架构

1. Web client 向 Web server 发送 http 请求
2. Web server 将 GIS 相关功能请求转发给 GIS server
3. GIS server 从 GIS database 中读取所需数据，对请求进行处理
4. GIS server 将结果通过 HTTP 响应返回到 client 中显示

#### 挑战

- 地理数据库需要支撑频繁数据读写的压力；
- GIS 服务器需要支撑多用户频繁访问的压力；
- Internet 需要支撑频繁传递大量数据的压力；
- 客户端（特别是 Web browser）GIS 功能的不足；
- 最终用户往往缺乏 GIS 专业知识经验。


#### webGIS 地图架构

基于 JS 的前端地图展示与交互分析的 api 库，以地图表达为中心，需要自建空间数据库与空间数据服务。

例如 Leaflet 、OpenLayers 、Mapbox 、Cesium 。

### 5.2 前端地图框架

#### 背景

- 前 HTML5 时代：Flex 、JS 、Silverlight

- HTML5 时代：JS 为主

#### Leaflet

Leaflet 是一个为建设移动设备友好的互动地图而开发的现代的、开源的 JavaScript 库，在设计时充分考虑了便捷性、高性能和可用性。

- 优点：
    - 主流投影坐标支持
    - 矢量表达
    - 全样式表达
    - 功能全面，操作友好
    - 跨平台性强
    - 考虑了移动设备的支持

- 缺点：
    - 未使用 WebGL 渲染，可视化表达方面稍有欠缺
    - 未使用硬件加速，没有发挥硬件的最大效果

#### OpenLayers

OpenLayers 也是创建交互式地图的最佳开源 JavaScript 框架之一。

- 优点：
    - 主流投影坐标系支持
    - 脚本一体化
    - 几乎是最遵循 OGC 协议的脚本
    - 兼容性好
- 缺点：
    - 许多功能有实现但是实际使用效果不理想
    - 可视化表达欠缺
    - 内存释放与优化欠缺

#### Mapbox GL JS

Mapbox GL JS 是一个 JS 库，它使用 WebGL 渲染交互式矢量瓦片地图和栅格瓦片地图。WebGL 渲染意味着高性能，MapboxGL 能够渲染大量的地图要素，拥有流畅的交互以及动画效果，可以显示立体地图并支持移动端，是用于创建高性能交互式地图的先进解决方案。

- 优点：
    - 高效矢量瓦片
    - 实现顶级的可视化渲染效果
    - 高清矢量
    - 尖端 Web 技术加持

- 缺点：
    - 空间分析能力相对欠缺
    - 三维表达相对欠缺

#### Cesium

CesiumJS 是一个开源 JS 库，用于创建具有高性能、高精度、高视觉质量和易用性的世界级 3D 地图框架。

- 可以跨平台、跨浏览器展示三维地球和地图
- 使用 WebGL 进行硬件加速，要求浏览器必须支持 WebGL

## 6 Cesium

### 6.1 核心类

#### Viewer

展示三维要素内容的主要窗口，是一个带有多种功能的可交互的三维数字地球容器，包含三维地球和一些基本控件。

主要分为 Widgets 组件、Scene 、dataSources 三部分。

```js
const viewer = new Cesium.Viewer("cesiumContainer", {

})
```

#### Widgets 组件

Viewer 初始化界面上的组件，包括时间轴、位置搜索等

#### imageryLayers

影像数据

#### terrainProvider

地形数据

#### dataSources

矢量数据

#### Entities

几何实体集合

#### Camera 

相机

#### Event

事件

#### Scene

构建场景的类，包含 primitives 图元集合，groundPrimitives 贴地图元集合，postProcessStages 场景后期处理、相机、环境对象、事件等

### 6.2 Cesium 空间坐标系统

#### 常用坐标系统

- 地理坐标系：基于 WGS84 椭球体模型，使用经度、纬度、海拔表示位置，经纬度单位默认弧度制，海拔默认米，用 `Cartographic` 类定义
    - `var cartographic = new Cesium.Cartographic(1.57, 2, 200);`

- 笛卡尔空间直角坐标系：三维空间直角坐标系，原点在椭球中心，用 `Cartesian3` 类定义
    - `var cartesian3 = new Cesium.Cartesian3(-2764128, 4787610, 3170373);`

- 屏幕坐标系：是二维的笛卡尔平面坐标系，原点为屏幕左上角
    - `var cartesian2 = new Cesium.Cartesian2(x, y);`

#### 坐标系统转换

- 角度转弧度
    - `var cartographic = Cesium.Cartographic.fromDegrees(longitude, latitude, height);`
    - `var cartographic = Cesium.Cartographic.fromRadians(Cesium.Math.toRadians(longitude), Cesium.Math.toRadians(latitude), height);` 或者 `var cartographic = new Cesium.Cartographic(Cesium.Math.toRadians(longitude), Cesium.Math.toRadians(latitude), height);`

- 弧度转角度

    ```js
    var cartographic = new Cesium.Cartegraphic(lon, lat, h);
    var lon = Cesium.Math.toDegrees(cartographic.longitude);
    var lat = Cesium.Math.toDegrees(cartographic.latitude);
    ```

- 弧度转三维笛卡尔
    - `var cartesian3 = Cesium.Cartesian3.fromRadians(lon, lat, h);`
    - `var cartesian3 = Cesium.Ellipsoid.WGS84.cartographicToCartesian(cartographic);`

- 三维笛卡尔转弧度
    - `var cartographic = Cesium.Cartographic.fromCartesian(cartesian3);`
    - `var cartographic = Cesium.Ellipsoid.WGS84.cartesianToCartographic(cartesian3);`

- 角度转三维笛卡尔
    - `var cartesian3 = Cesium.Cartesian3.fromDegrees(lon, lat, h);`
    - 转弧度，再转三维笛卡尔

- 三维笛卡尔转角度
    - 转弧度，再转角度

### 6.3 Cesium 三维空间相机

主要用于控制三维场景中相机的飞行定位，基于 Camera 和 Viewer 两类实现。

#### 常用相机方法


#### 主要相机参数

### 6.4 空间实体可视化

#### 矢量数据

用 X 、Y 、Z 坐标表示图形或实体位置，数据结构紧凑、冗余度低、有利于网络和检索分析、图形显示质量好、精度高。

cesium 直接支持的格式包括 geoJSON 、topoJSON 、KML 、CZML 。

Cesium 中的 DataSource 是定义了数据源的接口，该接口将任意数据转换为 EntityCollection 以供一般使用。DataSource 中的 entities 属性就是当前数据源解析后生成的 Entity 集合。

- 提供 GeoJsonDataSource、KmlDataSource、CzmlDataSource、 CustomDataSource 等处理对应矢量数据的类，通过这些类与 Viewer 的 dataSources 属性，在 Viewer 实例上加载各种矢量数据。
- DataSourceCollection 类是 DataSource 实例的集合，有一系列操作集合中数据源的方法，能实现添加、删除、更改、查询等。

##### Shapefile

必须包含主文件 .shp 、索引文件 .shx 、dBase 表文件 .dbf 。

**⚠️cesium 无法直接加载 shapefile 文件！**要发布成地图服务，或转其他支持格式。


##### GeoJSON

JSON 是有固定格式的字符串数据，轻量级的文本数据交换格式。

geoJSON 专门表示地理信息

 - 最外层是一个单独对象，可以表示几何体、特征、特征集合
 - 最外层可能包含很多子对象
    - 每个对象有一个 type 属性表示类型

- topoJSON 是 geoJSON 按照拓扑学编码后的扩展形式，直接使用几何体表示图形，更少冗余。

`
viewer.dataSource.add(
    Cesium.GeoJsonDataSource.load();
);
`

##### KML

KML 是一种基于 XML 语法格式的文件，用来描述和存储地理信息数据。

`
viewer.dataSource.add(
    Cesium.KmlDataSource.load();
);
`

##### CZML

一种 JSON 格式的字符串，用于描述与时间有关的动画场景。

`
viewer.dataSource.add(
    Cesium.CzmlDataSouce.load();
);
`

#### 实体数据

cesium 有用于展示空间数据的api，分为

 - 面向图形开发人员的低级 api ，称为图元 primitive api ，主要是暴露手头执行任务所需的最小抽象量，为给定的可视化类型提供最有性能和灵活性的实现
 - 用于数据驱动的可视化的高级 api ，称为实体 entity api ，目的是公开一组设计一致的高级对象，将相关可视化和信息聚合到一个统一数据结构中，使我们能专注于展示数据（实际上是对 primitive api 的二次封装）

##### 加载实体

使用DataSource向Viewer中添加矢量数据时，Cesium会将其中的数据解析为一个个实体，也可以通过Viewer类的entities属性手动加载各种实体，例如
`
viewer.entities.add({});
`

cesium 目前支持 17 种类型的实体。

##### 管理实体

- `viewer.entities.removeById('idA');`

##### 拾取实体

Cesium通过 ScreenSpaceEventHandler 类监听鼠标事件，鼠标拾取到的信息可通过以下两种方式获取

- `viewer.scene.pick`：获取窗体坐标处最顶部的实体
- `viewer.scene.drillPick`：获取窗体坐标处所有实体的集合

#### glTF 模型

Graphics Language Transmission Format图形语言传输格式，是一种针对GL(WebGL，OpenGL ES以及OpenGL)接口的运行时资产传递格式。通过提供高效、可扩展、可互操作的格式来传输和加载三维内容，填补了3D建模工具与现代图形应用程序之间的空白，成为了 Web 上的3D 对象标准。

格式有两种：

- .gltf 基于 JSON 的文本文件
- .glb 二进制格式

一个 glTF 模型可以包括三部分：

- .gltf 文件
- .bin 文件
- 图像文件

Cesium通过Entity API 或 Primitive API 加载glTF，作为一个 model 类型的实体，例如
`
viewer.entities.add({});
`

#### 3D Tiles

3D Tiles 在glTF基础上提供了多细节层次（LOD）能力，定位就是Web环境下海量三维模型数据（具备LOD能力的glTF），即3D Tiles是用于流式传输大规模异构3D地理空间数据集的开放规范。

建议使用 primitive api 加载和渲染，例如
`
Cesium.Cesium3DTileset.fromIonAssetId()
 .then((tileset)=>{
    cityTileSet = tileset;
    viewer.scene.primitives.add(cityTileSet);
 })
 .catch();
`

#### Primitive API

Primitive类与Entity类都可用于绘制同样的几何图形，但Primitive方式更接近渲染引擎底层。

primitive 通常由几何实例（可以有多个）和外观（只能有一个）组成。

##### 粒子系统

小图像的集合，通过 ParticleSystem 类创建。

#### 材质与 Property 机制

为 entity 类或 primitive 类添加的空间几何数据提供材质修改方法

- primitive：Material 类
- entity：MaterialProperty 类

Property 本身是个抽象类，可以和时间相互关联，大致归为四类：

- 基本 Property
- MaterialProperty
- PositionProperty
- 其他 Property

### 6.5 数据服务可视化与分析

#### 影像数据服务

核心的三个类：

- ImageryProvider 影像图层的数据源，本身是抽象类不能直接实例化

- ImageryLayer 用于创建影像图层

- ImageryLayerCollection 是 ImageryLayer 类对象的容器，提供对影像图层进行操作的方法

#### 地形数据

影像可以有多个，但地形只有一个，Cesium提供了TerrainProvider基类，该Provider负责每一个Tile对应的地形数据的构建，定义了一套地形Provider需要实现的接口和规范，但本身并不会参与其中的操作。

Cesium封装了5个现成的继承类操作地形数据

- ArcGISTileElevationTerrainProvider
- CesiumTerrainProvider
- EllipsoidTerrainProvider
- GoogleEarthEnterpriseTerrainProvider
- VRTheWorldTerrainProvider

#### 三维空间

- 空间量测
- 淹没分析：根据某片区域的地形及洪水流量速度，动态模拟该地形区域水位逐渐上涨的淹没过程。
    - 主要利用 polygon 的 extrudedHeight 属性实现
- 其他

## 7 Web 应用前端开发框架

### 7.1 概述

前端框架简化网页设计，封装了一些功能代码。

主流框架：react 、vue 、angular

### 7.2 react

- 操作虚拟 DOM
- 把组件视为状态机，只需更新 state
    - 组件对象有 props 属性，用来从组件外向内传递变化的数据，它不可变
    - 组件包含一系列钩子函数，在特定时刻调用

### 7.3 UI 框架

UI即用户界面，主要包含视觉（比如图像、文字、动画等可视化内容）以及交互（比如按钮点击、列表滑动、图片缩放等用户操作）。
UI框架，则是为开发UI而提供的基础设施，比如视图布局，UI组件，事件响应机制等。

## 8 Web 应用后端开发概述

### 8.1 后端

### 8.2 Python 基础

#### Numpy

#### Pandas


## 9 后端开发框架

### 9.1 概述

后端的核心是业务逻辑设计、功能实现、数据库交互，经典三层架构为

- 表现层
- 业务逻辑层
- 数据逻辑层

加上数据库，遵循高内聚低耦合的原则。

### 9.2 FastAPI

FastAPI 是一个用于构建 api 的 Python web 框架，基于标准的 Python 类型提示。

一个简易后端接口大致如下：

```py
from fastapi import FastAPI 
import uvicorn # 导入uvicorn，用于启动应用

app = FastAPI(title="WebGIS") # 创建FastAPI应用实例
@app.get("/") # 注册路由
async def root(): # 路由处理函数
    return {"message": "欢迎使用WebGIS"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) # 启动应用
```


- FastAPI使用请求体（Body）从客户端（例如浏览器）向API发送数据。
    - 通过Pydantic模型声明请求体结构，原生支持类型驱动校验、自动数据转换、文档自动生成

- 路由操作是Web开发中将不同的URL请求路径映射到特定处理函数的过程


- FastAPI 允许为函数的参数声明额外的信息和校验，常用函数包括：Query（URL查询参数）、Path(URL路径参数)、Field（Pydantic模型字段）

- 通过读取 API 的结构，Swagger等应用可以自动构建美观且交互式的文档。FastAPI基于OpenAPI标准开发，能以多种方式构建API文档，默认支持Swagger和Redoc。

## 10 几何对象与 GeoPandas

### 10.1 几何对象与几何数据

#### Shapely

Shapely是一个遵循BSD许可协议的Python包，用于在笛卡尔平面内操作和分析平面几何对象。

GeoPandas使用shapely下的geometry模块来定义几何对象，具体包括：

- 点：Points
- 多点：MultiPoint
- 线： LineString
- 多线：MultiLineString
- 线环：LinerRing
- 多边形：Polygon （有孔/无孔）
- 多多边形：MultiPolygon
