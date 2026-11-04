# 前端代码部分

>2026.6


## 一、HTML 模块

### 1.1 文档基本结构

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>网页标题</title>
    <link rel="stylesheet" href="https://sfile.chatglm.cn/workspace/file/fd/fd2a42c99d.css">
    <script src="xxx.js"></script>
</head>
<body>
    <!-- 内容 -->
</body>
</html>
```

**要点：**

- `<!DOCTYPE html>` 声明 HTML5 文档类型
- `<head>` 内放元信息：`<meta>`、`<title>`、`<link>`、`<script>`
- `<title>` 设置浏览器选项卡上显示的标题（作业1要求）
- `<meta charset="UTF-8">` 设置字符编码
- `<meta name="viewport" ...>` 设置视口，适配移动端

### 1.2 常用标签

| 标签 | 用途 | 代码示例 |
|------|------|----------|
| `<h1>` ~ `<h6>` | 标题，h1最大 h6最小 | `<h1>实时天气</h1>` |
| `<p>` | 段落 | `<p id="position">经度：120°</p>` |
| `<div>` | 块级容器（独占一行） | `<div class="panel">...</div>` |
| `<span>` | 行内容器（不换行） | `<span class="name">杭州</span>` |
| `<br>` | 换行（空标签） | `第一行<br/>第二行` |
| `<img>` | 图片（空标签） | `<img src="weather.gif" alt="加载失败" id="weather_gif">` |
| `<label>` | 标签关联表单控件 | `<label for="city">选择城市</label>` |
| `<ul>` / `<li>` | 无序列表 / 列表项 | `<ul><li>书签1</li></ul>` |
| `<form>` | 表单容器 | `<form>...</form>` |

### 1.3 表单控件标签

#### `<select>` 下拉框 + `<option>` 选项

```html
<select name="city" id="city_choice">
    <option value="hangzhou">杭州</option>
    <option value="shanghai">上海</option>
    <option value="beijing">北京</option>
</select>
```

- **`<select>`** 是下拉框容器，`<option>` 是其中的选项
- `value` 属性存储选项值，标签内文本是显示给用户的内容
- 通过 JS 获取选中值：`document.getElementById('city_choice').value`

#### `<input>` 输入框

```html
<!-- 普通文本输入 -->
<input type="text" id="bookmarkName" placeholder="请输入书签名称">

<!-- 按钮 -->
<input type="button" id="small_tools" value="生成天气小组件">

<!-- 滑块（范围选择） -->
<input type="range" id="r_slider" min="5" max="35" value="20">

<!-- 颜色选择器 -->
<input type="color" id="point_color" value="#00ffff">

<!-- 单选按钮 -->
<input type="radio" name="styleChoice" value="default" checked>默认
<input type="radio" name="styleChoice" value="highlight">高亮
```

| `type` 值 | 用途 |
|-----------|------|
| `text` | 文本输入框 |
| `button` | 按钮（`value` 为显示文字） |
| `range` | 滑块（`min`/`max`/`value`） |
| `color` | 颜色选择器 |
| `radio` | 单选按钮（同 `name` 为一组） |
| `checkbox` | 复选框 |

#### `<button>` 按钮

```html
<button id="addBookmark">创建</button>
<button id="start" title="开始"><img src="start.png"></button>
```

- `<button>` 与 `<input type="button">` 功能类似，但 `<button>` 内可放 HTML（如图片）
- `title` 属性设置鼠标悬浮提示

### 1.4 关键属性

| 属性 | 说明 | 示例 |
|------|------|------|
| `id` | 唯一标识，CSS/JS 用 `#` 选择 | `id="city_choice"` |
| `class` | 类名，CSS 用 `.` 选择，可多个 | `class="panel baseLayer"` |
| `name` | 表单元素名 / 单选按钮分组 | `name="styleChoice"` |
| `value` | 输入框/按钮/选项的值 | `value="hangzhou"` |
| `src` | 图片路径 | `src="weather.gif"` |
| `alt` | 图片加载失败时的替代文本 | `alt="图片加载失败"` |
| `placeholder` | 输入框占位提示文字 | `placeholder="请输入书签名称"` |
| `checked` | 单选/复选默认选中 | `checked` |
| `title` | 悬浮提示文字 | `title="选择底图"` |
| `for` | label 关联的控件 id | `for="city"` |

### 1.5 引入外部资源

```html
<!-- 引入 CSS -->
<link rel="stylesheet" href="https://sfile.chatglm.cn/workspace/file/fd/fd2a42c99d.css">

<!-- 引入 Cesium 的 JS 和 CSS -->
<script src="../scripts/Cesium/Cesium.js"></script>
<link rel="stylesheet" href="../scripts/Cesium/Widgets/widgets.css">

<!-- CDN 引入 Axios -->
<script src="https://cdn.bootcdn.net/ajax/libs/axios/1.3.4/axios.js"></script>

<!-- 引入自己的 JS（注意位置：body 末尾） -->
<script src="https://sfile.chatglm.cn/workspace/file/7d/7dcad60e91.js"></script>

<!-- ES6 模块引入 -->
<script type="module">
    import {baselayer} from './baselayer.js';
    baselayer(viewer);
</script>
```

**文档解析顺序：**

- JS 脚本应在 HTML 元素**之后**引入（通常放 `body` 末尾），否则 JS 执行时 DOM 尚未加载，找不到元素
- `<script>` 放在 `<head>` 中会在 DOM 解析前执行（如 Axios CDN 引入）
- `type="module"` 启用 ES6 模块语法（`import`/`export`）

### 1.6 JS 编写位置

| 位置 | 写法 | 特点 |
|------|------|------|
| 行内式 | `<input onclick="alert('hi')">` | 结构与行为耦合，不推荐 |
| 内嵌式 | `<script>alert('hi')</script>` | 写在 HTML 文件中 |
| 外部式 | `<script src="index.js"></script>` | 推荐，结构与行为分离 |

---

## 二、CSS 模块

### 2.1 选择器

#### 类选择器 `.`

```css
.panel {
    background-color: #1e1e1e;
    border-radius: 15px;
}
```

#### ID 选择器 `#`

```css
#weather_now {
    font-size: 46px;
    font-weight: 600;
}
```


#### 标签选择器

```css
body { font-family: 'JetBrains Mono', sans-serif; }
input, select, button, option { font-family: inherit; }
```

#### 后代选择器

```css
#weather_conditions p { margin: 0; }
#bookmarkList li { display: flex; }
```

