---  
title: Diagramm nach PDF mit Node.js über C++  
linktitle: Diagramm in PDF umwandeln  
description: Lernen Sie, wie Sie mit Aspose.Cells for Node.js via C++ ein Diagramm in ein PDF Dokument konvertieren. Unser Leitfaden zeigt, wie man ein Diagramm aus Microsoft Excel exportiert und als PDF speichert für weitere Verteilung und Archivierung.  
keywords: Aspose.Cells for Node.js via C++, Diagramm zu PDF, Microsoft Excel, PDF Konvertierung, Export, Verteilung, Archivierung.  
type: docs  
weight: 47  
url: /de/nodejs-cpp/chart-to-pdf/  
---  

## **Diagramm in PDF umwandeln**

Um das Diagramm im PDF-Format darzustellen, haben die Aspose.Cells APIs die [**Chart.toPdf(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toPdf-string-)-Methode mit der Fähigkeit bereitgestellt, das resultierende PDF auf Disk oder Stream zu speichern.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Converting chart to PDF
chart.toPdf(path.join(dataDir, "chartPDF_out.pdf"));
```

## **Erstellen Sie ein Diagramm-PDF mit gewünschter Seitengröße**  
Sie können Diagramm-PDFs mit Ihrer gewünschten Seitengröße erstellen, indem Sie Aspose.Cells verwenden, und festlegen, wie Sie das Diagramm innerhalb der Seite ausrichten möchten, z. B. oben, unten, zentriert, links, rechts usw. Außerdem kann das Ausgabe-Diagramm im Stream oder auf Festplatte erstellt werden. Im Folgenden finden Sie einen Beispielcode, der die [Beispieldatei Excel](64716906.xlsx) lädt, auf das erste Diagramm im Arbeitsblatt zugreift und es dann in ein [Ausgabe-PDF](64716907.pdf) mit gewünschter Seitengröße konvertiert. Das folgende Bildschirmfoto zeigt, dass die Seitengröße im Ausgabe-PDF 7x7 ist, wie im Code angegeben, und das Diagramm sowohl horizontal als auch vertikal zentriert ausgerichtet ist.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **Beispielcode**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing the chart.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateChartPDFWithDesiredPageSize.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet.
const chart = worksheet.getCharts().get(0);

// Create chart pdf with desired page size.
chart.toPdf(path.join(outputDir, "outputCreateChartPDFWithDesiredPageSize.pdf"), 7, 7, AsposeCells.PageLayoutAlignmentType.Center, AsposeCells.PageLayoutAlignmentType.Center);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
