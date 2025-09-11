---  
title: Adding Custom Labels to Data Points in the Series of the Chart with Node.js via C++  
linktitle: Adding Custom Labels to Data Points in the Series of the Chart  
description: Learn how to add custom labels to data points in the series of a chart using Aspose.Cells for Node.js via C++. This guide will demonstrate how to modify labels' appearance, position, and formatting, while linking them to your data source for accurate representation.  
keywords: Aspose.Cells for Node.js, charting, custom labels, data points, series, appearance, position, formatting, data source, representation.  
type: docs  
weight: 100  
url: /nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/  
---  

{{% alert color="primary" %}}  

You can add custom labels to data points in the series of the chart. Aspose.Cells provides [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) property to add these custom labels. This article will explain how to use this property to add custom labels to data points in the series of the chart.

{{% /alert %}}  

The following code creates **Scatter Chart Connected By Lines With Data Markers** and then adds **Custom Labels** to the **Data Points** in the **Series** of the **Chart**. Each custom label shows the **Series Name** and **Point Name**. You can use any other text instead of it.

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
  
{{< app/cells/assistant language="nodejs-cpp" >}}