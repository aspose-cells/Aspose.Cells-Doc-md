---
title: Einführung von GridWeb
type: docs
weight: 10
url: /de/java/introduction-of-gridweb/
---
## **Grundlagen von GridWeb**
Aspose.Cells.GridWeb ist eine GUI-basierte Web-Steuerung, die in JSP-Webseiten oder jeder HTML-Seite in Java Server eingebettet werden kann. 
{{% alert color="primary" %}} 

Es ist einfach und leicht zu bedienen.

Es hilft Ihnen dabei, schnell einen Online-Web-Editor für Tabellendateien zu erstellen.

Es unterstützt auch den Import und Export von Spreadsheets in allen Formaten, die zu 100% mit MS Excel kompatibel sind.

## **Aspose.Cells.GridWeb - Demos**
{{% alert color="primary" %}} 

Um schnell an den Start zu kommen, stellen wir eine Reihe von Codebeispielen und Demos bereit, die zeigen, wie man die Aspose.Cells.GridWeb API verwendet.

Bitte laden Sie die Demos über den unten stehenden Link herunter:
[Aspose.Cells.GridWeb Demos](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


## **Wie man Aspose.Cells für GridWeb Java Demos ausführt**
{{% alert color="primary" %}} 

Aspose.Cells für GridWeb Java Demos sind einfach auszuführen. Sie müssen einfach **gridwebdemo.war** in Ihren Webserver bereitstellen. Bitte laden Sie die Demos von diesem [Link](https://forum.aspose.com/uploads/discourse_instance3/22292) herunter.

Dieser Artikel beschreibt, wie man Aspose.Cells für GridWeb Java Demos im Apache Tomcat Server ausführt.

{{% /alert %}} 
### **Schritt-für-Schritt-Anleitung zum Ausführen der GridWeb Java Demos**
1. Entpacken Sie **apache-tomcat-7.0.52.zip** in einem beliebigen Verzeichnis z.B. C:\Tomcat 

![todo:image_alt_text](introduction-of-gridweb_1.png)



Der folgende Screenshot zeigt die extrahierten Verzeichnisse und Dateien des Apache Tomcat Servers 

![todo:image_alt_text](introduction-of-gridweb_2.png)



Möglicherweise müssen Sie auch die Umgebungsvariable **CATALINA_HOME** setzen 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1. Öffnen Sie die Datei **tomcat-users.xml**. 

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. Fügen Sie diesen Benutzer hinzu:

{{< highlight java >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Hier ist der Benutzername tomcat und das Passwort ist secret** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1. Führen Sie die Datei **startup.bat** aus.
   Es wird der Apache Tomcat Server ausgeführt. 

![todo:image_alt_text](introduction-of-gridweb_6.png)



**Apache Tomcat Server läuft in einem Befehlsfenster** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. Öffnen Sie jetzt den Browser und geben Sie **localhost:8080** ein.
   Die Apache Tomcat-Webseite wird angezeigt. 

   **Die Apache Tomcat-Webseite** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1. Klicken Sie auf **Manager-App** und geben Sie Benutzername und Passwort ein (wie oben: tomcat, secret) 

![todo:image_alt_text](introduction-of-gridweb_9.png)

1. Scrollen Sie zum Abschnitt **Zu implementierende WAR-Datei** und durchsuchen Sie die Datei **gridwebdemo.war**.
1. Klicken Sie auf **Bereitstellen**. 

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. Durchsuchen Sie die Datei **gridwebdemo.war**. 

![todo:image_alt_text](introduction-of-gridweb_11.png)

1. Klicken Sie auf **Bereitstellen**. 

![todo:image_alt_text](introduction-of-gridweb_12.png)

1. Sobald es bereitgestellt ist, klicken Sie auf **/gridwebdemo** und starten Sie Demos. 

![todo:image_alt_text](introduction-of-gridweb_13.png)


Die GridWeb-Demo-Seite wird angezeigt. 

**Die GridWeb-Demo-Seite** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1. Klicken Sie auf eine beliebige Demo und führen Sie sie aus. 

   **Erstellen von Inhalten Demo läuft** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**Arbeitsblätter-Demo läuft** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**HeaderBar und CommandButton-Demo wird ausgeführt** 

![todo:image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
## **Browserfunktionen und Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb ist ein GUI-basiertes Websteuerelement, das in JSP-Webseiten wie andere Websteuerelemente eingebettet werden kann. Das Wichtigste an Web-Steuerelementen ist die Unterstützung für verschiedene Browser. Aspose.Cells.GridWeb bietet eine solche Unterstützung.
### **Vergleich**
Aspose.Cells.GridWeb wird vollständig von Microsoft's Internet Explorer (IE) unterstützt. Auf anderen Browsern gibt es jedoch geringfügige Einschränkungen. Dieses Thema bietet einen detaillierten Vergleich, welche Funktionen von verschiedenen Browsern unterstützt werden.

|**Client-Seitenfunktionen**|**Microsoft Internet Explorer**|**Google Chrome**|**Mozilla Firefox**|**Opera**|
| :- | :- | :- | :- | :- |
|Kontextmenü der Zelle|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Clientseitige Validierung|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Doppelklick-Ereignis|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|DropDown-Liste ( *ComboBox-Modus* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|DropDown-Liste ( *Popup-Menü-Modus* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formeleingabe/Bearbeitung|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zeilen/Spalten fixieren oder lösen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Hyperlinks ( *CellCommand-Modus* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Hyperlinks ( *URL-Modus* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zellen zusammenführen oder trennen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Mehrere Zellen kopieren/einfügen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Mehrere Zellen eingeben/bearbeiten, einzelnes Postback|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zahlenformat|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Blättern im Arbeitsblatt|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Schreibgeschützte Zellen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Schreibgeschützte Zeilen/Spalten|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Datenvalidierung mit regulären Ausdrücken|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Spaltenbreite ändern|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zeilenhöhe ändern|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zeilen & Spalten einfügen/löschen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Inhalt scrollen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Registerkarten scrollen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zellenränder festlegen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Schriftart-Einstellungen der Zellen festlegen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Context menu of a cell can only be activated by clicking the Client side menu button.
