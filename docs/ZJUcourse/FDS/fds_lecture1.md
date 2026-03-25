# Algorithm Analysis

## 0 什么是算法

### 定义

算法 Algorithm 是指为了完成特定任务而规定的一组有限的指令序列。

### 特点

- input 有零个或多个外部提供的参数。

- output 至少有一个结果。

- definiteness 指令必须清晰、无歧义。

- finiteness 算法必须在执行有限步后结束。

- effectiveness 算法必须有效可行。

## 1 算法分析

### 分析维度

- 运行时间 run times：会受硬件和编译器的影响。

- 时间与空间复杂度 time & space complexities：独立于硬件和编译器，是算法分析的重点。

### 基本假设

为了比较不同算法，给出理性化的计算模型：

- 指令按顺序执行，不考虑并行；
- 每条指令简单并且耗费一个单位时间；
- 整数大小固定，并且拥有无限大的内存。

### 时间复杂度函数

设输入规模为 $N$ ，引入函数 $T(N)$ ：

- $T_{avg}(N)$ 在所有可能的输入情况下，算法运行时间的平均值。

- $T_{worst}(N)$ 在最不利的输入情况下，算法运行时间的最大值。

## 2 渐进表示法 Asymptotic Notation

### 目的

预测当输入规模 $N$ 改变时，运行时间如何增长；据此可以比较处理大规模数据时算法的表现。

### 数学表达式

- 大 O 表示法：$T(N) = O(f(N))$

    - 要求存在正整数 $c$ 和 $n_0$ ，使得当 $N \ge n_0$ 时有 $T(N) \le c \cdot f(N)$ 。
    - 实际上刻画了算法的上界。

- 大 Omega 表示法：$T(N) = \Omega (g(N))$

    - 要求存在正整数 $c$ 和 $n_0$ ，使得当 $N \ge n_0$ 时有 $T(N) \ge c \cdot g(N)$ 。
    - 实际上刻画了算法的下界。

- 大 Theta 表示法：$T(N) = \Theta (h(N))$

    - 要求 $T(N) = O(h(N)) = \Omega (h(N))$ 。
    - 表示了算法的阶数。

- 小 o 表示法：$T(N) = o(p(N))$

    - 要求 $T(N) = O(p(N))$ 且 $T(N) \ne \Theta (p(N))$ 。
    - 表示 $T(N)$ 严格小于 $p(N)$ 的增长。

## 3 Compare the Algorithms

### Divide and Conque

??? note "找到和最大的子序列"

    每次把序列从中间切分，寻找左边、右边、中间的和最大子序列。


### On-line Algorithm

??? note "找到和最大的子序列"

    ```c
    int MaxSubsequenceSum(const int A[], int N){ 
        int ThisSum, MaxSum, j; 
        ThisSum = MaxSum = 0; 
        for (j = 0; j < N; j++){ 
            ThisSum += A[j]; 
     	    if (ThisSum > MaxSum) 
         		MaxSum = ThisSum; 
     	    else if (ThisSum < 0) 
         		ThisSum = 0;
        }  
        return MaxSum; 
    } 
    ```

    这个算法的复杂度为 $T(N) = O(N)$ 。

## 4 Logarithms in the Running Time

??? note "二分查找 Binary Search"

    ```c
    int BinarySearch (const ElementType A[], ElementType X, int N){ 
        int  Low, Mid, High; 
        Low = 0;  
        High = N - 1; 
        while (Low <= High){ 
     	    Mid = (Low + High) / 2; 
     	    if (A[Mid] < X) 
     		    Low = Mid + 1; 
     	    else if (A[Mid] > X) 
     		    High = Mid - 1; 
            else 
     		    return  Mid;  
        }  
     	return NotFound;  
    } 
    ```

    这个算法的复杂度为 $T(N) = O(\log{N})$ 。

