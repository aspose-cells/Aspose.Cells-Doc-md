---
title: Seiteneinrichtung und Druckoptionen
type: docs
weight: 60
url: /de/net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

Manchmal müssen Entwickler die Seiteneinrichtung und die Druckeinstellungen konfigurieren, um den Druckprozess zu steuern. Die Seiteneinrichtung und Druckeinstellungen bieten verschiedene Optionen und werden von Aspose.Cells vollständig unterstützt.

Dieser Artikel zeigt, wie Sie mit wenigen einfachen Zeilen Code unter Verwendung der Aspose.Cells-API eine Konsolenanwendung in Visual Studio .Net erstellen und Seite einrichten sowie Druckoptionen auf ein Arbeitsblatt anwenden.

{{% /alert %}}

## **Arbeiten mit Seiten- und Druckeinstellungen**

Für dieses Beispiel haben wir eine Arbeitsmappe in Microsoft Excel erstellt und Aspose.Cells verwendet, um die Seiteneinrichtung und Druckoptionen festzulegen.

### **Verwenden von Aspose.Cells zum Festlegen von Seiteneinrichtungsoptionen**

Erstellen Sie zuerst ein einfaches Arbeitsblatt in Microsoft Excel. Wenden Sie dann Seiteneinrichtungsoptionen darauf an. Das Ausführen des Codes ändert die Seiteneinrichtungsoptionen, wie im Screenshot unten dargestellt.

|**Ausgabedatei.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Erstellen Sie ein Arbeitsblatt mit einigen Daten in Microsoft Excel:
   1. Öffnen Sie eine neue Arbeitsmappe in Microsoft Excel.
   1. Fügen Sie einige Daten hinzu.
1. Legen Sie Seiteneinrichtungsoptionen fest:
   Wenden Sie die Seiteneinrichtungsoptionen auf die Datei an. Unten ist ein Screenshot der Standardoptionen vor der Anwendung der neuen Optionen zu sehen.

|**Standardseiteneinrichtungsoptionen.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Download](https://downloads.aspose.com/cells/net) Aspose.Cells für .Net.
   1. Installieren Sie es auf Ihrem Entwicklungscomputer.
      Alle Aspose-Komponenten arbeiten im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.
1. Ein Projekt erstellen:
   1. Starten Sie Visual Studio. Net.
   1. Erstellen Sie eine neue Konsolenanwendung.
      Dieses Beispiel zeigt eine C#-Konsolenanwendung, aber Sie können auch VB.NET verwenden.
1. Fügen Sie Verweise hinzu:
   1. Dieses Beispiel verwendet Aspose.Cells, fügen Sie daher einen Verweis auf diese Komponente im Projekt hinzu. Zum Beispiel:
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Schreiben Sie die Anwendung, die die API aufruft:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **Druckoptionen festlegen**

Die Seiteneinrichtungseinstellungen bieten auch mehrere Druckoptionen (auch Blattoptionen genannt), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden. Sie ermöglichen Benutzern:

- Eine bestimmte Druckbereich eines Arbeitsblatts auswählen.
- Titel drucken.
- Gitternetzlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Entwurfsqualität erreichen.
- Kommentare drucken.
- Zellenfehler drucken.
- Seiteneinteilung definieren.

Das folgende Beispiel wendet Druckoptionen auf die Datei an, die im obigen Beispiel erstellt wurde (PageSetup.xls). Der nachfolgende Screenshot zeigt die Standard-Druckoptionen, bevor neue Optionen angewendet werden.

|**Eingabedokument**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
Das Ausführen des Codes ändert die Druckoptionen.

|**Ausgabedatei**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
