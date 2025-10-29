---
title: 通过C++用Node.js处理主轴与次轴
description: 了解如何在Aspose.Cells for Node.js via C++中理解并使用主轴和次轴。我们的指南将帮助您理解主轴和次轴的区别，以及如何有效配置和使用它们。
keywords: Aspose.Cells for Node.js via C++、主轴、次轴、理解、区别、配置、使用。
type: docs
weight: 190
url: /zh/nodejs-cpp/primary-and-second-axis/
---

## **可能的使用场景**
当图表中的数据系列之间的数值差异很大，或者当您有多种类型的数据（价格和成交量）时，请在次垂直（值）轴上绘制一个或多个数据系列。次垂直轴的刻度显示了相关数据系列的值。在显示柱形图和折线图的组合图中，次要轴效果很好。

## **处理主轴和第二轴，就像处理Microsoft Excel一样**
请参阅以下示例代码，此代码创建一个新的Excel文件并将图表的值放在第一个工作表中。 
然后我们添加一个图表并显示第二轴。

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
{{< app/cells/assistant language="nodejs-cpp" >}}