#### 伪类选择器

```css
/* 鼠标悬浮 */
#small_tools:hover {
    background-color: #3b3a3a;
    color: #ffffff;
}

/* 鼠标按下 */
#small_tools:active {
    background-color: #222;
    transform: scale(0.95);
}

/* 输入框获得焦点 */
#bookmarkName:focus {
    outline: none;
    border-color: #f0f0f0;
}

/* 单选按钮被选中 */
input[type="radio"]:checked {
    filter: brightness(1);
}
```

#### 属性选择器

```css
input[type="radio"] { accent-color: #ffffff; }
```

#### 选择器组合

```css
/* 同时选多个 */
input, select, button, option { font-family: inherit; }

/* 后代 */
.bookmark-operations .fly-icon { width: 20px; }

/* 自定义类（JS 动态添加） */
.baseLayer.active { background-color: #3b3a3a; }
```

### 2.2 盒模型


#### padding（内边距）

```css
padding: 50px;           /* 四边均为50px */
padding: 10px 20px;      /* 上下10px, 左右20px */
padding: 10px 20px 30px; /* 上10, 左右20, 下30 */
padding: 10px 20px 30px 40px; /* 上 右 下 左 */
```

#### border（边框）

```css
/* 2px粗红色实线边框 */
border: 2px solid red;

/* 完整语法：border: <宽度> <样式> <颜色> */
border: 1px solid #ffffff1a;       /* 1px半透明白色实线 */
border: 1px solid #555;            /* 1px灰色实线 */
border-radius: 15px;                /* 圆角 */
```

**边框样式值：**

| 值 | 说明 |
|----|------|
| `solid` | 实线 |
| `dashed` | 虚线 |
| `dotted` | 点线 |
| `none` | 无边框 |

#### margin（外边距）

```css
margin: 0;              /* 清除默认外边距 */
margin-bottom: 10px;    /* 仅下边距 */
margin-left: auto;      /* 自动左外边距（右对齐效果） */
```

### 2.3 定位（position）

```css
/* 固定定位 — 相对浏览器视口，不随滚动移动 */
.panel {
    position: fixed;
    top: 30px;
    right: 30px;       /* 面板固定右上角，距上右边界各30px */
}

/* 绝对定位 — 相对最近的已定位祖先元素 */
#bookmarkPanel {
    position: absolute;
    top: 20px;
    left: 20px;
    z-index: 1000;     /* 层级，值越大越在上层 */
}
```

| 值 | 说明 |
|----|------|
| `static` | 默认值，正常文档流 |
| `relative` | 相对自身原位置偏移 |
| `absolute` | 脱离文档流，相对最近已定位祖先 |
| `fixed` | 固定在视口，不随滚动移动 |

- `z-index`：控制重叠元素的层叠顺序，值越大越在上层

### 2.4 Flex 布局

```css
/* 水平排列，两端对齐 */
.main_head {
    display: flex;
    justify-content: space-between;
}

/* 垂直排列 */
.menu {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
```

| 属性 | 值 | 说明 |
|------|----|------|
| `display` | `flex` | 启用弹性布局 |
| `flex-direction` | `row` / `column` | 主轴方向（水平/垂直） |
| `justify-content` | `space-between` / `center` / `flex-start` | 主轴对齐 |
| `align-items` | `center` / `flex-start` / `stretch` | 交叉轴对齐 |
| `gap` | `10px` | 子元素间距 |
| `align-self` | `center` | 单个子元素单独对齐 |

### 2.5 常用样式属性

#### 文字样式

```css
color: #d4cccc;                /* 文字颜色 */
font-size: 24px;               /* 字号 */
font-weight: 600;              /* 字重（normal/bold/数字） */
font-family: 'JetBrains Mono', sans-serif;  /* 字体 */
text-align: center;            /* 文字水平对齐 */
line-height: 1.4;              /* 行高 */
white-space: nowrap;           /* 不换行 */
```

#### 背景

```css
background-color: #1e1e1e;                    /* 纯色背景 */
background: rgba(30, 30, 30, 0.9);            /* 半透明背景 */
```

#### 阴影

```css
/* box-shadow: 水平偏移 垂直偏移 模糊半径 颜色 */
box-shadow: 0 10px 20px #00000080;
box-shadow: inset 0 2px 4px #00000080;  /* 内阴影 */
```

#### 圆角与过渡

```css
border-radius: 15px;         /* 圆角 */
transition: all 0.3s;        /* 所有属性变化0.3秒过渡 */
transform: scale(0.95);      /* 缩放（按下效果） */
cursor: pointer;             /* 鼠标变手型 */
```

#### 滤镜

```css
filter: invert(1) brightness(0.9);           /* 反色+亮度 */
filter: drop-shadow(0 0 2px #d4cccc);        /* 投影 */
backdrop-filter: blur(5px) saturate(200%);   /* 背景模糊（毛玻璃） */
```

#### 溢出处理

```css
overflow: auto;         /* 内容溢出时显示滚动条 */
overflow-y: auto;       /* 仅垂直方向溢出时滚动 */
max-height: 150px;      /* 最大高度（配合 overflow 使用） */
list-style: none;       /* 去除列表默认样式 */
```

### 2.6 清除默认样式

```css
html, body {
    margin: 0;
    padding: 0;
    height: 100%;
}
```

### 2.7 鼠标交互样式

```css
/* 默认状态 */
#small_tools {
    background-color: #3c3c3c;
    border: 1px solid #ffffff1a;
    cursor: pointer;
    transition: all 0.3s;
}

/* 悬浮状态 */
#small_tools:hover {
    background-color: #3b3a3a;
    color: #ffffff;
}

/* 按下状态 */
#small_tools:active {
    background-color: #222;
    transform: scale(0.95);
}
```

### 2.8 @import 引入外部字体

```css
@import url('https://cdn.jsdelivr.net/npm/lxgw-wenkai-screen-webfont@1.1.0/https://sfile.chatglm.cn/workspace/file/fd/fd2a42c99d.css');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono&display=swap');
```

## 三、JavaScript 基础语法


### 3.1 变量与常量

```js
var a = 1;        // ES5，函数作用域，可重复声明（不推荐）
let b = 2;        // ES6，块级作用域，不可重复声明（推荐）
const c = 3;      // ES6，常量，声明后不可修改
```

- 变量名：字母(A-Za-z)、数字(0-9)、下划线(_)、美元符号($)，**不能以数字开头**
- 建议小驼峰命名：`userFirstName`
- `typeof` 检查变量类型

