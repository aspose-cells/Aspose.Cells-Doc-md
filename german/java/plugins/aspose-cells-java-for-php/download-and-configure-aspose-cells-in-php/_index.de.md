---
title: Laden Sie Aspose.Cells in PHP herunter und konfigurieren Sie es
type: docs
weight: 10
url: /de/java/download-and-configure-aspose-cells-in-php/
---
## **Erforderliche Bibliotheken herunterladen**
Laden Sie die unten aufgeführten erforderlichen Bibliotheken herunter. Dies sind die für die Ausführung von Aspose.Cells Java for PHP Beispielen erforderlichen.

- **Aspose:** [Aspose.Cells for Java Komponente](https://downloads.aspose.com/cells/java/)
- [PHP/Java Brücke](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Laden Sie Beispiele von Social-Coding-Sites herunter**
Die folgenden Versionen von Laufbeispielen stehen auf den unten genannten Social-Coding-Sites zum Download zur Verfügung:

-----
### **GitHub**
- **Aspose.Cells Java for PHP Beispiele** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **So konfigurieren Sie den Quellcode auf der Linux-Plattform**
Bitte befolgen Sie diese einfachen Schritte, um den Quellcode zu öffnen und zu erweitern, während Sie ihn verwenden:
## **1. Tomcat-Server installieren**
 Um den Tomcat-Server zu installieren, geben Sie den folgenden Befehl auf der Linux-Konsole ein. Dadurch wird der Tomcat-Server erfolgreich installiert.

{{< highlight "actionscript3" >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. Laden Sie PHP/JavaBridge herunter und konfigurieren Sie es**
 Um die PHP/JavaBridge-Binärdateien herunterzuladen, geben Sie den folgenden Befehl auf der Linux-Konsole ein.

{{< highlight "actionscript3" >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Entpacken Sie die PHP/JavaBridge-Binärdateien, indem Sie den folgenden Befehl auf der Linux-Konsole ausführen.

{{< highlight "actionscript3" >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Dadurch wird extrahiert**JavaBridge.war**Datei. Kopieren Sie es nach tomcat88**webapps** Ordner, indem Sie den folgenden Befehl auf der Linux-Konsole ausgeben.

{{< highlight "actionscript3" >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


Durch das Kopieren erstellt Tomcat8 automatisch einen neuen Ordner "**JavaBridge**" in**webapps**. Stellen Sie nach dem Erstellen des Ordners sicher, dass Ihr Tomcat8 ausgeführt wird, und überprüfen Sie es dann<http://localhost:8080/JavaBridge> im Browser sollte eine Standardseite von JavaBridge geöffnet werden.

 Wenn eine Fehlermeldung angezeigt wird, installieren Sie sie**FastCGI**indem Sie den folgenden Befehl auf der Linux-Konsole ausgeben.

{{< highlight "actionscript3" >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

Starten Sie nach der Installation von php5.5 cgi den Tomcat8-Server neu und überprüfen Sie<http://localhost:8080/JavaBridge>wieder im Browser.

Wenn**JAVA_HOME**Fehler angezeigt wird, öffnen Sie dann die Datei /etc/default/tomcat8 und kommentieren Sie die Zeile aus, die JAVA_HOME. Überprüfen Sie erneut <http://localhost:8080/JavaBridge> im Browser, es sollte eine PHP/JavaBridge-Beispielseite enthalten sein.
## **3. Konfigurieren Sie Aspose.Cells Java for PHP Beispiele**
 Klonen Sie PHP-Beispiele, indem Sie die folgenden Befehle im Ordner webapps/JavaBridge ausführen.

{{< highlight "actionscript3" >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP]{{< /highlight >}}

## **So konfigurieren Sie den Quellcode auf der Windows-Plattform**
Bitte befolgen Sie die folgenden einfachen Schritte, um PHP/Java Bridge auf der Windows-Plattform zu konfigurieren

\1. Installieren Sie PHP5 und konfigurieren Sie es wie gewohnt
\2. Installieren Sie JRE 6 (Java Runtime Environment), falls Sie es noch nicht haben. Sie können dies in C:\Program Files usw. überprüfen. Sie können es hier herunterladen. Ich verwende JRE 6, da es mit PHP Java Bridge (PJB) kompatibel ist.

\3. Installieren Sie Apache Tomcat 8.0. Sie können es hier herunterladen

 4.Herunterladen[JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Kopieren Sie diese Datei in das Tomcat-Webapps-Verzeichnis.
(Bsp.: C:\Programme\Apache Software Foundation\Tomcat 8.0\webapps )

\5. Starten Sie den Tomcat-Apache-Dienst neu.

 6.Gehe zu<http://localhost:8080/JavaBridge/test.php> um zu prüfen, ob php funktioniert. Dort finden Sie weitere Beispiele

7.Kopieren Sie Ihre JAR-Datei Aspose.Cells Java nach C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

 \8. Klon[Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) Beispiele im Ordner C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

\8. Kopieren Sie den Ordner C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java in Ihren Beispielordner Aspose.Cells Java for PHP.

 \10. Starten Sie den Apache Tomcat-Dienst neu und beginnen Sie mit der Verwendung von Beispielen.
