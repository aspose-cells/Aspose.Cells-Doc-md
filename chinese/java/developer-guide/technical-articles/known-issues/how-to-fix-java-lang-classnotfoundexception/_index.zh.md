---
title: 如何解决java.lang.ClassNotFoundException
type: docs
weight: 30
url: /zh/java/how-to-fix-java-lang-classnotfoundexception/ 
description: 学习如何修复java.lang.ClassNotFoundException在Aspose.Cells for Java中的问题。
keywords: 如何在Java中修复BouncyCastleProvider ClassNotFoundException，使用Java解决BouncyCastleProvider异常，解决Java中的ClassNotFoundException BouncyCastleProvider。
---

Aspose.Cells for Java API依赖于一些额外的库，如果它们缺失，就会抛出"java.lang.ClassNotFoundException"异常。
本文列出了这类异常，并解释了安装哪些库以解决这些异常。

如何修复ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **摘要**
Aspose.Cells for Java API依赖于Bouncy Castle用于加密和解密功能，也就是说，如果程序需要加载或保存加密电子表格，则需要在项目的类路径中添加bcprov-jdk16-146.jar的引用。
### **症状**
您可能会遇到java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider。 
### **Solution**
解决方案实际上非常简单，如下所述。

1. 下载任何一个[Aspose.Cells for Java](https://downloads.aspose.com/cells/java)的主要发布版本。
1. 解压下载的存档并浏览到\JDK 1.6\aspose-cells-x.x.0-java\lib目录。
1. 在项目的类路径中引用bcprov-jdk16-146.jar。

或者，您可以在pom.xml中添加依赖项，让项目通过maven解决依赖关系。

{{< highlight java >}}

 <dependencies>

	<dependency>

		<groupId>org.bouncycastle</groupId>

		<artifactId>bcprov-jdk16</artifactId>

		<version>1.46</version>

		<type>jar</type>

	</dependency>

</dependencies>

{{< /highlight >}}

