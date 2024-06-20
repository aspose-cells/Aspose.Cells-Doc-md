---
title: Einstieg in den Tabellen Editor
type: docs
weight: 10
url: /de/java/spreadsheet-editor-getting-started/
---

**Inhaltsverzeichnis**

- [Einführung](#SpreadsheetEditorGettingStarted-Introduction)
- [Systemanforderungen](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [Herunterladen und Installation](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Unterstützung](#SpreadsheetEditorGettingStarted-Support)
- [Beitragen](#SpreadsheetEditorGettingStarted-Contribute)
- [Lizenz](#SpreadsheetEditorGettingStarted-License)
### **Einführung**
Html5 Spreadsheet Editor ist eine Webanwendung, mit der Tabellendokumente in einem Webbrowser angezeigt und bearbeitet werden können. Es unterstützt Excel, SpreadsheetML, CVS, OpenDocument und viele andere von Microsoft Excel unterstützte Formate. Alle grundlegenden Funktionen wie Zellenbearbeitung, Formatierung, Formelbearbeitung, Zeilen- und Spaltenverwaltung usw. werden unterstützt.

![todo:image_alt_text](aowcrc1.png)

HTML5 Spreadsheet Editor verwendet viele Funktionen von [Aspose.Cells for Java](https://products.aspose.com/cells/java/) und zeigt, wie sie verwendet werden können, um eine Tabelle in Ihrer Java-Anwendung zu erstellen, zu manipulieren und darzustellen.

**Eigenschaften**

- Arbeiten mit Dateien 
  - Unterstützte Formate
  - Lokale Dateien öffnen
  - Aus Dropbox öffnen
  - Aus URL öffnen
  - Neue Tabelle erstellen
  - Exportieren in verschiedene Formate
- Arbeiten mit Blättern 
  - Blätter hinzufügen und entfernen
  - Blätter umbenennen
  - Zwischen Blättern wechseln
- Arbeiten mit Zeilen und Spalten 
  - Eine Zeile hinzufügen
  - Eine Spalte hinzufügen
  - Zeile entfernen
  - Spalte entfernen
  - Spaltenbreite und Zeilenhöhe
- Arbeiten mit Zellen 
  - Auswahl einer Zelle
  - Bearbeiten einer Zelle
  - Formel bearbeiten
  - Zellenausrichtung
  - Zelle leeren
  - Zelle hinzufügen
  - Zelle entfernen
- Arbeiten mit Textformatierung 
  - Fett, kursiv, unterstrichen
  - Schriftart und -größe
  - Formatierung löschen
### **Systemanforderungen**
**Softwareanforderungen**

- CDI-unterstützter Java-Anwendungsserver
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**Hardware-Anforderungen**

Die Hardware-Anforderungen variieren je nach dem Java-Anwendungsserver, den wir für die Bereitstellung des HTML5-Tabelleneditors wählen, und der Anzahl der gleichzeitig geöffneten Tabellen. Nachfolgend eine Schätzung, die bei der erstmaligen Einrichtung der Umgebung helfen wird.

- 2 GHz CPU
- 2 GB RAM
- 500 MB Festplatte
### **Herunterladen und Installation**
HTML5 Tabelleneditor ist eine Java EE-Anwendung und kann auf jedem Java-Anwendungsserver mit CDI-Unterstützung bereitgestellt werden. Er wurde mit [Glassfish](https://javaee.github.io/glassfish/) getestet.

**Quellcode**

Der Projektquellcode ist auf [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/) verfügbar. Wir pflegen auch Git-Spiegelungen auf den folgenden Websites:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Code](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Verwenden Sie einen der folgenden Befehle, um den Quellcode über die Befehlszeile herunterzuladen:

**Github**

{{< highlight bash >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight bash >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Code**

{{< highlight bash >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight bash >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Mit Maven erstellen**

Der Projekt-Build-Prozess wird mit Maven verwaltet. Sie können also ohne IDE über die Befehlszeile eine WAR-Datei erstellen. Verwenden Sie den folgenden Befehl, um eine WAR-Datei für die Bereitstellung zu generieren. Die Dokumentation des entsprechenden Anwendungsservers wird Ihnen dabei helfen, die generierte WAR-Datei und deren Abhängigkeiten zu bereitzustellen.

{{< highlight java >}}

 mvn clean install

{{< /highlight >}}

**Mit NetBeans verwenden**

Es ist sehr einfach, das Projekt mit der [NetBeans IDE](https://netbeans.apache.org/) zu verwalten. NetBeans ist eine der beliebtesten IDEs unter Java-Entwicklern und wird von Oracle unterstützt.

- Laden Sie den Projekt-Quellcode herunter.
- Öffnen Sie das Projekt in der NetBeans IDE.
- Klicken Sie auf die Schaltfläche ***Ausführen*** in der Symbolleiste.
- Wählen Sie den ***Glassfish***-Server als Anwendungsserver aus.

**Mit Eclipse**

[Eclipse IDE](http://www.eclipse.org/ide/) bietet eine offizielle Integration zum Import von Maven-Projekten namens [M2Eclipse](http://www.eclipse.org/m2e/):

1. Installieren Sie M2Eclipse in Ihrer Eclipse IDE. Die Installationsanleitung finden Sie auf ihrer Website.
1. Laden Sie den Projekt-Quellcode herunter.
1. Öffnen Sie den ***Import***-Dialog im Dateimenü.
1. Wählen Sie im Import-Dialog ***Maven-Projekt*** aus.
1. Klicken Sie auf ***Weiter***.
1. Klicken Sie auf ***Durchsuchen***, um den Speicherort des Quellcodes auszuwählen.
1. Wählen Sie ***pom.xml*** aus der Liste unten aus.
1. Klicken Sie auf ***Fertigstellen***.

Die Eclipse IDE sollte das Projekt importieren und laden.
### **Unterstützung**
**Fehlerbericht**

Um einen Fehlerbericht zu senden, erstellen Sie ein neues Problem auf der [Github Projektseite](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) und wenden Sie das Label ***Bug*** an.

**Feature-Anfrage**

Wir schätzen Ihr Feedback und die von Ihnen angeforderten Funktionen sehr. Um eine neue Funktion oder Verbesserung in einem bestehenden anzufordern, erstellen Sie bitte ein neues Problem auf der [Github-Projektseite](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) und wenden Sie das Label ***enhancement*** an.

**Fragen und Hilfe**

Sie können alle Arten von Fragen zum HTML5-Spreadsheet-Editor unter Verwendung eines [Github-Problems](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) stellen. Erstellen Sie einfach ein neues Problem und wenden Sie das Label ***question*** an.

**Aspose.Cells for Java Foren**

Die Aspose-Produktforen bieten umfassende Unterstützung sowohl für Test- als auch für zahlende Kunden. Experten stehen rund um die Uhr zur Verfügung, um zu helfen und Fragen zu beantworten. Besuchen Sie [hier die Produktforen](https://forum.aspose.com/c/cells/9).

**Aspose Blogs**

Bleiben Sie mit uns in Kontakt und informieren Sie sich über die neuesten Nachrichten zu unseren Produkten und Angeboten. Abonnieren Sie [hier unseren Blog](http://blog.aspose.com).
### **Beitragen**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)


Der HTML5-Spreadsheet-Editor ist ein Open-Source-Projekt, das maximale Optionen für jedermann bietet, um zum Projekt beizutragen.

**Quellcode**

Der Quellcode des Projekts ist auf [Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java) verfügbar. Wir pflegen auch Git-Spiegel auf den folgenden Websites:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Pull-Anfragen**

Um den Quellcode zum Projekt beizutragen, senden Sie einfach eine Pull-Anfrage über Github. Lesen Sie weitere Informationen im Github-Artikel zu [Erstellen einer Pull-Anfrage](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Lizenz**
**MIT-Lizenz**

Wir verwenden eine der liberalsten Open-Source-Lizenzen mit minimalen Haftungsansprüchen an die Beitragenden. Der HTML5-Spreadsheet-Editor wird unter der [MIT-Lizenz](https://opensource.org/licenses/mit-license.php) veröffentlicht.

**Aspose Lizenz**

Das Produkt funktioniert ohne Aspose Lizenz, [mit Einschränkungen](/cells/de/java/licensing/). Um die Einschränkungen zu entfernen, können Sie eine [kostenlose temporäre Lizenz](https://purchase.aspose.com/temporary-license) erwerben oder eine [Voll Lizenz kaufen](https://purchase.aspose.com/buy).

Standardmäßig versucht der Editor, die Datei **Aspose.Total.Java.lic** aus dem Verzeichnis **src/main/resources/com/aspose/spreadsheeteditor** zu laden. Kopieren Sie die Lizenzdatei einfach in dieses Verzeichnis. Das Standardverhalten kann durch Bearbeiten der Klasse **AsposeLicense** geändert werden.
