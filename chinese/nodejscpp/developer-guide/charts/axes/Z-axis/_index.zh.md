---
title: 用Node.js通过C++处理Z轴
description: 了解如何在Aspose.Cells for Node.js via C++中处理Z轴。我们的指南将帮助您理解如何配置和定制Z轴，包括其缩放和标签，以增强您的图表。
keywords: Aspose.Cells for Node.js via C++、Z轴、图表、配置、定制、缩放、标签。
type: docs
weight: 210
url: /zh/nodejs-cpp/z-axis/
---

## **可能的使用场景**
对于一些3D图表，如3D柱状图、3D锥体或3D金字塔，它们具有深度（系列）轴，也称为Z轴，可以进行调整。你可以指定刻度间隔、轴标签和其他操作。

## **像微软Excel一样处理主轴和次轴**
请查看以下示例代码，创建一个新Excel文件并将图表数值放在第一个工作表。然后添加图表并设置图表类型为Column3D，你也可以看到Z轴（深度轴）。 

![todo:image_alt_text](excel.png)

## **示例代码**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Put values to cells for creating chart
worksheet.getCells().get("A1").putValue("A");
worksheet.getCells().get("B1").putValue("B");
worksheet.getCells().get("C1").putValue("C");
worksheet.getCells().get("A2").putValue(2);
worksheet.getCells().get("A3").putValue(1);
worksheet.getCells().get("B2").putValue(2);
worksheet.getCells().get("B3").putValue(3);
worksheet.getCells().get("C2").putValue(2);
worksheet.getCells().get("C3").putValue(3);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column3D, 9, 6, 25, 16);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Calculate the chart
chart.calculate();
// Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
chart.setChartDataRange("A2:C3", true);
// Hide the CategoryAxis axis
chart.getCategoryAxis().setIsVisible(false);
// Hide the ValueAxis axis
chart.getValueAxis().setIsVisible(false);
// Save the file
workbook.save("ZAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
