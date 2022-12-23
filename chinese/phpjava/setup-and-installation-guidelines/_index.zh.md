---
title: 设置和安装指南
type: docs
weight: 20
url: /zh/php-java/setup-and-installation-guidelines/
keywords: php, excel, instal
description: 设置 Aspose.Cells for PHP via Java 和安装指南
---
## **系统要求**
Aspose.Cells for PHP via Java 与平台无关 API 并且可以在任何平台（Windows、Linux、MacOS 等）上使用，其中[PHP](https://www.php.net/downloads.php)安装了 7 或更高版本。在设置安装之前，机器必须具有 Oracle JDK 7 或更高版本。
## **安装与使用**
Aspose.Cells for PHP via Java 作为 ZIP 存档分发。

要设置环境，安装和使用 Aspose.Cells for PHP via Java，请按照说明进行操作：
### **Linux：**
- 下载[PHP](https://www.php.net/downloads.php)来源并安装它。或者，使用“sudo apt install php-xxx”命令安装 php 二进制文件。
- 安装适用于 Linux 的 Oracle JDK（1.7 或 1.8），配置 JAVA_HOME 环境变量。
- 下载/获取“Aspose.Cells for PHP via Java”API并解压。将有一个名为“aspose.cells”的文件夹。
- 从 http://php-java-bridge.sourceforge.net/pjb/download.php 下载 PHP/Java Bridge 二进制文件 (JavaBridge.jar) 并将其保存到“aspose.cells”文件夹中。
- 从 http://php-java-bridge.sourceforge.net/pjb/download.php 下载 java/Java.inc PHP 库 (Java.inc) 并将其保存到“aspose.cells”文件夹中。
- 使用以下命令在上述文件夹中运行“PHP/Java Bridge”。

|$Java_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_本地：8080 >/dev/null 2>&1 &|
|:- |
- 在“aspose.cells”文件夹中运行“example.php”以使用以下命令运行示例：

|$ php 示例.php|
|:- |
### **Windows:**
- 下载[PHP](https://www.php.net/downloads.php)Windows 二进制并将“php.exe”添加到 PATH。
- 为Windows安装Oracle JDK（1.7或1.8）并配置JAVA_HOME环境变量。
- 下载“Aspose.Cells for PHP via Java”API并解压。将有一个名为“aspose.cells”的文件夹。
- 从 http://php-java-bridge.sourceforge.net/pjb/download.php 下载 PHP/Java Bridge 二进制文件 (JavaBridge.jar) 并将其保存到“aspose.cells”文件夹中。
- 从 http://php-java-bridge.sourceforge.net/pjb/download.php 下载 java/Java.inc PHP 库 (Java.inc) 并将其保存到“aspose.cells”文件夹中。
- 使用以下命令在上述文件夹中运行“PHP/Java Bridge”。在桥启动时选择 8080 http 侦听器端口，然后单击确定按钮。

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- 在“aspose.cells”文件夹中运行“example.php”以使用以下命令运行示例：

|> PHP 示例.php|
|:- |
### **苹果：**
- 安装[PHP](https://www.php.net/downloads.php).
- 安装 Oracle JDK（1.7 或 1.8）for Mac，配置 JAVA_HOME 环境变量。
- 下载“Aspose.Cells for PHP via Java”API并解压。将有一个名为“aspose.cells”的文件夹。
- 从 http://php-java-bridge.sourceforge.net/pjb/download.php 下载 PHP/Java Bridge 二进制文件 (JavaBridge.jar) 并将其保存到“aspose.cells”文件夹中。
- 从 http://php-java-bridge.sourceforge.net/pjb/download.php 下载 java/Java.inc PHP 库 (Java.inc) 并将其保存到“aspose.cells”文件夹中。
- 使用以下命令在上述文件夹中运行“PHP/Java Bridge”。在桥启动时选择 8080 http 侦听器端口，然后单击确定按钮。

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- 在“aspose.cells”文件夹中运行“example.php”以使用以下命令运行示例：

|$ php 示例.php|
|:- |


