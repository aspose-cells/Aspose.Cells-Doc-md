---
title: 设置和安装指南
type: docs
weight: 20
url: /zh/php-java/setup-and-installation-guidelines/
keywords: "php, excel, install"
description: "设置Aspose.Cells for PHP via Java和安装指南。"
---



## **系统要求**
Aspose.Cells for PHP via Java是独立于平台的API，可在安装了[PHP](https://www.php.net/downloads.php) 7或更高版本的任何平台（Windows，Linux，MacOS等）上使用。在设置安装之前，机器必须安装Oracle JDK 7或更高版本。
## **安装与使用**
Aspose.Cells for PHP via Java以ZIP格式分发。

要设置环境，安装并使用Aspose.Cells for PHP via Java，请按照以下说明：
### **Linux:**
- 下载[PHP](https://www.php.net/downloads.php)源码并安装。或者使用“sudo apt install php-xxx”命令安装php二进制文件。
- 为Linux安装Oracle JDK（1.7或1.8），配置JAVA_HOME环境变量。
- 下载/获取"Aspose.Cells for PHP via Java" API并解压缩。将会有一个名为"aspose.cells"的文件夹。
- 从 http://php-java-bridge.sourceforge.net/pjb/download.php 下载 PHP/Java Bridge 二进制文件（JavaBridge.jar），并保存到“aspose.cells”文件夹中。
- 从 http://php-java-bridge.sourceforge.net/pjb/download.php 下载 java/Java.inc PHP 库（Java.inc），并保存到“aspose.cells”文件夹中。
- 使用以下命令在上述文件夹中运行“PHP/Java Bridge”。

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
| :- |
- 使用以下命令在“aspose.cells”文件夹中运行“example.php” 来运行示例:

|$ php example.php|
| :- |
### **Windows:**
- 下载[PHP](https://www.php.net/downloads.php)Windows二进制文件，并将“php.exe”添加到PATH。
- 为Windows安装Oracle JDK（1.7或1.8），配置JAVA_HOME环境变量。
- 下载“Aspose.Cells for PHP via Java”API并解压。将会有一个名为“aspose.cells”的文件夹。
- 从 http://php-java-bridge.sourceforge.net/pjb/download.php 下载 PHP/Java Bridge 二进制文件（JavaBridge.jar），并保存到“aspose.cells”文件夹中。
- 从 http://php-java-bridge.sourceforge.net/pjb/download.php 下载 java/Java.inc PHP 库（Java.inc），并保存到“aspose.cells”文件夹中。
- 在上述文件夹中使用以下命令运行“PHP/Java桥”。在桥启动时选择 8080 端口的 http 监听器，并点击“确定”按钮。

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- 使用以下命令在“aspose.cells”文件夹中运行“example.php” 来运行示例:

|> php example.php|
| :- |
### **Mac:**
- 安装[PHP](https://www.php.net/downloads.php)。
- 为 Mac 安装 Oracle JDK（1.7 或 1.8），配置 JAVA_HOME 环境变量。
- 下载“Aspose.Cells for PHP via Java”API并解压。将会有一个名为“aspose.cells”的文件夹。
- 从 http://php-java-bridge.sourceforge.net/pjb/download.php 下载 PHP/Java Bridge 二进制文件（JavaBridge.jar），并保存到“aspose.cells”文件夹中。
- 从 http://php-java-bridge.sourceforge.net/pjb/download.php 下载 java/Java.inc PHP 库（Java.inc），并保存到“aspose.cells”文件夹中。
- 在上述文件夹中使用以下命令运行“PHP/Java桥”。在桥启动时选择 8080 端口的 http 监听器，并点击“确定”按钮。

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- 使用以下命令在“aspose.cells”文件夹中运行“example.php” 来运行示例:

|$ php example.php|
| :- |


