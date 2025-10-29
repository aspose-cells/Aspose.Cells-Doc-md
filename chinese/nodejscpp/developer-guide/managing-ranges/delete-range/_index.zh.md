---  
title: 通过 C++ 使用 Node.js 删除范围  
linktitle: 删除范围  
type: docs  
weight: 105  
url: /zh/nodejs-cpp/delete-ranges-from-Excel/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 删除 Excel 中的范围并向左或向上移动单元格。  
---  

## **介绍**  

在 Excel 中，您可以选择一个范围，然后删除它并向左或向上移动其他数据。  

**![移动选项](delete-range.png)**  

## **使用 Aspose.Cells for Node.js via C++ 删除范围**  

Aspose.Cells 提供 [Cells.deleteRange(number, number, number, number, ShiftType)](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRange-number-number-number-number-shifttype-) 方法以删除范围。  

## **删除范围并向左移动单元格**  

使用 Aspose.Cells for Node.js via C++ 删除范围并向左移动单元格，代码如下：  

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

## **删除范围并向上移动单元格**  

使用 Aspose.Cells for Node.js via C++ 删除范围并向上移动单元格，代码如下：  

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
