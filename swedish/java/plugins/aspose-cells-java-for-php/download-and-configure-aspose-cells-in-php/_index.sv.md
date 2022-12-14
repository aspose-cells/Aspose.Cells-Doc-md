---
title: Ladda ner och konfigurera Aspose.Cells i PHP
type: docs
weight: 10
url: /sv/java/download-and-configure-aspose-cells-in-php/
---
## **Ladda ner obligatoriska bibliotek**
Ladda ner nödvändiga bibliotek som nämns nedan. Dessa är nödvändiga för att exekvera Aspose.Cells Java för PHP-exempel.

- **Aspose:** [Aspose.Cells för Java-komponent](https://downloads.aspose.com/cells/java/)
- [PHP/Java Bridge](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Ladda ner exempel från webbplatser för social kodning**
Följande versioner av löpande exempel finns att ladda ner på nedan nämnda webbplatser för social kodning:

-----
### **GitHub**
- **Aspose.Cells Java för PHP-exempel** 
  - [Aspose.Cells Java för PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Hur man konfigurerar källkoden på Linux-plattformen**
Följ dessa enkla steg för att öppna och utöka källkoden medan du använder:
## **1. Installera Tomcat Server**
För att installera tomcat-server, utfärda följande kommando på linux-konsolen. Detta kommer att installera tomcat-servern.

{{< highlight "actionscript3" >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. Ladda ner och konfigurera PHP/JavaBridge**
 För att ladda ner PHP/JavaBridge-binärfilerna, utfärda följande kommando på linux-konsolen.

{{< highlight "actionscript3" >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


 Packa upp PHP/JavaBridge-binärfilerna genom att utfärda följande kommando på linux-konsolen.

{{< highlight "actionscript3" >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Detta kommer att extrahera**JavaBridge.war**fil. Kopiera den till tomcat88**webbappar** mapp genom att utfärda följande kommando på Linux-konsolen.

{{< highlight "actionscript3" >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


Genom att kopiera kommer tomcat8 automatiskt att skapa en ny mapp "**JavaBridge**" i**webbappar**. När mappen har skapats, se till att din tomcat8 körs och kontrollera sedan<http://localhost:8080/JavaBridge> i webbläsaren bör den öppna en standardsida för JavaBridge.

 Om något felmeddelande visas, installera**FastCGI**genom att utfärda följande kommando på Linux-konsolen.

{{< highlight "actionscript3" >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

Efter att ha installerat php5.5 cgi, starta om tomcat8-servern och kontrollera<http://localhost:8080/JavaBridge>igen i webbläsaren.

Om**JAVA_HOME**felet visas, öppna sedan filen /etc/default/tomcat8 och avkommentera raden som ställer in JAVA_HOME. Kontrollera <http://localhost:8080/JavaBridge> i webbläsaren igen, den bör komma med PHP/JavaBridge-exempelsidan.
## **3. Konfigurera Aspose.Cells Java för PHP-exempel**
 Klona, PHP-exempel genom att utfärda följande kommandon i webapps/JavaBridge-mappen.

{{< highlight "actionscript3" >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP]{{< /highlight >}}

## **Hur man konfigurerar källkoden på Windows-plattformen**
Följ de enkla stegen nedan för att konfigurera PHP/Java Bridge på Windows-plattformen

\1. Installera PHP5 och konfigurera som du normalt gör
\2. Installera JRE 6 (Java Runtime Environment) om du inte redan har det. Du kan kontrollera detta i C:\Program Files etc. Du kan ladda ner det här . Jag använder JRE 6 eftersom det är kompatibelt med PHP Java Bridge (PJB).

\3. Installera Apache Tomcat 8.0. Du kan ladda ner den här

 4. Ladda ner[JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Kopiera den här filen till tomcat webapps-katalogen.
(ex: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

\5. Starta om Tomcat Apache-tjänsten.

 6. Gå till<http://localhost:8080/JavaBridge/test.php> för att kontrollera om php fungerar. Du kan hitta andra exempel där

7. Kopiera din Aspose.Cells Java jar-fil till C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

 \8. Klona[Aspose.Cells Java för PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) exempel i mappen C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

\8. Kopiera mappen C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java till mappen Aspose.Cells Java för PHP-exempel.

 \10. Starta om apache tomcat-tjänsten och börja använda exempel.
