---
title: 在 PHP 中下载并配置 Aspose.Cells
type: docs
weight: 10
url: /zh/java/download-and-configure-aspose-cells-in-php/
---
## **下载所需的库**
下载下面提到的所需库。这些是执行 Aspose.Cells Java PHP 示例所必需的。

- **Aspose:** [Aspose.Cells for Java 组件](https://downloads.aspose.com/cells/java/)
- [PHP/Java 桥梁](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **从社交编码网站下载示例**
以下版本的运行示例可在下面提到的社交编码网站上下载：

-----
### **GitHub**
- **Aspose.Cells Java 用于 PHP 示例** 
  - [Aspose.Cells Java 用于 PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **如何在 Linux 平台上配置源代码**
请按照以下简单步骤在使用时打开和扩展源代码：
## **1.安装Tomcat服务器**
要安装 tomcat 服务器，请在 linux 控制台上发出以下命令。这将成功安装tomcat服务器。

{{< highlight "actionscript3" >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. 下载并配置PHP/JavaBridge**
要下载 PHP/JavaBridge 二进制文件，请在 linux 控制台上发出以下命令。

{{< highlight "actionscript3" >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


通过在 linux 控制台上发出以下命令来解压缩 PHP/JavaBridge 二进制文件。

{{< highlight "actionscript3" >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


这将提取**JavaBridge.war**文件。复制到tomcat88**网络应用程序**通过在 Linux 控制台上发出以下命令来创建文件夹。

{{< highlight "actionscript3" >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


通过复制，tomcat8会自动新建一个文件夹》**Java桥**“ 在**网络应用程序**.创建文件夹后，确保您的 tomcat8 正在运行，然后检查<http://localhost:8080/JavaBridge>在浏览器中，它应该打开一个JavaBridge的默认页面。

如果出现任何错误消息，请安装**快速CGI**通过在 Linux 控制台上发出以下命令。

{{< highlight "actionscript3" >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

安装php5.5 cgi后，重启tomcat8服务器，查看<http://localhost:8080/JavaBridge>再次在浏览器中。

如果**JAVA_主页**显示错误，然后打开 /etc/default/tomcat8 文件并取消注释设置 JAVA_HOME 的行。再次在浏览器中检查 <http://localhost:8080/JavaBridge>，它应该带有 PHP/JavaBridge 示例页面。
## **3.为PHP示例配置Aspose.Cells Java**
通过在 webapps/JavaBridge 文件夹中发出以下命令来克隆 PHP 示例。

{{< highlight "actionscript3" >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP]{{< /highlight >}}

## **Windows平台源码配置方法**
请按照以下简单步骤在 Windows 平台上配置 PHP/Java Bridge

\1.像往常一样安装 PHP5 和配置
\2。如果您还没有安装 JRE 6（Java 运行时环境）。您可以在 C:\Program Files 等中查看。您可以在此处下载。我正在使用 JRE 6，因为它与 PHP Java Bridge (PJB) 兼容。

\3。安装 Apache Tomcat 8.0。你可以在这里下载

4.下载[JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download).将此文件复制到 tomcat webapps 目录。
（例如：C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps）

\5.重启tomcat apache服务。

 6.前往<http://localhost:8080/JavaBridge/test.php>检查 php 是否工作。你可以在那里找到其他例子

7.将你的Aspose.Cells Java jar文件复制到C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

 \8.克隆[Aspose.Cells Java 用于 PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ 文件夹中的示例。

\8.将文件夹 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java 复制到 Aspose.Cells Java for PHP examples 文件夹。

 \10。重新启动 apache tomcat 服务并开始使用示例。
