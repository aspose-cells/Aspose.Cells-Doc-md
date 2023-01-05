---
title: Seiteneinrichtung und Druckoptionen
type: docs
weight: 10
url: /de/java/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

Manchmal müssen Entwickler die Seiteneinrichtung und Druckeinstellungen konfigurieren, um den Druckprozess zu steuern. Seiteneinrichtung und Druckeinstellungen bieten verschiedene Optionen und werden in Aspose.Cells vollständig unterstützt.

Dieser Artikel zeigt, wie Sie eine Konsolenanwendung erstellen und Seiteneinrichtungs- und Druckoptionen auf ein Arbeitsblatt mit ein paar einfachen Codezeilen anwenden, indem Sie die Aspose.Cells API verwenden.

{{% /alert %}}

## **Arbeiten mit Seiten- und Druckeinstellungen**

Für dieses Beispiel haben wir eine Arbeitsmappe in Microsoft Excel erstellt und Aspose.Cells verwendet, um die Seiteneinrichtung und Druckoptionen festzulegen.

### **Festlegen von Seiteneinrichtungsoptionen**

Erstellen Sie zunächst ein einfaches Arbeitsblatt in Microsoft Excel. Wenden Sie dann Seiteneinrichtungsoptionen darauf an. Das Ausführen des Codes ändert die Seiteneinrichtungsoptionen wie im folgenden Screenshot.

**Ausgabedatei** 

![todo: Bild_alt_Text](page-setup-and-printing-options_1.png)

1. Erstellen Sie ein Arbeitsblatt mit einigen Daten in Microsoft Excel:
 1. Öffnen Sie eine neue Arbeitsmappe in Microsoft Excel.
 1. Fügen Sie einige Daten hinzu.
 Unten ist ein Screenshot der Datei.

      **Eingabedatei**

![todo: Bild_alt_Text](page-setup-and-printing-options_2.png)

1. Seiteneinrichtungsoptionen festlegen:
 Wenden Sie Seiteneinrichtungsoptionen auf die Datei an. Unten sehen Sie einen Screenshot der Standardoptionen, bevor die neuen Optionen angewendet werden.

   **Standardoptionen für die Seiteneinrichtung**

![todo: Bild_alt_Text](page-setup-and-printing-options_3.png)

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Download](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
 1. Entpacken Sie es auf Ihrem Entwicklungscomputer.
 Alles[Aspose](http://www.aspose.com/) Komponenten arbeiten, wenn sie installiert sind, im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in die produzierten Dokumente ein.
1. Erstellen Sie ein Projekt.
Erstellen Sie entweder ein Projekt mit einem Java-Editor, z. B. Eclipse, oder erstellen Sie ein einfaches Programm mit einem Texteditor.
1. Fügen Sie einen Klassenpfad hinzu.
1. Extrahieren Sie Aspose.Cells.jar und dom4j_1.6.1.jar aus Aspose.Cells.zip.
 1. Legen Sie den Klassenpfad des Projekts in Eclipse fest:
 1. Wählen Sie Ihr Projekt in Eclipse aus und klicken Sie dann auf**Projekt** gefolgt von**Eigenschaften**.
 1. Wählen**Java Erstellungspfad** links neben dem Dialog.
 1. Wählen Sie die Registerkarte Bibliotheken, klicken Sie auf**JARs hinzufügen** oder**Fügen Sie externe JARs hinzu** um Aspose.Cells.jar und dom4j_1.6.1.jar auszuwählen und sie den Erstellungspfaden hinzuzufügen.
 Oder Sie können es zur Laufzeit an einer DOS-Eingabeaufforderung in Windows festlegen:

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. Schreiben Sie die Anwendung, die APIs aufruft:
 Unten ist der Code, der von der Komponente in diesem Beispiel verwendet wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **Druckoptionen einstellen**

Die Seiteneinrichtungseinstellungen bieten auch mehrere Druckoptionen (auch als Blattoptionen bezeichnet), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden. Sie ermöglichen Benutzern Folgendes:

- Wählen Sie einen bestimmten Druckbereich eines Arbeitsblatts aus.
- Titel drucken.
- Rasterlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Erzielen Sie Entwurfsqualität.
- Kommentare drucken.
- Zellfehler drucken.
- Definieren Sie die Seitenreihenfolge.

Im folgenden Beispiel werden Druckoptionen auf die im obigen Beispiel erstellte Datei (PageSetup.xls) angewendet. Der folgende Screenshot zeigt die Standarddruckoptionen, bevor neue Optionen angewendet werden.
**Eingabedokument**

![todo: Bild_alt_Text](page-setup-and-printing-options_4.png)

Das Ausführen des Codes ändert die Druckoptionen.
**Ausgabedatei**

![todo: Bild_alt_Text](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **Zusammenfassung**

{{% alert color="primary" %}}

Dieser Artikel zeigt, wie Sie die Optionen für die Seiteneinrichtung und den Blattdruck mit Aspose.Cells festlegen. Hoffentlich gibt er Ihnen einen Einblick, und Sie können diese Optionen in Ihren eigenen Szenarien verwenden.

 Aspose.Cells profitiert von jahrelanger Forschung, Design und sorgfältiger Abstimmung. Wir freuen uns sehr über Ihre Fragen, Kommentare und Anregungen unter[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Wir garantieren eine zeitnahe Antwort.

{{% /alert %}}
