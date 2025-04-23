---
title: 通过Node.js和C++获取图表所在的工作表
linktitle: 获取图表的工作表
description: 学习如何使用Aspose.Cells for Node.js via C++检索与Excel图表相关联的工作表。高效访问和操作图表的底层数据。
keywords: Aspose.Cells for Node.js，Excel图表，工作表，数据操作，底层数据，操作，Node.js通过C++
type: docs
weight: 1000
url: /zh/nodejs-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

有时，您可能希望从图表的引用中访问工作表。Aspose.Cells提供了[**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--)属性，该属性返回包含图表的工作表的引用。

{{% /alert %}}

 以下示例展示如何使用[**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--)属性。代码首先打印工作表的名称，然后访问工作表上的第一个图表。接着再次使用[**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--)属性打印工作表名称。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet of the workbook
const worksheet = workbook.getWorksheets().get(0);

// Print worksheet name
console.log("Sheet Name: " + worksheet.getName());

// Access the first chart inside this worksheet
const charts = worksheet.getCharts();
if (charts.getCount() > 0) {
const chart = charts.get(0);

// Access the chart's sheet and display its name again
console.log("Chart's Sheet Name: " + chart.getWorksheet().getName());
} else {
console.log("No charts available in the worksheet.");
}
```

以下是示例代码产生的控制台输出。您可以看到，它两次打印了相同的工作表名称。

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