### 3.2 数据类型

**7种基本数据类型：**

| 类型 | 说明 | typeof 返回值 |
|------|------|--------------|
| String | 字符串，单引号或双引号 | `'string'` |
| Number | 数字（整数+浮点数） | `'number'` |
| Boolean | `true` / `false` | `'boolean'` |
| Null | 空值，只有 `null` 一个值 | **`'object'`**（特殊） |
| Undefined | 未定义，声明未赋值 | `'undefined'` |
| BigInt | 任意精度整数（ES11） | — |
| Symbol | 唯一标识符（ES6） | — |

- 除以上7种外都叫 **Object**（引用数据类型）
- `typeof null` 返回 `'object'`（历史遗留 bug）
- `typeof` 检查函数返回 `'function'`
- `instanceof` 判断对象是否某类的实例

**特殊值：**

- `NaN`：非数值（Not a Number），`typeof NaN` 返回 `'number'`
- `isNaN()` 判断是否非数字
- `Infinity`：无穷大

### 3.3 类型转换

```js
// 字符串 → 数字
parseInt("123");     // 123
parseFloat("3.14");  // 3.14
Number("123");       // 123

// 数字 → 字符串
String(123);         // "123"
(123).toString();    // "123"

// 其他 → 布尔
Boolean(0);          // false
Boolean("");         // false
Boolean(null);       // false
Boolean(undefined);  // false
Boolean(NaN);        // false
Boolean("非空");     // true
```

### 3.4 运算符

#### 算术运算符

`+` `-` `*` `/` `%`（取模）`++`（自增）`--`（自减）

- `+` 可用于字符串拼接：任何值与字符串做 `+`，都会先转为字符串再拼接
- 任何数与 `NaN` 运算结果为 `NaN`

#### 逻辑运算符

| 运算符 | 说明 | 特点 |
|--------|------|------|
| `&&` | 逻辑与 | 找短路：左值为假则不运算右值 |
| `\|\|` | 逻辑或 | 找通路：左值为真则不运算右值 |
| `!` | 逻辑非 | 必返回布尔值，`!!x` 可转布尔 |

#### 关系运算符

| 运算符 | 说明 | 示例 |
|--------|------|------|
| `==` | 宽松相等，**会类型转换** | `'123' == 123` → `true` |
| `===` | 全等，**不转换类型** | `'123' === 123` → `false` |
| `!=` | 不等（宽松） | |
| `!==` | 不全等 | |
| `>` `<` `>=` `<=` | 大小比较 | |

**特殊比较：**

- `null == undefined` → `true`
- `null === undefined` → `false`（类型不同）
- `NaN == NaN` → `false`

#### 赋值运算符

`=` `+=` `-=` `*=` `/=` `%=`

- `a += b` 等价于 `a = a + b`

#### 条件运算符（三元）

```js
条件 ? 表达式1 : 表达式2
// 条件为 true 返回表达式1，否则返回表达式2
```

#### 逗号运算符

```js
var a = 1, b = 2, c = 3;  // 一次声明多个变量
```

### 3.5 流程控制语句

#### if...else

```js
if (condition) {
    // ...
} else if (condition2) {
    // ...
} else {
    // ...
}
```

#### switch...case

```js
switch (key) {
    case value1:
        statement;
        break;        // ★ 不写 break 会继续执行下一个 case
    case value2:
        statement;
        break;
    default:
        statement;
        break;
}
```

- switch 与 case 比较使用 **全等（===）**

#### 循环

```js
// while：先判断后执行
while (条件) { 循环体 }

// do...while：先执行后判断（至少执行一次）
do { 循环体 } while (条件);

// for
for (初始化; 条件; 更新) { 循环体 }
```

#### break 与 continue

- `break`：退出当前循环（离它最近的循环）
- `continue`：跳过当次循环，进入下一次

### 3.6 函数

```js
// 方式1：function 关键字声明
function 函数名(形参1, 形参N) {
    函数体
}

// 方式2：函数表达式
var 函数名 = function(形参1, 形参N) {
    函数体
};
```

**要点：**

- 形参实参个数可以不一致：多余实参被忽略，缺少形参为 `undefined`
- `return` 返回值；`return` 后的语句不执行
- 没有 `return` 或 `return` 无值，返回 `undefined`
- `typeof` 检查函数返回 `'function'`

### 3.7 对象与类

#### 对象创建

```js
// 方式1：new Object()
var student = new Object();
student.name = '张三';
student.age = 20;

// 方式2：对象字面量
var student = {
    name: '张三',
    age: 20
};
```

#### 对象操作

```js
student.school = 'ZJU';       // 添加属性
student.school = 'PKU';       // 修改属性
delete student.school;        // 删除属性
```

#### 栈内存与堆内存

- **基本类型**存在栈内存，赋值是值拷贝
- **引用类型**（对象）存在堆内存，变量存的是地址，赋值是地址拷贝（浅拷贝）

#### ES6 class

```js
class Person {
    constructor(name) {
        this.name = name;
    }
    greet() {
        console.log(`Hello, I'm ${this.name}`);
    }
}

class Student extends Person {     // 继承
    constructor(name, school) {
        super(name);               // 调用父类构造函数
        this.school = school;
    }
}

const s = new Student('张三', 'ZJU');
s.greet();
console.log(s instanceof Student);  // true
console.log(s instanceof Person);   // true
```

### 3.8 数组

```js
// 创建
var arr1 = [2, 3, 4];          // 字面量
var arr2 = new Array(2, 3, 4); // 构造函数
var arr3 = new Array(5);       // 长度为5的空数组

