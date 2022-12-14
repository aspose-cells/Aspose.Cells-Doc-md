---
title: Arbeitsmappe drucken und in der Vorschau anzeigen
linktitle: Drucken und Vorschau
type: docs
weight: 70
url: /de/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells unterstützt das Drucken und die Vorschau von Excel-Dateien ohne Microsoft Excel-Installation.
---
{{% alert color="primary" %}}

Nachdem Sie ein Arbeitsblatt erstellt haben, möchten Sie es häufig ausdrucken. In diesem Artikel wird erläutert, wie Sie Tabellenkalkulationen mit Aspose.Cells drucken.

{{% /alert %}}

## **Einführung drucken**

Microsoft Excel geht davon aus, dass Sie den gesamten Arbeitsblattbereich drucken möchten, es sei denn, Sie geben eine Auswahl an. Um mit Aspose.Cells zu drucken, importieren Sie zuerst den Namensraum Aspose.Cells.Rendering in das Programm. Es hat mehrere nützliche Klassen, zum Beispiel[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) und[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **Drucken mit SheetRender**

 Das[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) Klasse stellt ein Arbeitsblatt dar und hat die[**ZumDrucker**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index)Methode, die ein Arbeitsblatt drucken kann. Der folgende Beispielcode zeigt, wie ein Arbeitsblatt gedruckt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **Drucken mit WorkbookRender**

 Um eine ganze Arbeitsmappe zu drucken, iterieren Sie durch die Blätter und drucken Sie sie, oder verwenden Sie die[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)Klasse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

 Aspose.Cells bietet auch Überladungen für die[**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) und[**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) Methoden, sodass es möglich ist, den Druckauftragsnamen beim Drucken von Excel-Tabellen festzulegen. Standardmäßig werden alle Druckaufträge mit dem Namen „Dokument“ erstellt.

{{% /alert %}}

## **Druckvorschau**

Es kann Fälle geben, in denen Excel-Dateien mit Millionen von Seiten in PDF oder Bilder konvertiert werden müssen. Die Verarbeitung solcher Dateien nimmt viel Zeit und Ressourcen in Anspruch. In solchen Fällen kann sich die Funktion Arbeitsmappen- und Arbeitsblatt-Druckvorschau als nützlich erweisen. Vor der Konvertierung solcher Dateien kann der Benutzer die Gesamtseitenzahl überprüfen und dann entscheiden, ob die Datei konvertiert werden soll oder nicht. Dieser Artikel konzentriert sich auf die Verwendung von[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)und[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)Klassen, um die Gesamtzahl der Seiten zu ermitteln.

 Aspose.Cells bietet die Druckvorschaufunktion. Dafür sorgt die API[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) und[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) Klassen. Um die Druckvorschau der gesamten Arbeitsmappe zu erstellen, erstellen Sie eine Instanz der[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) Klasse durch Bestehen[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) und[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) Objekte an den Konstruktor. Das[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) Klasse bietet eine[**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) -Methode, die die Anzahl der Seiten in der generierten Vorschau zurückgibt. Ähnlich zu[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)Klasse, die[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)Klasse wird verwendet, um eine Druckvorschau für ein bestimmtes Arbeitsblatt zu generieren. Um die Druckvorschau eines Arbeitsblatts zu erstellen, erstellen Sie eine Instanz der[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)Klasse durch Bestehen[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)und[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)Objekte an den Konstruktor. Das[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)Klasse bietet auch eine[**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)-Methode, die die Anzahl der Seiten in der generierten Vorschau zurückgibt.

Das folgende Code-Snippet demonstriert die Verwendung beider[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)und[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) Klassen mit der[Excel-Beispieldatei](94896177.xlsx).

### **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

Das Folgende ist die Ausgabe, die durch Ausführen des obigen Codes generiert wird.

### **Konsolenausgabe**

Seitenanzahl der Arbeitsmappe: 1
Seitenanzahl des Arbeitsblatts: 1


## **Themen vorantreiben**
- [Konfigurieren von Schriftarten zum Rendern von Tabellenkalkulationen](/cells/de/net/configuring-fonts-for-rendering-spreadsheets/)
- [Arbeitsblatt in Bild konvertieren - Entfernen Sie Leerzeichen um Daten](/cells/de/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Konvertieren von Arbeitsblatt in Bild und Arbeitsblatt in Bild für Seite](/cells/de/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Konvertieren des Arbeitsblatts in ein Bild mit ImageOrPrint-Optionen](/cells/de/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Exportieren Sie den Bereich von Cells in einem Arbeitsblatt in ein Bild](/cells/de/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extrahieren Sie Bilder aus Arbeitsblättern mit ImageOrPrintOptions](/cells/de/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Generieren Sie eine Miniaturansicht des Arbeitsblatts](/cells/de/net/generate-thumbnail-of-the-worksheet/)
- [Leere Seite ausgeben, wenn nichts zu drucken ist](/cells/de/net/output-blank-page-when-there-is-nothing-to-print/)
- [Seiteneinrichtung und Druckoptionen](/cells/de/net/page-setup-and-printing-options/)
- [Drucken des Seitenbereichs mit SheetRender und WorkbookRender](/cells/de/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Rendern Sie eine Seitenfolge mithilfe der PageIndex- und PageCount-Eigenschaften von ImageOrPrintOptions](/cells/de/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Rendern Sie das Arbeitsblatt in den grafischen Kontext](/cells/de/net/render-worksheet-to-graphic-context/)
- [Geben Sie einen individuellen oder privaten Satz von Schriftarten für das Rendern von Arbeitsmappen an](/cells/de/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Geben Sie den Auftrags- oder Dokumentnamen beim Drucken mit Aspose.Cells an](/cells/de/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
