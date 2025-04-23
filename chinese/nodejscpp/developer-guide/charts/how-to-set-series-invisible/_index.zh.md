---
title: 如何用 Node.js 通过 C++ 设置系列为隐藏
linktitle: 如何设置系列不可见
description: 学习如何用 Aspose.Cells for Node.js via C++ 设置 Excel 图表中的系列为隐藏。 
keywords: Excel 图表，系列，隐藏，是否过滤 Node.js 通过 C++
type: docs
weight: 74
url: /zh/nodejs-cpp/how-to-set-series-invisible/
---

## 如何在Excel图表中设置系列不可见

在Excel图表中，你可以右键点击图表，选择"选择数据"，在弹出窗口中，通过勾选或取消勾选系列来设置是否显示该系列。你可以下载下面的[示例文件](SeriesFiltered.xlsx)，在Excel中操作实现此功能。接下来，我们将告诉你如何使用Aspose.Cells库实现此功能。

![todo:image_alt_text](series-invisible.png)

## 如何使用Aspose.Cells设置系列不可见 

我们使用以下代码来将系列设置为不可见：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SeriesFiltered.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const charts = workbook.getWorksheets().get(0).getCharts();
const chart = charts.get("Chart 1");
const nSeriesFiltered = chart.getFilteredNSeries();
const nSeries = chart.getNSeries();
nSeries.get(1).setIsColorVaried(true);
nSeries.get(0).setIsColorVaried(true);
workbook.save(path.join(dataDir, "output.xlsx"));
```

你可以获取以下[输入文件](SeriesFiltered.xlsx)和[输出文件](output.xlsx)。

如下图所示，原本可见的前两个系列在输出文件中变成了隐藏。
![todo:image_alt_text](output.png)