// 访问
arr[0] = 10;
console.log(arr.length);       // 数组长度
```

#### 数组常用方法

| 方法 | 说明 |
|------|------|
| `push()` | 末尾添加元素，返回新长度 |
| `pop()` | 删除末尾元素，返回删除的元素 |
| `unshift()` | 开头添加元素，返回新长度 |
| `shift()` | 删除开头元素，返回删除的元素 |
| `forEach(fn)` | 遍历数组，`fn(value, index, array)` |
| `indexOf()` | 搜索元素，返回位置 |
| `includes()` | 判断是否包含某值 |
| `slice()` | 选取部分，返回新数组 |
| `concat()` | 连接数组，返回结果 |
| `filter(fn)` | 过滤，返回满足条件的新数组 |
| `find(fn)` | 查找第一个满足条件的元素 |
| `isArray()` | 判断是否数组 |
| `join()` | 数组转字符串 |

### 3.9 常用内置类

#### Math

| 方法/属性 | 说明 |
|-----------|------|
| `Math.PI` | π |
| `Math.ceil(x)` | 向上取整 |
| `Math.floor(x)` | 向下取整 |
| `Math.round(x)` | 四舍五入 |
| `Math.random()` | [0,1) 随机数 |
| `Math.max(a, b)` | 最大值 |
| `Math.min(a, b)` | 最小值 |
| `Math.abs(x)` | 绝对值 |

#### String

| 方法/属性 | 说明 |
|-----------|------|
| `length` | 字符串长度 |
| `charAt(i)` | 返回指定位置字符 |
| `indexOf()` | 查找子串位置 |
| `slice()` | 提取片段 |
| `concat()` | 连接字符串 |
| `toUpperCase()` | 转大写 |
| `toLowerCase()` | 转小写 |
| `split()` | 分割为数组 |
| `trim()` | 去除首尾空格 |

#### Date

| 方法 | 说明 |
|------|------|
| `getTime()` | 1970至今毫秒数 |
| `getDate()` | 月中第几天 (1~31) |
| `getDay()` | 周中第几天 (0~6) |
| `getMonth()` | 月份 (0~11) |
| `getFullYear()` | 四位年份 |

### 3.10 异步编程

#### 同步 vs 异步

- JS 是**单线程**，一次只完成一个任务
- 同步：排队执行，前者完成后才执行后者
- 异步：耗时任务挂起交子线程，主线程继续执行，完成后通知

#### 三种异步解决方案

| 方案 | 特点 |
|------|------|
| 回调函数 | 简单但易造成回调地狱，可读性差 |
| Promise | ES6，链式调用，代码清晰，`then/catch` |
| async/await | ES2017，基于Promise，像写同步代码一样写异步 |

#### Promise 基本流程

```js
const p = new Promise((resolve, reject) => {
    // 异步操作
    if (成功) resolve(result);   // 成功
    else reject(error);           // 失败
});

p.then(result => { /* 成功 */ })
 .catch(error => { /* 失败 */ });
