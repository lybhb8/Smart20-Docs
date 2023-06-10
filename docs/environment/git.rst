================
Git / GitHub
================
.. note:: git 与 github 犹如 "手机银行APP" 与 "银行" 的关系.

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

git 主要设置
~~~~~~~~~~~~~~~~~~~
.. note:: 代码 "--global " 表示全局git用户名/电子邮件地址, 不加表示本仓库<文件夹>git用户名/电子邮件地址 .

鼠标右键打开 :guilabel:`Git Bash`

设置用户名
`````````````````

.. code-block:: bash

    $ git config --global user.name "xiaoming"


- 确认用户名正确
  
.. code-block:: bash

    $ git config --global user.name
  
设置电子邮件地址
```````````````````

.. code-block:: bash
    
    $ git config --global user.email "email@example.com"


- 确认电子邮件地址正确

.. code-block:: bash
    
    $ git config --global user.email
    

上述命令生成文件".gitconfig"", 存储为 "C:\\Users\\ <计算机用户名> \\.gitconfig",写字板打开核实是否正确.


Git SSH密钥生成
```````````````````

:ref:`environment/git:git 远程仓库`

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


Git 基本操作
Git 的工作就是创建和保存你项目的快照及与之后的快照进行对比。
Git 常用的是以下 6 个命令: git clone、git push、git add 、git commit、git checkout、git pull. 

.. figure:: https://www.runoob.com/wp-content/uploads/2015/02/git-command.jpg
    :width: 80%
    :align: center
    :name: git 命令图示

说明：


*  workspace:工作区
*  staging area:暂存区/缓存区
* local repository:版本库或本地仓库
* remote repository:远程仓库


看懂这张图片, Git 就可以使用了,详细参考 `Git教程 <https://www.w3cschool.cn/git/git-tutorial.html>`_

----

Github
------------
GitHub是一个面向开源及私有软件项目的托管平台, 因为只支持Git作为唯一的版本库格式进行托管, 故名GitHub. Github拥有1亿以上的开发人员, 400万以上组织机构和3.3亿以上资料库.

作为一个分布式的版本控制系统, 在Git中并不存在主库这样的概念, 每一份复制出的库都可以独立使用，任何两个库之间的不一致之处都可以进行合并.

GitHub的独特卖点在于从另外一个项目进行分支的简易性. 为一个项目贡献代码非常简单：首先点击项目站点的“fork”的按钮，然后将代码检出并将修改加入到刚才分出的代码库中, 最后通过内建的 **pull reques** 机制向项目负责人申请代码合并.

随着越来越多的应用程序转移到了云上, Github已经成为了管理软件开发以及发现已有代码的首选方法。


注册 github 账号
~~~~~~~~~~~~~~~~~~
.. important:: <注册 github 账号>是必须的.


- 浏览器打开 `Github主页 <https://github.com/>`_
 
- 点击 Github主页右上角 :guilabel:`Sign up` 按钮 , 按提示完成Github账号注册. 

登录 github
~~~~~~~~~~~~~~~~~~~~

拥有github账号后 , 再用浏览器打开 `Github主页 <https://github.com/>`_ , 浏览器会自动跳转至 Github 账户首次页面：

.. figure:: /docs/img/githublogo.png
    :width: 80%
    :align: center
    :name: github首次登陆页


github 设置
~~~~~~~~~~~~


本地git配置
~~~~~~~~~~~~

.. _ `Git 远程仓库`:

Git 远程仓库
~~~~~~~~~~~~~

hgfhf

`详细教程 <https://docs.github.com/zh/authentication/connecting-to-github-with-ssh>`_
