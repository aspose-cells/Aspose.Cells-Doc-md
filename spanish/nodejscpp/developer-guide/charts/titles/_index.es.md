---
title: Administrar títulos de gráficos de Excel con Node.js vía C++
description: Aprende cómo usar Aspose.Cells for Node.js via C++ para agregar y formatear títulos de gráficos y ejes en Microsoft Excel. Nuestra guía mostrará cómo establecer diferentes tipos de títulos, ajustar su apariencia y modificar títulos de ejes para una mejor representación y claridad de los datos.
keywords: Aspose.Cells for Node.js via C++, Títulos de gráficos, Títulos de ejes, Microsoft Excel, Representación de datos, Apariencia.
linktitle: Títulos
type: docs
weight: 50
url: /es/nodejs-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

En los gráficos de Excel, hay 2 tipos de títulos:
1. Título del Gráfico 
1. Títulos de Ejes

{{% /alert %}}

## **Opciones de Títulos**
Aspose.Cells for Node.js via C++ también permite gestionar los títulos del gráfico en tiempo de ejecución. Con el objeto [Title](https://reference.aspose.com/cells/nodejs-cpp/title/), puedes cambiar el texto, la fuente y el formato de relleno para los títulos.

|![todo:image_alt_text](chart_title.png)|

## **Configuración de los Títulos de Gráficos o Ejes**
Puedes usar Microsoft Excel para establecer los títulos de un gráfico y sus ejes en un entorno WYSIWYG. Aspose.Cells for Node.js via C++ también permite a los desarrolladores establecer los títulos de un gráfico y sus ejes en tiempo de ejecución. Todos los gráficos y sus ejes contienen una propiedad [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) que puede usarse para establecer sus títulos, como se muestra en el ejemplo a continuación.

El siguiente fragmento de código demuestra cómo establecer títulos a gráficos y ejes.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Setting the title of category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Temas avanzados**
- [Leer subtítulo del gráfico desde un archivo ODS](/cells/es/nodejs-cpp/read-chart-subtitle-from-ods-file/)
