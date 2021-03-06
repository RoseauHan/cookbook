# IPython: 超越 Python

> 本文主要参考自 _Python Data Science Handbook by Jake VanderPlas (O’Reilly).Copyright 2017 Jake VanderPlas,978-1-491-91205-8_

### 一、IPython 简介

#### 1、IPython

Python 有很多种开发环境，一个不错的选择是：IPython。

“IPython（interactive Python 的简称，即交互式 Python）由 Fernando Perez 作为一个增强的 Python 解释器于 2001 年启动，并由此发展为一个项目。用 Perez 的原话来说，该项目致力于提供“科学计算的全生命周期开发工具”。如果将 Python 看作数据科学任务的引擎，那么 IPython 就是一个交互式控制面板。”

除了作为 Python 的一个交互式接口，IPython 还提供了一些有用的 Python 语法附加功能，下面就将总结其中最有用的一些。

![](https://raw.githubusercontent.com/RoseauHan/upic/master/ipython_screen.png)


### 二、IPython 常用功能总结

#### 帮助和文档：

- 符号`？`获取文档
- 符号`??`获取源代码
- Tab 补全探索模块
- 反向搜索：`ctrl r`：对历史命令反向搜索

#### IPython 魔法命令：

IPython 提供了一些在普通 Python 语法基础之上的增强功能，这些功能被称作 IPython 魔法命令，都以`%`作为前缀。

主要分为两大类：

:one: 行魔法：`%`前缀，作用于单行输入

:two: 单元魔法：`%%`前缀，作用于多行输入。

常用命令如下：

- `%lsmagic` 所有魔法函数
- `%run` 执行外部代码
- `%timeit` 计算代码执行时间
- `%%timeit` 计算多行代码执行时间 
- `%paste %cpaste` 粘贴代码块 (解决了直接 **粘贴** 时格式会混乱的问题)
- `%history` 一次性获取此前所有的历史输入 (解决了从ipython **复制** 时总有···的烦恼)

>  [%history 1 6-14 可以输出第1行和6到14行的命令。 后面加`-f FILENAME`可以直接将结果写入文件。](https://stackoverflow.com/questions/41070403/how-to-copy-from-ipython-session-without-terminal-prompts)

- `%xmode` 控制异常
- `%debug` 调试
- `%prun` 分析整个脚本

#### 输入输出：
使用ipython shell，你一定对左边这些in，out特别熟悉，但是，它们不是装饰品：
IPython 实际上创建了叫做 In 和 Out 的 Python **变量**，这些变量自动更新以反应命令历史。

- In 是一个 list，而 Out 是一个 Dictionary
- 可以根据数字调用：`In[num] Out[num]`
- 变量 `_`(单下划线)获取前一个输出结果，两条下划线获得倒数第二个历史输出，三条下滑线获得倒数第三个历史输出
- `Out[num]`的简写形式是 `_[num]`
- 禁止一个命令输出：行尾处添加分号
- 命令前添加！，可执行 shell 命令，还可以在 shell 中传入或传出值
- 从Shell向ipython传值：直接写个赋值表达式就可以，等号的右边是Shell命令：`contents = !dir`
- 从ipython向Shell传值：使用{变量名}的形式赋值：`echo {message}`

### 三、IPython 参考资料

- http://ipython.org
- http://nbviewer.ipython.org
- http://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks/

### 四、衍生项目：Jupyter Notebook

另外，IPython 被紧密地连接在 Jupyter 项目（http://jupyter.org）中。该项目提供一个基于浏览器的 Notebook，它可以开发、协作、分享甚至发布数据科学结果。IPython Notebook 其实只是通用 Jupyter Notebook 结构的特例，而 Jupyter Notebook 不仅支持 Python，还包括用于 Julia、R 和其他编程语言的 Notebook。”

> Jupyter 为 Python 提供了方便的交互式数据科学和科学计算平台。Jupyter 物品是一个非营利组织，旨在“为数十种编程语言的交互式计算开发开源软件，开放标准和服务”。

<img src="https://jupyter.org/assets/labpreview.png" alt="jupyter lab" style="zoom: 25%;" />

JupyterLab 1.0: **Jupyter’s Next-Generation Notebook Interface**

JupyterLab is a web-based interactive development environment for Jupyter notebooks, code, and data. JupyterLab is flexible: configure and arrange the user interface to support a wide range of workflows in data science, scientific computing, and machine learning. JupyterLab is extensible and modular: write plugins that add new components and integrate with existing ones.

JupyterLab 是 Jupyter 物品的下一代用户界面。它在一个灵活且强大的用户界面中提供了经典的 Jupyter Notebook（笔记本、终端、文本编辑器、文件浏览器、丰富输出等）所有熟悉的构建模块。第一个稳定版本于 2018 年 2 月 20 日发布。

使用 JupyterLab 你可以方便的进行交互式的数据计算和科学计算，并且 lab 提供了笔记本、终端、文本编辑器、文件浏览器、丰富输出等，非常好用。

1. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_web.png" alt="web" style="zoom:15%;" /> https://jupyter.org](https://jupyter.org)
2. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_doc.png" alt="docu" style="zoom:15%;" /> Installing the Jupyter Software](https://conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
3. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> 安装文档](https://docs.anaconda.com/anaconda/install/)
4. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> Getting started with conda](Getting started with conda)
5. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> Conda Cheat sheet ](https://conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
6. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_cn_doc.png" alt="cn_doc" style="zoom:15%;" /> [译] 给初学者的 Jupyter Notebook 教程](https://juejin.im/post/5af8d3776fb9a07ab7744dd0)
7. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_git.png" alt="git" style="zoom:15%;" /> notebook](https://github.com/jupyter/notebook/tree/8881a06e0e01eaba277dfd118cfa429f9c418b9f)
8. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_wiki.png" alt="wiki" style="zoom:15%;" /> Jupyter](https://en.wikipedia.org/wiki/Project_Jupyter)

