---
kstitle: NumPy intro
summary: NumPy feature summary
authors:
   - roseau
date: 2019-11-29
lastUpdate: 2019-11-29
---

# NumPy 入门

```
title: NumPy intro
summary: NumPy feature summary
authors:
   - roseau
date: 2019-11-29
lastUpdate: 2019-11-29
```

> 本文主要参考自 *Python Data Science Handbook by Jake VanderPlas (O’Reilly).Copyright 2017 Jake VanderPlas,978-1-491-91205-8*

### 一、Numpy简介

> NumPy是Python语言的一个扩展程序库。支持高端大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/1200px-NumPy_logo.svg.png" style="zoom: 33%;" />

NumPy引入了多维数组以及可以直接有效率地操作多维数组的函数与运算符。因此在NumPy上只要能被表示为针对数组或矩阵运算的算法，其运行效率几乎都可以与编译过的等效C语言代码一样快。

NumPy提供了高效存储和操作密集数据缓存的接口。在某些方面，NumPy数组与Python内置的列表类型非常相似。但是随着数组在维度上的变大，NumPy提供了更加高效的存储和数据操作。**NumPy几乎是整个Python数据科学工具生态系统的核心。**

一般来说，我们使用`import numpy as np`来使用NumPy。

### 二、理解Python中的数据类型

Python为了获得灵活的类型，列表中的每一项都必须包含各自的类型信息，也就是，每一项都是一个完整的Python对象。

不同于Python列表，**Numpy要求数组必须包含同一类型的数据**。如果类型不匹配，NumPy将会向上转换。如果希望明确设置数组的数据类型，可以用`dtype`关键字：

```python
import numpy as np
np.array([1,2,3,4], dtype=float32)
```

最后，不同于Python列表，NumPy可以被指定为多维的。

面对大型数组的时候，用numpy内置的方法从头创建数组是一种更高效的方法，示例如下：

```python
In[12]: 创建一个长度为10的数组，数组的值都是0
        np.zeros(10, dtype=int)

Out[12]: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

In[13]: # 创建一个3×5的浮点型数组，数组的值都是1
        np.ones((3, 5), dtype=float)

Out[13]: array([[ 1.,  1.,  1.,  1.,  1.],
                [ 1.,  1.,  1.,  1.,  1.],
                [ 1.,  1.,  1.,  1.,  1.]])

In[14]: # 创建一个3×5的浮点型数组，数组的值都是3.14
        np.full((3, 5), 3.14)
Out[14]: array([[ 3.14,  3.14,  3.14,  3.14,  3.14],
                [ 3.14,  3.14,  3.14,  3.14,  3.14],
                [ 3.14,  3.14,  3.14,  3.14,  3.14]])

In[15]: # 创建一个3×5的浮点型数组，数组的值是一个线性序列
        # 从0开始，到20结束，步长为2
        # （它和内置的range()函数类似）
        np.arange(0, 20, 2)

Out[15]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

In[16]: # 创建一个5个元素的数组，这5个数均匀地分配到0~1
        np.linspace(0, 1, 5)

Out[16]: array([ 0.  ,  0.25,  0.5 ,  0.75,  1. ])

In[17]: # 创建一个3×3的、在0~1均匀分布的随机数组成的数组
        np.random.random((3, 3))

Out[17]: array([[ 0.99844933,  0.52183819,  0.22421193],
                [ 0.08007488,  0.45429293,  0.20941444],
                [ 0.14360941,  0.96910973,  0.946117 ]])


In[18]: # 创建一个3×3的、均值为0、方差为1的
        # 正态分布的随机数数组
        np.random.normal(0, 1, (3, 3))

Out[18]: array([[ 1.51772646,  0.39614948, -0.10634696],
                [ 0.25671348,  0.00732722,  0.37783601],”

“                [ 0.68446945,  0.15926039, -0.70744073]])

In[19]: # 创建一个3×3的、[0, 10)区间的随机整型数组
        np.random.randint(0, 10, (3, 3))

Out[19]: array([[2, 3, 4],
                [5, 7, 8],
                [0, 5, 0]])

In[20]: # 创建一个3×3的单位矩阵
        np.eye(3)

Out[20]: array([[ 1.,  0.,  0.],
                [ 0.,  1.,  0.],
                [ 0.,  0.,  1.]])

In[21]: # 创建一个由3个整型数组成的未初始化的数组
        # 数组的值是内存空间中的任意值
        np.empty(3)

Out[21]: array([ 1.,  1.,  1.])”

Excerpt From: [美] Jake VanderPlas. “Python数据科学手册.” Apple Books. 
```

### 三、NumPy数组基础

Python 中的数据操作几乎等同于 NumPy 数组操作，甚至新出现的 Pandas 工具（之后介绍）也是构建在 NumPy 数组的基础之上的。

#### 1、数组的属性

- ndim 数组维度
- shape 数组每个维度的大小
- size 数组的大小
- dtype 数组的数据类型

#### 2、数组索引

- 中括号指定索引值
- 多维数组中，采用逗号分隔的索引元组
- 数组切片：x[start:stop:step]
- 空切片 ( : ) 用来获取数组的行和列
- **数组切片返回的是数组数据的视图，如果修改子数组，原始数组也被修改**
- 利用 copy() 明确复制数据，此时子数组对原始数组无影响

#### 3、数组变形

- reshape（）实现灵活的数组变形
- 利用 newaxis 关键字将一个一维数组转变为二维的行或列的矩阵

