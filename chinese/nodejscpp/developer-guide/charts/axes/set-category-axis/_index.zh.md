---
title: 如何使用Node.js通过C++设置类别轴
linktitle: 如何设置类别轴
description: 了解如何在Aspose.Cells for Node.js via C++中设置类别轴。我们的指南将帮助您理解如何定义类别轴范围、调整其属性和格式化标签。
keywords: Aspose.Cells for Node.js via C++、类别轴、设置、范围、属性、格式化。
type: docs
weight: 205
url: /zh/nodejs-cpp/how-to-set-category-axis/
---

## **可能的使用场景**
在工作表中创建图表后，您可以为它设置类别轴。本文将向您展示如何使用Aspose.Cells为Excel图表设置类别轴的示例代码。

## **示例代码中的步骤**

1. 创建一个新的工作簿。

2. 在第一个工作表中创建一个新的图表。

3. 在第一个工作表的单元格中添加一些值。

现在可以设置类别轴；有两种方法：使用单元格数据或直接使用字符串，示例代码中均有显示。

设置值轴，并保存工作簿以查看结果。

## **示例代码**
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
