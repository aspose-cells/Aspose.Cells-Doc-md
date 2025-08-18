---
title: 通过 C++ 和 Node.js 过滤图表数据的三种方法
linktitle: 过滤图表数据的三种方法
description: 学习如何使用 Aspose.Cells for Node.js via C++ 在 Excel 中过滤图表。我们的 comprehensive 指南将演示如何应用过滤器到图表，定制图表元素，以及使用数据分析工具获得更好的洞察和做出更明智的决策。
keywords: Aspose.Cells for Node.js via C++，Excel 图表过滤，数据分析，决策制定，可视化。
type: docs
weight: 2210
url: /zh/nodejs-cpp/filtering-charts-in-excel/
---


## **1. 过滤以渲染图表的系列**

### **在Excel中，我们可以过滤掉图表中的特定系列，导致这些被过滤的系列不会显示在图表中。 原始图表显示在**图1**中。然而，当我们过滤掉**Testseries2**和**Testseries4**时，图表将会如**图2**所示。**
在Excel中，我们可以筛选出特定系列，从而在图表中隐藏那些筛选的系列。原始图表如**图1**所示。当我们筛选掉**Testseries2**和**Testseries4**后，图表将如**图2**所示。

在 Aspose.Cells for Node.js via C++ 中，我们可以执行类似操作。对于像这样的 [示例](seriesFiltered.xlsx) 文件，如果我们想过滤掉 **Testseries2** 和 **Testseries4**，可以执行以下代码。此外，我们将维护两个列表：一个（[Chart.getNSeries()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getNSeries--)）列表存储所有已选择的系列。

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **示例代码**
以下示例代码加载了[示例Excel文件](seriesFiltered.xlsx)。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "seriesFiltered.xlsx");
// Create an instance of existing Workbook
let workbook = new AsposeCells.Workbook(filePath);
// Get filtered series list
let nSeriesFiltered = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getFilteredNSeries();
// Get selected series list
let nSeries = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getNSeries();
// Should be 0
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 6
console.log("Visible Series count: " + nSeries.getCount());
// Process from the end to the beginning
nSeries.get(1).setIsFiltered(true);
nSeries.get(0).setIsFiltered(true);
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
workbook.save("seriesFiltered-out.xlsx");
workbook = new AsposeCells.Workbook("seriesFiltered-out.xlsx");
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
```

## **2. 过滤数据并使图表发生变化**

筛选数据是处理大量图表数据的好方法。当你筛选数据时，图表也会相应变化。需要注意的是，要确保图表始终显示在屏幕上，筛选可能会隐藏行，而图表可能位于这些隐藏行中。

![todo:image_alt_text](Figure3.png)

### **使用数据筛选器更改Excel中图表的步骤**

1. 点击数据范围内部。
2. 单击**数据**选项卡，通过单击筛选器进行筛选。 您的标题行将有下拉箭头。
3. 通过转到**插入**选项卡并选择列图表来创建图表。
4. 现在使用数据中的下拉箭头筛选您的数据。 不要使用图表筛选器。

### **示例代码**
以下示例代码展示了使用Aspose.Cells实现相同功能。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of Worksheet
const sheet = workbook.getWorksheets().get("Sheet1");
// Add data into details cells.
sheet.getCells().get(0, 0).putValue("Fruits Name");
sheet.getCells().get(0, 1).putValue("Fruits Price");
sheet.getCells().get(1, 0).putValue("Apples");
sheet.getCells().get(2, 0).putValue("Bananas");
sheet.getCells().get(3, 0).putValue("Grapes");
sheet.getCells().get(4, 0).putValue("Oranges");
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(2, 1).putValue(2);
sheet.getCells().get(3, 1).putValue(1);
sheet.getCells().get(4, 1).putValue(4);

// Add a chart to the worksheet
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
// Access the instance of the newly added chart
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B5", true);
// Set AutoFilter range
sheet.getAutoFilter().setRange("A1:B5");
// Add filters for a filter column.
sheet.getAutoFilter().addFilter(0, "Bananas");
sheet.getAutoFilter().addFilter(0, "Oranges");
// Apply the filters
sheet.getAutoFilter().refresh();
chart.toImage("Autofilter.png");
workbook.save("Autofilter.xlsx");
```

## **3. 使用表格过滤数据并使图表发生变化**

使用表格类似于方法2，使用范围，但表格比范围有优势。当您将范围更改为表格并添加数据时，图表会自动更新。使用范围时，您将不得不更改数据源。

### **在Excel中格式化为表格**

单击数据内部并使用**CTRL + T**或使用主页选项卡，**格式为表格**

![todo:image_alt_text](Figure4.png)

### **示例代码**
以下示例代码加载了[示例Excel文件](TableFilters.xlsx)，展示了使用Aspose.Cells实现相同功能。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "TableFilters.xlsx");
// Create a workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const sheet = workbook.getWorksheets().get(0);
// Access the instance of the newly added chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B7", true);
// Convert the chart to image
chart.toImage("TableFilters.before.png");
// Add a new List Object to the worksheet
const listObject = sheet.getListObjects().get(sheet.getListObjects().add("A1", "B7", true));
// Add default style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);
// Show Total
listObject.setShowTotals(false);
// Add filters for a filter column.
listObject.getAutoFilter().addFilter(0, "James");
// Apply the filters
listObject.getAutoFilter().refresh();
// After adding new value the chart will change
listObject.putCellValue(7, 0, "Me");
listObject.putCellValue(7, 1, 1000);
// Check the changed images
chart.toImage("TableFilters.after.png");
// Saving the Excel file
workbook.save("TableFilter.out.xlsx");
```
