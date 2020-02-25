# Matplotlib 数据可视化

> 本文主要参考自 _Python Data Science Handbook by Jake VanderPlas (O’Reilly).Copyright 2017 Jake VanderPlas,978-1-491-91205-8_

Matplotlib 是建立在 NumPy 数组基础上的多平台数据可视化程序库，最初被设计用于完善 SciPy 的生态环境。

Matplotlib 最重要的特性之一就是具有良好的操作系统兼容性和图形显示底层接口兼容性（graphics backend）。

## 常用技巧

### 导入 Matplotlib

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
```

### 设置绘图风格

```python
plt.style.use('classic')
```

### 如何显示图形

取决于具体的开发环境：

- **在脚本中画图**：必须使用 plt.show()。
  plt.show() 会启动一个事件循环（event loop），并找到所有当前可用的图形对象，然后打开一个或多个交互式窗口显示图形。

- **在 IPython shell 中画图**： 使用魔法命令：`%matplotlib`此后的任何 plt 命令都会自动打开一个图形窗口，增加新的命令，图形就会更新。对于某些不会自动及时更新的变化，可以使用 `plt.draw()` 强制更新。
- **在 IPython Notebook 中画图**: 将图形直接嵌在 IPython Notebook 页面中: 1. `%matplotlib notebook # 会在 Notebook 中启动交互式图形。` 2.`%matplotlib inline # 会在 Notebook 中启动静态图形。`

### 将图形保存为文件

```python
plt.savefig('my_figure.png')
```

## 两种画图接口

#### 便捷的 Matlab 风格接口

这种接口最重要的特性是有状态的（stateful）：它会持续跟踪“当前的”图形和坐标轴，所有 plt 命令都可以应用。你可以用 plt.gcf()（获取当前图形）和 plt.gca()（获取当前坐标轴）来查看具体信息。

```python
%matplotlib inline
import numpy as np
plt.figure()  # create a plot figure

# create the first of two panels and set current axis
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))

# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x));
```

#### 功能强大的面向对象接口

在面向对象接口中，画图函数不再受到当前“活动”图形或坐标轴的限制，而变成了显式的 Figure 和 Axes 的方法。

```python
import numpy as np
x = np.linspace(1,10,100)
# 先创建图形网格
# ax是一个包含两个Axes对象的数组
fig, ax = plt.subplots(2)
# 在每个对象上调用plot()方法
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
```

在画简单图形时，选择哪种绘图风格主要看个人喜好，但是在画比较复杂的图形时，面向对象方法会更方便。

## 简易线形图

首先用面向对象的方式，画一个简单的图像和坐标

```python
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

fig = plt.figure()
ax = plt.axes()
```

有坐标 axes 之后，我们可以就利用 ax.plot()画图了。

```python
fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x));
```

现在使用另外一种 matlab 接口风格进行画图

```python
plt.plot(x, np.sin(x));
```

### 调整图形：线条的颜色和风格

```python
plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported
```

线条风格，利用`linestyle`关键字

```python
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');
# 简写
plt.plot(x, x + 4, linestyle='-')  # 实线
plt.plot(x, x + 5, linestyle='--') # 虚线
plt.plot(x, x + 6, linestyle='-.') # 点划线
plt.plot(x, x + 7, linestyle=':') # 实点线
```

不同风格的线条，简便形式：

```python
plt.plot(x, x + 0, '-g')  # 绿色实线
plt.plot(x, x + 1, '--c') # 青色虚线
plt.plot(x, x + 2, '-.k') # 黑色点划线
plt.plot(x, x + 3, ':r') # 红色实点线
```

### 调整图形： 坐标轴上下限

基础方法：使用`plt.xlim()` 和 `plt.ylim()`

```python
plt.plot(x, np.sin(x))
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)
```

方法二：利用 `plt.axis()`关键字

```python
plt.plot(x, np.sin(x))
plt.axis([-1, 11, -1.5, 1.5]);
```

```python
plt.plot(x, np.sin(x))
plt.axis('tight') # 按照图形的内容自动收紧坐标轴，不留空白区域
plt.axis('equal') # 让屏幕上显示的图形分辨率为 1:1，x 轴单位长度与 y 轴单位长度相等
```

### 设置图形标签

```python
plt.title("title")
plt.xlabel("x")
plt.ylabel("sin(x)")
```

#### 配置图例

```python
plt.plot(x,np.sin(x),'-g',label='sin(x)')
plt.plot(x,np.cos(x),':b',label='cos(x)')
plt.axis('equal')
plt.legend() # legend将每条线的标签与其风格、颜色自动匹配。
plt.legend(loc='upper left', frameon=False) # 设置图例位置，取消外边框
# 更多配置查询legend的文档
```

## 简易散点图

### 用 plt.plot 画散点图

函数的第三个参数是一个字符，表示图形符号的类型，例如：`'o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd'`

```python
x = np.linspace(0, 10, 30)
y = np.sin(x)
plt.plot(x, y, 'o', color='black')
```

另外，plt.plot 支持许多设置线条和散点属性的参数，例如：

```python
plt.plot(x, y, '-p', color='gray',
                markersize=15, linewidth=4,
                markerfacecolor='white',
                markeredgecolor='gray',
                markeredgewidth=2)
plt.ylim(-1.2, 1.2)
```

### 用 plt.scatter 画散点图

```python
plt.scatter(x, y, marker='o');
```

plt.scatter 具有更高的灵活性，可以单独控制每个散点与数据匹配，也可以让每个散点具有不同的属性（大小、表面颜色、边框颜色等）。\
下面来创建一个随机散点图，里面有各种颜色和大小的散点。为了能更好地显示重叠部分，用 alpha 参数来调整透明度:

```python
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar();  # show color scale
```

## 注释

### 文字注释

可以通过 `plt.text/ax.text` 命令手动添加注释，它们可以在具体的 x / y 坐标点上放上文字。

### 箭头注释

推荐使用 `plt.annotate()` 函数。这个函数既可以创建文字，也可以创建箭头，而且它创建的箭头能够进行非常灵活的配置。

## **用 Seaborn 做数据可视化**

Seaborn 在 Matplotlib 的基础上开发了一套 API，为默认的图形样式和颜色设置提供了理智的选择，为常用的统计图形定义了许多简单的高级函数，并与 Pandas DataFrame 的功能有机结合。

```python
import seaborn as sns
sns.set()
```
