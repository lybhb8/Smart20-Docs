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


页面变量
`````````

所有页面变量都为HMI内部变量,通过按钮给页面变量赋值可以实现页面的切换 . 

下表为页面变量具体内容：

.. list-table::
   :header-rows: 1
   :widths: 15 15 10 10 40
   
   * - 主页面
     - 子页面
     - 变量
     - 值
     - 描述
   * - 首页
     - 
     - LW0
     - 1
     - 首页
   * - 
     - land
     - LW1
     - 100
     - 登录页
   * - 
     - screen
     - LW1
     - 105
     - 屏保页
   * - 控制台
     - 
     - LW0
     - 4
     - 控制台主页
   * - 按钮
     - 
     - LW0
     - 5
     - 手动按钮页
   * - WDS
     - 
     - LW0
     - 6
     - 壁厚控制页
   * - 
     - Profile
     - LW6
     - 60
     - 曲线编辑
   * - 
     - WDS 设置
     - LW6
     - 61
     - WDS 参数设置
   * - 
     - DCDT
     - LW6
     - 62
     - 电子尺设置
   * - 
     - 储料式设置
     - LW6
     - 63
     - 储料电子尺设置
   * - 
     - Profile数据
     - LW6
     - 64
     - 曲线数据
   * - 
     - Profile配方
     - LW6
     - 65
     - 曲线配方
   * - 
     - 壁厚配方操作
     - 功能键
     - 
     - 曲线配方操作
   * - 
     - 图形对比
     - 功能键
     - 
     - 设定曲线/配方曲线图型对比
   * - 挤出机
     - 
     - LW0
     - 7
     - 挤出机页
   * - 
     - 挤出机控制
     - LW7
     - 70
     - 挤出机控制
   * - 
     - 挤出机设置
     - LW7
     - 71
     - 挤出机参数控制