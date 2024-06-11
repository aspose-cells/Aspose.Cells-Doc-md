---
title: 检查组件的版本号
type: docs
weight: 70
url: /zh/java/check-version-number-of-the-component/
---

{{% alert color="primary" %}} 

在某些情况下，您可能会想知道产品的版本号。通常我们会在论坛上发布新的修复版本（针对用户指出的bug进行修复）来满足他们的急迫需求。版本号由主版本号、次版本号和热修复版本号组成。所有定义的组件必须是大于或等于 0 的整数。版本号的格式如下：

主版本号.次版本号.热修复版本号，我们可以通过增加其中一部分来构建一个新版本。通常，我们会增加最后一部分并构建一个新的修复版本以发布到论坛供用户使用。

本文档描述了一些检查系统中安装的组件版本的方法。

{{% /alert %}} 
## **检查版本号**
### **1）手动方式**
如果您有Java版本/修复版(Aspose.Cells for Java),您可以解压Aspose.Cells库jar文件,用记事本打开MANIFEST文件,搜索字符串即"Specification-Version:"来检查其值。

![todo:image_alt_text](check-version-number-of-the-component_1.png)


**图：** 检查Java修补程序的版本号
### **2）使用API**
您还可以使用以下API来获取产品的版本号。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

