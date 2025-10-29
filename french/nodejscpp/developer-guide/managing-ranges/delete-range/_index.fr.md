---  
title: Supprimer des plages avec Node.js via C++  
linktitle: Supprimer des plages  
type: docs  
weight: 105  
url: /fr/nodejs-cpp/delete-ranges-from-Excel/  
description: Apprenez comment supprimer des plages dans Excel et décaler les cellules vers la gauche ou vers le haut en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Introduction**  

Dans Excel, vous pouvez sélectionner une plage, puis la supprimer et décaler d'autres données vers la gauche ou vers le haut.  

**![Options de décalage](delete-range.png)**  

## **Supprimer des plages en utilisant Aspose.Cells for Node.js via C++**  

Aspose.Cells fournit la méthode [Cells.deleteRange(nombre, nombre, nombre, nombre, ShiftType)](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRange-...-...) pour supprimer une plage.  

## **Supprimer des plages et décaler les cellules à gauche**  

Supprimer une plage et décaler les cellules vers la gauche avec les codes suivants utilisant Aspose.Cells for Node.js via C++ :  

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

## **Supprimer des plages et décaler les cellules vers le haut**  

Supprimer une plage et décaler les cellules vers le haut avec les codes suivants utilisant Aspose.Cells for Node.js via C++ :  

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
