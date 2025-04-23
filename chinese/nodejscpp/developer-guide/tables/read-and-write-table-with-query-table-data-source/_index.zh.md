---
title: 通过Node.js读取和写入带有查询表数据源的表
linktitle: 读取和写入带有查询表数据源的表格
type: docs
weight: 30
url: /zh/nodejs-cpp/read-and-write-table-with-query-table-data-source/
description: 学习如何使用Aspose.Cells for Node.js via C++读取和写入带有QueryTable数据源的表。 
---

## **读取和写入带有查询表数据源的表格**
使用Aspose.Cells for Node.js via C++，可以读取和写入具有QueryTable作为数据源的表。此功能也支持XLS文件。以下代码演示读取和写入此类表，先读取表格，再进行修改以添加合计行。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the source directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTableWithQueryTable.xls"));

const worksheet = workbook.getWorksheets().get(0);

const table = worksheet.getListObjects().get(0);

// Check the data source type if it is query table
if (table.getDataSourceType() === AsposeCells.TableDataSourceType.QueryTable) {
table.setShowTotals(true);
}

// Save the file
workbook.save(path.join(outputDir, "SampleTableWithQueryTable_out.xls"));
```

源和输出的Excel文件已附上供参考。

[源文件](96928091.xls)

[输出文件](96928092.xls)
