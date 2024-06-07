---
title: 检查组件的版本号
type: docs
weight: 70
url: /zh/java/check-version-number-of-the-component/
---

{{% alert color="primary" %}} 

在某些情况下，您可能想知道您拥有的产品版本。我们经常发布新的修复程序（针对用户提出的错误修复方案），并在论坛上发布。版本号由主版本号、次版本号和紧急补丁版本号组成。所有定义的组件都必须是大于或等于 0 的整数。版本号的格式如下：

主.次.紧急，我们可能提高其中一部分来制作一个新版本。通常情况下，我们将最后一部分加一，并构建一个新的修复程序发布到论坛供用户使用。

本文档描述了检查系统上安装的组件版本的一些方法。

{{% /alert %}} 
## **检查版本号**
### **1）手动方式**
如果您使用 Java 版本/修复程序（Aspose.Cells for Java），则可以解压 Aspose.Cells 库的 jar 文件，使用记事本打开 MANIFEST 文件，并搜索字符串，即"Specification-Version: " ，以检查其值。

![todo:image_alt_text](check-version-number-of-the-component_1.png)


**图：** 检查 Java 修复程序的版本号
### **2）使用 API**
您还可以使用以下 API 来获取产品的版本号。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

