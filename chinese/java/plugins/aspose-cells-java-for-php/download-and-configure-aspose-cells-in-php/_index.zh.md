---
title: 下载并配置PHP中的Aspose.Cells
type: docs
weight: 10
url: /zh/java/download-and-configure-aspose-cells-in-php/
---

## **下载所需的库**
下载下面提到的所需库。这些库是执行Aspose.Cells Java for PHP示例所必需的。

- **Aspose:** [Aspose.Cells for Java组件](https://downloads.aspose.com/cells/java/)
- [PHP/Java桥](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **从社交编码网站下载示例**
可在下面列出的社交编码网站上下载以下版本的运行示例:

-----
### **GitHub**
- **Aspose.Cells Java for PHP 示例** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **如何在Linux平台上配置源代码**
请按以下简单步骤进行，以便在使用时打开和扩展源代码:
## **1. 安装Tomcat服务器**
要安装Tomcat服务器，请在Linux控制台上输入以下命令。这将成功安装Tomcat服务器。 

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. 下载并配置PHP/JavaBridge**
为了下载PHP/JavaBridge二进制文件，请在Linux控制台上输入以下命令。 

{{< highlight actionscript3 >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


通过在Linux控制台上输入以下命令来解压PHP/JavaBridge二进制文件。 

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


这将提取**JavaBridge.war**文件。通过在Linux控制台上输入以下命令，将其复制到tomcat88的**webapps**文件夹中。 

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


By copying, tomcat8 will automatically create a new folder "**JavaBridge**" in **webapps**. Once the folder is created, make sure your tomcat8 is running and then check <http://localhost:8080/JavaBridge> in browser, it should open a default page of JavaBridge. 

如果出现任何错误消息，请通过在Linux控制台上输入以下命令来安装 **FastCGI**。

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

After installing php5.5 cgi, restart tomcat8 server and check <http://localhost:8080/JavaBridge> again in the browser.

If **JAVA_HOME** error is displayed, then open /etc/default/tomcat8 file and uncomment the line that sets the JAVA_HOME. Check <http://localhost:8080/JavaBridge> in browser again, it should come with PHP/JavaBridge Examples page. 
## **3. 配置Aspose.Cells Java for PHP示例**
通过在webapps/JavaBridge文件夹内输入以下命令来克隆PHP示例。  

{{< highlight actionscript3 >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP] 

{{< /highlight >}}

## **如何在Windows平台上配置源代码**
请按照以下简单步骤在Windows平台上配置PHP/Java Bridge

1. 安装PHP5并像通常一样配置
2. 安装JRE 6（Java运行时环境），如果还没有安装。您可以在C:\Program Files等位置检查。您可以在此处下载它。我正在使用JRE 6因为它与PHP Java Bridge（PJB）兼容。

3. 安装Apache Tomcat 8.0。您可以在此处下载。

4. 下载[JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download)。将此文件复制到tomcat webapps目录。
(例如：C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

\5. 重新启动Tomcat Apache服务。

6.Go to <http://localhost:8080/JavaBridge/test.php> to check if php works. You can find other examples in there

7. 将您的Aspose.Cells Java jar文件复制到C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

\8. 在C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\文件夹中克隆[Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) 示例。

\8. 将文件夹C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java复制到您的Aspose.Cells Java for PHP示例文件夹。

\10. 重新启动Apache Tomcat服务并开始使用示例。 
