---  
title: Chart to PDF with Node.js via C++  
linktitle: Chart to PDF  
description: Learn how to use Aspose.Cells for Node.js via C++ to convert a chart to a PDF document. Our guide will demonstrate how to export a chart from Microsoft Excel and save it as a PDF for further distribution and archiving.  
keywords: Aspose.Cells for Node.js via C++, Chart to PDF, Microsoft Excel, PDF Conversion, Export, Distribution, Archiving.  
type: docs  
weight: 47  
url: /nodejs-cpp/chart-to-pdf/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Rendering Chart to PDF**

In order to render the chart to PDF format, the Aspose.Cells APIs have exposed the [**Chart.toPdf(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toPdf-string-) method with the ability to store the resultant PDF on disk path or Stream.

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

## **Create Chart PDF with Desired Page Size**  
You can create chart Pdf with your desired page size using Aspose.Cells and specify how you want to align the chart inside the page as top, bottom, center, left, right etc. Besides, the output chart can be created in stream or on disk. Please see the following sample code that loads the [sample Excel file](64716906.xlsx), accesses the first chart inside the worksheet and then converts it into [output Pdf](64716907.pdf) with desired page size. The following screenshot shows that the page size in the output Pdf is 7x7 as specified inside the code and chart is center aligned both horizontally as well as vertically.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **Sample Code**  
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
