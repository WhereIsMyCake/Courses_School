# K-Nearest Neighbor and the Bias-Variance Trade-Off

## 1 回归模型

定义回归模型

$$
Y = f(X) + \epsilon ，
$$ 

其中：

 - $Y$ 是观测值，实际会发生的情况，

 - $f(X)$ 是真值，一个完美的函数关系，

 - $\epsilon$ 是噪声，是满足 $E(\epsilon) = 0$ 和 $Var(\epsilon) = \sigma^2$ 的随机变量。

目标是在收集到的训练集 $D_n = \{x_i, y_i \}_{i=1}^n$ 上，找到这个模型的近似规律，记为 $\hat{f}$ ；并通过已知数据 $X$ ，利用这个规律预测 $Y$ 。

!!! hint "注意"

    #待补充

## 2 k-近邻算法

### 概念

kNN 是一种非参数化方法，它不预先假设 $f(X)$ 的具体数学形式，而是根据目标点 $x_0$ 的邻近点的值预测它对应的 $y_0$ 的值，记为 $\hat{f}(x_0)$ 。

kNN 可以用于回归，即预测具体数值；也可以用于分类，即预测类别。

### 预测回归模型

对于已知的目标点 $x_0$ ，预测值为附近 $k$ 个样本的平均值

$$
\hat{y_0} = \frac{1}{k} \sum_{x_i \in N_k(x_0)} y_i ，
$$

其中 $N_k(x_0)$ 是离 $x_0$ 最近的 $k$ 个样本的集合。

!!! hint "注意"

    kNN 中的“最近”，可能是欧式距离最近，也可能是其他情况。

## 3 偏差-方差权衡

我们需要引入方法评价模型预测的准确性。

### 方差

方差描述的是模型预测的稳定性，即在不同的训练集上预测 $\hat{f}(x_0)$ 的波动程度。

对于目标点 $x_0$ 的预测值 $\hat{f}(x_0)$ ，方差为

$$
Var(\hat{f}(x_0)) = E[(\hat{f}(x_0) - E[\hat{f}(x_0)])^2] 。
$$

### 偏差

偏差描述的是模型预测的系统性偏离，即预测与真值的差距。

对于目标点 $x_0$ 的预测值 $\hat{f}(x_0)$ ，偏差为

$$
Bias(\hat{f}(x_0)) = f(x_0) - E[\hat{f}(x_0)] 。
$$

### 平方误差损失

平方误差损失衡量了模型预测的误差来源

$$
Err(x_0) = \sigma^2 + Bias^2 + Var 。
$$

??? note "平方误差损失公式推导"
    
    $$
    Err(x_0) = E_{D_n, Y_0}[(Y_0 - \hat{f}(x_0))^2]
    $$

    #待学习

!!! hint "从 1NN 到 kNN"

    #待补充

## 4 模型选择

我们需要引入模型复杂度和自由度的概念，来决定 k 的合适取值。

### 过拟合与欠拟合

- k 很小，容易过拟合。

- k 很大，容易欠拟合。

### 模型复杂度

在 kNN 中，k 决定了模型复杂度。

### 自由度

定义自由度为

$$
df(\hat{f}) = \frac{1}{\sigma^2} \sum_{i=1}^n Cov{(\hat{Y}_i, Y_i)} 。
$$

??? note "自由度定义公式化简"

    记 $\hat{Y} = (\hat{Y}_1, \cdot , \hat{Y}_n)$ 和 $Y = (Y_1, \cdot , Y_n)$ ，则自由度可表示为

    $$
    df(\hat{f}) = \frac{1}{\sigma^2} Trace(Cov(\hat{Y}, Y)) 。
    $$

    #待学习

在 kNN 中有 $df = \frac{n}{k}$ 。

### K 折交叉验证

为了选择较优的 k ，采用 K 折交叉验证：
 
 - 将数据随机分为 K 份（一般取 $K = 10$ ），
 
 - 每次用 K-1 份作为训练集，

 - 用剩余的 1 份作为测试集并计算测试误差，

 - 遍历所有情况，计算平均测试误差。

!!! hint "留一法" 

    当取 $K = n$ 时的特殊交叉验证方法，在训练集很小时比较有用，训练集很大时计算时间很长。


## 5 分类模型

kNN 分类的本质是估计条件概率

$$
P(Y = c|X = x_0) ，
$$

即给定特征 $x_0$ ，属于类别 $c$ 的概率。

通过检查 $x_0$ 周围的 k 个点的类别，估计这个概率

$$
\hat{P}(Y = c|X = x_0) = \frac{1}{k} \sum_{x_i \in N_k(x_0)} 1\{y_i = c\} 。
$$

让这个概率最大，就是最有可能的 $x_0$ 属于的类别

$$
\hat{y} = \arg{\max{\sum_{x_i \in N_k(x_0)} 1\{y_i = c\}}} 。
$$

### 贝叶斯错误率

贝叶斯错误率描述了分类问题的误差边界，即完美分类器也无法消除的误差

$$
Bayes Error = 1 - E[\max_c P(Y = c | X)] 。
$$

### 1NN 的理论边界

当样本量 $n \to \infty$ 时，1NN 的错误率最高不会超过贝叶斯错误率的两倍。

## 总结

### 距离度量

### 纬度灾难

### 双重下降


??? hint "英语词汇表"

    k-Nearest Neighbor k-近邻算法

    Regression Model 回归模型

    Independent and Identically Distributed 独立同分布

    Nonparametric Method 非参数方法

    Neighborhood 邻域

    Majority Vote 多数投票制

    Indicator Function 指示函数

    Bias-Variance Trade-off 偏差-方差权衡

    Irreducible Error 不可约误差

    Mean Squared Error 均方误差

    Overfitting 过拟合

    Underfitting 欠拟合

    Conditional Class Probabilities 条件类别概率

    Decision Boundary 决策边界

    Bayes Classifier 贝叶斯分类器

    Bayes Error Rate 贝叶斯错误率

    K-fold Cross Validation K-折交叉验证

    Curse of Dimensionality 维度灾难

    Double Descent 双下降现象



