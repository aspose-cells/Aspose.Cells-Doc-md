---
title: java.lang.ClassNotFoundException org.bouncycastle.jce.provider.BouncyCastleProvider
type: docs
weight: 30
url: /java/java-lang-classnotfoundexception-org-bouncycastle-jce-provider-bouncycastleprovider/
---

### **Summary**
Aspose.Cells for Java API depends on Bouncy Castle for encryption and decryption features, that is; if the program is required to load or save encrypted spreadsheets, it is required to add reference of bcprov-jdk16-146.jar in the project's class path.
### **Symptoms**
You may get the java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider. 
### **Solution**
The solution is actually very simple as detailed below.

1. Download any major release of [Aspose.Cells for Java](http://www.aspose.com/downloads/cells/java).
1. Extract the downloaded archive and browse to \JDK 1.6\aspose-cells-x.x.0-java\lib directory.
1. Reference the bcprov-jdk16-146.jar in the class path of the project.

Alternatively, you can add the dependency in the pom.xml and let the project resolve the dependency via maven.

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
