---  
title: Vorschau des Arbeitsbuchs mit Node.js über C++  
linktitle: Arbeitsbuchvorschau 
type: docs  
weight: 70  
url: /de/nodejs-cpp/workbook-and-worksheet-preview/  
description: Aspose.Cells unterstützt das Drucken und die Vorschau von Excel Dateien ohne Microsoft Excel Installation mit Node.js über C++.  
---  

## **Druckvorschau**  

In manchen Fällen müssen Excel-Dateien mit Millionen von Seiten in PDFs oder Bilder umgewandelt werden. Die Verarbeitung solcher Dateien kann viel Zeit und Ressourcen in Anspruch nehmen. In solchen Fällen kann die Funktion „Arbeitsbuch- und Arbeitsblatt-Druckvorschau“ nützlich sein. Vor der Konvertierung können Nutzer die Gesamtzahl der Seiten überprüfen und entscheiden, ob die Datei konvertiert werden soll oder nicht. Dieser Artikel konzentriert sich auf die Verwendung der Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/), um die Gesamtzahl der Seiten zu ermitteln.  

Aspose.Cells bietet die Funktion der Druckvorschau. Für diese Funktion stellt die API die Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) bereit. Um die Druckvorschau des gesamten Arbeitsbuchs zu erstellen, erstellen Sie eine Instanz der [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)-Klasse durch Übergabe der Objekte [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) an den Konstruktor. Die [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)-Klasse bietet eine Methode [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--), die die Anzahl der Seiten in der generierten Vorschau zurückgibt. Ähnlich wie die [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)-Klasse wird die [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)-Klasse verwendet, um eine Druckvorschau für ein bestimmtes Arbeitsblatt zu erstellen. Um die Vorschau eines Arbeitsblatts zu erstellen, erstellen Sie eine Instanz der [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)-Klasse durch Übergabe der Objekte [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) an den Konstruktor. Die [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)-Klasse bietet ebenfalls eine [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--)-Methode, die die Anzahl der Seiten in der generierten Vorschau zurückgibt.  

Das folgende Codebeispiel demonstriert die Verwendung der Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) anhand einer [Beispieldatei](94896177.xlsx).  

### **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const filePath = path.join(sourceDir, "Book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const imgOptions = new AsposeCells.ImageOrPrintOptions();
const preview = new AsposeCells.WorkbookPrintingPreview(workbook, imgOptions);
console.log("Workbook page count: " + preview.getEvaluatedPageCount());

const preview2 = new AsposeCells.SheetPrintingPreview(workbook.getWorksheets().get(0), imgOptions);
console.log("Worksheet page count: " + preview2.getEvaluatedPageCount());
```  

Das folgende ist die Ausgabe, die durch das Ausführen des obigen Codes generiert wird.  

### **Konsolenausgabe**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Erweiterte Themen**  
- [Konfiguration von Schriftarten für die Darstellung von Tabellenkalkulationen](/cells/de/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Arbeitsblatt in Bild konvertieren - Leerraum um Daten entfernen](/cells/de/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Arbeitsblatt in Bild und Arbeitsblatt in Bild nach Seite konvertieren](/cells/de/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Arbeitsblatt in Bild mit den Optionen Bild oder Druck konvertieren](/cells/de/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren](/cells/de/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Extrahieren von Bildern aus Arbeitsblättern mit ImageOrPrintOptions](/cells/de/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Generieren einer Miniaturansicht des Arbeitsblatts](/cells/de/nodejs-cpp/generate-thumbnail-of-the-worksheet/)  
- [Leeres Blatt ausgeben, wenn nichts gedruckt werden muss](/cells/de/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Seiteneinrichtungs- und Druckoptionen](/cells/de/nodejs-cpp/page-setup-and-printing-options/)  
- [Sequenz von Seiten rendern mithilfe der Eigenschaften PageIndex und PageCount von ImageOrPrintOptions](/cells/de/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Arbeitsblatt in Grafikkontext rendern](/cells/de/nodejs-cpp/render-worksheet-to-graphic-context/)  
- [Individuelle oder private Schriftsätze für das Rendern von Arbeitsbüchern angeben](/cells/de/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)   

{{< app/cells/assistant language="nodejs-cpp" >}}