```

#### async/await

```js
async function demo() {
    try {
        const result = await promiseAjax(url);
        console.log(result);
    } catch (error) {
        console.log(error);
    }
}
```

- `async` 声明异步函数，返回 Promise
- `await` 等待 Promise 完成，返回结果
- `try...catch` 捕获异常

### 3.11 Axios

CDN 引入：

```html
<script src="https://cdn.bootcdn.net/ajax/libs/axios/1.3.4/axios.js"></script>
```

发送 GET 请求：

```js
getWeather.onclick = async function() {
    let city = cityChoice.value;
    let lon = cityPosition_api[city].lon;
    let lat = cityPosition_api[city].lat;

    const key = 'af9c316f6a11424da22db1dd04f5e036';
    // ★ URL 必须用反引号（模板字符串），${变量} 才能插值
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${key}&units=metric&lang=zh`;

    try {
        const res = await axios.get(url);   // 等待请求返回

        const weather = res.data.weather[0].description;
        const temperature = res.data.main.temp;
        const pressure = res.data.main.pressure;
        const humidity = res.data.main.humidity;

        document.getElementById('description').innerHTML = weather;
        document.getElementById('temperature').innerHTML = '温度：' + temperature + ' ℃';

        console.log(res.data);  // 控制台输出返回体（作业2要求）
    }
    catch(error) {
        console.error("error");
    }
};
```

**关键点：**

- `async` 声明异步函数，`await` 等待 Promise 完成
- URL 必须用**反引号** `` ` `` 包裹（模板字符串），`${变量}` 才能正确插值
- `res.data` 是返回体数据
- `try...catch` 捕获请求异常
- Axios 特性：支持 Promise API、自动转换 JSON、可拦截请求/响应

### 3.12 fetch 读取本地 JSON

```js
const cityJson = await fetch('../assets/cityList.json');
const cityList = await cityJson.json();

cityList.forEach(element => {
    let position = element.centerPoint.split(',').map(Number);
    // ...
});
```

### 3.13 数据处理技巧

```js
// 字符串分割 + 转数字
let position = "120.21,30.25".split(',').map(Number);
// position = [120.21, 30.25]

// 数组遍历
cityList.forEach(element => { ... });

// 数组过滤（删除书签）
bookmarks = bookmarks.filter(b => b.id !== item.id);

// 数组查找
let data = cityList.find(i => i.code === code);

// 字符串去空格
const name = addName.value.trim();

// toFixed 保留小数
currentHeight.innerText = waterHeight.toFixed(1);
```

### 3.14 ES6 模块（import/export）

```js
// 导出（cityjson.js）
export async function cityJSONoperation(viewer) {
    // ...
}

// 导入（HTML 中的 module 脚本）
<script type="module">
    import {cityJSONoperation} from './cityjson.js';
    cityJSONoperation(viewer);
</script>
```

- `export` 导出函数/变量
- `import {名称} from '路径'` 导入
- 必须在 `<script type="module">` 中使用

### 3.15 window 全局对象传递

```js
window.viewer = viewer;
window.cityList = cityList;
window.selectEntity = selectEntity;
```

- 不同 JS 文件之间无法直接共享变量
- 通过 `window.变量名` 实现跨文件共享


## 四、JavaScript DOM 与 BOM


### 4.1 DOM 节点类型

| 节点类型 | 说明 |
|----------|------|
| 文档节点 `document` | 整个 HTML 文档，所有节点的祖先 |
| 元素节点 `Element` | HTML 标签，最常用 |
| 文本节点 `Text` | 标签外的文本内容 |
| 属性节点 `Attr` | 标签中的属性 |

### 4.2 获取 DOM 元素

```js
// 通过 ID 获取（返回单个元素）
const panel = document.getElementById('weather_panel');

// 通过标签名获取（返回类数组 HTMLCollection）
const divs = document.getElementsByTagName('div');

// 通过 name 属性获取（返回 NodeList，常用于单选按钮组）
const radios = document.getElementsByName('styleChoice');

// 通过 CSS 选择器获取（返回第一个匹配）
const firstIcon = document.querySelector('.fly-icon');

// 通过 CSS 选择器获取所有匹配（返回 NodeList）
const buttons = document.querySelectorAll('.baseLayer');
```

### 4.3 操作 DOM 内容与样式

```js
// 修改元素内部 HTML
document.getElementById('description').innerHTML = weather;

// 修改元素纯文本
r_label.innerText = r + "px";

// 修改元素值（表单控件）
cityChoice.value = code;

// 修改内联样式
panel.style.display = 'none';    // 隐藏
panel.style.display = 'block';   // 显示
panel.style.left = '100px';

// ★ 注意：CSS 的 background-color 在 JS 中用驼峰 backgroundColor
box1.style.backgroundColor = "red";

// 修改 CSS 类
tool.classList.add('active');      // 添加类
tool.classList.remove('active');   // 移除类
```

**读取元素当前样式：**

- `元素.style.样式名` 只能读取内联样式
- `getComputedStyle(元素, null).样式名` 可读取 CSS 中定义的样式

**尺寸相关属性：**

| 属性 | 说明 |
|------|------|
| `clientWidth` / `clientHeight` | 可见宽高（不含 border） |
| `offsetWidth` / `offsetHeight` | 宽高（含 padding + border） |
| `offsetLeft` / `offsetTop` | 相对定位父元素的偏移 |
| `offsetParent` | 最近的已定位祖先元素 |

### 4.4 创建和添加 DOM 元素

```js
// 创建 <li> 元素
const li = document.createElement('li');

// 设置内部 HTML
li.innerHTML = `
    <span class="change-view">${item.name}</span>
    <div class="bookmark-operations">
        <img src="map-pin.png" class="fly-icon" title="飞向视角">
    </div>
`;

// 添加到父元素末尾
listContainer.appendChild(li);

// 创建 <option> 并添加到 <select>
let option = document.createElement('option');
option.value = element.code;
option.innerText = element.name;
city.appendChild(option);

// 清空父元素所有子元素
listContainer.innerHTML = "";
```

**DOM 节点操作方法汇总：**

| 方法 | 说明 |
|------|------|
| `createElement(标签名)` | 创建元素节点 |
| `appendChild(子节点)` | 末尾添加子节点 |
| `insertBefore(新节点, 旧节点)` | 在指定节点前插入 |
| `removeChild(子节点)` | 删除子节点 |
| `replaceChild(新节点, 旧节点)` | 替换节点 |
| `parentNode` | 获取父节点 |
| `firstChild` / `lastChild` | 第一个/最后一个子节点 |

### 4.5 事件绑定

#### 三种绑定方式

| 方式 | 写法 | 特点 |
|------|------|------|
| HTML 属性 | `<button onclick="fn()">` | 结构行为耦合，不推荐 |
| DOM 属性 | `btn.onclick = function(){}` | 可分离结构行为，但只能绑一个 |
| 事件监听器 | `btn.addEventListener('click', fn)` | ★推荐，可绑定多个处理函数 |

```js
// 方式2：DOM 属性
control.onclick = function() {
    if (panel.style.display !== 'none') {
        panel.style.display = 'none';
    }
};

// 方式3：事件监听器
document.getElementById('start').addEventListener('click', () => {
    run = true;
});
```

**onclick vs addEventListener：**

- `onclick` 只能绑定一个处理函数（后赋值会覆盖）
- `addEventListener` 可绑定多个，且支持事件捕获/冒泡控制
- `removeEventListener()` 可移除监听

#### 常用事件类型

| 事件 | 说明 |
|------|------|
| `onclick` | 单击 |
| `ondblclick` | 双击 |
| `onmousedown` | 鼠标按下 |
| `onmouseup` | 鼠标松开 |
| `onmousemove` | 鼠标移动 |
| `onmouseenter` | 鼠标进入元素 |
| `onkeydown` | 键盘按下 |
| `onkeyup` | 键盘松开 |
| `onchange` | 内容改变（下拉框等） |
| `oninput` | 输入实时变化 |

#### 事件对象

```js
btn.onclick = function(event) {
    console.log(event.type);    // 事件类型，如 'click'
    console.log(event.clientX); // 鼠标水平坐标
    console.log(event.clientY); // 鼠标垂直坐标
};
```

#### 拖拽三件套

```js
panel.onmousedown = function(e) {
    // 1. 按下鼠标，记录鼠标相对面板的偏移
    let mouseX = e.clientX - panel.offsetLeft;
    let mouseY = e.clientY - panel.offsetTop;

    // 2. 鼠标移动时，更新面板位置
    document.onmousemove = function(e) {
        panel.style.left = (e.clientX - mouseX) + 'px';
        panel.style.top = (e.clientY - mouseY) + 'px';
    };

    // 3. 松开鼠标，停止移动
    document.onmouseup = function() {
        document.onmousemove = null;
        document.onmouseup = null;
    };
};
```

**关键属性：**

| 属性 | 说明 |
|------|------|
| `e.clientX` / `e.clientY` | 鼠标相对浏览器视口的坐标 |
| `element.offsetLeft` / `offsetTop` | 元素相对已定位父元素的偏移 |
| `element.offsetWidth` / `offsetHeight` | 元素自身宽高 |

### 4.6 BOM 浏览器对象模型

#### window 对象

- BOM 核心，表示浏览器窗口，也是**全局对象**
- `window.open()` 打开新窗口
- `alert()` / `confirm()` / `prompt()` 系统对话框
  - `confirm()` 返回 `true`（确定）或 `false`（取消）
  - `prompt()` 返回用户输入内容

#### 定时器

```js
// 延时调用：过一段时间执行一次
var id = setTimeout(function() {
    alert("hello");
}, 2000);           // 2秒后执行
clearTimeout(id);   // 取消

// 定时调用：每隔一段时间执行一次
var token = setInterval(function() {
    console.log("tick");
}, 1000);           // 每1秒执行
clearInterval(token);  // 停止
```

#### Location 对象

| 方法 | 说明 |
|------|------|
| `location.assign(url)` | 跳转到指定页面 |
| `location.reload()` | 重新加载当前页面 |
| `location.replace(url)` | 替换页面（不生成历史记录） |

#### History 对象

| 方法 | 说明 |
|------|------|
| `history.back()` | 回退 |
| `history.forward()` | 前进 |
| `history.go(n)` | 前后跳转 n 步 |
| `history.length` | 历史记录数量 |

---

## 五、Cesium 模块

### 5.1 环境搭建与 Viewer 初始化

#### 引入 Cesium

```html
<script src="../scripts/Cesium/Cesium.js"></script>
<link rel="stylesheet" href="../scripts/Cesium/Widgets/widgets.css">
```

#### 设置 Token

```js
Cesium.Ion.defaultAccessToken = "eyJhbGciOiJIUzI1NiIs...";
```

#### 创建 Viewer

```js
var viewer = new Cesium.Viewer('cesiumContainer', {
    animation: false,              // 关闭动画控件
    timeline: false,               // 关闭时间轴
    baseLayerPicker: false,        // 关闭底图选择器
    navigationHelpButton: false,   // 关闭导航帮助按钮
    infoBox: false,                // 关闭信息框
    selectionIndicator: false,     // 关闭选中指示器
    // fullscreenButton: false,    // 关闭全屏按钮
    // geocoder: false,            // 关闭地理编码搜索
    // homeButton: false,          // 关闭主页按钮
    // sceneModePicker: false,     // 关闭场景模式选择器
});
```


**HTML 容器：**
```html
<div id="cesiumContainer" style="height: 100%"></div>
```

### 5.2 相机系统

#### camera.flyTo() — 飞行到指定位置

```js
// 飞到矩形区域
viewer.camera.flyTo({
    destination: Cesium.Rectangle.fromDegrees(118.0, 28.0, 122.0, 32.0)
});

// 飞到相机视角（书签功能）
viewer.camera.flyTo({
    destination: item.position,          // Cartesian3 位置
    orientation: {
        heading: item.heading,           // 航向角
        pitch: item.pitch,               // 俯仰角
        roll: item.roll                  // 翻滚角
    },
    duration: 4.0                         // 飞行时间（秒）
});
```

#### camera.setView() — 直接设置视角（无动画）

```js
viewer.camera.setView({
    destination: Cesium.Cartesian3.fromDegrees(120.0, 30.0, 5000),
    orientation: {
        heading: Cesium.Math.toRadians(0),
        pitch: Cesium.Math.toRadians(-90),
        roll: 0
    }
});
```

#### camera.lookAt() — 锁定视角看向目标点

```js
viewer.camera.lookAt(
    Cesium.Cartesian3.fromDegrees(120.0, 30.0),  // 目标点
    new Cesium.HeadingPitchRange(0, -Math.PI/4, 5000)  // 航向、俯仰、距离
);
```

#### viewer.flyTo() vs camera.flyTo()

```js
// viewer.flyTo() — 飞向实体/3D Tiles（自动计算范围）
viewer.flyTo(tileset);
viewer.flyTo(waterPolygon);

// camera.flyTo() — 飞向指定坐标/视角
viewer.camera.flyTo({ destination: ... });
```

- `viewer.flyTo(entities)` **能**实现视角转换到实体位置
- `viewer.zoomTo()` 类似但无动画

#### 相机属性（书签存储）

```js
position: viewer.camera.position.clone(),  // 相机位置（Cartesian3）
heading: viewer.camera.heading,             // 航向角
pitch: viewer.camera.pitch,                 // 俯仰角
roll: viewer.camera.roll                    // 翻滚角
```

### 5.3 坐标系与位置表示

```js
// 经纬度 → Cartesian3（三维笛卡尔坐标）
Cesium.Cartesian3.fromDegrees(lon, lat)              // 经度, 纬度
Cesium.Cartesian3.fromDegrees(lon, lat, height)      // 带高度

// 经纬度数组 → 多边形顶点
Cesium.Cartesian3.fromDegreesArray([
    119.47, 28.17,
    119.47, 28.24,
    119.54, 28.24,
    119.54, 28.17,
])

// 矩形区域
Cesium.Rectangle.fromDegrees(西经, 南纬, 东经, 北纬)
```

### 5.4 实体（Entity）加载与可视化

#### 添加点实体（Point）

```js
viewer.entities.add({
    id: element.code,                              // 唯一标识
    name: element.name,                             // 名称
    position: Cesium.Cartesian3.fromDegrees(lon, lat),  // 位置
    point: new Cesium.PointGraphics({               // 点样式
        pixelSize: 20,                              // 像素大小
        color: Cesium.Color.CYAN,                   // 颜色
        outlineWidth: 1,                            // 轮廓宽度
        outlineColor: Cesium.Color.CYAN,            // 轮廓颜色
        scaleByDistance: new Cesium.NearFarScalar(  // 距离缩放
            2.0e3, 2.0,    // 近处：缩放2.0
            1.0e7, 0.0     // 远处：缩放0.0
        ),
        disableDepthTestDistance: Number.POSITIVE_INFINITY,  // 禁用深度测试
    }),
});
```

#### 添加多边形实体（Polygon）

```js
const waterPolygon = viewer.entities.add({
    name: "waterPolygon",
    polygon: {
        hierarchy: Cesium.Cartesian3.fromDegreesArray([...]),
        material: new Cesium.Color.fromBytes(64, 157, 253, 150),  // RGBA
        extrudedHeight: 0,    // 拉伸高度（淹没分析用）
    },
});
```

#### 添加广告牌（Billboard）

```js
selectEntity.billboard = new Cesium.BillboardGraphics({
    image: './selected_point.png',
    width: 60,
    height: 60,
    scaleByDistance: new Cesium.NearFarScalar(2.0e3, 2.0, 1.0e7, 0.0),
    verticalOrigin: Cesium.VerticalOrigin.BOTTOM,  // 底部对齐
    disableDepthTestDistance: Number.POSITIVE_INFINITY,
});
```

#### Entity 集合操作

```js
// 获取所有实体数组
viewer.entities.values    // Entity[] 数组

// 遍历所有实体
viewer.entities.values.forEach(entity => {
    if (entity.point) {
        entity.point.pixelSize = 20;
    }
});

// 按 ID 获取实体
let entity = viewer.entities.getById(code);

// 判断实体是否已存在
if (viewer.entities.getById(element.code)) {
    return;  // 已存在则跳过
}
```

#### 修改实体样式

```js
entity.point.pixelSize = cur_point_size;
entity.point.color = Cesium.Color.fromCssColorString(cur_point_color);
entity.point.outlineWidth = cur_side_size;
entity.point.outlineColor = Cesium.Color.fromCssColorString(cur_side_color);
entity.point.show = false;  // 隐藏点

// 删除 billboard
entity.billboard = undefined;
```

### 5.5 颜色对象

```js
// Cesium 内置颜色
Cesium.Color.CYAN       // 青色
Cesium.Color.YELLOW     // 黄色
Cesium.Color.WHITE      // 白色

// 从 RGBA 创建
Cesium.Color.fromBytes(64, 157, 253, 150)   // R, G, B, A (0-255)

// 从 CSS 颜色字符串创建（★Color 与 CSS 颜色互转）
Cesium.Color.fromCssColorString('#00ffff')
Cesium.Color.fromCssColorString('#FFFFFF')

// 转回 CSS 颜色字符串
color.toCssColorString()   // 返回如 "rgba(0, 255, 255, 1.0)"
```

### 5.6 影像数据服务

#### 三大核心类

| 类 | 说明 |
|----|------|
| `ImageryProvider` | 影像图层**数据源**，抽象类，不可直接实例化，有14个子类 |
| `ImageryLayer` | 影像**图层**，封装 Provider + 亮度/透明度/对比度配置 |
| `ImageryLayerCollection` | 图层**容器**，`viewer.imageryLayers` 即此类型，可装多个图层 |

**ImageryLayerCollection 常用方法：**

| 方法 | 说明 |
|------|------|
| `add(layer, index)` | 添加 ImageryLayer 到集合 |
| `addImageryProvider(provider, index)` | 用 Provider 创建图层并添加 |
| `remove(layer, destroy)` | 移除图层 |
| `contains(layer)` | 检查是否包含 |
| `get(index)` | 按索引获取图层 |
| `lower(layer)` | 图层下移一层 |
| `raise(layer)` | 图层上移一层 |
| `removeAll()` | 移除所有图层 |

#### ImageryProvider 类型汇总

| Provider 类 | 用途 |
|-------------|------|
| `WebMapServiceImageryProvider` | WMS 服务（GeoServer） |
| `WebMapTileServiceImageryProvider` | WMTS 服务（天地图矢量注记） |
| `ArcGisMapServerImageryProvider` | ArcGIS 地图服务 |
| `IonImageryProvider` | Cesium Ion 资产（Bing Maps 等） |
| `UrlTemplateImageryProvider` | URL 模板（高德/天地图等） |
| `OpenStreetMapImageryProvider` | OpenStreetMap 在线地图 |

#### WMS 图层（GeoServer）

```js
var provider = new Cesium.WebMapServiceImageryProvider({
    url: 'http://localhost:8080/geoserver/Hangzhou_hw3/wms',
    layers: 'Hangzhou_hw3:hangzhou_img',
    parameters: {
        service: 'WMS',
        format: 'image/png',
        transparent: true,
    },
});

viewer.imageryLayers.addImageryProvider(provider);
```

#### ArcGIS 地图服务

```js
Cesium.ArcGisMapServerImageryProvider.fromUrl(
    'https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer'
)
```

#### Ion 影像资产

```js
Cesium.IonImageryProvider.fromAssetId(2)     // Bing Maps
Cesium.IonImageryProvider.fromAssetId(3812)   // 夜间灯光
```

#### URL 模板影像（高德/天地图）

```js
// 高德地图
new Cesium.UrlTemplateImageryProvider({
    url: 'https://webst02.is.autonavi.com/appmaptile?style=7&x={x}&y={y}&z={z}',
    minimumLevel: 1,
    maximumLevel: 18
});
```

#### ImageryLayer 封装

```js
// 方式一：ImageryLayer.fromProviderAsync（新API）
const layer = Cesium.ImageryLayer.fromProviderAsync(
    Cesium.ArcGisMapServerImageryProvider.fromUrl('...')
);
viewer.imageryLayers.add(layer);          // 传 ImageryLayer

// 方式二：直接添加 Provider
viewer.imageryLayers.addImageryProvider(provider);   // 传 ImageryProvider
```

**两种添加方式区别：**

| 方法 | 参数类型 | 说明 |
|------|----------|------|
| `add(layer)` | `ImageryLayer` | 新 API，推荐 |
| `addImageryProvider(provider)` | `ImageryProvider` | 旧 API，直接传 Provider |

### 5.7 地形数据

#### TerrainProvider 类型

| Provider | 说明 |
|----------|------|
| `EllipsoidTerrainProvider` | 默认，椭球体，高程为0，无起伏 |
| `CesiumTerrainProvider` | ★最常用，高精度全球地形，支持光照和水面 |
| `ArcGISTiledElevationTerrainProvider` | ArcGIS 高程瓦片地形 |
| `GoogleEarthEnterpriseTerrainProvider` | Google Earth 高程地形 |


#### 加载地形

```js
Cesium.CesiumTerrainProvider.fromIonAssetId(1, {
    requestWaterMask: true,        // 请求水面效果
    requestVertexNormals: true,    // 请求法线（光照效果）
})
.then((terrainProvider) => {
    viewer.terrainProvider = terrainProvider;
})
.catch((e) => {
    console.log("ERROR!" + e);
});
```

- `requestWaterMask: true` — 水面效果
- `requestVertexNormals: true` — 光照效果
- 赋值给 `viewer.terrainProvider`

#### 开启光照和深度测试

```js
viewer.scene.globe.depthTestAgainstTerrain = true;  // 地形深度测试（实体被地形遮挡）
```

### 5.8 3D Tiles 加载

```js
// 异步加载 3D Tileset
const tileset = await Cesium.Cesium3DTileset.fromUrl('../assets/Tileset/tileset.json');
viewer.scene.primitives.add(tileset);

// 飞向 3D Tiles
viewer.flyTo(tileset);
// 或
viewer.zoomTo(tileset);

// 设置 3D Tiles 样式
tileset.style = new Cesium.Cesium3DTileStyle({
    color: 'color("#FFFFFF")',
    show: true,
});
```

#### 3D Tiles 点击高亮

```js
let handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);

