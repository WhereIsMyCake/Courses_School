# The Disjoint Set ADT

## 1 等价关系 Equivalence Relations

### 一些定义

- 如果对于集合 $S$ 中的任意一对元素 $(a, b)$ ，关系 $a R b$ 要么为真、要么为假，如果关系为真，那么就说 $a$ 与 $b$ 相关，记作 $a$ ~ $b$ 。

- 如果一个集合 $S$ 上的某个关系同时满足对称性、自反性、传递性，则称该关系为 $S$ 上的等价关系。

    - 对称性 symmetric 

    - 自反性 reflexive 

    - 传递性 transitive 

- 如果集合 $S$ 中的两个元素 $x$ 和 $y$ 满足 $x$ ~ $y$ ，则称它们属于同一个等价类 equivalence class 。


## 2 动态等价问题 The Dynamic Equivalence Problem

### 问题

给定多个等价对，判断任意两个元素 $a$ 和 $b$ 是否满足等价关系。

对此，我们需要完成两类操作：
 
 - Find(i) ：判断一个元素属于哪个集合

 - Union(i, j) ：将两个不相交的集合合并为一个集合

### 示例

 Given S = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 } and 9
relations: 12~4, 3~1, 6~10, 8~9, 7~4, 6~8, 3~5, 2~11, 11~12.

考虑动态、在线的算法：
```c
Algorithm: (Union / Find)
{   
    // each element is a set at first
    Initialize N disjoint sets;
    
    // step 1: read the relations in 
    while (read in a ~ b){
        if (Find(a) != Find(b))
            Union the two sets;
    } 
    
    // step 2: decide if a ~ b 
    while (read in a and b){ 
        if (Find(a) == Find(b))   
            output(true);
        else   
            output(false);
    }
}
```


## 3 基础数据结构

### 3.1 并查集

一般用树来表示，一棵树表示一个集合，每个节点保存指向父节点的指针。



### 3.2 Union(i, j)

#### Implementation I

用一个数组来存储每个元素所属的集合名称，数组索引就是元素编号，需要遍历数组将所有属于集合 $i$ 的元素修改成属于集合 $j$ 。

这种合并方式每次时间复杂度为 $O(N)$ ，效率很低。

#### Implementation II

用一个数组来存储每个元素的父节点编号，数组索引是元素本身的编号，如果是根节点则存储 0 。

现在进行合并可以直接修改一棵树的根节点存储的父节点编号，时间复杂度为 $O(1)$ 。

### 3.3 Find(i)

#### Implementation I

通过数组索引访问的内容就是该元素所属的集合。

#### Implementation II

沿着路径向上找根节点，时间复杂度和树的深度有关

```c
SetType  Find (ElementType X, DisjSet S){   
    for (; S[X] > 0; X = S[X]);   
    
    return X;
}
```

### 3.4 分析

按照第二种思路，`union()` 和 `find()` 操作成对出现时，并查集构建的树在最坏的情况下会退化成一个链表，时间复杂度变为 $O(N^2)$ 。

## 4 Smart Union Algorithms

考虑在合并集合的时候控制树的形态，防止 `find()` 的时间复杂度太大。

### 4.1 Union by Size

主要思路是统计两棵树各自的节点数量，把节点数少的树连接到节点数多的树的根部。

原来根节点存储的父节点编号规定为 0 ，现在我们把它改成一个负数，绝对值就是这棵树的节点数；即初始化时每个节点的父节点编号都为 -1 。

这样子构造树，`find()` 的时间复杂度变为 $O(\log{N})$ 。


### 4.2 Union by Height

主要思路是将高度较矮的树连接到高度较高的树的根部。

仍然可以用根节点存储的内容记录这棵树的高度。

## 5 Path Compression

考虑提升 `find()` 算法的效率。

主要思路是把一条路径上的节点都直接连接到根节点上，相当于把树的深度降下来。

递归实现
```c
SetType Find(ElementType X, DisjSet S) {
    if (S[X] <= 0)
        return X;
    else
        return S[X] = Find( S[X], S ); 
}
```

迭代实现
```c
SetType Find (ElementType X, DisjSet S){
    ElementType root, trail, lead;

    // find the root
    for (root = X; S[root] > 0; root = S[root]);  

    for (trail = X; trail != root; trail = lead){
       lead = S[trail];   
       S[trail] = root;   
    } 

    return root;
}
```

!!! warning "注意"

    路径压缩方法与 Union by Height 不兼容，因为会改变树的高度，要优化建议使用 Union by Size。

