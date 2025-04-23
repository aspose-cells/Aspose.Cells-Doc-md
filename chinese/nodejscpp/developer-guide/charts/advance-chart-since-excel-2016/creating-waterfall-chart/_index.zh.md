---
title: 如何通过C++在Node.js中创建瀑布图
linktitle: 如何创建瀑布图表
type: docs
weight: 160
url: /zh/nodejs-cpp/creating-waterfall-chart/
description: 使用Node.js和Aspose.Cells for Node.js via C++在Excel中创建瀑布图。
keywords: 在Excel中使用C++通过Node.js创建瀑布图，如何创建瀑布图，如何在Node.js中用C++创建瀑布图
---

{{% alert color="primary" %}}

瀑布图是一种特殊的图表，通常用于展示起始位置的增减。微软Excel有多种预定义的图表类型，包括柱状图、折线图、饼图、条形图、雷达图等，但瀑布图超出了基本图形范围，可以用现有的图表类型通过少量或较多的定制化创建。

{{% /alert %}} 

Aspose.Cells APIs允许使用折线图创建瀑布图。API还允许通过设置[**Series.getUpBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getUpBars--)和[**Series.getDownBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getDownBars--)属性来自定义图表外观，使其具有瀑布的形状。

下面的代码片段演示如何使用Aspose.Cells for Node.js via C++从零开始创建瀑布图。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();

// Retrieve the first Worksheet in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Retrieve the Cells of the first Worksheet
const cells = worksheet.getCells();

// Input some data which chart will use as source
cells.get("A1").putValue("Previous Year");
cells.get("A2").putValue("January");
cells.get("A3").putValue("March");
cells.get("A4").putValue("August");
cells.get("A5").putValue("October");
cells.get("A6").putValue("Current Year");

cells.get("B1").putValue(8.5);
cells.get("B2").putValue(1.5);
cells.get("B3").putValue(7.5);
cells.get("B4").putValue(7.5);
cells.get("B5").putValue(8.5);
cells.get("B6").putValue(3.5);

cells.get("C1").putValue(1.5);
cells.get("C2").putValue(4.5);
cells.get("C3").putValue(3.5);
cells.get("C4").putValue(9.5);
cells.get("C5").putValue(7.5);
cells.get("C6").putValue(9.5);

// Add a Chart of type Waterfall in same worksheet as of data
const idx = worksheet.getCharts().add(AsposeCells.ChartType.Waterfall, 4, 4, 25, 13);

// Retrieve the Chart object
const chart = worksheet.getCharts().get(idx);

// Add Series
chart.getNSeries().add("$B$1:$C$6", true);

// Add Category Data
chart.getNSeries().setCategoryData("$A$1:$A$6");

// Series has Up Down Bars
chart.getNSeries().get(0).setHasUpDownBars(true);

// Set the colors of Up and Down Bars
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Red);

// Make both Series Lines invisible
chart.getNSeries().get(0).getBorder().setIsVisible(false);
chart.getNSeries().get(1).getBorder().setIsVisible(false);

// Set the Plot Area Formatting Automatic
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.Automatic);

// Delete the Legend
chart.getLegend().getLegendEntries().get(0).setIsDeleted(true);
chart.getLegend().getLegendEntries().get(1).setIsDeleted(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## 相关文章

- [创建图表](/cells/zh/nodejs-cpp/creating-charts/)
- [自定义图表](/cells/zh/nodejs-cpp/customizing-charts/)
