---
title: Cómo configurar el eje de categorías con Node.js mediante C++
linktitle: Cómo configurar el eje de categoría
description: Aprende cómo configurar el eje de categorías en Aspose.Cells for Node.js via C++. Nuestra guía te ayudará a entender cómo definir el rango del eje de categorías, ajustar sus propiedades y formatear sus etiquetas.
keywords: Aspose.Cells for Node.js via C++, eje de categorías, configuración, rango, propiedades, formateo.
type: docs
weight: 205
url: /es/nodejs-cpp/how-to-set-category-axis/
---

## **Escenarios de uso posibles**
Después de crear un gráfico en una hoja de cálculo, puedes configurar el eje de categorías para él. En este artículo, te mostraremos cómo configurar el eje de categorías para un gráfico de Excel usando Aspose.Cells con código de ejemplo.

## **Los pasos en el código de muestra**

1. Cree un nuevo libro de trabajo.

2. Cree un nuevo gráfico en la primera hoja de cálculo.

3. Agregue algunos valores a las celdas en la primera hoja de cálculo.

4. Ahora puedes configurar el eje de categorías; hay dos formas: usando datos de celdas o usando cadenas directamente, ambas se muestran en el código de ejemplo.

5. Configura el eje de valores y guarda el libro de trabajo para ver el resultado.

## **Código de muestra**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const dataDir = ""; // Update with your path

// Create a new workbook
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CHART");

// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 8, 0, 20, 10);
const chart = worksheet.getCharts().get(chartIndex);

// Add some values to cells
worksheet.getCells().get("A1").putValue("Sales");
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(130);
worksheet.getCells().get("A5").putValue(160);
worksheet.getCells().get("A6").putValue(150);
worksheet.getCells().get("B1").putValue("Days");
worksheet.getCells().get("B2").putValue(1);
worksheet.getCells().get("B3").putValue(2);
worksheet.getCells().get("B4").putValue(3);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("B6").putValue(5);

// Some values in string
const Sales = "100,150,130,160,150";
const Days = "1,2,3,4,5";

// Set Category Axis Data with string
chart.getNSeries().setCategoryData(`{${Days}}`);
// Or you can set Category Axis Data with data in cells
// chart.getNSeries().setCategoryData("B2:B6");

// Add Series to the chart
chart.getNSeries().add("Demand1", true);
// Set value axis with string 
chart.getNSeries().get(0).setValues(`{${Sales}}`);
chart.getNSeries().add("Demand2", true);
// Set value axis with data in cells
chart.getNSeries().get(1).setValues("A2:A6");

// Set some Category Axis properties
chart.getCategoryAxis().getTickLabels().setRotationAngle(45);
chart.getCategoryAxis().getTickLabels().getFont().setSize(8);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

// Save the workbook to view the result file
workbook.save(path + "Output.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
