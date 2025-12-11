---
title: Download and Configure Aspose.Cells in PHP
type: docs
weight: 10
url: /java/download-and-configure-aspose-cells-in-php/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Download Required Libraries**
Download the required libraries mentioned below. These are required for executing Aspose.Cells Java for PHP examples.

- **Aspose:** [Aspose.Cells for Java Component](https://downloads.aspose.com/cells/java/)
- [PHP/Java Bridge](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)

## **Download Examples from Social Coding Sites**
The following runnable examples are available for download on the social coding sites mentioned below:

-----

### **GitHub**
- **Aspose.Cells Java for PHP Examples**  
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)

## **How to configure the source code on Linux Platform**
Please follow these simple steps in order to open and extend the source code while using:

## **1. Install Tomcat Server**
To install Tomcat server, issue the following command on the Linux console. This will install Tomcat server.

{{< highlight actionscript3 >}}
sudo apt-get install tomcat8
{{< /highlight >}}

## **2. Download and Configure PHP/JavaBridge**
In order to download the PHP/JavaBridge binaries, issue the following command on the Linux console.

{{< highlight actionscript3 >}}
wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip
{{< /highlight >}}

Unzip the PHP/JavaBridge binaries by issuing the following command on the Linux console.

{{< highlight actionscript3 >}}
unzip -d php-java-bridge_6.2.1_documentation.zip 
{{< /highlight >}}

This will extract **JavaBridge.war** file. Copy it to the tomcat8 **webapps** folder by issuing the following command on the Linux console.

{{< highlight actionscript3 >}}
sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 
{{< /highlight >}}

By copying, tomcat8 will automatically create a new folder **JavaBridge** in **webapps**. Once the folder is created, make sure tomcat8 is running and then check <http://localhost:8080/JavaBridge> in a browser; it should open the default page of JavaBridge.

If any error message appears, install **FastCGI** by issuing the following command on the Linux console.

{{< highlight actionscript3 >}}
sudo apt-get install php55-cgi 
{{< /highlight >}}

After installing php5.5 CGI, restart the tomcat8 server and check <http://localhost:8080/JavaBridge> again in the browser.

If a **JAVA_HOME** error is displayed, open the `/etc/default/tomcat8` file and uncomment the line that sets `JAVA_HOME`. Check <http://localhost:8080/JavaBridge> again; it should show the PHP/JavaBridge Examples page.

## **3. Configure Aspose.Cells Java for PHP Examples**
Clone the PHP examples by issuing the following commands inside the `webapps/JavaBridge` folder.

{{< highlight actionscript3 >}}
git init
git clone https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP
{{< /highlight >}}

## **How to configure the source code on Windows Platform**
Please follow the simple steps below to configure PHP/Java Bridge on Windows Platform.

1. Install PHP 5 and configure it as you normally do.  
2. Install JRE 6 (Java Runtime Environment) if you don’t already have it. You can check this in `C:\Program Files`, etc. You can download it here. I am using JRE 6 as it is compatible with PHP Java Bridge (PJB).  
3. Install Apache Tomcat 8.0. You can download it here.  
4. Download [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copy this file to the Tomcat `webapps` directory (e.g., `C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps`).  
5. Restart the Tomcat service.  
6. Go to <http://localhost:8080/JavaBridge/test.php> to check if PHP works. You can find other examples there.  
7. Copy your Aspose.Cells Java JAR file to `C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib`.  
8. Clone the Aspose.Cells Java for PHP examples inside the `C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\` folder.  
9. Copy the folder `C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java` to your Aspose.Cells Java for PHP examples folder.  
10. Restart the Apache Tomcat service and start using the examples.
