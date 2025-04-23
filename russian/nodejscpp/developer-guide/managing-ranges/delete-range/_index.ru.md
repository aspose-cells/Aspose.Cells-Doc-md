---  
title: Удалять диапазоны с помощью Node.js через C++  
linktitle: Удалить диапазоны  
type: docs  
weight: 105  
url: /ru/nodejs-cpp/delete-ranges-from-Excel/  
description: Узнайте, как удалять диапазоны в Excel и сдвигать ячейки влево или вверх с помощью Aspose.Cells for Node.js via C++.  
---  

## **Введение**  

В Excel можно выбрать диапазон, затем удалить его и сдвинуть другие данные влево или вверх.  

**![Параметры сдвига](delete-range.png)**  

## **Удаление диапазонов с помощью Aspose.Cells for Node.js via C++**  

Aspose.Cells предоставляет метод [Cells.deleteRange(number, number, number, number, ShiftType)](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRange-number-number-number-number-shifttype-) для удаления диапазона.  

## **Удалить диапазоны и сдвинуть ячейки влево**  

Удаление диапазона и сдвиг ячеек влево, как в следующих кодах с Aspose.Cells for Node.js via C++:  

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

## **Удалить диапазоны и сдвинуть ячейки вверх**  

Удаление диапазона и сдвиг ячеек вверх, как в следующих кодах с Aspose.Cells for Node.js via C++:  

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


