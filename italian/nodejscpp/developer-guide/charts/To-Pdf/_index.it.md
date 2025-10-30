---  
title: Convertire grafico in PDF con Node.js via C++  
linktitle: Grafico in PDF  
description: Impara come usare Aspose.Cells for Node.js via C++ per convertire un grafico in un documento PDF. La nostra guida dimostrerà come esportare un grafico da Microsoft Excel e salvarlo come PDF per ulteriore distribuzione e archiviazione.  
keywords: Aspose.Cells for Node.js via C++, Grafico in PDF, Microsoft Excel, Conversione PDF, Esportazione, Distribuzione, Archiviazione.  
type: docs  
weight: 47  
url: /it/nodejs-cpp/chart-to-pdf/  
---  

## **Rendering del grafico in PDF**

Per rendere il grafico in formato PDF, le API Aspose.Cells hanno esposto il metodo [**Chart.toPdf(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toPdf-string-) con la capacità di memorizzare il PDF risultante su percorso disk o Stream.

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

## **Crea Grafico PDF con Dimensione Pagina Desiderata**  
Puoi creare il PDF del grafico con le dimensioni di pagina desiderate usando Aspose.Cells e specificare come vuoi allineare il grafico all’interno della pagina come in alto, in basso, al centro, a sinistra, a destra ecc. Inoltre, il grafico di output può essere creato in stream o su disco. Consulta il seguente esempio di codice che carica il [file Excel di esempio](64716906.xlsx), accede al primo grafico all’interno del foglio di lavoro e poi lo converte in [PDF di output](64716907.pdf) con le dimensioni di pagina desiderate. Lo screenshot seguente mostra che la dimensione della pagina nel PDF di output è 7x7 come specificato nel codice e il grafico è allineato al centro sia orizzontalmente che verticalmente.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **Codice di Esempio**  
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
