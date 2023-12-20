---
title: Einführung von GridWeb
type: docs
weight: 10
url: /de/java/introduction-of-gridweb/
---
## **So führen Sie Aspose.Cells für GridWeb Java-Demos aus**
{{% alert color="primary" %}} 

 Aspose.Cells für GridWeb Java Demos sind einfach auszuführen. Sie müssen nur bereitstellen**gridwebdemo.war** in Ihrem Webserver. Bitte laden Sie die Demos von diesem herunter[Verknüpfung](https://forum.aspose.com/uploads/discourse_instance3/22292).

Dieser Artikel beschreibt, wie Sie Aspose.Cells für GridWeb Java Demos in Apache Tomcat Server ausführen.

{{% /alert %}} 
### **Schritt-für-Schritt-Anleitung zum Ausführen von GridWeb Java-Demos**
1.  Extrakt**apache-tomcat-7.0.52.zip** in einem beliebigen Verzeichnis zB C:\Tomcat

![todo: Bild_alt_Text](introduction-of-gridweb_1.png)



 Der folgende Schnappschuss zeigt die extrahierten Verzeichnisse und Dateien des Apache-Tomcat-Servers

![todo: Bild_alt_Text](introduction-of-gridweb_2.png)



 Möglicherweise müssen Sie auch die Umgebungsvariable festlegen**CATALINA_HOME** 

![todo: Bild_alt_Text](introduction-of-gridweb_3.png)

1. Öffne das**tomcat-users.xml** Datei.

![todo: Bild_alt_Text](introduction-of-gridweb_4.png)

1. Diesen Benutzer hinzufügen:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Hier ist der Benutzername Kater und das Passwort geheim** 

![todo: Bild_alt_Text](introduction-of-gridweb_5.png)

1.  Führen Sie die aus**startup.bat** Datei.
 Es wird den Apache Tomcat Server ausführen.

![todo: Bild_alt_Text](introduction-of-gridweb_6.png)



**Tomcat-Server, der in einem Befehlsfenster ausgeführt wird** 

![todo: Bild_alt_Text](introduction-of-gridweb_7.png)

1.  Öffnen Sie nun den Browser und geben Sie ein**lokaler Host: 8080**.
 Die Apache Tomcat-Webseite wird angezeigt.

   **Die Apache Tomcat-Webseite** 

![todo: Bild_alt_Text](introduction-of-gridweb_8.png)

1.  Klicken**Manager-App** und geben Sie Benutzername und Passwort ein. (Wie oben: Kater, Geheimnis)

![todo: Bild_alt_Text](introduction-of-gridweb_9.png)

1.  Scrollen Sie nach unten zum Abschnitt**WAR-Datei bereitzustellen** und durchsuchen Sie die**gridwebdemo.war** Datei.
1.  Klicken**Einsetzen**. 

![todo: Bild_alt_Text](introduction-of-gridweb_10.png)

1.  Durchsuche**gridwebdemo.war** Datei.

![todo: Bild_alt_Text](introduction-of-gridweb_11.png)

1.  Klicken**Einsetzen**. 

![todo: Bild_alt_Text](introduction-of-gridweb_12.png)

1.  Sobald es bereitgestellt ist, klicken Sie auf**/gridwebdemo** und starten Sie Demos.

![todo: Bild_alt_Text](introduction-of-gridweb_13.png)


 Die GridWeb-Demoseite wird angezeigt.

**Die GridWeb-Demoseite** 

![todo: Bild_alt_Text](introduction-of-gridweb_14.png)

1.  Klicken Sie auf eine beliebige Demo und führen Sie sie aus.

   **Demo zum Erstellen von Inhalten läuft** 

![todo: Bild_alt_Text](introduction-of-gridweb_15.png)



**Arbeitsblätter-Demo läuft** 

![todo: Bild_alt_Text](introduction-of-gridweb_16.png)



**HeaderBar- und CommandButton-Demo läuft** 

![todo: Bild_alt_Text](introduction-of-gridweb_17.png)
## **Aspose.Cells.GridWeb - Demos**
{{% alert color="primary" %}} 

Damit Sie schnell loslegen können, stellen wir eine Reihe von Codebeispielen und Demos bereit, die zeigen, wie Sie das Aspose.Cells.GridWeb API verwenden.

Bitte laden Sie die Demos über den folgenden Link herunter:
[Aspose.Cells.GridWeb-Demos](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)

{{% /alert %}} 
## **Browserfunktionen und Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb ist ein GUI-basiertes Websteuerelement, das wie andere Websteuerelemente in JSP-Webseiten eingebettet werden kann. Das Wichtigste an der Websteuerung ist die Bereitstellung von Cross-Browser-Unterstützung. Aspose.Cells. GridWeb bietet browserübergreifende Unterstützung.
### **Vergleich**
Aspose.Cells.GridWeb wird vom Internet Explorer (IE) von Microsoft vollständig unterstützt. Bei anderen Browsern gibt es jedoch geringfügige Einschränkungen. Dieses Thema enthält einen detaillierten Vergleich, welche Funktionen von verschiedenen Browsern unterstützt werden.

|**Clientseitige Funktionen**|**Microsoft Internet Explorer**|**Google Chrom**|**Mozilla-Firefox**|**Oper**|
|:- |:- |:- |:- |:- |
|Kontextmenü von Cell|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Clientseitige Validierung|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Doppelklick-Ereignis|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Dropdown-Liste (*ComboBox-Modus* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Dropdown-Liste (*Popup-Menü-Modus* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formeleingabe/-bearbeitung|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Einfrieren oder Freigeben von Zeilen/Spalten|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Hyperlinks (*CellCommand-Modus* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Hyperlinks (*URL-Modus* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zusammenführen oder Zusammenführung aufheben Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Mehrere Cells Kopieren/Einfügen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Mehrere Cells Input/Edit, Single Postback|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zahlenformat|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Blatt-Paging|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Schreibgeschützt Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Schreibgeschützte Zeilen/Spalten|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Datenvalidierung mit regulären Ausdrücken|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Spaltenbreite ändern|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zeilenhöhe ändern|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zeilen und Spalten einfügen/löschen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Inhalt scrollen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Blätterblatt-Tabs|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Legen Sie Grenzen von Cells fest|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Stellen Sie die Schriftarteinstellungen auf Cells ein|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Das Kontextmenü einer Zelle kann nur durch Klicken auf die Menüschaltfläche Clientseite aktiviert werden.
