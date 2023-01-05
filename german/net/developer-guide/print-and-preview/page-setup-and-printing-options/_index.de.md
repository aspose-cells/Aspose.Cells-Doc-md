---
title: Seiteneinrichtung und Druckoptionen
type: docs
weight: 60
url: /de/net/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

Manchmal müssen Entwickler die Seiteneinrichtung und Druckeinstellungen konfigurieren, um den Druckprozess zu steuern. Seiteneinrichtung und Druckeinstellungen bieten verschiedene Optionen und werden in Aspose.Cells vollständig unterstützt.

Dieser Artikel zeigt, wie Sie eine Konsolenanwendung in Visual Studio.Net erstellen und Seiteneinrichtungs- und Druckoptionen auf ein Arbeitsblatt mit ein paar einfachen Codezeilen anwenden, indem Sie die Aspose.Cells API verwenden.

{{% /alert %}}

## **Arbeiten mit Seiten- und Druckeinstellungen**

Für dieses Beispiel haben wir eine Arbeitsmappe in Microsoft Excel erstellt und Aspose.Cells verwendet, um die Seiteneinrichtung und Druckoptionen festzulegen.

### **Verwenden von Aspose.Cells zum Einstellen der Seiteneinrichtungsoptionen**

Erstellen Sie zunächst ein einfaches Arbeitsblatt in Microsoft Excel. Wenden Sie dann Seiteneinrichtungsoptionen darauf an. Das Ausführen des Codes ändert die Seiteneinrichtungsoptionen wie im folgenden Screenshot.

|**Ausgabedatei.**|
|:- |
|![todo: Bild_alt_Text](page-setup-and-printing-options_1.png)|

1. Erstellen Sie ein Arbeitsblatt mit einigen Daten in Microsoft Excel:
 1. Öffnen Sie eine neue Arbeitsmappe in Microsoft Excel.
 1. Fügen Sie einige Daten hinzu.
1. Seiteneinrichtungsoptionen festlegen:
 Wenden Sie Seiteneinrichtungsoptionen auf die Datei an. Unten sehen Sie einen Screenshot der Standardoptionen, bevor die neuen Optionen angewendet werden.

|**Standardoptionen für die Seiteneinrichtung.**|
|:- |
|![todo: Bild_alt_Text](page-setup-and-printing-options_2.png)|

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Download](https://downloads.aspose.com/cells/net) Aspose.Cells für .Net.
 1. Installieren Sie es auf Ihrem Entwicklungscomputer.
 Alle Aspose-Komponenten arbeiten, wenn sie installiert sind, im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in die produzierten Dokumente ein.
1. Erstellen Sie ein Projekt:
 1. Starten Sie Visual Studio. Netz.
 1. Erstellen Sie eine neue Konsolenanwendung.
 Dieses Beispiel zeigt eine C#-Konsolenanwendung, aber Sie können auch VB.NET verwenden.
1. Referenzen hinzufügen:
 1. Dieses Beispiel verwendet Aspose.Cells, also fügen Sie dem Projekt einen Verweis auf diese Komponente hinzu. Zum Beispiel:
 …\Programme\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Schreiben Sie die Anwendung, die die API aufruft:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

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

|**Eingabedokument**|
|:- |
|![todo: Bild_alt_Text](page-setup-and-printing-options_3.png)|
Das Ausführen des Codes ändert die Druckoptionen.

|**Ausgabedatei**|
|:- |
|![todo: Bild_alt_Text](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
