---  
title: Bereiche mit Node.js über C++ löschen  
linktitle: Bereiche löschen  
type: docs  
weight: 105  
url: /de/nodejs-cpp/delete-ranges-from-Excel/  
description: Lernen Sie, wie man Bereiche in Excel mit Aspose.Cells for Node.js via C++ löscht und Zellen nach links oder nach oben verschiebt.  
---  

## **Einführung**  

In Excel können Sie einen Bereich auswählen, löschen und andere Daten links oder nach oben verschieben.  

**![Verschieboptionen](delete-range.png)**  

## **Bereiche mit Aspose.Cells for Node.js via C++ löschen**  

Aspose.Cells bietet die Methode [Cells.deleteRange(number, number, number, number, ShiftType)](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRange-number-number-number-number-shifttype-) zum Löschen eines Bereichs.  

## **Bereiche löschen und Zellen nach links verschieben**  

Ein Bereich löschen und Zellen nach links verschieben mit folgendem Code mit Aspose.Cells for Node.js via C++:  

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

## **Bereiche löschen und Zellen nach oben verschieben**  

Ein Bereich löschen und Zellen nach oben verschieben mit folgendem Code mit Aspose.Cells for Node.js via C++:  

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
