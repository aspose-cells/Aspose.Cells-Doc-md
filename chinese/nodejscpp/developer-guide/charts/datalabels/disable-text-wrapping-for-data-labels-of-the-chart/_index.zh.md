---
title: 禁用Node.js via C++中图表数据标签的换行功能
description: 学习如何在Aspose.Cells for Node.js via C++中禁用图表中数据标签的文本换行。我们的指南将向您展示如何防止长标签重叠，从而提供更清晰易懂的图表显示。
keywords: Aspose.Cells for Node.js via C++，制图，数据标签，文本换行，重叠，易读性，显示。
type: docs
weight: 70
url: /zh/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013允许用户在图表的数据标签中换行或取消换行。默认情况下，图表的数据标签中的文字是处于换行状态。

Aspose.Cells 提供一个 [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#isTextWrapped--) 属性，您可以设置为 true 或 false 以分别启用或禁用数据标签的文本换行。

{{% /alert %}}

下面的代码示例显示了如何禁用图表数据标签的文字换行。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_wrap_label.xlsx");
// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Disable the Text Wrapping of Data Labels in all Series
chart.getNSeries().get(0).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(1).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(2).getDataLabels().setIsTextWrapped(false);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
