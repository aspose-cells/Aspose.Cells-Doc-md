---
title: Arbeitsmappe und Arbeitsblatt-Druckvorschau
type: docs
weight: 130
url: /de/java/workbook-and-worksheet-print-preview/
---
## **Nutzungsszenario**

Es kann Fälle geben, in denen Excel-Dateien mit Millionen von Seiten in PDF oder Bilder konvertiert werden müssen. Die Verarbeitung solcher Dateien nimmt viel Zeit und Ressourcen in Anspruch. In solchen Fällen kann sich die Funktion Arbeitsmappen- und Arbeitsblatt-Druckvorschau als nützlich erweisen. Vor der Konvertierung solcher Dateien kann der Benutzer die Gesamtseitenzahl überprüfen und dann entscheiden, ob die Datei konvertiert werden soll oder nicht. Dieser Artikel konzentriert sich auf die Verwendung von[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)und[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)Klassen, um die Gesamtzahl der Seiten zu ermitteln.

## **Arbeitsmappe und Arbeitsblatt-Druckvorschau**

Aspose.Cells bietet die Druckvorschaufunktion. Dafür sorgt die API[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)und[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)Klassen. Um die Druckvorschau der gesamten Arbeitsmappe zu erstellen, erstellen Sie eine Instanz der[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)Klasse durch Bestehen[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)und[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)Objekte an den Konstruktor. Das[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)Klasse bietet eine[**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount)-Methode, die die Anzahl der Seiten in der generierten Vorschau zurückgibt. Ähnlich zu[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)Klasse, die[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)Klasse wird verwendet, um eine Druckvorschau für ein bestimmtes Arbeitsblatt zu generieren. Um die Druckvorschau eines Arbeitsblatts zu erstellen, erstellen Sie eine Instanz der[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)Klasse durch Bestehen[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)und[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)Objekte an den Konstruktor. Das[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)Klasse bietet auch eine[**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount)-Methode, die die Anzahl der Seiten in der generierten Vorschau zurückgibt.

Das folgende Code-Snippet demonstriert die Verwendung beider[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)und[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)Klassen mit der[Excel-Beispieldatei](Book1.xlsx).

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

Das Folgende ist die Ausgabe, die durch Ausführen des obigen Codes generiert wird.

### **Konsolenausgabe**

Seitenanzahl der Arbeitsmappe: 1</br>
Seitenanzahl des Arbeitsblatts: 1
