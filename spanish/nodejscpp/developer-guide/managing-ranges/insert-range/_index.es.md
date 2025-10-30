---
title: Insertar rangos con Node.js mediante C++
linktitle: Insertar Rangos
type: docs
weight: 105
url: /es/nodejs-cpp/insert-ranges-to-excel/
description: Aprenda cómo insertar rangos en Excel y desplazar otros datos usando Aspose.Cells for Node.js via C++. 
---

## **Introducción**

En Excel, puedes seleccionar un rango, luego insertar un rango y desplazar otros datos hacia la derecha o hacia abajo.

**![Opciones de desplazamiento](InsertRange.png)**

## **Insertar rangos usando Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ proporciona el método [Cells.insertRange(CellArea, número, TipoDeDesplazamiento, boolean)](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRange-cellarea-number-shifttype-boolean-) para insertar un rango.

## **Insertar Rangos y Desplazar Celdas a la Derecha**

Inserta un rango y desplaza las celdas hacia la derecha con los siguientes códigos usando Aspose.Cells:

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

## **Insertar Rangos y Desplazar Celdas hacia Abajo**

Inserta un rango y desplaza las celdas hacia abajo con los siguientes códigos usando Aspose.Cells:

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
