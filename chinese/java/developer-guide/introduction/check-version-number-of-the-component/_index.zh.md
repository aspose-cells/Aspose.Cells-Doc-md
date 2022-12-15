---
title: 检查组件的版本号
type: docs
weight: 70
url: /zh/java/check-version-number-of-the-component/
---
{{% alert color="primary" %}} 

在某些情况下，您可能想知道您拥有的产品版本。我们经常构建新的修复程序（针对他们指出的用户场景的错误修复程序）并根据他们的需要紧急将它们发布在论坛中。版本号由主版本号、次版本号和修补程序版本号组成。所有定义的组件必须是大于或等于0的整数。版本号的格式如下：

major.minor.hotfix ，我们可能会增加一个部分并制作一个新版本。通常，我们将最后一部分增加 1 并构建一个新的修复程序以将其发布到论坛中供用户使用。

本文档介绍了一些检查系统上安装的组件版本的方法。

{{% /alert %}} 
## **检查版本号**
### **1) 手动方式**
如果您有 Java 版本/修复 (Aspose.Cells for Java)，则可以解压缩 Aspose.Cells 库 jar 文件，用记事本打开 MANIFEST 文件并搜索字符串，即“Specification-Version:”以检查其值。

![待办事项：图像_替代_文本](check-version-number-of-the-component_1.png)


**数字：**检查 Java 修复的版本号
### **2) 使用API**
您还可以使用以下 API 获取产品的版本号。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

