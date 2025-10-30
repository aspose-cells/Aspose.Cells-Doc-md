---
title: Node.jsを使った範囲の挿入（C++経由）
linktitle: 範囲の挿入
type: docs
weight: 105
url: /ja/nodejs-cpp/insert-ranges-to-excel/
description: Excelに範囲を挿入し、他のデータをシフトさせる方法をAspose.Cells for Node.js via C++で学びましょう。 
---

## **紹介**

Excelでは、範囲を選択し、その後、他のデータを右または下にシフトして範囲を挿入できます。

**! [挿入オプション](InsertRange.png)**

## **Aspose.Cells for Node.js via C++を使った範囲の挿入**

Aspose.Cells for Node.js via C++は [Cells.insertRange(CellArea, number, ShiftType, boolean)](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRange-cellarea-number-shifttype-boolean-) メソッドを提供します。

## **範囲の挿入とセルの右シフト**

以下のコード例では、範囲を挿入し、セルを右にシフトします（Aspose.Cellsを使用）：

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

## **範囲の挿入とセルの下シフト**

以下のコード例では、範囲を挿入し、セルを下にシフトします（Aspose.Cellsを使用）：

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
