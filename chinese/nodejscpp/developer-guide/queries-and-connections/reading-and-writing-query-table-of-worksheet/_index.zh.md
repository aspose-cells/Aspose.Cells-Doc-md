---
title: 用Node.js和C++读取和写入工作表的查询表
linktitle: 工作表的查询表读取和写入
type: docs
weight: 40
url: /zh/nodejs-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells提供了Worksheet.QueryTables集合，它按索引返回QueryTable类型的对象。它有以下两个属性

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

这两个都是布尔值。你可以在Microsoft Excel中通过数据 > 连接 > 属性查看它们。

{{% /alert %}}

## 工作表的查询表读取和写入

以下示例读取第一个工作表的第一个QueryTable，并打印两个QueryTable属性，然后将QueryTable.preserveFormatting设置为true。

您可以从以下链接下载用于此代码的源Excel文件和代码生成的输出Excel文件。

- [源Excel文件](5115533.xlsx)
- [输出Excel文件](5115537.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first Query Table
const qt = worksheet.getQueryTables().get(0);

// Print Query Table Data
console.log("Adjust Column Width: " + qt.getAdjustColumnWidth());
console.log("Preserve Formatting: " + qt.getPreserveFormatting());

// Now set Preserve Formatting to true
qt.setPreserveFormatting(true);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```

### 控制台输出

这是上述示例代码的控制台输出

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## 检索查询表结果范围

Aspose.Cells提供了读取查询表结果范围的选项。以下代码演示了通过读取查询表的结果范围地址来实现此功能。示例文件可以从[这里](72417290.xlsx)下载。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");

// Create workbook from source excel file
const wb = new AsposeCells.Workbook(filePath);

// Display the address(range) of result range of query table
console.log(wb.getWorksheets().get(0).getQueryTables().get(0).getResultRange().getAddress());
```
