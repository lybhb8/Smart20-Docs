---
hide-toc: true
---

# 开源 | Open Source

## 历程

- 吹塑机控制系统中，[倍福](https://www.beckhoff.com.cn/zh-cn/industries/plastics-machines/blow-molding/)、[贝加莱](https://www.br-automation.com/zh/)、[杰弗伦](https://www.gefran.cn/%E4%BA%A7%E5%93%81/%e8%bd%af%e4%bb%b6/%e6%a8%a1%e6%9d%bf/plastic-blow-template-%e8%87%aa%e5%8a%a8%e5%8c%96%e5%b9%b3%e5%8f%b0/)等虽然系统成熟稳定，但也存在系统封闭、难于上手，学习成本高、功能扩展性差，系统成本高。

- 国内吹塑机生产商大多采用Moog壁厚控制器+HMI+PLC构成系统（秦川为HMI+PLC自研系统），存在系统集成度低，数据不易交互，HMI页面设计美观度低，层次比较凌乱，专业性不足，用户使用度差，多语言专业性用词欠缺，物联网、5G技术无法应用，系统成本高。

- 随之物联网、5G技术的发展，其在工业自动化实践中的应用如雨后春笋般爆发。

- 自主的、开放的、先进的、功能强大的、性能稳定的、易用的、经济的**吹塑机控制系统**是行业的迫切需求。

- 多年来，有感于吹塑机控制系统行业现状，有心想在这方面做点事情，尝试开发一套理想的**吹塑机控制系统**。

- 技术架构综合了技术开发和应用等多个因素，确定HMI（附加物联网功能）+PLC。

- HMI硬件选型经过了一系列痛苦的“**选择**->**放弃**”的过程，国内常见的HMI主流品牌都做过开发过程，全部不能达到系统开发要求。其中的原因五花八门，实际可以归纳成一点：技术架构落后，封闭不开放。

- 也尝试用工控机+SCADA实现，典型的SCADA软件是西门子WINCC7.5。开始时，自己还比较乐观，主要原因还是比较迷信西门子的东西。当项目试建时，其封闭性的弊端显现出来。在搭建<u><strong>壁厚控制</strong></u>模块时，Wincc的<u><strong>函数趋势控件FunctionTrendControl</strong></u>需要结合<u><strong>User Archive用户归档</strong></u>，才能实现多点（X、Y）坐标值的读写（将多点X、Y坐标变量如TagX0,TagX1,TagX2...TagY0,TagY1,TagY2...看作两个变量TagX,TagY的多个归档，自己当时无法理解西门子为什么这样做？后来才明白因为西门子WINCC的Tag数量与售价紧密关联，**都是“月亮”惹的祸！**）。可当用C脚本实现100点变量操作时，却无法保证所有数据的正确和有序（期待Wincc高手指导），也只好放弃。

- 还有另一种很有前途技术路线：以工控机做上位机，[PCHMI](http://pchmi.com/)作为组态软件框架库，使用微软的Visual Studio开发自有系统。但是考虑到国内电气工程师上手C#、C++、VB等高级语言普遍困难，不利于未来系统发展和推广，也一直未下决心走这条路线，但后续也可考虑。

- 也是偶然的机会，圈内的朋友推荐**繁易HMI**，初步尝试时，在别的平台难于实现的系统功能，却能很快组态完成，测试模拟很成功。经过进一步系统搭建，**繁易HMI**平台的优势逐步呈现出来:
  
  - 基于成熟的Linux操作系统。
  
  - 长期高可靠的嵌入式内存管理技术。
  
  - 实用的HMI控件，满足各种使用要求。
  
  - 传统的组态操作方法，组态工作效率高。
  
  - 高性能实时C语言脚本技术，能完成各种高级组态功能。
  
  - 原生的C语言系统平台，足够的系统开放性，可以调用大量的C库函数，还可以自建静态链接库，增强组态功能。
  
  - 更多优点在项目文档中会详细说明，这里不再赘述。
  
  总之，**繁易HMI**平台有一种“”梦里寻他千百度，蓦然回首，那人却在灯火阑珊处“的感觉。

- PLC 部分选用**OMRON** C系列，因为本人对其PLC熟悉，也能轻松驾驭其指令集。更重要的原因：本系统PLC代码经过多个实际项目常年使用检验，证明了其正确性、可靠性、稳定性，用户可放心使用。使用其余PLC平台（如西门子，三菱）也可以借鉴移植。

- 本来是不想开源的，因为如果开源，就需要对代码做大量的注释和封装工作，还需要撰写详细的项目文档，这会耗费不少的精力和时间。回想起系统初步构建时，为了使用C语言脚本，前后半年利用业余时间主要学习和浏览了以下知识和网络资源：
  
  - C语言（书籍：C语言程序设计/北京理工大学版；视频教程：[ linux嵌入式C语言学习教程](https://www.bilibili.com/video/BV18p4y167Md/?spm_id_from=333.337.search-card.all.click) ,网络教程：[C 语言教程 - 网道](https://wangdoc.com/clang/)  )。
  
  - [Git](https://git-scm.com/) &[Github](https://github.com/)
  
  - [Docker](https://www.docker.com/)(视频教程:[Docker最新超详细版教程通俗易懂](https://www.bilibili.com/video/BV1og4y1q7M4/?spm_id_from=333.337.search-card.all.click))
  
  - [JavaScript 算法与数据结构](https://github.com/trekhleb/javascript-algorithms/blob/master/README.zh-CN.md)
  
  - [西门子SIMATIC WinCC官方网站](http://www.wincc.com.cn/zxjc.aspx#)
  
  - ...

- 受益于5G&互联网技术的实惠，感受到了开源的力量。随着项目的顺利推进，开源的意愿愈加强烈：
  
  - 项目受益于各种开源书籍和开源组件等社会资源。
  
  - 开源可以汇集大家的力量推进**吹塑机控制系统**做的更好、更大、更强。
  
  - 开源可以惠及吹塑机行业发展。
  
  - 或许只要项目对他人有一点点帮助，都是有意义的。

- 最终决定**Smart20-BlowmoldingControlSystem** **开源**！

## 说明 | Notice

### 使用须知

**Smart20-BlowmoldingControlSystem** 由作者Bobolin及其他贡献者开发，所有版权归作者Bobolin所有，程序集源代码在遵循 **Apache-2.0 license**的开源协议以及附加协议下，可免费供其他开发者二次开发或（商业）使用。

### 个人使用

- 不能将程序集用作违法犯罪活动。

- 不能将程序集单独包装售卖，申请专利等。

- 不能擦除程序集所有有关作者的信息。

- 以上内容必须全部符合，个人使用授权才成立。

### 二次开发

- 不能将程序集用作违法犯罪活动。

- 不能将程序集单独包装售卖，申请专利等。

- 不能擦除程序集所有有关作者的信息。

- 二次开发完成后的作品必须附带源作品所有作者信息，包括但不限于作者名、Gitee、Github 地址等。

- 完成后的作品（仅 **Smart20-BlowmoldingControlSystem**部分）必须将发布时最新源代码提交一份给本作者，QQ 邮箱：**[1341979804@qq.com](mailto:1341979804@qq.com)**。

- 以上内容必须全部符合，二次开发授权才成立。

### 商业用途

- 不能将程序集用作违法犯罪活动。

- 不能将程序集单独包装售卖，申请专利等。

- 不能擦除程序集所有有关作者的信息，并必须于用户可见界面（如关于）中提名。

- 以上内容必须全部符合，商业使用授权才成立。

### 免责申明

在使用 Smart20-BlowmoldingControlSystem 之前请进行缜密的测试。在使用期间，由本程序集造成或间接造成的所有损失，均自己承担，与本程序集无关。

## Smart20-BlowmoldingControlSystemPro 商用许可

- **Smart20-BlowmoldingControlSystemPro**软件框架与 **Smart20-BlowmoldingControlSystem**是一致的，只另包含增强功能模块。

- **Smart20-BlowmoldingControlSystemPro**所有版权归作者Bobolin所有。

- **Smart20-BlowmoldingControlSystemPro**是非开源部分，需要付费购买，欢迎商业用户积极选用。

## License

```{include} ../README.md
:start-after: <!-- start license -->
:end-before: <!-- end license -->
```