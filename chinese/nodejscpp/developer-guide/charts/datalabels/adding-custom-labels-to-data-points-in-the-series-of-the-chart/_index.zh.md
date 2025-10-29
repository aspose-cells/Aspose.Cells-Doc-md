---  
title: 在Node.js via C++中为图表系列中的数据点添加自定义标签  
linktitle: 向图表系列的数据点添加自定义标签  
description: 了解如何在图表系列的数据点中添加自定义标签，使用Aspose.Cells for Node.js via C++。本指南将演示如何修改标签的外观、位置和格式，同时将它们链接到您的数据源以实现准确的表示。  
keywords: Aspose.Cells for Node.js、图表、自定义标签、数据点、系列、外观、位置、格式、数据源、表现。  
type: docs  
weight: 100  
url: /zh/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/  
---  

{{% alert color="primary" %}}  

您可以向图表系列的数据点添加自定义标签。Aspose.Cells提供了[**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--)属性以添加这些自定义标签。本文将解释如何使用此属性向图表系列的数据点添加自定义标签。

{{% /alert %}}  

以下代码创建了**用数据标记连接的散点图**，并向**系列**的**数据点**添加了**自定义标签**，每个标签显示**系列名称**和**点名称**。你可以用任何其他文字替代。

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