handler.setInputAction(function(movement) {
    let feature = viewer.scene.pick(movement.position);

    if (Cesium.defined(prevFeature)) {
        prevFeature.color = Cesium.Color.fromCssColorString('#FFFFFF');
    }

    if (Cesium.defined(feature) && feature instanceof Cesium.Cesium3DTileFeature) {
        feature.color = Cesium.Color.fromCssColorString('#00FFFF');
        prevFeature = feature;
    }
}, Cesium.ScreenSpaceEventType.LEFT_CLICK);
```

### 5.9 事件处理（ScreenSpaceEventHandler）

```js
// 创建事件处理器
const handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);

// 注册左键点击事件
handler.setInputAction((move) => {
    // move.position 是屏幕坐标（Cartesian2）
    let select = viewer.scene.pick(move.position);

    // 判断是否点中了实体
    if (Cesium.defined(select) && select.id) {
        updateWeather(select.id.id);   // select.id 是 Entity
    }
}, Cesium.ScreenSpaceEventType.LEFT_CLICK);
```

**ScreenSpaceEventType 事件类型：**

| 事件常量 | 说明 |
|----------|------|
| `LEFT_CLICK` | 左键点击 |
| `RIGHT_CLICK` | 右键点击 |
| `MOUSE_MOVE` | 鼠标移动 |
| `LEFT_DOWN` / `LEFT_UP` | 左键按下/松开 |

**scene.pick() 返回值：**

- 如果点中实体：返回对象，`select.id` 是 Entity
- 如果点中 3D Tile Feature：返回 `Cesium3DTileFeature` 实例
- 如果未点中任何对象：返回 `undefined`

### 5.10 淹没分析（CallbackProperty）

```js
let waterHeight = 0;
let targetHeight = 750;
let run = false;

