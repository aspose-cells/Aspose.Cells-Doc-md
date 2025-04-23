---  
title: Gráfico a PDF con Node.js vía C++  
linktitle: Gráfico a PDF  
description: Aprende cómo usar Aspose.Cells for Node.js via C++ para convertir un gráfico en un documento PDF. Nuestra guía demostrará cómo exportar un gráfico desde Microsoft Excel y guardarlo como PDF para su distribución y archivo.  
keywords: Aspose.Cells for Node.js via C++, Gráfico a PDF, Microsoft Excel, Conversión a PDF, Exportar, Distribución, Archivado.  
type: docs  
weight: 47  
url: /es/nodejs-cpp/chart-to-pdf/  
---  

## **Renderizando gráfico a PDF**

Para renderizar el gráfico en formato PDF, las APIs de Aspose.Cells han expuesto el método [**Chart.toPdf(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toPdf-string-) con la capacidad de almacenar el PDF resultante en la ruta del disco o en un Stream.

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

## **Crear PDF de gráfico con tamaño de página deseado**  
Puedes crear un PDF de gráfico con el tamaño de página deseado usando Aspose.Cells y especificar cómo deseas alinear el gráfico dentro de la página, como arriba, abajo, centro, izquierda, derecha, etc. Además, el gráfico de salida puede crearse en un stream o en disco. Consulta el siguiente ejemplo de código que carga el [archivo Excel de ejemplo](64716906.xlsx), accede al primer gráfico dentro de la hoja de cálculo y lo convierte en [PDF de salida](64716907.pdf) con el tamaño de página deseado. La siguiente captura de pantalla muestra que el tamaño de página en el PDF de salida es 7x7 como se especifica en el código y el gráfico está alineado en el centro tanto horizontal como verticalmente.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **Código de muestra**  
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


