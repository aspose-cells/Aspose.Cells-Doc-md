---
title: 如何修复 java.lang.ClassNotFoundException
type: docs
weight: 30
url: /zh/java/how-to-fix-java-lang-classnotfoundexception/ 
description: 了解如何修复 Aspose.Cells for Java 中的 java.lang.ClassNotFoundException。
keywords: How to fix BouncyCastleProvider ClassNotFoundException in Java, Solve BouncyCastleProvider exception using Java, Java solve ClassNotFoundException BouncyCastleProvider.
---
Aspose.Cells for Java API 依赖于一些额外的库，如果缺少这些库，可能会抛出“java.lang.ClassNotFoundException”异常。
本文列出了此类异常，并解释了安装哪些库来解决这些异常。

## 如何修复 ClassNotFoundException：org.bouncycastle.jce.provider.BouncyCastleProvider
###  **概括**
Aspose.Cells for Java API 依赖于 Bouncy Castle 进行加密和解密功能，即如果程序需要加载或保存加密电子表格，则需要在项目的类路径中添加 bcprov-jdk16-146.jar 的引用。
###  **症状**
您可能会收到 java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider。
###  **解决方案**
解决方案实际上非常简单，如下详述。

1. 下载任何主要版本[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. 解压下载的存档并浏览到 \JDK 1.6\aspose-cells-xx0-java\lib 目录。
1. 引用项目类路径下的bcprov-jdk16-146.jar。

或者，您可以在 pom.xml 中添加依赖项，并让项目通过 maven 解析依赖项。

{{< highlight "java" >}}

 <dependencies>

	<dependency>

		<groupId>org.bouncycastle</groupId>

		<artifactId>bcprov-jdk16</artifactId>

		<version>1.46</version>

		<type>jar</type>

	</dependency>

</dependencies>

{{< /highlight >}}

