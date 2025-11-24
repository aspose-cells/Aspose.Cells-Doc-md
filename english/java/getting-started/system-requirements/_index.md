---
title: System Requirements
type: docs
weight: 10
url: /java/system-requirements/
---

{{% alert color="primary" %}} 

Aspose.Cells for Java does not require having Microsoft Excel installed, as Aspose.Cells itself is an Excel spreadsheet creation, conversion, and rendering engine. To view Excel documents produced by Aspose.Cells, you need to have at least Microsoft Excel Viewer installed.

{{% /alert %}} 
## **Supported Operating Systems**
Aspose.Cells for Java supports any operating system that runs the Java runtime including, but not limited:
### **Windows**
- Microsoft Windows 2000 ( x64, x86)
- Microsoft Windows XP ( x64, x86)
- Microsoft Windows Server 2003 ( x64, x86)
- Microsoft Windows Server 2008 ( x64, x86)
- Microsoft Windows Server 2012 ( x64, x86)
- Microsoft Windows Vista ( x64, x86)
- Microsoft Windows 7 ( x64, x86)
- Microsoft Windows 8 ( x64, x86)
- Microsoft Windows 10 ( x64, x86)
### **Linux**
- Linux (Ubuntu, openSUSE, CentOS and others)
### **Mac**
- Mac OS X etc.
## **Supported Java Versions**
Aspose.Cells for Java supports the following Java versions:

- J2SE 6.0 (1.6)
- J2SE 7.0 (1.7)
- or above

## **Optional Dependencies**
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

{{< app/cells/assistant language="java" >}}