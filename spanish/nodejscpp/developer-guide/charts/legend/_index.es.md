---
title: Gestiona la leyenda de gráficos de Excel con Node.js a través de C++
description: Aprende cómo utilizar Aspose.Cells for Node.js via C++ para aprovechar y personalizar eficazmente las leyendas de gráficos en Microsoft Excel. Nuestra guía completa explica la funcionalidad de la leyenda, cómo acceder y modificarla, así como cómo mejorar la visualización y comprensión de datos con las leyendas.
keywords: Aspose.Cells for Node.js via C++, Leyendas de gráficos, Microsoft Excel, Visualización, Comprensión de datos.
linktitle: Leyenda
type: docs
weight: 50
url: /es/nodejs-cpp/chart-legend/
---

## **Opciones de Leyenda**
Aspose.Cells for Node.js via C++ también permite gestionar la leyenda de un gráfico en tiempo de ejecución. El objeto [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/) puede ser movido, actualizado y formateado.

|![todo:image_alt_text](chart_legend.png)|

## **Establecimiento de la Leyenda del Gráfico**
Es sencillo gestionar la leyenda del gráfico con Aspose.Cells [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/).

El siguiente fragmento de código muestra cómo gestionar la leyenda:


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

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

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Move the legend to left
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Left);

// Set font color of the legend
chart.getLegend().getFont().setColor(AsposeCells.Color.Blue);

// Save the file
workbook.save("chart_legend.xlsx");
```

## **Temas avanzados**
- [Establecer el texto de relleno de entrada de leyenda del gráfico a ninguno usando Aspose.Cells](/cells/es/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
