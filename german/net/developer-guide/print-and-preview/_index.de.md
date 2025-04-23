---
title: Arbeitsmappe drucken und Vorschau anzeigen
linktitle: Drucken und Vorschau
type: docs
weight: 70
url: /de/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells unterstützt das Drucken und die Voransicht von Excel Dateien ohne Microsoft Excel Installation.
---

{{% alert color="primary" %}}

Nachdem Sie ein Arbeitsblatt erstellt haben, möchten Sie oft eine gedruckte Kopie davon haben. Dieser Artikel erklärt, wie Sie Tabellenkalkulationen mit Aspose.Cells drucken können.

{{% /alert %}}

## **Drucken-Einführung**

Microsoft Excel geht davon aus, dass Sie den gesamten Arbeitsblattbereich drucken möchten, es sei denn, Sie geben eine Auswahl an. Um mit Aspose.Cells zu drucken, importieren Sie zuerst den Aspose.Cells.Rendering-Namespace in das Programm. Es enthält mehrere nützliche Klassen, z.B. [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) und [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **Drucken mit SheetRender**

Die [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) Klasse repräsentiert ein Arbeitsblatt und verfügt über die [**ToPrinter**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index) Methode, die ein Arbeitsblatt drucken kann. Der folgende Beispielcode zeigt, wie ein Arbeitsblatt gedruckt werden kann.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **Drucken mit WorkbookRender**

Um ein ganzes Arbeitsbuch zu drucken, durchlaufen Sie die Blätter und drucken Sie sie oder verwenden Sie die [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) Klasse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells bietet auch Überladungen für die Methoden [**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) und [**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2), sodass der Druckauftrag beim Drucken von Excel-Tabellenkalkulationen festgelegt werden kann. Standardmäßig werden alle Druckaufträge mit dem Namen "Dokument" erstellt.

{{% /alert %}}

## **Druckvorschau**

Es kann Fälle geben, in denen Excel-Dateien mit Millionen von Seiten in PDF oder Bilder konvertiert werden müssen. Solche Dateien zu verarbeiten, wird viel Zeit und Ressourcen in Anspruch nehmen. In solchen Fällen könnte die Arbeitsbuch- und Arbeitsblatt-Druckvorschau nützlich sein. Bevor solche Dateien konvertiert werden, kann der Benutzer die Gesamtzahl der Seiten überprüfen und dann entscheiden, ob die Datei konvertiert werden soll oder nicht. Dieser Artikel konzentriert sich auf die Verwendung der Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview), um die Gesamtzahl der Seiten zu ermitteln.

Aspose.Cells bietet die Druckvorschau-Funktion. Dazu stellt die API die Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) bereit. Um die Druckvorschau des gesamten Arbeitsbuchs zu erstellen, erstellen Sie eine Instanz der Klasse [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview), indem Sie [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) Objekte an den Konstruktor übergeben. Die Klasse [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) bietet eine [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount)-Methode, die die Anzahl der Seiten in der generierten Vorschau zurückgibt. Ähnlich wie bei der Klasse [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) wird die Klasse [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) verwendet, um eine Druckvorschau für ein bestimmtes Arbeitsblatt zu generieren. Erstellen Sie zum Erstellen der Druckvorschau eines Arbeitsblatts eine Instanz der Klasse [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview), indem Sie [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) Objekte an den Konstruktor übergeben. Die Klasse [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) bietet ebenfalls eine [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)-Methode, die die Anzahl der Seiten in der generierten Vorschau zurückgibt.

Der folgende Codeausschnitt zeigt die Verwendung sowohl der Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) als auch [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview), indem die [Beispiel-Excel-Datei](94896177.xlsx) verwendet wird.

### **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

Das folgende ist die Ausgabe, die durch das Ausführen des obigen Codes generiert wird.

### **Konsolenausgabe**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Erweiterte Themen**
- [Konfiguration von Schriftarten für die Darstellung von Tabellenkalkulationen](/cells/de/net/configuring-fonts-for-rendering-spreadsheets/)
- [Arbeitsblatt in Bild konvertieren - Leerraum um Daten entfernen](/cells/de/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Arbeitsblatt in Bild und Arbeitsblatt in Bild nach Seite konvertieren](/cells/de/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Arbeitsblatt in Bild mit den Optionen Bild oder Druck konvertieren](/cells/de/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren](/cells/de/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extrahieren von Bildern aus Arbeitsblättern mit ImageOrPrintOptions](/cells/de/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Generieren einer Miniaturansicht des Arbeitsblatts](/cells/de/net/generate-thumbnail-of-the-worksheet/)
- [Leeres Blatt ausgeben, wenn nichts gedruckt werden muss](/cells/de/net/output-blank-page-when-there-is-nothing-to-print/)
- [Seiteneinrichtungs- und Druckoptionen](/cells/de/net/page-setup-and-printing-options/)
- [Drucken eines Seitenbereichs mit SheetRender und WorkbookRender](/cells/de/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Sequenz von Seiten rendern mithilfe der Eigenschaften PageIndex und PageCount von ImageOrPrintOptions](/cells/de/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Arbeitsblatt in Grafikkontext rendern](/cells/de/net/render-worksheet-to-graphic-context/)
- [Individuelle oder private Schriftsätze für das Rendern von Arbeitsbüchern angeben](/cells/de/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Job- oder Dokumentnamen beim Drucken mit Aspose.Cells angeben](/cells/de/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
{{< app/cells/assistant language="csharp" >}}
