---
title: Einführung von GridWeb
type: docs
weight: 10
url: /de/java/introduction-of-gridweb/
---
##  **Grundlagen von GridWeb**
 Aspose.Cells.GridWeb ist eine GUI-basierte Websteuerung, die in JSP-Webseiten oder jede HTML-Seite im Java-Server eingebettet werden kann.
{{% alert color="primary" %}} 

Es ist einfach und unkompliziert zu bedienen.

Es hilft Ihnen, schnell einen Online-Webeditor für Tabellenkalkulationsdateien zu erstellen.

Es unterstützt auch den Import und Export aller Arten von Tabellenformatdateien, die zu 100 % mit MS-Excel-Dateien kompatibel sind.

##  **Aspose.Cells.GridWeb – Demos**
{{% alert color="primary" %}} 

Damit Sie schnell einsatzbereit sind, stellen wir eine Reihe von Codebeispielen und Demos zur Verfügung, die zeigen, wie Sie Aspose.Cells.GridWeb API verwenden.

Bitte laden Sie die Demos über den folgenden Link herunter:
[Aspose.Cells.GridWeb Demos](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


##  **So führen Sie Aspose.Cells für GridWeb Java-Demos aus**
{{% alert color="primary" %}} 

 Aspose.Cells für GridWeb Java-Demos sind einfach auszuführen. Sie müssen es nur bereitstellen**Gridwebdemo.war** auf Ihrem Webserver. Bitte laden Sie hier die Demos herunter[Verknüpfung](https://forum.aspose.com/uploads/discourse_instance3/22292).

In diesem Artikel wird beschrieben, wie Sie Aspose.Cells für GridWeb Java-Demos in Apache Tomcat Server ausführen.

{{% /alert %}} 
###  **Schritt-für-Schritt-Anleitung zum Ausführen von GridWeb Java-Demos**
1.  Extrakt**Apache-Tomcat-7.0.52.zip** in einem beliebigen Verzeichnis, z. B. C:\Tomcat

![todo:image_alt_text](introduction-of-gridweb_1.png)



 Der folgende Schnappschuss zeigt die extrahierten Verzeichnisse und Dateien des Apache Tomcat-Servers

![todo:image_alt_text](introduction-of-gridweb_2.png)



 Möglicherweise müssen Sie auch die Umgebungsvariable festlegen**CATALINA_HOME** 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1.  Öffne das**tomcat-users.xml** Datei.

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. Fügen Sie diesen Benutzer hinzu:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Hier ist der Benutzername tomcat und das Passwort ist geheim** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1.  Führen Sie das aus**Startup.bat** Datei.
 Es wird der Apache Tomcat Server ausgeführt.

![todo:image_alt_text](introduction-of-gridweb_6.png)



**Tomcat-Server, der in einem Befehlsfenster ausgeführt wird** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. Öffnen Sie nun den Browser und geben Sie *localhost:8080** ein.
 Die Apache Tomcat-Webseite wird angezeigt.

   **Die Apache Tomcat-Webseite** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1.  Klicken**Manager-App** und geben Sie Benutzernamen und Passwort ein. (Wie oben: Kater, Geheimnis)

![todo:image_alt_text](introduction-of-gridweb_9.png)

1.  Scrollen Sie nach unten zum Abschnitt**WAR-Datei zur Bereitstellung** und durchstöbern Sie die**Gridwebdemo.war** Datei.
1.  Klicken Sie auf *Bereitstellen**.

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. Durchsuche**Gridwebdemo.war** Datei.

![todo:image_alt_text](introduction-of-gridweb_11.png)

1.  Klicken Sie auf *Bereitstellen**.

![todo:image_alt_text](introduction-of-gridweb_12.png)

1.  Sobald es bereitgestellt ist, klicken Sie auf**/gridwebdemo** und beginnen Sie mit der Ausführung von Demos.

![todo:image_alt_text](introduction-of-gridweb_13.png)


 Die GridWeb-Demoseite wird angezeigt.

**Die GridWeb-Demoseite** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1.  Klicken Sie auf eine beliebige Demo und führen Sie sie aus.

   **Inhaltsdemo wird erstellt** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**Arbeitsblätter-Demo läuft** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**HeaderBar- und CommandButton-Demo läuft** 

![todo:image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
##  **Browserfunktionen und Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb ist ein GUI-basiertes Websteuerelement, das wie andere Websteuerelemente in JSP-Webseiten eingebettet werden kann. Das Wichtigste bei der Webkontrolle ist die Bereitstellung browserübergreifender Unterstützung. Aspose.Cells.GridWeb bietet browserübergreifende Unterstützung.
###  **Vergleich**
Aspose.Cells.GridWeb wird vom Internet Explorer (IE) von Microsoft vollständig unterstützt. Bei anderen Browsern gibt es jedoch geringfügige Einschränkungen. Dieses Thema bietet einen detaillierten Vergleich, welche Funktionen von verschiedenen Browsern unterstützt werden.

|**Clientseitige Funktionen**|**Microsoft Internet Explorer**|**Google Chrom**|**Mozilla Firefox**|**Oper**|
| :- | :- | :- | :- | :- |
|Kontextmenü von Cell|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Clientseitige Validierung|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Doppelklicken Sie auf Ereignis|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Dropdown-Liste (*ComboBox-Modus* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Dropdown-Liste (*Popup-Menümodus* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formeleingabe/-bearbeitung|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zeilen/Spalten einfrieren oder freigeben|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Hyperlinks (*CellCommand-Modus* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Hyperlinks (*URL-Modus* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zusammenführen oder Aufheben der Zusammenführung Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Mehrere Cells Kopieren/Einfügen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Mehrere Cells Eingabe/Bearbeitung, einzelnes Postback|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zahlenformat|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Blatt-Paging|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Schreibgeschützt Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Schreibgeschützte Zeilen/Spalten|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Datenvalidierung mit regulären Ausdrücken|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Spaltenbreite ändern|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zeilenhöhe ändern|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Zeilen und Spalten einfügen/löschen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Scrollinhalt|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Blattregisterkarten scrollen|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Legen Sie die Grenzen von Cells fest|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Legen Sie die Schriftarteinstellungen auf Cells fest|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Das Kontextmenü einer Zelle kann nur durch Klicken auf die Schaltfläche „Clientseitiges Menü“ aktiviert werden.
