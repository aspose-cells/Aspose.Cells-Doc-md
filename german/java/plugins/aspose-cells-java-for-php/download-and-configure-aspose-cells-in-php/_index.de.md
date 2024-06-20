---
title: Aspose.Cells in PHP herunterladen und konfigurieren
type: docs
weight: 10
url: /de/java/download-and-configure-aspose-cells-in-php/
---

## **Erforderliche Bibliotheken herunterladen**
Die unten genannten erforderlichen Bibliotheken herunterladen. Diese sind erforderlich zur Ausführung von Beispielen zu Aspose.Cells Java für PHP.

- **Aspose:** [Aspose.Cells for Java Komponente](https://downloads.aspose.com/cells/java/)
- [PHP/Java-Brücke](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Beispiele von Social Coding Sites herunterladen**
Folgende Versionen von laufenden Beispielen können auf den unten genannten Social Coding Sites heruntergeladen werden:

-----
### **GitHub**
- **Aspose.Cells Java für PHP Beispiele** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **So konfigurieren Sie den Quellcode auf der Linux-Plattform**
Bitte befolgen Sie diese einfachen Schritte, um den Quellcode zu öffnen und zu erweitern, während Sie verwenden:
## **1. Tomcat Server installieren**
Um den Tomcat-Server zu installieren, geben Sie den folgenden Befehl in die Linux-Konsole ein. Dies installiert den Tomcat-Server erfolgreich. 

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. PHP/JavaBridge herunterladen und konfigurieren**
Um die PHP/JavaBridge-Binärdateien herunterzuladen, geben Sie den folgenden Befehl in die Linux-Konsole ein. 

{{< highlight actionscript3 >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Entpacken Sie die PHP/JavaBridge-Binärdateien, indem Sie den folgenden Befehl in der Linux-Konsole eingeben. 

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Dadurch wird die Datei **JavaBridge.war** extrahiert. Kopieren Sie sie in den **webapps**-Ordner von tomcat8, indem Sie den folgenden Befehl in der Linux-Konsole eingeben. 

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


By copying, tomcat8 will automatically create a new folder "**JavaBridge**" in **webapps**. Once the folder is created, make sure your tomcat8 is running and then check <http://localhost:8080/JavaBridge> in browser, it should open a default page of JavaBridge. 

Wenn eine Fehlermeldung angezeigt wird, installieren Sie **FastCGI**, indem Sie den folgenden Befehl in der Linux-Konsole ausgeben.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

After installing php5.5 cgi, restart tomcat8 server and check <http://localhost:8080/JavaBridge> again in the browser.

If **JAVA_HOME** error is displayed, then open /etc/default/tomcat8 file and uncomment the line that sets the JAVA_HOME. Check <http://localhost:8080/JavaBridge> in browser again, it should come with PHP/JavaBridge Examples page. 
## **3. Konfigurieren Sie Aspose.Cells Java für PHP-Beispiele**
Klonen Sie PHP-Beispiele, indem Sie die folgenden Befehle im webapps/JavaBridge-Verzeichnis ausgeben.  

{{< highlight actionscript3 >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP] 

{{< /highlight >}}

## **Wie man den Quellcode auf der Windows-Plattform konfiguriert**
Bitte befolgen Sie die folgenden einfachen Schritte, um die PHP/Java Bridge unter Windows zu konfigurieren

\1. Installieren Sie PHP5 und konfigurieren Sie es wie gewohnt
\2. Installieren Sie JRE 6 (Java-Laufzeitumgebung), wenn Sie es noch nicht haben. Sie können dies in C:\Programme usw. überprüfen. Sie können es hier herunterladen. Ich verwende JRE 6, da es mit PHP Java Bridge (PJB) kompatibel ist.

\3. Installieren Sie Apache Tomcat 8.0. Sie können es hier herunterladen

4. Laden Sie [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download) herunter. Kopieren Sie diese Datei in das Verzeichnis tomcat webapps.
(z. B. C:\Programme\Apache Software Foundation\Tomcat 8.0\webapps )

\5. Starten Sie den Tomcat Apache-Dienst neu.

6.Go to <http://localhost:8080/JavaBridge/test.php> to check if php works. You can find other examples in there

7. Kopieren Sie Ihre Aspose.Cells Java-Jar-Datei nach C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

\8. Klonen Sie [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) Beispiele im Verzeichnis C:\Programme\Apache Software Foundation\Tomcat 8.0\webapps\.

\8. Kopieren Sie den Ordner C:\Programme\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java in Ihren Aspose.Cells Java for PHP Beispiele-Ordner.

\10. Starten Sie den Apache Tomcat-Dienst neu und beginnen Sie mit der Verwendung von Beispielen. 
