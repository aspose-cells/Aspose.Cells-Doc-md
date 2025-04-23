---
title: Eje primario y secundario con Node.js vía C++
description: Aprende cómo entender y trabajar con ejes primarios y secundarios en Aspose.Cells for Node.js via C++. Nuestra guía te ayudará a entender las diferencias entre los ejes primarios y secundarios, y cómo configurarlos y usarlos eficazmente en tus gráficos.
keywords: Aspose.Cells for Node.js via C++, ejes primarios, ejes secundarios, comprensión, diferencias, configuración, uso.
type: docs
weight: 190
url: /es/nodejs-cpp/primary-and-second-axis/
---

## **Escenarios de uso posibles**
Cuando los números en un gráfico varían ampliamente de serie de datos a serie de datos, o cuando se tienen tipos mixtos de datos (precio y volumen), se traza una o más series de datos en un eje vertical (valor) secundario. La escala del eje vertical secundario muestra los valores de las series de datos asociadas. Un eje secundario funciona bien en un gráfico que muestra una combinación de gráficos de columnas y líneas.

## **Manejar el eje primario y secundario como en Microsoft Excel**
Por favor, vea el siguiente código de ejemplo que crea un nuevo archivo Excel y coloca los valores del gráfico en la primera hoja. 
Luego agregamos un gráfico y mostramos el segundo eje.

![todo:image_alt_text](excel.png)

## **Código de muestra**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in a chart
worksheet.getCells().get("A1").putValue("Region");
worksheet.getCells().get("A2").putValue("Peking");
worksheet.getCells().get("A3").putValue("New York");
worksheet.getCells().get("A4").putValue("Paris");
worksheet.getCells().get("B1").putValue("Sales Volume");
worksheet.getCells().get("C1").putValue("Growth Rate");
worksheet.getCells().get("B2").putValue(100);
worksheet.getCells().get("B3").putValue(80);
worksheet.getCells().get("B4").putValue(140);
worksheet.getCells().get("C2").putValue(0.7);
worksheet.getCells().get("C3").putValue(0.8);
worksheet.getCells().get("C4").putValue(1.0);

// Create a Scatter chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Scatter, 6, 6, 15, 11);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:C4", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$4");
// Set the Second-Axis
chart.getNSeries().get(1).setPlotOnSecondAxis(true);
// Show the Second-Axis
chart.getSecondValueAxis().setIsVisible(true);
// Set the second series ChartType to line
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);
// Set the series name
chart.getNSeries().get(0).setName("Sales Volume");
chart.getNSeries().get(1).setName("Growth Rate");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the file
workbook.save("PrimaryandSecondaryAxis.xlsx");
```
