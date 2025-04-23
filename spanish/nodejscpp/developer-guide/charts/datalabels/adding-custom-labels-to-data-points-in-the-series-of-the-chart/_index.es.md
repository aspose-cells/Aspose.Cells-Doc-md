---  
title: Agregar etiquetas personalizadas a los puntos de datos en la serie del gráfico con Node.js a través de C++  
linktitle: Agregar etiquetas personalizadas a los puntos de datos en la serie del gráfico  
description: Aprende cómo agregar etiquetas personalizadas a los puntos de datos en la serie de un gráfico utilizando Aspose.Cells for Node.js via C++. Esta guía demostrará cómo modificar la apariencia, posición y formato de las etiquetas, vinculándolas a tu fuente de datos para una representación precisa.  
keywords: Aspose.Cells para Node.js, creación de gráficos, etiquetas personalizadas, puntos de datos, serie, apariencia, posición, formato, fuente de datos, representación.  
type: docs  
weight: 100  
url: /es/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/  
---  

{{% alert color="primary" %}}  

Puede agregar etiquetas personalizadas a los puntos de datos en la serie del gráfico. Aspose.Cells proporciona la propiedad [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) para agregar estas etiquetas personalizadas. Este artículo explicará cómo usar esta propiedad para agregar etiquetas personalizadas a los puntos de datos en la serie del gráfico.

{{% /alert %}}  

El siguiente código crea **Gráfico de dispersión conectado por líneas con marcadores de datos** y luego agrega **Etiquetas personalizadas** a los **puntos de datos** en la **serie** del **gráfico**. Cada etiqueta personalizada muestra el **nombre de la serie** y el **nombre del punto**. Puedes usar otro texto en su lugar.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Put data
sheet.getCells().get(0, 0).putValue(1);
sheet.getCells().get(0, 1).putValue(2);
sheet.getCells().get(0, 2).putValue(3);

sheet.getCells().get(1, 0).putValue(4);
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(1, 2).putValue(6);

sheet.getCells().get(2, 0).putValue(7);
sheet.getCells().get(2, 1).putValue(8);
sheet.getCells().get(2, 2).putValue(9);

// Generate the chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
const chart = sheet.getCharts().get(chartIndex);

chart.getTitle().setText("Test");
chart.getCategoryAxis().getTitle().setText("X-Axis");
chart.getValueAxis().getTitle().setText("Y-Axis");

chart.getNSeries().setCategoryData("A1:C1");

// Insert series
chart.getNSeries().add("A2:C2", false);

let series = chart.getNSeries().get(0);

let pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 1" + "\n" + "Point " + i);
}

// Insert series
chart.getNSeries().add("A3:C3", false);

series = chart.getNSeries().get(1);

pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 2" + "\n" + "Point " + i);
}

workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