// CallbackProperty：每帧回调返回动态值
const altitudeProperty = new Cesium.CallbackProperty(() => {
    if (run) {
        waterHeight += 0.5;           // 每帧增加0.5米
        if (waterHeight > targetHeight) {
            waterHeight = targetHeight;
        }
    }
    currentHeight.innerText = waterHeight.toFixed(1);
    return waterHeight;               // 返回当前水面高度
}, false);                            // false = 非恒定值（每帧执行）

// 开始按钮
document.getElementById('start').addEventListener('click', () => {
    run = true;
    waterPolygon.polygon.extrudedHeight = altitudeProperty;  // 绑定动态属性
});

// 暂停按钮
document.getElementById('pause').addEventListener('click', () => {
    run = false;
});

// 重置按钮
document.getElementById('reset').addEventListener('click', () => {
    run = false;
    waterHeight = 0;
    viewer.zoomTo(waterPolygon);
});
```

**CallbackProperty 要点：**

- 用于创建动态变化的属性值（每帧重新计算）
- 第二个参数 `false` 表示值会变化（非恒定）
- 常用于动画效果（如水面上涨）
- 淹没分析核心：利用 polygon 的 `extrudedHeight` 属性 + CallbackProperty 动态改变水面高度

### 5.11 书签功能完整逻辑

```js
let bookmarks = [];

