#### 写在前面

在计算机领域，长久以来，先进的技术一直在国外诞生，近几年我们欣喜的看到国内的发展势头很足：

- 前端领域尤雨溪大神创造了[Vue](https://vuejs.org)框架，作为一款个人开发的框架可以与 Facebook 维护的[React](https://reactjs.org)、Google 维护的[Angular](https://angular.io)竞争，并且越来越受欢迎，着实非常了不起。
- 阿里巴巴积极参与开源社区的发展，旗下的[ant design](https://github.com/ant-design/ant-design) UI 框架也在近几年快速发展，使用人数众多。
- 腾讯微信引领的小程序创造出了极大的价值，国内大公司纷纷开发自己的小程序平台。

我们很高兴目睹到这些积极的变化，但尽管如此，我们不能忽视的一点是英语依然是编程人员必备的一项硬技能。理由如下：

- 计算机在国外的发展长久以来处于世界领先水平，计算机领域的大牛几乎都是英语母语者，几乎所有语言的文档都是英文编写的。
- 国外的技术社区氛围较好，在[stackoverflow](http://stackoverflow.com)上很多问题大家都遇到过，并且给出了较好的解决方案。
- 计算机社区的交流都使用英语，如果你想参与到社区的发展中，熟练的英语是必不可少的。
- 国内的搜索引擎普遍对于技术内容的索引少，质量低下。
- 语言或软件文档的第一手资料都是英文书写，中文几乎都至少是第二手资料，最新发展的领域有成熟的中文教程常常需要一定时间，而众所周知：科技行业日新月异。
- 如果我们都直接用英语来交流，那么可以节省出很多原来浪费在翻译上的时间。
- 除了在技术上可以用到英语，在娱乐方面也可以使用到英语资料，汉语资料在互联网上占比可能不超过 10%
- 学习一门语言总是好的，不会带来任何副作用。

因此，我想表达的核心观点是：**计算机领域从业者要熟练使用英语，多找一手英语资料。**
所以在接下来的文章中，我会尽量提供一手的英语参考资料。

李笑来在 github 上开源了一份资料：[人人都能用英语](https://github.com/xiaolai/everyone-can-use-english)，可供参考。

## 工具链 tool chain

### 一、Python3

> Python 是一种广泛使用的解释型、高级编程、通用型编程语言。

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2880px-Python_logo_and_wordmark.svg.png" alt="Python logo" style="zoom:20%;" />

Python 是[龟叔](https://zh.wikipedia.org/wiki/吉多·范罗苏姆)于在 1989 年圣诞节创造出的一种广泛使用的解释型、高级编程、通用型编程语言。

Guido 为了打发圣诞节的无趣，决定开发一个新的解释型语言，由于他是 Monty Python 喜剧团体的爱好者，所以取名誉 Python（巨蟒）。
Python 目前是由一个核心开发团队在开发与维护，Guido van Rossum 一直以来被称为 Python[仁慈的独裁者](https://zh.wikipedia.org/zh-hans/终身仁慈独裁者)（Benevolent Dictator For Life），龟叔最近刚刚[宣布从 Dropbox 退休](https://twitter.com/gvanrossum/status/1189546865114529792)。

Python 由于其简单优雅的特点，吸引了大量的使用者。再加上最近几年机器学习、人工智能领域的大热，Python 变得更为炙手可热。Python 有很多数据处理的库，极大的方便了人工智能从业者的使用，具体的库我们后面会详细展开。

1. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_web.png" alt="web" style="zoom:15%;" /> https://www.python.org](https://www.python.org)
2. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_doc.png" alt="docu" style="zoom:15%;" /> Python documentation](https://docs.python.org/3/)
3. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> Python For Beginners](https://www.python.org/about/gettingstarted/)
4. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> realpython](https://realpython.com)
5. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_cn_doc.png" alt="cn_doc" style="zoom:15%;" /> 廖雪峰的 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

6. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_cn_doc.png" alt="cn_doc" style="zoom:15%;" /> 李笑来：自学是门手艺](https://github.com/selfteaching/the-craft-of-selfteaching)
7. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_git.png" alt="git" style="zoom:15%;" /> Python](https://github.com/python)
8. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_wiki.png" alt="wiki" style="zoom:15%;" /> Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

### 二、Conda

> Conda 是一个集包管理、依赖管理、环境管理等功能于一身的集成工具。

![conda logo](https://conda.io/en/latest/_images/conda_logo.svg)

Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer. It was created for Python programs, but it can package and distribute software for any language.

Conda as a package manager helps you find and install packages. If you need a package that requires a different version of Python, you do not need to switch to a different environment manager, because conda is also an environment manager. With just a few commands, you can set up a totally separate environment to run that different version of Python, while continuing to run your usual version of Python in your normal environment.

如果你在物品中需要使用不同的 Python 环境，那么 Conda 绝对是一个非常合适的助手，它可以方便的帮助你切换不同的 Python 环境，方便的进行包管理、依赖管理。此外，Anaconda 是目前世界上最流行的数据科学平台，而且它会内置一些常见的科学计算基础包，非常适合新手使用。

1. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_web.png" alt="web" style="zoom:15%;" /> https://conda.io](https://conda.io)
2. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_doc.png" alt="docu" style="zoom:15%;" />Getting started with conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
3. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" />安装文档](https://docs.anaconda.com/anaconda/install/)
4. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" />Conda Cheat sheet ](https://conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
5. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_git.png" alt="git" style="zoom:15%;" /> conda](https://github.com/conda/conda)
6. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_wiki.png" alt="wiki" style="zoom:15%;" /> conda](<https://en.wikipedia.org/wiki/Conda_(package_manager)>)

### 三、Jupyter

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

### 四、NumPy

> NumPy 是 Python 语言的一个扩展程序库。支持高端大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/1200px-NumPy_logo.svg.png" style="zoom: 33%;" />

NumPy 引入了多维数组以及可以直接有效率地操作多维数组的函数与运算符。因此在 NumPy 上只要能被表示为针对数组或矩阵运算的算法，其运行效率几乎都可以与编译过的等效 C 语言代码一样快。

NumPy 的核心功能是"ndarray"(即 n-dimensional array，多维数组)数据结构。这是一个表示多维度、同质并且固定大小的数组对象。而由一个与此数组相关系的数据类型对象来描述其数组元素的数据格式(例如其字符组顺序、在存储器中占用的字符组数量、整数或者浮点数等等)。

1. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_web.png" alt="web" style="zoom:15%;" /> https://numpy.org](https://numpy.org)
2. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_doc.png" alt="docu" style="zoom:15%;" /> Quickstart tutorial ](https://numpy.org/devdocs/user/quickstart.html)
3. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> 安装文档](https://scipy.org/install.html)
4. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> numpy devdocs](https://numpy.org/devdocs/)
5. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_git.png" alt="git" style="zoom:15%;" /> NumPy ](https://github.com/numpy/numpy)
6. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_wiki.png" alt="wiki" style="zoom:15%;" /> NumPy](https://zh.wikipedia.org/zh-cn/NumPy)

### 五、pandas

> 高性能、易用的开源数据分析工具包。

<img src="https://camo.githubusercontent.com/5cb734f6fc37f645dc900e35559c60d91cc6b550/68747470733a2f2f6465762e70616e6461732e696f2f7374617469632f696d672f70616e6461732e737667" alt="pandas" style="zoom: 15%;" />

pandas 解决的问题：

Python has long been great for data munging and preparation, but less so for data analysis and modeling. _pandas_ helps fill this gap, enabling you to carry out your entire data analysis workflow in Python without having to switch to a more domain specific language like R.

Combined with the excellent [IPython](https://ipython.org/) toolkit and other libraries, the environment for doing data analysis in Python excels in performance, productivity, and the ability to collaborate.

_pandas_ does not implement significant modeling functionality outside of linear and panel regression; for this, look to [statsmodels](http://statsmodels.sf.net/) and [scikit-learn](http://scikit-learn.org/). More work is still needed to make Python a first class statistical modeling environment, but we are well on our way toward that goal.

1. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_web.png" alt="web" style="zoom:15%;" /> https://pandas.pydata.org/index.html](https://pandas.pydata.org/index.html)
2. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_doc.png" alt="docu" style="zoom:15%;" /> pandas docs ](https://pandas.pydata.org/pandas-docs/stable/index.html)
3. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> 10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
4. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> numpy devdocs](https://numpy.org/devdocs/)
5. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_git.png" alt="git" style="zoom:15%;" /> pandas ](https://github.com/pandas-dev/pandas)
6. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_wiki.png" alt="wiki" style="zoom:15%;" /> pandas](<https://en.wikipedia.org/wiki/Pandas_(software)>)

### 六、小结

[<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_cn_doc.png" alt="cn_doc" style="zoom:15%;" /> [译] 给初学者的 Jupyter Notebook 教程](https://juejin.im/post/5af8d3776fb9a07ab7744dd0)

![](https://raw.githubusercontent.com/RoseauHan/upic/master/py_learn_jupyter.png)