#### 4、数组的拼接和变形

- 拼接或连接两个数组：np.concatenate np.vstack np.hstack 

- 分裂：np.split np.hsplit np.vsplit，参数为索引列表，记录分裂点的位置


### 四、NumPy数组的计算：通用函数

NumPy 为很多类型的操作提供了非常方便的、静态类型的、可编译程序的接口，也被称作向量操作。你可以通过简单地对数组执行操作来实现，这里对数组的操作将会被用于数组中的每一个元素。这种向量方法被用于将循环推送至 NumPy 之下的编译层，这样会取得更快的执行效率。

通过通用函数用向量的方式进行计算几乎总比用 Python 循环实现的计算更加有效，尤其是当数组很大时。只要你看到 Python 脚本中有这样的循环，就应该考虑能否用向量方式替换这个循环。

- 数组的运算：标准的加减乘除、逻辑非、`**` 表示的指数运算和`%`表示的模运算
- 绝对值 np.abs()
- 三角函数
- 指数和对数
- 很多通用函数，包括双曲三角函数、比特位运算、比较运算符、弧度转化为角度的运算、取整和求余运算，等等。
- 还有一个更加专用，也更加晦涩的通用函数优异来源是子模块 scipy.special。如果你希望对你的数据进行一些更晦涩的数学计算，scipy.special 可能包含了你需要的计算函数”

高级的通用函数特性：

- 指定输出：所有通用函数都可通过out参数来指定计算结果存放的位置

- 聚合：一个reduce方法会对给定的元素和操作重复执行，直至得到单个的结果，如果需要存放每次计算的中间结果，可以使用accumulate。在一些特殊情况中，NumPy提供了专用的函数（np.sum、np.prod、np.cumsum、np.cumprod ），它们也可以实现以上 reduce 的功能

- 任何通用函数都可以用 outer 方法获得两个不同输入数组所有元素对的函数运算结果。

### 五、聚合：最小值、最大值和其他值

NumPy 有非常快速的内置聚合函数可用于数组：

- 数组值求和：np.sum
- 最小值和最大值：np.min np.max 
- 多维度聚合：聚合函数参数axis可以指定沿着哪个轴的方向进行聚合

Numpy中可用的聚合函数：
函数名称	NaN安全版本	描述
np.sum	np.nansum	计算元素的和
np.prod	np.nanprod	计算元素的积
np.mean	np.nanmean	计算元素的平均值
np.std	np.nanstd	计算元素的标准差
np.var	np.nanvar	计算元素的方差
np.min	np.nanmin	找出最小值
np.max	np.nanmax	找出最大值
np.argmin	np.nanargmin	找出最小值的索引
np.argmax	np.nanargmax	找出最大值的索引
np.median	np.nanmedian	计算元素的中位数
np.percentile	np.nanpercentile	计算基于元素排序的统计值
np.any	N/A	验证任何一个元素是否为真
np.all	N/A	验证所有元素是否为真

### 六、数组的计算：广播broadcast

广播可以简单理解为用于不同大小数组的二进制通用函数（加、减、乘等）的一组规则。

![](https://raw.githubusercontent.com/RoseauHan/upic/master/31rD3t.png)

广播的规则：

- 如果两个数组的维度数不相同，那么小维度数组的形状将会在最左边补 1。
- 如果两个数组的形状在任何一个维度上都不匹配，那么数组的形状会沿着维度为 1 的维度扩展以匹配另外一个数组的形状。
- 如果两个数组的形状在任何一个维度上都不匹配并且没有任何一个维度等于 1，那么会引发异常

### 七、比较、掩码和布尔逻辑

- NumPy 还实现了如 <（小于）和 >（大于）的逐元素比较的通用函数。
- 利用布尔数组统计记录的个数
- np.all() 和np.any() 也可以用于沿着特定的坐标轴

- 利用布尔运算符
- 将布尔数组作为掩码，通过掩码选择数据的字数据集
- and 和 or 判断整个对象是真或假，而 & 和 | 是指每个对象中的比特位。

### 八、花哨的数组 fancy indexing 

花哨的索引和前面那些简单的索引非常类似，但是传递的是索引数组，而不是单个标量。花哨的索引让我们能够快速获得并修改复杂的数组值的子数据集。

利用花哨的索引，结果的形状与索引数组的形状一致，而不是与被索引数组的形状一致。

花哨的索引可以和其他索引方案结合起来形成更强大的索引操作。

花哨的索引的一个常见用途是从一个矩阵中选择行的子集


### 九、其他资料

NumPy的核心功能是"ndarray"(即n-dimensional array，多维数组)数据结构。这是一个表示多维度、同质并且固定大小的数组对象。而由一个与此数组相关系的数据类型对象来描述其数组元素的数据格式(例如其字符组顺序、在存储器中占用的字符组数量、整数或者浮点数等等)。

1. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_web.png" alt="web" style="zoom:15%;" /> https://numpy.org](https://numpy.org)
2. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_doc.png" alt="docu" style="zoom:15%;" /> Quickstart tutorial ](https://numpy.org/devdocs/user/quickstart.html)
3. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> 安装文档](https://scipy.org/install.html)
4. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> numpy devdocs](https://numpy.org/devdocs/)
5. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_git.png" alt="git" style="zoom:15%;" /> NumPy ](https://github.com/numpy/numpy)
6. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_wiki.png" alt="wiki" style="zoom:15%;" /> NumPy](https://zh.wikipedia.org/zh-cn/NumPy)