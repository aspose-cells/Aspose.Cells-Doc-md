---
title: 使用Chart.SetChartDataRange方法轻松设置图表的简易方法（Node.js通过C++）
linktitle: 使用Chart.SetChartDataRange方法轻松设置图表。
description: 学习如何在Aspose.Cells for Node.js via C++中使用Chart.SetChartDataRange方法轻松设置图表。我们的指南将向您展示如何指定图表的数据范围，让您以最小的努力创建专业和准确的图表。
keywords: Aspose.Cells for Node.js via C++、图表、SetChartDataRange方法、数据范围、专业、准确、图表。
type: docs
weight: 190
url: /zh/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/
---

{{% alert color="primary" %}}

Aspose.Cells现在提供[**Chart.setChartDataRange(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#setChartDataRange-string-boolean-)方法来轻松设置图表。使用此方法，您不需要分别添加系列和分类轴数据。

{{% /alert %}}

以下示例代码说明了如何使用[**Chart.setChartDataRange(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#setChartDataRange-string-boolean-)方法轻松设置图表。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add data for chart

// Category Axis Values
worksheet.getCells().get("A2").putValue("C1");
worksheet.getCells().get("A3").putValue("C2");
worksheet.getCells().get("A4").putValue("C3");

// First vertical series
worksheet.getCells().get("B1").putValue("T1");
worksheet.getCells().get("B2").putValue(6);
worksheet.getCells().get("B3").putValue(3);
worksheet.getCells().get("B4").putValue(2);

// Second vertical series
worksheet.getCells().get("C1").putValue("T2");
worksheet.getCells().get("C2").putValue(7);
worksheet.getCells().get("C3").putValue(2);
worksheet.getCells().get("C4").putValue(5);

// Third vertical series
worksheet.getCells().get("D1").putValue("T3");
worksheet.getCells().get("D2").putValue(8);
worksheet.getCells().get("D3").putValue(4);
worksheet.getCells().get("D4").putValue(2);

// Create Column chart with easy way
const idx = worksheet.getCharts().add(AsposeCells.ChartType.Column, 6, 5, 20, 13);
const ch = worksheet.getCharts().get(idx);
ch.setChartDataRange("A1:D4", true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
