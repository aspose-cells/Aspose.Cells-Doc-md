---
title: Eje X vs. Eje de Categorías con Node.js mediante C++
linktitle: Eje X Vs. Eje de Categoría
description: Aprende cómo diferenciar entre el eje X y el eje de categorías en Aspose.Cells for Node.js via C++. Nuestra guía te ayudará a entender las diferencias en su uso y propiedades, y cómo configurarlos según tus necesidades.
keywords: Aspose.Cells for Node.js via C++, eje X, eje de categorías, diferencia, uso, propiedades, configuración.
type: docs
weight: 180
url: /es/nodejs-cpp/X-axis-vs-category-axis/
---

## **Escenarios de uso posibles**
Existen diferentes tipos de ejes X. Mientras que el eje Y es un eje de tipo Valor, el eje X puede ser un eje de tipo Categoría o un eje de tipo Valor. Utilizando un eje de Valor, los datos se tratan como datos numéricos continuamente variables, y el marcador se coloca en un punto a lo largo del eje que varía según su valor numérico. Utilizando un eje de Categoría, los datos se tratan como una secuencia de etiquetas de texto no numéricas, y el marcador se coloca en un punto a lo largo del eje según su posición en la secuencia. El ejemplo a continuación ilustra la diferencia entre los Ejes de Valor y de Categoría.
Nuestros datos de muestra se muestran en el [archivo de tabla de muestra](sample.png) a continuación. La primera columna contiene nuestros datos del eje X, que pueden tratarse como Categorías o como Valores. Tenga en cuenta que los números no están igualmente espaciados, ni tampoco aparecen en orden numérico.

![todo:image_alt_text](sample.png)
## **Maneje el eje X y el eje de categoría como Microsoft Excel**
Mostraremos estos datos en dos tipos de gráficos: el primero es un gráfico XY ( dispersión) con eje de valores en X y el segundo es un gráfico de línea con eje de categorías en X.

![todo:image_alt_text](compare.png)
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

// Put the sample values used in charts
worksheet.getCells().get("A2").putValue(1);
worksheet.getCells().get("A3").putValue(3);
worksheet.getCells().get("A4").putValue(2.5);
worksheet.getCells().get("A5").putValue(3.5);
worksheet.getCells().get("B1").putValue("Cats");
worksheet.getCells().get("C1").putValue("Dogs");
worksheet.getCells().get("D1").putValue("Fishes");
worksheet.getCells().get("B2").putValue(7);
worksheet.getCells().get("B3").putValue(6);
worksheet.getCells().get("B4").putValue(5);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("C2").putValue(7);
worksheet.getCells().get("C3").putValue(5);
worksheet.getCells().get("C4").putValue(4);
worksheet.getCells().get("C5").putValue(3);
worksheet.getCells().get("D2").putValue(8);
worksheet.getCells().get("D3").putValue(7);
worksheet.getCells().get("D4").putValue(3);
worksheet.getCells().get("D5").putValue(2);

// Create Line Chart: X as Category Axis
let pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 6, 15, 20, 21);
// Retrieve the Chart object
let chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$5");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);

// Create XY (Scatter) Chart: X as Value Axis
pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
// Retrieve the Chart object
chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set X values for series 
chart.getNSeries().get(0).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(1).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(2).setXValues("{1,3,2.5,3.5}");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("XAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
