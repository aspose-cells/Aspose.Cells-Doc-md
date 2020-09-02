---
title: Installation
type: docs
weight: 40
url: /java/installation/
---

## **Installing Aspose.Cells for Java from Maven Repository**

Aspose hosts all Java APIs on [Maven repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose). You can easily use [Aspose.Cells for Java API](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) directly in your Maven Projects with simple configurations.

First, you need to specify Aspose Maven Repository configuration/location in your Maven pom.xml as below:

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>http://repository.aspose.com/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

Then define Aspose.Cells for Java API dependency in your pom.xml as follows (This will include everything, e.g main jar file, Java Docs, and other libraries accordingly):

{{< highlight java >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>20.8</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>20.8</version>

            <classifier>javadoc</classifier>

        </dependency>

		<dependency>

            <groupId>org.bouncycastle</groupId>

            <artifactId>bcprov-jdk15on</artifactId>

            <version>1.60</version>

        </dependency>        

    </dependencies>

{{< /highlight >}}

Congratulations! You have successfully defined the Aspose.Cells for Java Maven dependency in your Maven project.

## **Support**

Please check the following to get quick technical support

[Aspose.Cells - Forums](https://forum.aspose.com/c/cells)
