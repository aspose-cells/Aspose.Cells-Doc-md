---
title: 如何使用Node.js通过C++创建动态滚动图表
linktitle: 如何创建动态滚动图表
description: 学习如何使用Aspose.Cells for Node.js via C++创建动态滚动图表。我们的指南将演示如何在您的图表中实现平滑的数据过渡和滚动平均，实现连续更新的显示效果。
keywords: Aspose.Cells for Node.js, 动态滚动图表, 数据转换, 平滑平均, 连续显示, 更新可视化。
type: docs
weight: 74
url: /zh/nodejs-cpp/create-dynamic-rolling-chart/
---

## **可能的使用场景**
动态滚动图表是指显示数据点不断变化和更新的图形表示。这是一种图表类型，会不断更新自己，展示最近数据点的滚动窗口，同时丢弃旧的数据点，因为新的数据点出现。

动态滚动图表通常用于可视化实时或流数据中的趋势和模式。在临时方面和随时间的变化至关重要的场景中特别有用，如股票市场分析、天气监测或实时性能跟踪。

这些图表通常采用动画或自动滚动机制，以确保始终呈现最新的信息。滚动窗口的长度可以自定义，以显示特定的时间段，如最近一小时、一天或一周。

总之，动态滚动图表是不断更新的图形表示，显示最新数据点，丢弃旧数据点，使用户能够观察实时趋势和模式。

## **使用Aspose Cells创建动态滚动图表**
在接下来的段落中，我们将向您展示如何使用Aspose.Cells创建动态滚动图表。我们将向您展示示例的代码以及使用该代码创建的Excel文件。

## **示例代码**
以下示例代码将生成[动态滚动图表文件](DynamicRollingChart.xlsx)。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A1").putValue("Month");
sheet.getCells().get("A2").putValue(1);
sheet.getCells().get("A3").putValue(2);
sheet.getCells().get("A4").putValue(3);
sheet.getCells().get("A5").putValue(4);
sheet.getCells().get("A6").putValue(5);
sheet.getCells().get("A7").putValue(6);
sheet.getCells().get("A8").putValue(7);

sheet.getCells().get("B1").putValue("Sales");
sheet.getCells().get("B2").putValue(50);
sheet.getCells().get("B3").putValue(45);
sheet.getCells().get("B4").putValue(55);
sheet.getCells().get("B5").putValue(60);
sheet.getCells().get("B6").putValue(55);
sheet.getCells().get("B7").putValue(65);
sheet.getCells().get("B8").putValue(70);

// Set the dynamic range for the chart's data source.
let index = sheets.getNames().add("Sheet1!ChtData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

// Set the dynamic range for the chart's data labels.
index = sheets.getNames().add("Sheet1!ChtLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 10, 3, 25, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicRollingChart.xlsx"));
```

## **备注**
在生成的文件中，您可以继续在A列和B列中添加数据，同时图表动态计算最新的 5 组数据。这是通过示例代码中的“OFFSET”公式完成的：

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

您可以尝试在公式中将数字“-5”更改为“-10”，动态图表将计算最新的 10 组数据。现在，我们已成功使用Aspose.Cells创建了动态滚动图表。
