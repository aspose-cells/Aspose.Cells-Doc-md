---
title: Вставить диапазоны с помощью Node.js через C++
linktitle: Вставка диапазонов
type: docs
weight: 105
url: /ru/nodejs-cpp/insert-ranges-to-excel/
description: Узнайте, как вставлять диапазоны в Excel и смещать другие данные с помощью Aspose.Cells for Node.js via C++. 
---

## **Введение**

В Excel можно выбрать диапазон, а затем вставить диапазон и сдвинуть другие данные вправо или вниз.

**![Опции сдвига](InsertRange.png)**

## **Вставлять диапазоны с помощью Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ предоставляет метод [Cells.insertRange(CellArea, number, ShiftType, boolean)](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRange-cellarea-number-shifttype-boolean-) для вставки диапазона.

## **Вставка диапазонов и сдвиг ячеек вправо**

Вставить диапазон и сдвинуть ячейки вправо, как показано в кодах с Aspose.Cells:

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

## **Вставка диапазонов и сдвиг ячеек вниз**

Вставить диапазон и сдвинуть ячейки вниз, как показано в кодах с Aspose.Cells:

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

