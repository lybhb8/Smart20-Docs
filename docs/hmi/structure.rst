========
页面结构
========

功能区划分
```````````

.. image:: /docs/img/moldpage.png
    :width: 70%
    :align: center

1 页眉
~~~~~~

显示软件版本信息、日期时间、 :ref:`hmi/structure:一级菜单` 按钮 :guilabel:`≡`

2 状态栏
~~~~~~~~

显示产品信息，设备工作状态、报警信息、登录用户，目前内容为空白。

3 主按钮菜单
~~~~~~~~~~~~

系统主要控制按钮

.. image:: /docs/img/mainbtn.gif
    :width: 25%
    :align: center


4 挤出机菜单
~~~~~~~~~~~~

挤出机调速按钮

.. image:: /docs/img/extruder.gif
    :width: 25%
    :align: center


5 动作按钮菜单
~~~~~~~~~~~~~~

动作按钮

* 5.1 "动作按钮页面"状态条
* 5.2 "动作按钮页面"切换按钮

.. image:: /docs/img/button1.gif
    :width: 25%
    :align: center



6 底部页面菜单
~~~~~~~~~~~~~~~~~~

页面按钮,详见 :ref:`hmi/structure:二级菜单`



7 页面显示区域
~~~~~~~~~~~~~~

主页面和子页面显示区域

8 子页面菜单
~~~~~~~~~~~~

子页面按钮，详见 :ref:`hmi/structure:三级菜单`

----


页面菜单
`````````

页面层次结构
~~~~~~~~~~~~~~

.. image:: /docs/img/page.svg
    :width: 70%
    :align: center


一级菜单
~~~~~~~~

弹出式，布局在画面的右上侧，需要点画面的右上角 :guilabel:`≡` 弹出，再按为隐藏 .

.. image:: /docs/img/1class.gif
    :width: 70%
    :align: center

二级菜单
~~~~~~~~~

布局在底部，始终显示。"系统设置"与其余页面的"二级菜单"不同 .
图中所示为页面按钮，点击后页面就会跳转至相应页面，这些页面全是主页面 .

.. image:: /docs/img/2class.gif
    :width: 70%
    :align: center




三级菜单
~~~~~~~~

在主页面的顶部，布局有各主页面的子页面菜单 ( :ref:`hmi/structure:8 子页面菜单` ) ,用于子页面的切换 .

.. image:: /docs/img/3aclass.gif
    :width: 70%
    :align: center