---
title: 使用 Node.js 和 C++ 删除工作表中的空白行和列
linktitle: 在工作表中删除空行和空列
type: docs
weight: 300
url: /zh/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 删除工作表中的所有空白行和列。 
---

{{% alert color="primary" %}}

可以从工作表中删除所有空白行和列。这在例如从微软Excel文件生成PDF文件时非常有用，只转换包含数据或相关对象的行和列。

使用以下Aspose.Cells方法来删除空行和空列:

1. 要删除空行，请使用[**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankRows--)方法。请注意，对于将要被删除的空行，不仅需要[**Row.isBlank()**](https://reference.aspose.com/cells/nodejs-cpp/row/#isBlank--)为true，还必须在这些行中的任何单元格没有可见的注释定义，也不应该和任何数据透视表的范围相交。
2. 要删除空白列，使用 [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankColumns--) 方法。

{{% /alert %}}

## 使用 Node.js 删除空白行的代码示例

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(filePath);

// Create a Worksheets object with reference to
// The sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Rows from the worksheet
sheet.getCells().deleteBlankRows();

// Save the excel file.
wb.save(path.join(dataDir, "mybook.out.xlsx"));
```

## 使用 Node.js 删除空白列的代码示例

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an existing excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleInput.xlsx"));

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = workbook.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Columns from the worksheet
sheet.getCells().deleteBlankColumns();

// Save the excel file.
workbook.save(path.join(dataDir, "mybook.out.xlsx"));
```
