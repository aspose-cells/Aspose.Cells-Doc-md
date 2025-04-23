---
title: Arbeitsmappe drucken und Vorschau anzeigen
linktitle: Drucken und Vorschau
type: docs
weight: 70
url: /de/python-net/workbook-and-worksheet-print-preview/
description: Aspose.Cells für Python via .NET unterstützt das Drucken und die Vorschau von Excel Dateien ohne Microsoft Excel Installation.
---

{{% alert color="primary" %}}

Nach dem Erstellen eines Arbeitsblatts möchten Sie oft eine gedruckte Kopie davon. Dieser Artikel erklärt, wie man mit Aspose.Cells für Python via .NET Tabellenkalkulationen druckt.

{{% /alert %}}

## **Drucken-Einführung**

Microsoft Excel geht davon aus, dass Sie den gesamten Arbeitsblattbereich drucken möchten, es sei denn, Sie geben eine Auswahl an. Um mit Aspose.Cells für Python via .NET zu drucken, importieren Sie zuerst den Namespace aspose.cells.rendering in das Programm. Er verfügt über mehrere nützliche Klassen, zum Beispiel [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) und [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender).

### **Drucken mit SheetRender**

Die [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) Klasse repräsentiert ein Arbeitsblatt und verfügt über die [**to_printer**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/) Methode, die ein Arbeitsblatt drucken kann. Der folgende Beispielcode zeigt, wie ein Arbeitsblatt gedruckt werden kann.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingExcelWorkbookUsingSheetRender.py" >}}

### **Drucken mit WorkbookRender**

Um ein ganzes Arbeitsbuch zu drucken, durchlaufen Sie die Blätter und drucken Sie sie oder verwenden Sie die [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) Klasse.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingUsingWorkbookRender-1.py" >}}

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET bietet auch Überladungen für die Methoden [**WorkbookRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#str-str) und [**SheetRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#aspose.pydrawing.printing.PrinterSettings), sodass der Name des Druckauftrags beim Drucken von Excel-Tabellen festgelegt werden kann. Standardmäßig werden alle Druckaufträge mit dem Namen "Dokument" erstellt.

{{% /alert %}}

## **Druckvorschau**

Es kann Fälle geben, in denen Excel-Dateien mit Millionen von Seiten in PDF oder Bilder konvertiert werden müssen. Solche Dateien zu verarbeiten, wird viel Zeit und Ressourcen in Anspruch nehmen. In solchen Fällen könnte die Arbeitsbuch- und Arbeitsblatt-Druckvorschau nützlich sein. Bevor solche Dateien konvertiert werden, kann der Benutzer die Gesamtzahl der Seiten überprüfen und dann entscheiden, ob die Datei konvertiert werden soll oder nicht. Dieser Artikel konzentriert sich auf die Verwendung der Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview), um die Gesamtzahl der Seiten zu ermitteln.

Aspose.Cells für Python via .NET bietet die Druckvorschau-Funktion. Dafür stellt die API die Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) bereit. Um die Druckvorschau des gesamten Arbeitsbuchs zu erstellen, erstellen Sie eine Instanz der [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview)-Klasse, indem Sie [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) Objekte an den Konstruktor übergeben. Die Klasse [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) bietet eine Methode [**evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview/evaluated_page_count/), die die Anzahl der Seiten in der generierten Vorschau zurückgibt. Ähnlich wie die Klasse [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) wird die Klasse [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) verwendet, um eine Druckvorschau für ein bestimmtes Arbeitsblatt zu erstellen. Um eine Druckvorschau eines Arbeitsblatts zu erstellen, erstellen Sie eine Instanz der [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview)-Klasse, indem Sie [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) Objekte an den Konstruktor übergeben. Die Klasse [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) bietet ebenfalls eine Methode [**SheetPrintingPreview.evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview/evaluated_page_count/), die die Anzahl der Seiten in der generierten Vorschau zurückgibt.

Der folgende Codeausschnitt zeigt die Verwendung sowohl der Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) als auch [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview), indem die [Beispiel-Excel-Datei](94896177.xlsx) verwendet wird.

### **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintPreview-1.py" >}}

Das folgende ist die Ausgabe, die durch das Ausführen des obigen Codes generiert wird.

### **Konsolenausgabe**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

