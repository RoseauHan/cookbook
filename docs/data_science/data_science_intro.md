---
title: data science intro
summary: first step to data science
authors:
   - roseau
date: 2019-11-29
lastUpdate: 2019-11-29
---

# 数据科学概述

```
title: data science intro
summary: first step to data science
authors:
   - roseau
date: 2019-11-29
lastUpdate: 2019-11-29
```
> 本文主要参考自 *Python Data Science Handbook by Jake VanderPlas (O’Reilly).Copyright 2017 Jake VanderPlas,978-1-491-91205-8*
>
> Github：https://github.com/jakevdp/PythonDataScienceHandbook

### 一、什么是数据科学？

给`数据科学`下定义是一件困难的事，尤其在它现在这么流行的时候。数据科学可能算是目前为止对跨学科技能的最佳称呼，无论是在工业界还是在学术界。跨学科是数据学科的关键，一个不错的定义是Drew Conway在2010年9月提出来的：

![](https://raw.githubusercontent.com/RoseauHan/upic/master/s1oVGU.png)

数据学科综合了三个领域的能力：

- 统计学家的能力：建立模型和聚合（数据量正在不断增大的数据库）
- 计算机科学家的能力：设计并使用算法对数据进行高效存储、分析和可视化
- 领域专家的能力：在细分领域经过专业训练，既可以提出正确的问题，也可以做出专业的回答

数据科学不是一个新的知识领域，我们可以把它看成在自己熟悉领域中运用的新能力。无论你是在：

- 汇报竞选结果
- 预测股票收益
- 优化点击率
- 识别微生物
- 寻找新天体

还是在其他数据相关的领域中工作，我们都可以利用数据科学发现问题，并且具备解决问题的能力。

### 二、Python是什么？

> Python是一种广泛使用的解释型、高级编程、通用型编程语言。

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2880px-Python_logo_and_wordmark.svg.png" alt="Python logo" style="zoom:20%;" />

Python 是[龟叔](https://zh.wikipedia.org/wiki/吉多·范罗苏姆)于在1989年圣诞节创造出的一种广泛使用的解释型、高级编程、通用型编程语言。

*Guido为了打发圣诞节的无趣，决定开发一个新的解释型语言，由于他是Monty Python喜剧团体的爱好者，所以取名誉Python（巨蟒）。
Python目前是由一个核心开发团队在开发与维护，Guido van Rossum 一直以来被称为Python[仁慈的独裁者](https://zh.wikipedia.org/zh-hans/终身仁慈独裁者)（Benevolent Dictator For Life），龟叔最近刚刚[宣布从Dropbox退休](https://twitter.com/gvanrossum/status/1189546865114529792)。*

### 三、为什么选择Python？

Python由于其简单优雅的特点，吸引了大量的使用者。再加上最近几年机器学习、人工智能领域的大热，Python变得更为炙手可热。

Python之所以能在数据科学领域广泛使用，主要是由于它的第三方包拥有庞大而活跃的生态系统：

- NumPy：处理同类型数组型数据型号数据
- Pandas：处理多种类型带标签的数据
- SciPy：解决常见的科学计算问题
- MatplotLib：绘制用于印刷的可视化图形
- IPython：实现交互式编程和快速分享代码
- Scikit-Learn：可以进行机器学习

关于Python的更多参考资料如下：

1. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_web.png" alt="web" style="zoom:15%;" /> https://www.python.org](https://www.python.org)
2. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_doc.png" alt="docu" style="zoom:15%;" /> Python documentation](https://docs.python.org/3/)
3. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> Python For Beginners](https://www.python.org/about/gettingstarted/)
4. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" /> realpython](https://realpython.com) 
5. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_cn_doc.png" alt="cn_doc" style="zoom:15%;" /> 廖雪峰的Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

6. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_cn_doc.png" alt="cn_doc" style="zoom:15%;" /> 李笑来：自学是门手艺](https://github.com/selfteaching/the-craft-of-selfteaching)
6. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_git.png" alt="git" style="zoom:15%;" /> Python](https://github.com/python)
7. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_wiki.png" alt="wiki" style="zoom:15%;" /> Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### 四、利用Anaconda安装Python

安装Python其实很简单，安装上面给出的文档一步一步操作即可。虽然安装Python的方法有很多，但在数据科学方面，Anaconda发行版是一个不错的的选择。

> Conda 是一个集包管理、依赖管理、环境管理等功能于一身的集成工具。

![conda logo](https://conda.io/en/latest/_images/conda_logo.svg)


Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer. It was created for Python programs, but it can package and distribute software for any language.

Conda as a package manager helps you find and install packages. If you need a package that requires a different version of Python, you do not need to switch to a different environment manager, because conda is also an environment manager. With just a few commands, you can set up a totally separate environment to run that different version of Python, while continuing to run your usual version of Python in your normal environment.

如果你在物品中需要使用不同的Python环境，那么Conda绝对是一个非常合适的助手，它可以方便的帮助你切换不同的Python环境，方便的进行包管理、依赖管理。此外，Anaconda是目前世界上最流行的数据科学平台，而且它会内置一些常见的科学计算基础包，非常适合新手使用。

Anaconda发行版有两种：

- Miniconda：只包含Python解释器和一个名为conda的命令行工具。conda是一个跨平台的程序包管理器，可以管理各种Python程序包。
- Anaconda：除了包含Python和conda之外，还同时绑定了四五百个科学计算程序包。

可以根据自己的需求选择安装其中一个发行版，下面是更多详细的参考资料：

1. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_web.png" alt="web" style="zoom:15%;" /> https://conda.io](https://conda.io)
2. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_doc.png" alt="docu" style="zoom:15%;" />Getting started with conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
3. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" />安装文档](https://docs.anaconda.com/anaconda/install/)
4. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_en_doc.png" alt="en_doc" style="zoom:15%;" />Conda Cheat sheet ](https://conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
5. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_git.png" alt="git" style="zoom:15%;" /> conda](https://github.com/conda/conda)
6. [<img src="https://raw.githubusercontent.com/RoseauHan/upic/master/py_wiki.png" alt="wiki" style="zoom:15%;" /> conda](https://en.wikipedia.org/wiki/Conda_(package_manager))

### 五、Anaconda 与 pip 的对比

根据[anaconda官方的文档](https://www.anaconda.com/understanding-conda-and-pip/)，anaconda 与 pip 的主要区别如下：

|                       | conda                   | pip                             |
| :-------------------- | :---------------------- | :------------------------------ |
| manages               | binaries                | wheel or source                 |
| can require compilers | no                      | yes                             |
| package types         | any                     | Python-only                     |
| create environment    | yes, built-in           | no, requires virtualenv or venv |
| dependency checks     | yes                     | no                              |
| package sources       | Anaconda repo and cloud | PyPI                            |

总结来说，anaconda提供了二进制的包，不存在编译过程，因此可以有很好的兼容性，同时还提供虚拟环境支持，这就是anaconda的核心优势。