---  
title: Gestionar las etiquetas de datos (DataLabels) de gráficos de Excel con Node.js via C++  
description: Aprende cómo gestionar de manera efectiva las etiquetas de datos en los gráficos de Excel usando Aspose.Cells for Node.js via C++. Esta guía completa cubre diversas tareas de gestión, incluyendo añadir, eliminar y modificar etiquetas para mejorar la legibilidad y usabilidad del gráfico.  
keywords: Aspose.Cells para Node.js, gráficos de Excel, etiquetas de datos, gestión, legibilidad, usabilidad, añadir, eliminar, modificar.  
linktitle: Etiquetas de datos  
type: docs  
weight: 50  
url: /es/nodejs-cpp/insert-datalabels-to-chart/  
---  

{{% alert color="primary" %}}  

Las etiquetas de datos son una parte importante de un gráfico.  
Podemos conocer fácilmente el valor, el porcentaje, etc. de cada serie  

{{% /alert %}}  

## **Opciones de etiquetas de datos**  
Aspose.Cells for Node.js via C++ también permite gestionar las etiquetas de datos del gráfico en tiempo de ejecución, con el objeto [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/), es sencillo mover, actualizar y formatear las etiquetas de datos del gráfico.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Administrar las etiquetas de datos del gráfico**  
Es simple gestionar las etiquetas de datos del gráfico con Aspose.Cells [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/).  

El siguiente fragmento de código demuestra cómo gestionar DataLabels.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Show value labels
chart.getNSeries().get(0).getDataLabels().setShowValue(true);
// Show series name labels
chart.getNSeries().get(1).getDataLabels().setShowSeriesName(true);
// Move labels to center
chart.getNSeries().get(1).getDataLabels().setPosition(AsposeCells.LabelPositionType.Center);

// Save the file
workbook.save("chart_datalabels.xlsx");
```  

## **Temas avanzados**  
- [Agregar etiquetas personalizadas a los puntos de datos en la serie del gráfico](/cells/es/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Deshabilitar el ajuste de texto para las etiquetas de datos del gráfico](/cells/es/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Redimensionar la forma de la etiqueta de datos del gráfico para que se ajuste al texto](/cells/es/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Etiqueta de datos personalizada de texto enriquecido del punto del gráfico](/cells/es/nodejs-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Establecer el tipo de forma de las etiquetas de datos del gráfico](/cells/es/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Mostrar el rango de celdas como las etiquetas de datos](/cells/es/nodejs-cpp/showing-cell-range-as-the-data-labels/)  

