---
title: Insérer des plages avec Node.js via C++
linktitle: Insérer des plages
type: docs
weight: 105
url: /fr/nodejs-cpp/insert-ranges-to-excel/
description: Apprenez comment insérer des plages dans Excel et décaler les autres données en utilisant Aspose.Cells for Node.js via C++. 
---

## **Introduction**

Dans Excel, vous pouvez sélectionner une plage, puis insérer une plage et déplacer d'autres données vers la droite ou vers le bas.

**![Options de décalage](InsertRange.png)**

## **Insérer des plages en utilisant Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ fournit la méthode [Cells.insertRange(CellArea, nombre, ShiftType, boolean)](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRange-cellarea-number-shifttype-boolean-) pour insérer une plage.

## **Insérer des plages et déplacer les cellules vers la droite**

Insérer une plage et décaler les cellules vers la droite avec Aspose.Cells :

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

## **Insérer des plages et décaler les cellules vers le bas**

Insérer une plage et décaler les cellules vers le bas avec Aspose.Cells :

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

