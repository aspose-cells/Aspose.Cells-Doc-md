---
title: Ladda ner och konfigurera Aspose.Cells i PHP
type: docs
weight: 10
url: /sv/java/download-and-configure-aspose-cells-in-php/
---

## **Hämta nödvändiga bibliotek**
Ladda ner de nödvändiga biblioteken som nämns nedan. Dessa krävs för att köra exempel på Aspose.Cells Java för PHP.

- **Aspose:** [Aspose.Cells for Java Component](https://downloads.aspose.com/cells/java/)
- [PHP/Java Bridge](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Hämta exempel från sociala kodningssajter**
Följande versioner av körande exempel finns tillgängliga att ladda ner på nedan angivna sociala kodningssajter:

-----
### **GitHub**
- **Aspose.Cells Java för PHP Exempel** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Hur man konfigurerar källkoden på Linux-plattform**
Följ dessa enkla steg för att öppna och utöka källkoden medan du använder:
## **1. Installera Tomcat Server**
För att installera tomcat-server, ange följande kommando i Linux-konsolen. Detta kommer att installera tomcat-server framgångsrikt. 

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. Ladda ner och konfigurera PHP/JavaBridge**
För att ladda ner PHP/JavaBridge-binärer, ange följande kommando i Linux-konsolen. 

{{< highlight actionscript3 >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Packa upp PHP/JavaBridge-binärerna genom att ange följande kommando i Linux-konsolen. 

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Detta kommer att extrahera **JavaBridge.war**-filen. Kopiera den till tomcat88 **webapps**-mappen genom att ange följande kommando i Linux-konsolen. 

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


By copying, tomcat8 will automatically create a new folder "**JavaBridge**" in **webapps**. Once the folder is created, make sure your tomcat8 is running and then check <http://localhost:8080/JavaBridge> in browser, it should open a default page of JavaBridge. 

Om något felmeddelande visas, installera **FastCGI** genom att ange följande kommando i Linux-konsolen.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

After installing php5.5 cgi, restart tomcat8 server and check <http://localhost:8080/JavaBridge> again in the browser.

If **JAVA_HOME** error is displayed, then open /etc/default/tomcat8 file and uncomment the line that sets the JAVA_HOME. Check <http://localhost:8080/JavaBridge> in browser again, it should come with PHP/JavaBridge Examples page. 
## **3. Konfigurera Aspose.Cells Java för PHP Exempel**
Klona PHP-exempel genom att utfärda följande kommandon inuti webapps/JavaBridge-mappen.  

{{< highlight actionscript3 >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP] 

{{< /highlight >}}

## **Hur man konfigurerar källkoden på Windows-plattformen**
Följ nedan enkla steg för att konfigurera PHP/Java Bridge på Windows-plattformen

1. Installera PHP5 och konfigurera som du normalt gör
2. Installera JRE 6 (Java Runtime Environment) om du inte redan har det. Du kan kontrollera detta i C:\Program Files etc. Du kan ladda ner det här. Jag använder JRE 6 eftersom det är kompatibelt med PHP Java Bridge (PJB).

3. Installera Apache Tomcat 8.0. Du kan ladda ner det här

4. Ladda ner [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Kopiera denna fil till tomcat webapps-mappen.
(t.ex. C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

5. Starta om tomcat apache-tjänsten.

6.Go to <http://localhost:8080/JavaBridge/test.php> to check if php works. You can find other examples in there

7. Kopiera din Aspose.Cells Java jar-fil till C: \ Program Files \ Apache Software Foundation \ Tomcat 8.0 \ webapps \ JavaBridge \ WEB-INF \ lib

8. Klon [Aspose.Cells Java för PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) exempel inne i C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\mappen.

8. Kopiera mappen C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java till din Aspose.Cells Java för PHP-exempelmapp.

10. Starta om apache tomcat-tjänsten och börja använda exempel. 