// 创建书签 — 保存当前相机状态
addBookmark.onclick = function() {
    const name = addName.value.trim();
    if (!name) { alert("请输入书签名称！"); return; }

    const currentView = {
        id: Date.now(),
        name: name,
        position: viewer.camera.position.clone(),  // 克隆位置
        heading: viewer.camera.heading,
        pitch: viewer.camera.pitch,
        roll: viewer.camera.roll
    };

    bookmarks.push(currentView);
    renderBookmarks();
};

// 查询书签 — 飞向保存的视角
li.querySelector('.fly-icon').onclick = function() {
    viewer.camera.flyTo({
        destination: item.position,
        orientation: {
            heading: item.heading,
            pitch: item.pitch,
            roll: item.roll
        },
        duration: 4.0
    });
};

// 删除书签 — 过滤掉指定 id
li.querySelector('.delete-icon').onclick = function() {
    bookmarks = bookmarks.filter(b => b.id !== item.id);
    renderBookmarks();
};
```

### 5.12 地球拾取（屏幕坐标→地球坐标）

```js
// 屏幕坐标 → 射线
let ray = viewer.camera.getPickRay(center);

// 射线 → 地球表面 Cartesian3 坐标
let cartesian = viewer.scene.globe.pick(ray, viewer.scene);

// 判断是否在地球上
if (Cesium.defined(cartesian)) {
    // 在地球上
}
```

### 5.13 viewer.zoomTo()

```js
viewer.zoomTo(tileset);
viewer.zoomTo(waterPolygon);
// 与 flyTo 的区别：zoomTo 无飞行动画，直接缩放
```

### 5.14 NearFarScalar（距离缩放）

```js
new Cesium.NearFarScalar(
    2.0e3, 2.0,    // 近距离(2000米)：缩放2.0
    1.0e7, 0.0     // 远距离(10000000米)：缩放0.0
)
```

- 控制实体在近处大、远处小（或消失）
- 常用于 PointGraphics 和 BillboardGraphics

### 5.15 空间分析

- **空间量测**：拾取屏幕点→转换为地理坐标→几何解算距离/面积
- **淹没分析**：polygon 的 extrudedHeight + CallbackProperty 动态上涨
- **其他分析**：剖面分析、可视域分析、光照分析、缓冲区分析

**扩展库：**

- `heatmap.js`：热力图可视化
- `Turf.js`：空间分析库（空间操作、GeoJSON、分类统计）


## 六、前端框架（React）

### 6.1 前端框架概述

**为什么需要框架：**

- 原生 JS 操作 DOM 繁琐重复
- 代码复用性差
- 难以维护大型项目

**三大主流框架：**

| 框架 | 来源 | 特点 |
|------|------|------|
| **Angular** | Google 2009 | 功能最完整（路由/表单/Ajax/双向绑定全自带），学习成本高 |
| **React** | Facebook 2013 | 虚拟DOM，组件化，单向数据流，灵活但需搭配其他库 |
| **Vue** | 尤雨溪 2014 | 渐进式，简单易学，体积小（~20KB），中文友好 |

### 6.2 React 

#### 虚拟 DOM

- React 先将代码转换成 JavaScript 对象（虚拟DOM），再转换为真实DOM
- 通过 diff 算法对比新旧虚拟DOM，只更新变化的部分（局部更新）
- 优点：速度快、跨浏览器兼容

#### JSX 语法

- JSX = JavaScript XML，JS 的语法扩展
- 可以在 JS 中写 HTML 标签
- 例：`let ele = <h1>Hello JSX!</h1>`

#### 组件

- 组件 = 实现局部功能的代码和资源集合（html/css/js/image）
- **函数组件**（推荐）和**类组件**（已归为过时API）

#### state 与 props

| 概念 | 说明 | 特点 |
|------|------|------|
| `state` | 组件内部状态 | **可变**，用 `setState()` 更新，更新后自动重新渲染 |
| `props` | 从组件外向组件内传递的数据 | **不可变**，由父组件传递 |

#### Hook（React 16.8 新增）

| Hook | 用途 |
|------|------|
| `useState` | 让函数组件拥有内部状态 |
| `useRef` | 存放可变值的 ref 对象 |
| `useEffect` | 在指定情况下执行副作用 |





