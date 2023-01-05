---
title: 如何修复 java.lang.ClassNotFoundException
type: docs
weight: 30
url: /zh/java/how-to-fix-java-lang-classnotfoundexception/ 
---
Aspose.Cells for Java API 依赖一些额外的库，如果缺少，可能会抛出“java.lang.ClassNotFoundException”异常。
本文列出了此类异常，并解释了安装哪些库来解决它们。

## 如何修复 ClassNotFoundException：org.bouncycastle.jce.provider.BouncyCastleProvider
### **概括**
Aspose.Cells for Java API 依赖Bouncy Castle的加解密功能，即如果程序需要加载或保存加密的电子表格，需要在项目的类路径中添加bcprov-jdk16-146.jar的引用。
### **症状**
您可能会得到 java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider。
### **解决方案**
解决方法其实很简单，详见下文。

1. 下载任何主要版本[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. 解压缩下载的存档并浏览到 \JDK 1.6\aspose-cells-xx0-java\lib 目录。
1. 在项目的类路径中引用 bcprov-jdk16-146.jar。

或者，你可以在 pom.xml 中添加依赖，让项目通过 maven 解析依赖。

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

