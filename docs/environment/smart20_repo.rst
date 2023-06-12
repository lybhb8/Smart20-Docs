===================
Smart20 系统仓库
===================

* **Smart20-BlowmoldingControlSystem** 是系统在Github 的远程仓库名.

* 系统代码供公众免费下载.

----

系统下载
--------
经过前面的步骤 , 就满足了下载 Smart20 系统的条件.

1 进入系统仓库
~~~~~~~~~~~~~~

打开作者 **github**  主页 : `www.github.com/lybhb8 <https://github.com/lybhb8>`_

.. figure:: /docs/img/smart20repo.png
    :width: 70%
    :align: center
    

2 fork 系统
~~~~~~~~~~~~~~~

进入系统仓库，点击右上角 :guilabel:`fork` , 生成系统的一个新拷贝

.. note:: Fork 是对一个仓库的克隆 . 克隆一个仓库允许你自由试验各种改变，而不影响原始的项目 . 一般来说, forks 被用于去更改别人的项目（贡献代码给已经开源的项目）或者使用别人的项目作为你自己想法的初始开发点 .
.. figure:: /docs/img/fork.png
    :width: 70%
    :align: center

3 复制 <code> "SSH -> git clone" 地址
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

等一会, 自动进入您的代码仓库的系统fork .

恭喜您拥有了属于自己的Smart20系统库文件!

.. figure:: /docs/img/clone.png
    :width: 70%
    :align: center

4 本地 git clone
~~~~~~~~~~~~~~~~~~~

本地计算机新建文件夹，比如 "smart20_fork" , 
左键单击新建文件夹，右键打开 :guilabel:`git Bash`

* 输入"git clone 空格",右键 :guilabel:`Paste`
* 或者复制下面代码, 右键 :guilabel:`Paste`，改"yourAccount" 为自己的账户名称

.. code-block:: shell

    git clone git@github.com:yourAccount/Smart20-BlowmoldingControlSystem.git

* 回车后如下图

.. figure:: /docs/img/git_clone.png
    :width: 70%
    :align: center

这时,已经将 **Smart20-BlowmoldingControlSystem** 代码完整复制到本地计算机的smart20_fork文件夹里 , 完成了系统下载 .



流程图
--------

上述流程如图所示,各步骤如数字顺序进行

.. figure:: /docs/img/fork_imge.jpg
    :width: 70%
    :align: center




