======================
Nodejs / Git / VScode 
======================
.. important:: 操作系统: windows10<64位>pro及以上, 推荐 <Windows 10 Professional Version 2009/20H2>
 
Nodejs
---------------
.. note:: 非必需，建议安装，不需深入学习，只需了解  `npm <https://www.runoob.com/nodejs/nodejs-npm.html>`_  机制和 `nvm <https://www.cnblogs.com/powerwu/articles/16614130.html>`_ 版本管理就可以.

Node.js是一个基于Chrome V8引擎的JavaScript运行环境,使用了一个事件驱动、非阻塞式I/O模型,让JavaScript 运行在服务端的开发平台.

Node.js对一些特殊用例进行优化，提供替代的API，使得V8在非浏览器环境下运行得更好，V8引擎执行Javascript的速度非常快，性能非常好，基于Chrome JavaScript运行时建立的平台， 用于方便地搭建响应速度快、易于扩展的网络应用.

Node.JS逐渐发展成一个成熟的开发平台，吸引了许多开发者。有许多大型高流量网站都采用Node.JS进行开发，此外，开发人员还可以使用它来开发一些快速移动Web框架.

Nodejs是现在WEB应用程序的基础,非常多的应用软件都依赖它.


*  `Nodejs 官网 <https://nodejs.org/zh-cn>`_
*  `Nodejs 官网下载 <https://nodejs.org/download/release/v18.16.0/node-v18.16.0-win-x64.zip>`_ : 版本 Version 18.16.0 winx64
*  `Nodejs 入门教程 <https://iowiki.com/nodejs/nodejs_index.html>`_


----

Git
---------------
.. note:: 需要安装, 是软件在 **本地** 仓库 & **github** 远程仓库的操作管理工具, Smart20系统需要它存储和版本管理.

官网介绍：

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
Git is easy to learn and has a tiny footprint with lightning fast performance. It outclasses SCM tools like Subversion, CVS, Perforce, and ClearCase with features like cheap local branching, convenient staging areas, and multiple workflows.

Google翻译:

Git 是一个免费的开源分布式版本控制系统，旨在快速高效地处理从小型项目到大型项目的所有内容。
Git 易于学习，占用空间小，性能快如闪电。它超越了 Subversion、CVS、Perforce 和 ClearCase 等 SCM 工具，具有廉价的本地分支、方便的临时区域和多个工作流等特性。

* `Git 下载<淘宝镜像> <https://registry.npmmirror.com/-/binary/git-for-windows/v2.41.0.windows.1/Git-2.41.0-64-bit.exe>`_ : 版本 Version 2.41.0 winx64
* `Git 官网文档/中文 <https://git-scm.com/book/zh/v2>`_
* `Git 1小时视频教程 <https://www.bilibili.com/video/BV1FE411P7B3/?spm_id_from=333.337.search-card.all.click&vd_source=72d47f920610891857fb5340afefeb8e>`_

----

git 使用前主要设置
~~~~~~~~~~~~~~~~~~~
.. note:: 代码 "--global " 表示全局git用户名/电子邮件地址, 不加表示本仓库<文件夹>git用户名/电子邮件地址

鼠标右键打开 :guilabel:`Git Bash`

设置用户名
`````````````````

.. code-block:: bash

    $ git config --global user.name "xiaoming"


- 确认用户名正确
  
.. code-block:: bash

    $ git config --global user.name
    > xiaoming
  
设置电子邮件地址
```````````````````

.. code-block:: bash
    
    $ git config --global user.email "email@example.com"


- 确认电子邮件地址正确

.. code-block:: bash
    
    $ git config --global user.email
    email@example.com   


Git 链接 GitHub 的身份验证
```````````````````````````````````

https://docs.github.com/zh/authentication/connecting-to-github-with-ssh

----

git常用的指令
~~~~~~~~~~~~~~~

-> 本地仓库
```````````````
初始化或从远程仓库 **Github** 拉取<pull>/克隆<clone>


.. code-block:: shell

    git init
    git fetch <remote>
    git clone https://github.com/username/XXX.git


->远程仓库
`````````````````
本地仓库同步远程仓库

.. code-block:: shell

   git add .
   git commit -m "text"
   git push

将结合后续章节 :doc:`/environment/project` 讲解Git的使用.

VScode
---------------
.. note:: 非必需的, Smart20系统高级应用和二次开发, C脚本代码编辑和自有的系统静态库文件封装时会使用, 也可以后期安装.

Visual Studio Code (简称 VSCode) 是一款免费开源的现代化轻量级代码编辑器，支持几乎所有主流的开发语言的语法高亮、智能代码补全、自定义热键、括号匹配、代码片段、代码对比 Diff、Git 等特性，支持插件扩展，并针对网页开发和云端应用开发做了优化。软件跨平台支持 Win、Mac 以及 Linux，运行流畅，同类型软件还有 Sublime Text、Notepad++等。

* `VScode 官网 <https://code.visualstudio.com/>`_
* `VScode 官网下载 <https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user>`_ : 版本 Version 1.79
* `VScode 安装教程 <https://blog.csdn.net/MSDCP/article/details/127033151?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-127033151-blog-123216812.235^v38^pc_relevant_sort_base2&spm=1001.2101.3001.4242.1&utm_relevant_index=3>`_
  
