---  
title: Delete Ranges med Node.js via C++  
linktitle: Radera områden  
type: docs  
weight: 105  
url: /sv/nodejs-cpp/delete-ranges-from-Excel/  
description: Lär dig hur man tar bort intervall i Excel och flyttar celler till vänster eller upp med Aspose.Cells for Node.js via C++.  
---  

## **Introduktion**  

I Excel kan du markera ett område, sedan radera det och flytta andra data åt vänster eller upp.  

**![Förflyttningsalternativ](delete-range.png)**  

## **Ta bort intervall med Aspose.Cells for Node.js via C++**  

Aspose.Cells ger [Cells.deleteRange(number, number, number, number, ShiftType)](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRange-number-number-number-number-shifttype-) metoden för att ta bort ett område.  

## **Radera områden och flytta celler åt vänster**  

Ta bort ett område och flytta celler till vänster med följande kodexempel med Aspose.Cells for Node.js via C++:  

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

## **Radera områden och flytta celler uppåt**  

Ta bort ett område och flytta celler uppåt med följande kodexempel med Aspose.Cells for Node.js via C++:  

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
