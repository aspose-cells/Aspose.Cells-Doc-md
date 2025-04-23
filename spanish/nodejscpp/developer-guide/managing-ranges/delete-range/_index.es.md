---  
title: Eliminar rangos con Node.js vía C++  
linktitle: Eliminar Rangos  
type: docs  
weight: 105  
url: /es/nodejs-cpp/delete-ranges-from-Excel/  
description: Aprende cómo eliminar rangos en Excel y desplazar celdas a la izquierda o hacia arriba usando Aspose.Cells for Node.js via C++.  
---  

## **Introducción**  

En Excel, puedes seleccionar un rango, luego eliminarlo y desplazar otros datos a la izquierda o hacia arriba.  

**![Opciones de Desplazamiento](delete-range.png)**  

## **Eliminar rangos usando Aspose.Cells for Node.js via C++**  

Aspose.Cells proporciona el método [Cells.deleteRange(número, número, número, número, ShiftType)](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRange-number-number-number-number-shifttype-) para eliminar un rango.  

## **Eliminar Rangos y Desplazar Celdas a la Izquierda**  

Eliminar un rango y desplazar las celdas a la izquierda con los siguientes códigos usando Aspose.Cells for Node.js via C++:  

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

## **Eliminar rangos y desplazar celdas hacia arriba**  

Eliminar un rango y desplazar las celdas hacia arriba como los siguientes códigos con Aspose.Cells for Node.js via C++:  

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


