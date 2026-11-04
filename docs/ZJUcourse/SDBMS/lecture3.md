# 关系数据库标准语言

## SQL 概述

Structured Query Language 是一种高级编程语言，用于查询和操作数据。

当然要注意不同数据库具体语法细节可能不同。

### 特点

- 操作和风格统一

- 高度非过程化

- 面向集合的操作方式

- 同一语法结构，既是自含式语言，又是嵌入式语言
 
    >自含式语言可以独立使用，嵌入式语言可以嵌入其他高级语言（如 C 、Python ）程序中

- 简洁

## 数据定义

关系数据库的基本对象是基本表、视图和索引，数据定义包括对三者的定义。

>⚠️SQL命令不区分大小写

### 创建表

```sql
CREATE TABLE 表名 (列名 数据类型 [列级完整性约束条件] [, 表级完整性约束条件]);
```

其中：
 - 一列就是一个属性
 - 列级完整性约束条件涉及相应属性列的完整性约束条件
 - 表级完整性约束条件涉及一个或多个属性列的完整性约束条件

>⚠️中括号中的内容可以没有，并且一个表可以有一列或多列

>🌰创建 students 和 enrolled 关系
>```sql
>CREATE TABLE students(
>   sid CHAR(10) PRIMARY KEY, 
>   name VARCHAR(20) NOT NULL, 
>   age INT CHECK(age > 10)
>);
>
>CREATE TABLE enrolled(
>   sid CHAR(10) REFERENCES students(sid), 
>   cid CHAR(20), 
>   grade INT, 
>   PRIMARY KEY(sid, cid)
>);
>```
>
>定义上面的基本关系 enrolled 也可以把主码和外码的声明放到最后，写成
>```sql
>CREATE TABLE enrolled(
>   sid CHAR(10), 
>   cid CHAR(20), 
>   grade INT, 
>   CONSTRAINT pk_en PRIMARY KEY(sid, cid), 
>   CONSTRAINT fk_en FOREIGN KEY students(sid)
>);
>```


#### 数据类型

定义表的属性时，需要指明该属性的域，在 SQL 中就用数据类型来实现。

常见数据类型有：
 - `char(20)`
 - `varchar(50)`
 - `text`
 - `int`
 - `bigint`
 - `smallint`
 - `float`
 - `float8`
 - `date`
 - `timestamp`
 - `point`
 - `line`
 - `polygon`
 - `box`
 - `bit`
 - `bool`
 - `memory`


#### 完整性约束

- 实体完整性 PRIMARY KEY

- 参照完整性 FOREIGN KEY
    >⚠️基本关系中的外码取值只能是被参照关系中的主码值、唯一值或空值（`NULL`）

- 用户定义完整性

>🌰用 `CHECK` 实现 `NOT NULL`
>```sql
>CREATE TABLE students(
>   id INT PRIMARY KEY, 
>   name TEXT, 
>   gpa REAL CHECK(gpa IS NOT NULL)
>);
>```

### 修改表

```sql
ALTER TABLE 表名 
    [ADD 新列名 数据类型 [完整性约束]]
    [DROP 列名]
    [DROP 完整性约束]
    [MODIFY 列名 数据类型];
```

>🌰更改表的约束条件（接创建表的例子）
>```sql
>ALTER TABLE enrolled ADD CONSTRAINT grade_check CHECK(grade BETWEEN 0 AND 100);
>```


### 删除表

```sql
DROP TABLE 表名 ;
```

## 数据更新

### 插入数据

```sql
INSERT 
    INTO 表名 [(属性1)]
    VALUES (常量1);
```

其中可以插入多个值到多个属性，如果没有给出属性那么默认插入一行数据，但是都要注意值与属性位置对应。

>🌰插入数据（接创建表的例子）
>```sql
>INSERT INTO students VALUES ('111', 'Zhang', 19);
>
>INSERT INTO students(sid, age, name) VALUES ('112', 20, 'Wang'); 
>
>INSERT INTO students(sid, name) VALUES ('113', 'Xu');
>```

### 修改数据

```sql
UPDATE 表名
    SET 列名=表达式
    [WHERE 条件];
```
其中也可以有多个列名及对应表达式，之间以逗号分隔。

>🌰修改数据（接创建表的例子）
>```sql
>UPDATE students SET age = age + 1;
>
>UPDATE students SET age = 22 WHERE sid = '113'; 
>```

### 删除数据

```sql
DELETE FROM 表名
    [WHERE 条件];
```

这会删除指定表中符合条件的数据记录（元组），如果没有条件则删除所有元组。

#### 参照完整性

在修改、删除数据的时候，如果某个关系的某属性参照另一关系的某属性，是有可能违反参照完整性的，务必注意。

## 数据查询

### SELECT 语句

```sql
SELECT 属性1, 属性2, 属性3...
    FROM 关系1, 关系2, 关系3...
    WHERE 条件 ;
```

如果不写具体属性，而是写 `SELECT *` 那就选中全部属性。
如果在属性名前面加上 `DISTINCT` 那返回会去除重复行。

⚠️注意，用 `SELECT` 查询时，如果涉及多张表且没有给出连接条件的情况，先把 `FROM` 指明的表做笛卡尔积，然后在新的集合中选择符合条件的记录。所以如果有一张表为空，那返回也是空！

### 表变量和属性变量

查询涉及多张表而不同表有同名属性时，或一张表要使用多次时，可以：
 - 查询语句给属性加上表名限定，写成 `表名.属性名`
 - 也可以用 `AS` 给查询返回的列重命名，或给表重命名（注意 `AS` 可以省略）

