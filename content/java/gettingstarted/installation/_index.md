---
title : "Installation" 
description : "" 
weight : 8006 
toc : false
type: docs
url: /java/gettingstarted/installation/
---

# Aspose.Cells for Java : Installation


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Installing Aspose.Cells for Java from Maven Repository](#installing-aspose.cells-for-java-from-maven-repository)
*   2 [Support](#support)
{{< /panel >}}
 

 

## Installing Aspose.Cells for Java from Maven Repository

Aspose hosts all Java APIs on [Maven repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose). You can easily use [Aspose.Cells for Java API](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) directly in your Maven Projects with simple configurations.

First, you need to specify Aspose Maven Repository configuration/location in your Maven pom.xml as below:

{{< code lang="cs" >}}
<repositories>
      <repository>
          <id>AsposeJavaAPI</id>
          <name>Aspose Java API</name>
          <url>http://repository.aspose.com/repo/</url>
      </repository>
</repositories>
{{< /code >}}

Then define Aspose.Cells for Java API dependency in your pom.xml as follows (This will include everything, e.g main jar file, Java Docs, and other libraries accordingly):

{{< code lang="cs" >}}
    <dependencies>
        <dependency>
            <groupId>com.aspose</groupId>
            <artifactId>aspose-cells</artifactId>
            <version>20.6</version>
        </dependency>
        <dependency>
            <groupId>com.aspose</groupId>
            <artifactId>aspose-cells</artifactId>
            <version>20.6</version>
            <classifier>javadoc</classifier>
        </dependency>
		<dependency>
            <groupId>org.bouncycastle</groupId>
            <artifactId>bcprov-jdk15on</artifactId>
            <version>1.60</version>
        </dependency>        
    </dependencies>
{{< /code >}}

Congratulations! You have successfully defined the Aspose.Cells for Java Maven dependency in your Maven project.

## Support

Please check the following to get quick technical support

[Aspose.Cells - Forums](https://forum.aspose.com/c/cells)

