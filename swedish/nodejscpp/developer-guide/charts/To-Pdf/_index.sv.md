---  
title: Diagram till PDF med Node.js via C++  
linktitle: Diagram till PDF  
description: Lär dig att använda Aspose.Cells for Node.js via C++ för att konvertera ett diagram till ett PDF dokument. Vår guide visar hur man exporterar ett diagram från Microsoft Excel och sparar det som en PDF för vidare distribution och arkivering.  
keywords: Aspose.Cells for Node.js via C++, Diagram till PDF, Microsoft Excel, PDF konvertering, Export, Distribution, Arkivering.  
type: docs  
weight: 47  
url: /sv/nodejs-cpp/chart-to-pdf/  
---  

## **Rendera diagram till PDF**

För att rendera diagrammet till PDF-format har Aspose.Cells API-exponerat [**Chart.toPdf(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toPdf-string-) metoden med möjlighet att lagra den resulterande PDF-filen på diskväg eller Stream.

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

## **Skapa diagram-PDF med önskad sidstorlek**  
Du kan skapa diagram-Pdf med önskad sidstorlek med Aspose.Cells och specificera hur du vill justera diagrammet inuti sidan som topp, botten, centrum, vänster, höger etc. Dessutom kan utgångsdiagrammet skapas i stream eller på disk. Se följande exempel som laddar [exempel Excel-fil](64716906.xlsx), får tillgång till det första diagrammet i kalkbladet och konverterar det till [utdata Pdf](64716907.pdf) med önskad sidstorlek. Följande skärmbild visar att sidstorleken i den utgående Pdf är 7x7 som angivits i koden och diagrammet är centrerat både horisontellt och vertikalt.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **Exempelkod**  
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
