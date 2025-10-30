---
title: Bereiche mit Node.js über C++ einfügen
linktitle: Bereiche einfügen
type: docs
weight: 105
url: /de/nodejs-cpp/insert-ranges-to-excel/
description: Erfahren Sie, wie man Bereiche in Excel einfügt und andere Daten verschiebt mit Aspose.Cells for Node.js via C++. 
---

## **Einführung**

In Excel können Sie einen Bereich auswählen, dann einen Bereich einfügen und andere Daten nach rechts oder nach unten verschieben.

**![Verschieboptionen](InsertRange.png)**

## **Bereiche mit Aspose.Cells for Node.js via C++ einfügen**

Aspose.Cells for Node.js via C++ stellt die Methode [Cells.insertRange(CellArea, number, ShiftType, boolean)](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRange-cellarea-number-shifttype-boolean-) bereit, um einen Bereich einzufügen.

## **Bereiche einfügen und Zellen nach rechts verschieben**

Einen Bereich einfügen und die Zellen nach rechts verschieben mit Aspose.Cells:

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

## **Bereiche einfügen und Zellen nach unten verschieben**

Einen Bereich einfügen und die Zellen nach unten verschieben mit Aspose.Cells:

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
