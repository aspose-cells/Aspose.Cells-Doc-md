---
title: Installation
type: docs
weight: 20
url: /java/installation/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Installing Aspose.Cells for Java from Maven Repository**

Aspose hosts all Java APIs on [Maven repository](https://releases.aspose.com/java/repo/). You can easily use [Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) directly in your Maven Projects with simple configurations.

First, you need to specify Aspose Maven Repository configuration/location in your Maven pom.xml as below:

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

for Gradle in you build.gradle script as follows:
{{< highlight java >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Then define Aspose.Cells for Java API dependency in your pom.xml as follows (This will include everything, e.g main jar file, Java Docs, and other libraries accordingly):

{{< highlight java >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>25.12</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>25.12</version>

            <classifier>javadoc</classifier>

        </dependency>

        <dependency>

            <groupId>org.bouncycastle</groupId>

            <artifactId>bcprov-jdk15on</artifactId>

            <version>1.68</version>

        </dependency>        

        <dependency>

            <groupId>org.bouncycastle</groupId>

            <artifactId>bcpkix-jdk15on</artifactId>

            <version>1.68</version>

        </dependency>        

    </dependencies>

{{< /highlight >}}

Congratulations! You have successfully defined the Aspose.Cells for Java Maven dependency in your Maven project.

## **WebP Image Loading**

WebP is a modern image format. It is designed to produce smaller file sizes, while maintaining high visual quality.

Currenlty, In Microsoft Excel, WebP images are not allowed to be inserted directly. However,  there are cases that WebP images are inserted into Excel source files directly by some third party libraries.

Generally Aspose.Cells for Java uses Java's ImageIO to load raster images, currently the JDK itself doesn't support to load WebP images. Some additional plugins or extensions(e.g. [imageio-webp Plugin](https://mvnrepository.com/artifact/com.twelvemonkeys.imageio/imageio-webp)) is needed for Java's ImageIO to load WebP images.

## **To TIFF Images by Java 8 and Older**
As we stated above, Aspose.Cells for Java requires only the Java Runtime Environment, and you do not need to install any additional libraries. However, sometimes there are situations where you might need to add third-party libraries. Java Advanced Imaging (JAI) to support TIFF images. TIFF images are not supported by Java 8 and older. For TIFF support in old Java environments, Aspose.Cells for Java depends on the [Java Advanced Imaging (JAI) package](https://www.oracle.com/java/technologies/java-archive-downloads-java-client-downloads.html) from Oracle. We will describe how to install JAI below.

### **How to Install JAI on Windows**
Follow these steps to install native JAI and ImageIO on Windows:

1. Download JAI 1.1.3. At the time of writing, only the 32-bit version of the installer is available, so if you use a JDK you need to download [Jai-1_1_3-lib-windows-i586-jdk.exe](https://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-windows-i586-jdk.exe) and if you use a JRE you need to download [Jai-1_1_3-lib-windows-i586-jre.exe](https://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-windows-i586-jre.exe).
2. Run the installer and point it to the directory where JDK/JRE is installed.
3. Download JAI Image I/O 1.1. At the time of writing, only the 32-bit version of the installer is available, so if you use a JDK you need to download [jai_imageio-1_1-lib-windows-i586-jdk.exe](https://download.java.net/media/jai-imageio/builds/release/1.1/jai_imageio-1_1-lib-windows-i586-jdk.exe) and if you use a JRE you need to download [jai_imageio-1_1-lib-windows-i586-jre.exe](https://download.java.net/media/jai-imageio/builds/release/1.1/jai_imageio-1_1-lib-windows-i586-jre.exe).
4. Run the installer and point it to the directory where JDK/JRE is installed.

### **How to Install JAI on Linux**
Follow these steps to install native JAI and ImageIO on Linux:

1. Download JAI 1.1.3 choosing the appropriate architecture: [i586](https://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-linux-i586.tar.gz) for 32-bit systems and [amd64](https://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-linux-amd64.tar.gz) for 64-bit ones (even if using Intel processors).
2. Extract the file into a temporary directory.
3. Move JAR files to the JDK/JRE lib/ext folder.
4. Move SO files to the JDK/JRE lib/amd64 folder.
<br>
For example, on a 64-bit Ubuntu system, steps 1-4 will look like this:
```
cd /tmp
wget https://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-linux-amd64.tar.gz && \
gunzip -c jai-1_1_3-lib-linux-amd64.tar.gz | tar xf - && \
mv /tmp/jai-1_1_3/lib/*.jar $JAVA_HOME/jre/lib/ext/ && \
mv /tmp/jai-1_1_3/lib/*.so $JAVA_HOME/jre/lib/amd64/ && \
rm /tmp/jai-1_1_3-lib-linux-amd64.tar.gz && \
rm -r /tmp/jai-1_1_3
```
5. Download JAI Image I/O 1.1, choosing the appropriate architecture: [i586](https://download.java.net/media/jai-imageio/builds/release/1.1/jai_imageio-1_1-lib-linux-i586.tar.gz) for the 32-bit systems and [amd64](https://download.java.net/media/jai-imageio/builds/release/1.1/jai_imageio-1_1-lib-linux-i586.tar.gz) for the 64-bit ones (even if using Intel processors).
6. Extract the file into a temporary directory.
7. Move JAR files to the JDK/JRE lib/ext folder.
8. Move SO files to the JDK/JRE lib/amd64 folder.
<br>
For example, on a 64-bit Ubuntu system, steps 5-8 will look like this:
```
cd /tmp
wget https://download.java.net/media/jai-imageio/builds/release/1.1/jai_imageio-1_1-lib-linux-amd64.tar.gz && \
gunzip -c jai_imageio-1_1-lib-linux-amd64.tar.gz | tar xf - && \
mv /tmp/jai_imageio-1_1/lib/*.jar $JAVA_HOME/jre/lib/ext/ && \
mv /tmp/jai_imageio-1_1/lib/*.so $JAVA_HOME/jre/lib/amd64/ && \
rm /tmp/jai_imageio-1_1-lib-linux-amd64.tar.gz && \
rm -r /tmp/jai_imageio-1_1
```

## **Support**

Please check the following to get quick technical support

[Aspose.Cells - Forums](https://forum.aspose.com/c/cells/9)
{{< app/cells/assistant language="java" >}}
