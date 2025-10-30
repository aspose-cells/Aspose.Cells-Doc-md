---  
title: Node.jsとC++を使った範囲の削除  
linktitle: 範囲の削除  
type: docs  
weight: 105  
url: /ja/nodejs-cpp/delete-ranges-from-Excel/  
description: Excelで範囲を削除し、左または上にセルをシフトする方法をAspose.Cells for Node.js via C++を使用して学びましょう。  
---  

## **紹介**  

Excelでは、範囲を選択して削除し、他のデータを左にシフトすることができます。  

**![シフトオプション](delete-range.png)**  

## **Aspose.Cells for Node.js via C++を使用した範囲削除**  

Aspose.Cellsは、範囲を削除するための [Cells.deleteRange(number, number, number, number, ShiftType)](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRange-number-number-number-number-shifttype-) メソッドを提供します。  

## **範囲の削除と左にセルをシフト**  

以下のコード例を使用して、Aspose.Cells for Node.js via C++で範囲を削除し、左にセルをシフトします：  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

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

// Gets cells.
const cells = worksheet.getCells();

// Input some data with some formattings into
// A few cells in the range.
cells.get("C2").putValue("C2");
cells.get("C3").putValue("C3");
const ca = AsposeCells.CellArea.createCellArea("B2", "B3");
cells.deleteRange(ca.startRow, ca.startColumn, ca.endRow, ca.endColumn, AsposeCells.ShiftType.Left);
console.log(worksheet.getCells().get("B2").getStringValue() === "C2");
```  

## **範囲の削除と上にセルをシフト**  

以下のコード例を使用して、Aspose.Cells for Node.js via C++で範囲を削除し、上にセルをシフトします：  

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

// Gets cells.
const cells = worksheet.getCells();

// Input some data with some formattings into
// A few cells in the range.
cells.get("B4").putValue("B4");
cells.get("B5").putValue("B5");
const ca = AsposeCells.CellArea.createCellArea("B2", "B3");
cells.deleteRange(ca.startRow, ca.startColumn, ca.endRow, ca.endColumn, AsposeCells.ShiftType.Up);
console.log(cells.get("B2").stringValue === "B4");
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
