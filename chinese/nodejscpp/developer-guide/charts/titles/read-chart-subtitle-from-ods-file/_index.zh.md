---
title: 使用Node.js via C++读取ODS文件中的图表字幕
linktitle: 从ODS文件中读取图表副标题
description: 学习如何使用Aspose.Cells for Node.js via C++从OpenDocument Spreadsheet (ODS)文件中读取图表字幕。本指南将演示如何提取和访问图表的字幕以便进一步分析或显示。
keywords: Aspose.Cells for Node.js via C++，读取图表字幕，OpenDocument Spreadsheet，ODS文件，图表提取，数据分析。
type: docs
weight: 160
url: /zh/nodejs-cpp/read-chart-subtitle-from-ods-file/
---

## **从ODS文件中读取图表副标题**

Aspose.Cells 提供了通过使用[**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--)属性读取ODS文件中图表字幕的能力。以下示例代码加载[示例ODS文件](89620481.ods)，并使用[**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--)属性读取图表字幕，然后将其打印到控制台。请参考下面的代码输出。

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Load excel file containing charts
const filePath = path.join(sourceDir, "SampleChart.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

console.log("Chart Subtitle: " + chart.getSubTitle().getText());
```

## **控制台输出**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
