---
title: Druckvorschau von Arbeitsmappe und Arbeitsblatt
type: docs
weight: 130
url: /de/java/workbook-and-worksheet-print-preview/
---

## **Anwendungsszenario**

Es kann Fälle geben, in denen Excel-Dateien mit Millionen von Seiten in PDF oder Bilder konvertiert werden müssen. Die Verarbeitung solcher Dateien verbraucht viel Zeit und Ressourcen. In solchen Fällen könnte sich die Funktion zur Druckvorschau für Arbeitsmappen und Arbeitsblätter als nützlich erweisen. Bevor solche Dateien konvertiert werden, kann der Benutzer die Gesamtanzahl der Seiten überprüfen und dann entscheiden, ob die Datei konvertiert werden soll oder nicht. Dieser Artikel konzentriert sich darauf, die Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) zu verwenden, um die Gesamtanzahl der Seiten herauszufinden.

## **Arbeitsmappe- und Arbeitsblatt-Druckvorschau**

Aspose.Cells bietet die Druckvorschau-Funktion. Hierfür stellt die API die Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) bereit. Um die Druckvorschau der gesamten Arbeitsmappe zu erstellen, erstellen Sie eine Instanz der Klasse [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview), indem Sie [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) Objekte an den Konstruktor übergeben. Die Klasse [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) bietet eine Methode [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount), die die Anzahl der Seiten in der generierten Vorschau zurückgibt. Ähnlich wie bei der Klasse [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) wird auch die Klasse [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) verwendet, um eine Druckvorschau für ein bestimmtes Arbeitsblatt zu generieren. Um die Druckvorschau eines Arbeitsblatts zu erstellen, erstellen Sie eine Instanz der Klasse [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview), indem Sie [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) Objekte an den Konstruktor übergeben. Die Klasse [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) bietet ebenfalls eine Methode [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount), die die Anzahl der Seiten in der generierten Vorschau zurückgibt.

Der folgende Code-Ausschnitt zeigt die Verwendung der Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview), indem die [Beispieldatei](Book1.xlsx) verwendet wird.

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

Das folgende ist die Ausgabe, die durch das Ausführen des obigen Codes generiert wird.

### **Konsolenausgabe**

{{< highlight java >}}

Workbook page count: 1</br>
Worksheet page count: 1

{{< /highlight >}}