>🌰给出表 employee ，查询每位员工姓名及其领导姓名
>| id | name | manager_id |
>|---|---|---|
>| 1 | 张三	| NULL |
>| 2 | 李四	| 1 |
>| 3 | 王五 | 1 |
>| 4 | 赵六	| 2 |
>
>```sql
>SELECT e1.name AS employee, e2.name AS manager
>   FROM employ AS e1, employ AS e2
>   WHERE e1.manager_id = e2.id;
>```

### 集合运算

| `UNION` | `INTERSECT` | `EXCEPT` |
| --- | --- | --- |
| 并集 | 交集 | 差集 |

>🌰给出表 apply ，查询申请了 CS 但没申请 EE 的学生
>| sid| cname| major| decision |
>|---| --- | --- | --- |
>
>```sql
>SELECT sid FROM apply WHERE major='CS'
>EXCEPT
>SELECT sid FROM apply WHERE major='EE';
>```

### 子查询

子查询就是把一条 `SELECT` 返回结果在另一条语句中使用。

#### 运算符

- `IN` 是否属于返回结果

- `EXISTS` 是否至少返回一行

- `ALL` 是否满足与所有返回值的比较

- `ANY` 是否满足与至少某一行返回值的比较

注意这四个运算符前都可以加上 `NOT` 取否定。

>🌰接上一个查询申请的例子，可以写成
>```sql
>SELECT sid FROM apply 
>   WHERE sid IN (SELECT sid FROM apply WHERE major='CS') 
>   AND sid NOT IN (SELECT sid FROM apply WHERE major='EE');
>```
>
>或者是
>```sql
>SELECT DISTINCT sid FROM apply a1 
>   WHERE major='CS' AND
>   NOT EXISTS (SELECT * FROM apply a2 WHERE a1.sid=a2.sid AND major='EE');
>```

#### 实现交集和差集


用 `EXISTS` 实现交集
```sql
SELECT DISTINCT R.A, R.B FROM R
    WHERE EXISTS (
        SELECT * FROM S
        WHERE R.A = S.A AND R.B = S.B
    );
```

用 `EXISTS` 实现差集
```sql
SELECT DISTINCT R.A, R.B FROM R
    WHERE NOT EXISTS (
        SELECT * FROM S
        WHERE R.A = S.A AND R.B = S.B
    );
```

⚠️注意上面这种相关子查询（内层查询引用了外层表的属性），从逻辑上可以理解为检查 `WHERE` 条件时是针对外层的当前行的！

### 聚合运算

聚合运算能把多行数据的某一属性进行统计，得到一个值。
常见的聚合函数有

- `MIN`

    >⚠️不计算 `NULL`

- `MAX`

    >⚠️不计算 `NULL`

- `SUM`

    >⚠️不计算 `NULL`

- `AVG`

    >⚠️不计算 `NULL`

- `COUNT`

    >⚠️ `COUNT(*)` 会计算 `NULL` ，但是 `COUNT(attribute)` 不会计算 `NULL` ！

>⚠️如果所有数据行都含 `NULL` ，那么 `COUNT` 返回 `0` ，其他函数返回 `NULL` ！

要注意 SQL 操作时聚合函数计算的顺序，一般是在同级 `WHERE` 检查条件后。

#### 分组

把具有相同指定属性值的数据行分到一组，使得聚合函数能在组内计算。
```sql
SELECT A, MAX(B)
    FROM R
    GROUP BY A;
```
注意这里 `SELECT` 查询的属性一般要么是分组依据、要么进行聚合运算，这样返回符合表的结构，查询才成功。

如果希望根据分组或聚合计算的结果进行条件筛选，就使用 `HAVING` 
```sql
SELECT A1, A2, ..., An
    FROM R1, R2, ..., Rn
    WHERE C1
    GROUP BY Ai, Aj, ..., Ak
    HAVING C2;
```

### 连接运算

之前已经说明，`FROM` 后有多张表会进行笛卡尔积分。但是如果给出连接条件，那就会进行连接运算。

#### 内连接

```sql
SELECT *
    FROM R
    INNER JOIN S ON R.A = S.A;
```
其中 `INNER` 可以省略，`ON` 后指定连接条件。

或者进行自然连接
```sql
SELECT *
    FROM R 
    NATURAL JOIN S;
```
这会找出两个表中同名属性，有相等值的进行连接。并且要注意，连接后同名属性会自动去除重复列。

也可以用 `USING` 指定同名属性连接
```sql
SELECT *
    FROM R
    INNER JOIN S USING (A);
```
要注意连接后指定的同名属性 A 只会保留一列。

#### 外连接

外连接可以保留不符合连接条件的数据行。一般如果没有匹配数据行，则保留左边表的数据，用 `NULL` 填充右边表的数据。

- 左外连接

    ```sql
    SELECT R.A, R.B, S.C
        FROM R  --R表在左边
        LEFT JOIN S ON R.A = S.A;
    ```
    或者写成
    ```sql
    SELECT R.A, R.B, S.C
        FROM R  --R表在左边
        LEFT JOIN S USING A;
    ```

- 右外连接

    ```sql
    SELECT R.A, R.B, S.A, S.C
        FROM R  --R表在右边
        RIGHT JOIN S ON R.A = S.A;
    ```
    或者写成
    ```sql
    SELECT R.A, R.B, S.A, S.C
        FROM R  --R表在右边
        RIGHT JOIN S USING A;
    ```

- 全外连接：保留两表所有数据行，无法匹配的补 `NULL`

    ```sql
    SELECT R.A, R.B, S.A, S.C
        FROM R
        FULL JOIN S ON R.A = S.A;
    ```

    >⚠️全外连接不一定满足结合律！

