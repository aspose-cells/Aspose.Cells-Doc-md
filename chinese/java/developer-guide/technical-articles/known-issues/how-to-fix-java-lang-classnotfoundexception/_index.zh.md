---
title: 修复java.lang.ClassNotFoundException的方法
type: docs
weight: 30
url: /zh/java/how-to-fix-java-lang-classnotfoundexception/ 
description: 学习如何在Aspose.Cells for Java中修复java.lang.ClassNotFoundException。
keywords: 如何修复Java中的BouncyCastleProvider ClassNotFoundException，使用Java解决BouncyCastleProvider异常，Java解决ClassNotFoundException BouncyCastleProvider。
---

Aspose.Cells for Java API依赖于一些附加库，如果缺少这些库，则可能抛出“java.lang.ClassNotFoundException”异常。
本文列出了此类异常并解释了安装哪些库以解决它们。

如何修复ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **摘要**
Aspose.Cells for Java API依赖于Bouncy Castle进行加密和解密功能。因此，如果程序需要加载或保存加密的电子表格，则需要在项目的类路径中添加bcprov-jdk16-146.jar的引用。
### **症状**
您可能会遇到java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider。 
### **解决方案**
解决方案非常简单，如下所述。

1.下载任何主要版本的[Aspose.Cells for Java](https://downloads.aspose.com/cells/java)。
1.提取下载的归档文件并浏览到\JDK 1.6\aspose-cells-x.x.0-java\lib目录。
1.在项目的类路径中引用bcprov-jdk16-146.jar。

或者，您可以在pom.xml中添加依赖项，并让项目通过maven解析依赖项。

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

