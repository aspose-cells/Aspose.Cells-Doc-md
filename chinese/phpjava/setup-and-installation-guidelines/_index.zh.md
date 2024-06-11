---
title: 设置和安装指南
type: docs
weight: 20
url: /zh/php-java/setup-and-installation-guidelines/
keywords: "php, excel, install"
description: "设置Aspose.Cells for PHP via Java并进行安装指南"
---



## **系统要求**
Aspose.Cells for PHP via Java是独立于平台的API，可以在任何平台（Windows、Linux、MacOS等）上使用，只要安装了PHP 7或更高版本。在设置安装之前，机器必须先安装Oracle JDK 7或更高版本。
## **安装和使用**
Aspose.Cells for PHP via Java被分发为ZIP压缩包。

要设置环境、安装和使用Aspose.Cells for PHP via Java，请按照以下说明进行操作：
### **Linux:**
- 下载[PHP](https://www.php.net/downloads.php)源代码并安装。或者，使用“sudo apt install php-xxx”命令安装php二进制文件。
- 为Linux安装Oracle JDK（1.7或1.8），并配置JAVA_HOME环境变量。
- 下载/获取“Aspose.Cells for PHP via Java”API并解压缩。将会有一个名为“aspose.cells”的文件夹。
- 从http://php-java-bridge.sourceforge.net/pjb/download.php下载PHP/Java Bridge二进制文件（JavaBridge.jar）并保存到"aspose.cells"文件夹中。
- 从http://php-java-bridge.sourceforge.net/pjb/download.php下载java/Java.inc PHP库（Java.inc）并保存到"aspose.cells"文件夹中。
- 使用以下命令在上述文件夹中运行“PHP/Java Bridge”。

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
| :- |
- 运行"aspose.cells"文件夹中的"example.php"以运行以下命令的示例：

|$ php example.php|
| :- |
### **Windows:**
- 下载[PHP](https://www.php.net/downloads.php) Windows二进制文件，并将“php.exe”添加到PATH。
- 为Windows安装Oracle JDK（1.7或1.8），并配置JAVA_HOME环境变量。
- 下载"Aspose.Cells for PHP via Java" API并解压缩。将会有一个名为"aspose.cells"的文件夹。
- 从http://php-java-bridge.sourceforge.net/pjb/download.php下载PHP/Java Bridge二进制文件（JavaBridge.jar）并保存到"aspose.cells"文件夹中。
- 从http://php-java-bridge.sourceforge.net/pjb/download.php下载java/Java.inc PHP库（Java.inc）并保存到"aspose.cells"文件夹中。
- 在上述文件夹中运行“PHP/Java Bridge”并使用以下命令。当桥梁启动时选择8080 http监听端口，然后点击“OK”按钮。

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- 运行"aspose.cells"文件夹中的"example.php"以运行以下命令的示例：

|> php example.php|
| :- |
### **Mac:**
- 安装 [PHP](https://www.php.net/downloads.php)。
- 为Mac安装Oracle JDK（1.7或1.8），配置JAVA_HOME环境变量。
- 下载"Aspose.Cells for PHP via Java" API并解压缩。将会有一个名为"aspose.cells"的文件夹。
- 从http://php-java-bridge.sourceforge.net/pjb/download.php下载PHP/Java Bridge二进制文件（JavaBridge.jar）并保存到"aspose.cells"文件夹中。
- 从http://php-java-bridge.sourceforge.net/pjb/download.php下载java/Java.inc PHP库（Java.inc）并保存到"aspose.cells"文件夹中。
- 在上述文件夹中运行“PHP/Java Bridge”并使用以下命令。当桥梁启动时选择8080 http监听端口，然后点击“OK”按钮。

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- 运行"aspose.cells"文件夹中的"example.php"以运行以下命令的示例：

|$ php example.php|
| :- |


