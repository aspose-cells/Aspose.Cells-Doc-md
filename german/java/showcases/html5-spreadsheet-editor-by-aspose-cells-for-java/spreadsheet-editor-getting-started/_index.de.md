---
title: Erste Schritte mit dem Tabelleneditor
type: docs
weight: 10
url: /de/java/spreadsheet-editor-getting-started/
---
**Inhaltsverzeichnis**

- [Einführung](#SpreadsheetEditorGettingStarted-Introduction)
- [System Anforderungen](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [Download und Installation](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Die Unterstützung](#SpreadsheetEditorGettingStarted-Support)
- [Beitragen](#SpreadsheetEditorGettingStarted-Contribute)
- [Lizenz](#SpreadsheetEditorGettingStarted-License)
### **Einführung**
Html5 Spreadsheet Editor ist eine Webanwendung, die Tabellenkalkulationsdokumente in einem Webbrowser anzeigen und bearbeiten kann. Es unterstützt Excel, SpreadsheetML, CVS, OpenDocument und viele andere Formate, die von Microsoft Excel unterstützt werden. Alle grundlegenden Funktionen einschließlich Zellenbearbeitung, Formatierung, Formelbearbeitung, Zeilen- und Spaltenverwaltung usw. werden unterstützt.

![todo: Bild_alt_Text](aowcrc1.png)

 Der HTML5-Tabellen-Editor verwendet viele Funktionen von[Aspose.Cells for Java](https://products.aspose.com/cells/java/)und zeigt, wie Sie sie verwenden, um eine Tabelle in Ihrer Java-Anwendung zu erstellen, zu manipulieren und zu rendern.

**Merkmale**

-  Arbeiten mit Dateien
 - Unterstützte Formate
 - Lokale Dateien öffnen
 - Von Dropbox öffnen
 - Von URL öffnen
 - Erstellen Sie eine neue Tabelle
 - Export in verschiedene Formate
-  Arbeiten mit Blättern
 - Blätter hinzufügen und entfernen
 - Blätter umbenennen
 - Wechseln Sie zwischen den Blättern
-  Arbeiten mit Zeilen und Spalten
 - Fügen Sie eine Zeile hinzu
 - Fügen Sie eine Spalte hinzu
 - Entfernen Sie eine Zeile
 - Entfernen Sie eine Spalte
 - Spaltenbreite und Zeilenhöhe
-  Arbeiten mit Cells
 - Auswählen einer Zelle
 - Bearbeiten einer Zelle
 - Formel bearbeiten
 - Cell Ausrichtung
 - Klar Cell
 - Fügen Sie eine Zelle hinzu
 - Entfernen Sie eine Zelle
-  Arbeiten mit Textformatierung
 - Fett, kursiv, unterstrichen
 - Schriftstil und -größe
 - Klare Formatierung
### **System Anforderungen**
**Software Anforderungen**

- CDI unterstützt Java Anwendungsserver
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**Hardware-Anforderungen**

Die Hardwareanforderungen variieren je nach dem Java-Anwendungsserver, den wir für die Bereitstellung des HTML5-Tabellen-Editors ausgewählt haben, und der Anzahl der Tabellen, die wir gleichzeitig öffnen. Im Folgenden finden Sie eine Schätzung, die bei der anfänglichen Einrichtung der Umgebung hilfreich sein wird.

- 2-GHz-CPU
- 2 GB Arbeitsspeicher
- 500-MB-Festplatte
### **Download und Installation**
 HTML5 Spreadsheet Editor ist eine Java EE-Anwendung und kann auf jedem Java-Anwendungsserver-Webprofil mit CDI-Unterstützung bereitgestellt werden. Es wurde mit getestet[Glasfische](https://javaee.github.io/glassfish/).

**Quellcode**

 Die Projektquelle ist verfügbar unter[GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/). Wir unterhalten auch Git-Mirrors an den folgenden Standorten:

- [Bit Bucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Code](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Verwenden Sie einen der folgenden Befehle, um den Quellcode über die Befehlszeile herunterzuladen:

**GitHub**

{{< highlight "bash" >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bit Bucket**

{{< highlight "bash" >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Code**

{{< highlight "bash" >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight "bash" >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Erstellen Sie mit Maven**

Der Projekterstellungsprozess wird mit Maven verwaltet. Sie können also eine WAR-Datei von der Befehlszeile aus ohne IDE vorbereiten. Verwenden Sie den folgenden Befehl, um eine WAR-Datei für die Bereitstellung zu generieren. Die Dokumentation des entsprechenden Anwendungsservers hilft Ihnen bei der Bereitstellung der generierten WAR-Datei und ihrer Abhängigkeiten.

{{< highlight "java" >}}

 mvn clean install

{{< /highlight >}}

**Verwenden von NetBeans**

 Es ist sehr einfach, das Projekt mit zu verwalten[NetBeans-IDE](https://netbeans.apache.org/). NetBeans ist eine der beliebtesten IDEs unter Java-Entwicklern und wird von Oracle gesponsert.

- Laden Sie den Quellcode des Projekts herunter.
- Öffnen Sie das Projekt in NetBeans IDE.
-  Klicken***Laufen*** Schaltfläche auf der Symbolleiste.
-  Auswählen***Glasfische*** Server als Anwendungsserver.

**Verwenden von Eclipse**

[Eclipse-IDE](http://www.eclipse.org/ide/) bietet die offizielle Integration zum Importieren von Maven-Projekten namens[M2Eclipse](http://www.eclipse.org/m2e/):

1. Installieren Sie M2Eclipse in Ihrer Eclipse-IDE. Der Installationsvorgang ist auf deren Website beschrieben.
1. Laden Sie den Quellcode des Projekts herunter.
1. Öffne das***Importieren*** Dialog aus dem Menü Datei.
1.  Auswählen***Maven Projekt*** aus dem Importdialog.
1.  Klicken***Nächste***.
1.  Klicken***Durchsuche*** um den Speicherort des Quellcodes auszuwählen.
1.  Auswählen***pom.xml*** aus der Liste unten.
1.  Klicken***Fertig***.

Die Eclipse-IDE sollte das Projekt importieren und laden.
### **Die Unterstützung**
**Fehlerbericht**

 Um einen Fehlerbericht zu senden, erstellen Sie ein neues Problem unter[Github-Projektseite](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) und bringen Sie das Etikett an***Insekt***.

**Featureanfrage**

 Wir wissen Ihr Feedback und die von Ihnen gewünschten Funktionen sehr zu schätzen. Um eine neue Funktion oder eine Verbesserung bestehender Funktionen anzufordern, erstellen Sie bitte ein neues Problem unter[Github-Projektseite](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) und bringen Sie das Etikett an***Erweiterung***.

**Fragen und Hilfe**

 Sie können alle Arten von Fragen im Zusammenhang mit dem HTML5-Tabellen-Editor stellen[Github-Problem](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) . Erstellen Sie einfach ein neues Problem und wenden Sie die an***Frage*** Etikett.

**Aspose.Cells for Java Foren**

 Aspose Produktforen bieten vollen Support für Test- und kostenpflichtige Kunden. Experten sind rund um die Uhr da, um Hilfe zu leisten und Fragen zu beantworten. Besuch[Produktforen hier](https://forum.aspose.com/c/cells/9).

**Aspose Blogs**

 Nehmen Sie Kontakt mit uns auf und bleiben Sie über Neuigkeiten zu unseren Produkten und Angeboten auf dem Laufenden. Etwas abonnieren[unser Blog hier](http://blog.aspose.com).
### **Beitragen**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\]](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Kalkulationstabelle_Editor_durch_Aspose.Cells_zum_Java)


Der HTML5-Tabellen-Editor ist ein Open-Source-Projekt, das jedem maximale Möglichkeiten bietet, zum Projekt beizutragen.

**Quellcode**

 Die Projektquelle ist verfügbar unter[GitHub](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). Wir unterhalten auch Git-Mirrors an den folgenden Standorten:

- [Bit Bucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Pull-Requests**

 Um Quellcode zum Projekt beizutragen, senden Sie einfach eine Pull-Anfrage über Github. Weitere Informationen finden Sie in Githubs Artikel auf[Erstellen Sie eine Pull-Anforderung](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Lizenz**
**MIT-Lizenz**

 Wir verwenden eine der liberalsten Open-Source-Lizenzen für minimale Verbindlichkeiten gegenüber Mitwirkenden. Der HTML5-Tabellen-Editor wird veröffentlicht unter[MIT-Lizenz](https://opensource.org/licenses/mit-license.php).

**Aspose Lizenz**

 Das Produkt funktioniert ohne Aspose Lizenz,[mit Einschränkungen](/cells/de/java/licensing/) . Um Beschränkungen aufzuheben, können Sie eine erwerben[kostenlose temporäre Lizenz](https://purchase.aspose.com/temporary-license) oder[Volllizenz kaufen](https://purchase.aspose.com/buy).

 Standardmäßig versucht der Editor zu laden**Aspose.Total.Java.lic** Datei aus**src/main/resources/com/aspose/spreadsheeteditor** Verzeichnis. Kopieren Sie einfach die Lizenzdatei in dieses Verzeichnis. Das Standardverhalten kann durch Bearbeiten der geändert werden**AsposeLizenz** Klasse.
