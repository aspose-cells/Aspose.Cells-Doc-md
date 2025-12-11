---
title: How to fix java.lang.ClassNotFoundException
type: docs
weight: 30
url: /java/how-to-fix-java-lang-classnotfoundexception/
description: Learn how to fix java.lang.ClassNotFoundException in Aspose.Cells for Java.
keywords: How to fix BouncyCastleProvider ClassNotFoundException in Java, Solve BouncyCastleProvider exception using Java, Java solve ClassNotFoundException BouncyCastleProvider.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Aspose.Cells for Java API depends on some additional libraries; if they are missing, an exception may be thrown as **java.lang.ClassNotFoundException**.  
This article lists such kinds of exceptions and explains which libraries need to be installed to resolve them.

## How to fix ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **Summary**
Aspose.Cells for Java API depends on Bouncy Castle for encryption and decryption features. If the program needs to load or save encrypted spreadsheets, you must add a reference to **bcprov-jdk16-146.jar** in the project's class path.

### **Symptoms**
You may encounter the **java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider**.

### **Solution**
The solution is actually very simple, as detailed below.

1. Download any major release of [Aspose.Cells for Java](https://downloads.aspose.com/cells/java).  
2. Extract the downloaded archive and browse to `\JDK 1.6\aspose-cells-x.x.0-java\lib` directory.  
3. Reference the **bcprov-jdk16-146.jar** in the class path of the project.

Alternatively, you can add the dependency in the `pom.xml` and let the project resolve the dependency via **Maven**.

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

{{< app/cells/assistant language="java" >}}
