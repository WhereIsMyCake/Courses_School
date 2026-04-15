# Penalized Linear Regression

## 1 收缩方法 Shrinkage Methods

面对复杂数据时，使用普通最小二乘法 OLS 求解线性回归模型的参数存在计算精度和计算成本上的问题。

!!! hint "最小二乘法"

    最小二乘法是一种简单的最小化经验风险来求解模型的方法，目标是

    $$
    \min_{\beta}{||y - X \beta||^2} ,
    $$

    但是它只关注对训练数据集的拟合效果，而忽略了方差，复杂情况下预测准确度不一定好。


因此，引入收缩方法，它通过给模型加上一点偏差，换取大幅度的方差的降低，或者说就是对模型进行正则化。

本节我们讨论两种正则化：

 - $l_1$ 罚项：Lasso

 - $l_2$ 罚项：岭回归

## 2 岭回归 Ridge Regression

岭回归是最基础的正则化方法，它通过引入惩罚系数的平方和来防止系数过大

$$
\hat{\beta}_{ridge} = \arg{\min_{\beta}{||y - X \beta||^2 + \lambda ||\beta||^2}}
$$

其中 $\lambda \ge 0$ 是调节参数，控制正则化的程度。

等价的表达式为

$$
\min_{\beta}{\sum_{i=1}^n (y_i - \sum_{j=1}^p \beta_j x_{ij})^2} \\
s.t. \quad \sum_{j=1}^p \beta_j^2 \le s
$$

这里的参数 $s$ 和之前的参数 $\lambda$ 有一一对应的关系。

岭回归可以用于解决多重共线性的问题，即存在许多相关的变量时，一个变量的正系数可能被它的相关变量的负系数抵消，岭回归通过施加大小约束来缓解这个问题。

### 求解

通过求导得到岭回归的解

$$
\hat{\beta}_{ridge} = (X^T X + \lambda I)^{-1} X^T y
$$

其中 $I$ 是单位矩阵。

如果最小二乘法求解 $\beta_{OLS}$ 存在的话，也可以写成

$$
\hat{\beta}_{ridge} = (X^T X + \lambda I)^{-1} (X^T X) \hat{\beta}_{OLS} ,
$$

即岭回归求解可以看作最小二乘法求解的一个线性变换。

### 方差

岭回归的方差是关于 $\lambda$ 的单调递减函数

$$
Var(\hat{\beta}_{ridge}) = \sigma^2 (X^T X + \lambda I)^{-1} X^T X(X^T X + \lambda I)^{-1} ,
$$

相比最小二乘法的方差更小。

### 偏差

岭回归是有偏估计，平方偏差是关于 $\lambda$ 的单调递增函数。相比与无偏的最小二乘法，岭回归求解的期望为

$$
E[\hat{\beta}_{ridge}] = (X^T X + \lambda I)^{-1} (X^T X) \beta .
$$

## 3 最小绝对收缩和选择算子 Lasso

岭回归能把系数压缩向非常接近 0 ，而 Lasso 能使某些系数直接变成 0 ，实现变量选择

$$
\hat{\beta}_{lasso} = \arg{\min_{\beta}{||y - X \beta||^2 + \lambda |\beta|}}.
$$

等价的表达式为

$$
\min_{\beta}{\sum_{i=1}^n (y_i - \sum_{j=1}^p \beta_j x_{ij})^2} \\
s.t. \quad \sum_{j=1}^p |\beta_j| \le s
$$

其中 $s$ 和 $\lambda$ 具有一一对应关系。

## 4 Oracle 性质

处理高维数据时，我们假设模型是稀疏的，即 $p$ 维的输入数据里只有 $p_0$ 个维度对输出结果有影响，那么一个好的估计量 $\beta$ 需要满足：

 - 选择一致性：能选对 $p_0$ 个有用维度，剔除无效的维度；

 - 渐近正态性：选出来的变量系数的估计速度，要达到和预先就知道哪些是正确变量并只用它们做 OLS 一样的最优速率。

