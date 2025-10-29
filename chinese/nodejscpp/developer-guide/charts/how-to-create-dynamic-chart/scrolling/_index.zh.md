---
title: 如何使用Node.js通过C++创建动态滚动图表
linktitle: 如何创建动态滚动图表
description: 学习如何使用Aspose.Cells for Node.js via C++创建动态滚动图表。我们的逐步指南将演示如何在您的图表中实现平滑数据过渡和自动滚动，确保连续且更新的显示效果。
keywords: Aspose.Cells for Node.js, 动态滚动图表, 数据转换, 平滑滚动, 连续显示, 更新可视化。
type: docs
weight: 75
url: /zh/nodejs-cpp/create-dynamic-scrolling-chart/
---

## **可能的使用场景**
动态滚动图表是一种用于显示随时间变化的数据的图形表示类型。它旨在实时显示数据，使用户能够追踪连续的更新和趋势。随着新增数据的加入，图表将持续更新并自动滚动，以显示最新的信息。

动态滚动图表通常在各个行业中被广泛使用，如金融、股市分析、天气跟踪和社交媒体分析。它们使用户能够可视化和分析数据模式，并基于实时信息做出明智的决策。

这些图表通常是交互式的，允许用户放大或缩小、滚动历史数据和调整时间间隔。它们通常支持多个数据系列，提供不同指标及其相关性的综合视图。

总的来说，动态滚动图表是用于监控和分析时间序列数据的有价值的工具，有助于实时决策和增强数据可视化能力。

## **使用Aspose.Cells创建动态滚动图表**
接下来的段落中，我们将向您展示如何使用Aspose.Cells for Node.js via C++创建动态滚动图表。我们会提供示例代码，以及用此代码生成的Excel文件。

## **示例代码**
以下示例代码将生成[动态滚动图表文件](DynamicScrollingChart.xlsx)。

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
sheet.getCells().get("A1").putValue("Day");
sheet.getCells().get("B1").putValue("Sales");
// In this example, we will add 30 days of data
const allDays = 30;
const showDays = 10;
let currentDay = 1;

for (let i = 0; i < allDays; i++) {
const cellA = `A${i + 2}`;
const cellB = `B${i + 2}`;
sheet.getCells().get(cellA).putValue(i + 1);
sheet.getCells().get(cellB).putValue(50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3));
}

// This is the Dynamic Scrolling Control Data
sheet.getCells().get("G19").putValue("Start Day");
sheet.getCells().get("G20").putValue(currentDay);
sheet.getCells().get("H19").putValue("Show Days");
sheet.getCells().get("H20").putValue(showDays);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtScrollData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtScrollLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Add a ScrollBar for the Dynamic Scrolling Chart
const bar = sheet.getShapes().addScrollBar(2, 0, 3, 0, 200, 30);
bar.setMin(0);
bar.setMax(allDays - showDays);
bar.setCurrentValue(currentDay);
bar.setLinkedCell("$G$20");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 2, 4, 15, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtScrollData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtScrollLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicScrollingChart.xlsx"));
```

## **备注**
在生成的文件中，您可以操作滚动条，而图表会动态计算最新的10组数据。这是在示例代码中使用“OFFSET”公式完成的：

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

您可以尝试将单元格"Sheet1!$H$20"中的数字"10"改为"15"，这样动态图表将显示最新的15组数据。到目前为止，我们已经成功使用Aspose.Cells for Node.js via C++创建了一个动态滚动图表。
{{< app/cells/assistant language="nodejs-cpp" >}}
