---
title: Infoga områden med Node.js via C++
linktitle: Infoga intervall
type: docs
weight: 105
url: /sv/nodejs-cpp/insert-ranges-to-excel/
description: Lär dig att infoga områden i Excel och förskjuta annan data med Aspose.Cells for Node.js via C++. 
---

## **Introduktion**

I Excel kan du välja ett intervall, sedan infoga ett intervall och skifta andra data höger eller ned.

**![Skiftalternativ](InsertRange.png)**

## **Infoga områden med Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ erbjuder [Cells.insertRange(CellArea, number, ShiftType, boolean)](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRange-cellarea-number-shifttype-boolean-) metod för att infoga ett område.

## **Infoga Intervall och skifta celler höger**

Infoga ett område och skjut cellerna till höger med följande kodexempel med Aspose.Cells:

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

## **Infoga Intervall och skifta celler ned**

Infoga ett område och skjut cellerna nedåt med följande kodexempel med Aspose.Cells:

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