之前我们引入惩罚项的缩减方法还没有实现这个性质，接下来提出两种改进思路：

 - 偏差校正 Bias Correction ：调整求解系数的权重

 - 无偏惩罚 Unbiased Penalties ：修改惩罚项函数的形式

## 5 偏差校正

### Non-Negative Garrote

假定我们通过最小二乘法已经找到了初始估计量 $\hat{\beta}_{OLS}$ ，那么现在的目标是找到一组非负的缩减因子 $d_j$ 并确定新的系数 $\hat{\beta}_j^{ng} = d_j \hat{\beta}_j^{OLS}$ 。

目标函数变成

$$
\min_{d}{\frac{1}{2n} ||y - \sum_{j=1}^p d_j \hat{\beta}_j^{OLS} x_j||^2 + \lambda \sum_{j=1}^p d_j} \\
s.t. \quad d_j \ge 0 .
$$

求解之后，如果原本系数很小的话，那么缩减因子会把它缩减到接近 0 ，而如果原本系数很大，那么缩减因子几乎不会缩减它。

!!! hint "系数大小的含义"

    系数的绝对值大，表示这个特征对结果的影响强；系数的绝对值小，表示这个特征对结果的影响弱。

### 自适应 Lasso

Lasso 引入的惩罚参数 $\lambda$ 对所有系数效果一样，为了改进这一点，我们增加一个按照系数大小分配的权重 $\omega$ 

$$
\omega_j = \frac{1}{\gamma \cdot |\hat{\beta}_{init}|}
$$

其中 $\gamma$ 是一个大于 0 的常数；$\hat{\beta}_{init}$ 是初始估计量，可以由 OLS 或岭回归估计。

现在 Lasso 求解的目标变成

$$
\hat{\beta} = \arg{\min_{\beta}{||y - X \beta||^2 + \lambda \sum_{j=1}^p \omega_j |\beta_j|}}.
$$

## 6 无偏惩罚

!!! note "惩罚函数应该具有的性质"

    - Sparsity 估计量把不重要的变量压缩成 0

    - Continuity 估计量对数据的微小变化不敏感

    - Unbiasedness 真实系数 $\beta$ 很大的时候，估计量几乎没有偏差

### Smoothly Clipped Absolute Deviation

SCDA 是一个分段惩罚函数，它的导数（即惩罚力度）随着 $\beta$ 增大而减小

$$
P(\beta) = 
\begin{cases}
\lambda |\beta| ,& |\beta| \le \lambda \\
\frac{2 \gamma \lambda |\beta| - \beta^2 - \lambda^2}{2(\gamma -1)} ,& \lambda < |\beta| < \gamma \lambda \\
\frac{\lambda^2 (\gamma + 1)}{2} ,& |\beta| \ge \gamma \lambda \\
\end{cases}
$$

其中 $\lambda > 0$ 并且 $\gamma > 2$ 。 

当真实系数很小的时候，SCDA 把它向 0 压缩，保证稀疏性；随着真实系数增大，SCDA 的惩罚力度线性减小，达到某个阈值后不再增加惩罚，这时估计量几乎是无偏的。

### Minimax Concave Penalty

MCP 也是一个分段惩罚函数，它减小惩罚力度的速度比 SCDA 更快

$$
P(\beta) = 
\begin{cases}
\lambda |\beta| - \frac{\beta^2}{2 \gamma} ,& |\beta| \le \gamma \lambda \\
\frac{1}{2} \gamma \lambda^2 ,& |\beta| \ge \gamma \lambda \\
\end{cases}
$$

其中 $\gamma > 1$ 。 

## 7 特殊数据结构的惩罚项

之前的惩罚项，是把输入数据 $X$ 的每一个维度（特征）独立看待的。但是，各个维度可能存在相关性，因此惩罚项的设计应该考虑到相互关系。