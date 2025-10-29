---
title: 如何在Node.js via C++中使用PivotOptions管理PivotChart
linktitle: 数据透视表选项
type: docs
weight: 10
url: /zh/nodejs-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: 在Node.js via C++中如何使用PivotOptions管理PivotChart。
keywords: 数据透视图 Node.js 通过 C++
---
## 什么是数据透视图

Excel中的数据透视图是从数据透视表中创建的数据的图形表示。它允许用户通过以图表形式汇总和显示信息来动态可视化和分析数据。数据透视图是交互式的，可以轻松修改以显示数据的不同视角，因此是Excel中数据分析和演示的强大工具。

## 如何使用数据透视表选项管理数据透视图

通过使用Aspose.Cells for Node.js via C++，你可以使用[**PivotOptions**](https://reference.aspose.com/cells/nodejs-cpp/pivotoptions/)管理PivotChart。

样本文件和代码：
[样本文件](Sample.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const chart = workbook.getWorksheets().get(0).getCharts().get(0);
const opt = chart.getPivotOptions();

// Hide ZoneFilter in PivotChart
opt.setDropZoneFilter(false); // HideZoneFilter

// You can set more properties, try them!
// opt.setDropZoneCategories(false); // HideZoneCategories
// opt.setDropZoneData(false); // HideZoneData
// opt.setDropZoneSeries(false); // HideZoneSeries
// opt.setDropZonesVisible(false); // Hide All

// Save the file and see the effect.
workbook.save(path.join(dataDir, "HideZoneFilter.xlsx"));
```

通过上面的示例代码，您可以查看以下效果的结果文件，如下图所示：

**![输出](Output.png)**
{{< app/cells/assistant language="nodejs-cpp" >}}
