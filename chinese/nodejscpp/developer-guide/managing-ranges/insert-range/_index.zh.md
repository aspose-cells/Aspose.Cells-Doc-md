---
title: 在 Node.js 中插入范围
linktitle: 插入范围
type: docs
weight: 105
url: /zh/nodejs-cpp/insert-ranges-to-excel/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 在 Excel 中插入范围并移动其他数据。 
---

## **介绍**

在 Excel 中，您可以选择一个范围，然后插入一个范围，并向右或向下移动其他数据。

**![移动选项](InsertRange.png)**

## **使用 Aspose.Cells for Node.js via C++ 插入范围**

Aspose.Cells for Node.js via C++ 提供 [Cells.insertRange(CellArea, number, ShiftType, boolean)](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRange-cellarea-number-shifttype-boolean-) 方法插入范围。

## **插入范围并向右移动单元格**

使用Aspose.Cells插入范围并向右移动单元格的示例代码：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Instantiate a new Workbook.
const newWorkbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = newWorkbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = newWorkbook.getWorksheets().get(0);

// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue("123");
const ca = AsposeCells.CellArea.createCellArea("A1", "A2");
worksheet.getCells().insertRange(ca, AsposeCells.ShiftType.Right);
console.log(worksheet.getCells().get("B1").getValue() === "Test");
```

## **插入范围并向下移动单元格**

使用Aspose.Cells插入范围并向下移动单元格的示例代码：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Instantiate a new Workbook.
const newWorkbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = newWorkbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = newWorkbook.getWorksheets().get(0);

// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).putValue("Test");
sourceRange.get(1, 0).putValue(123);
const ca = AsposeCells.CellArea.createCellArea("A1", "A2");
worksheet.getCells().insertRange(ca, AsposeCells.ShiftType.Down);
console.log(worksheet.getCells().get("A3").getValue() === "Test");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
