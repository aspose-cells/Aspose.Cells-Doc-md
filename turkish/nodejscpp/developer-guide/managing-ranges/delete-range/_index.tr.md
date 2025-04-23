---  
title: Node.js ile C++ kullanarak Aralıkları Silme  
linktitle: Aralıkları Sil  
type: docs  
weight: 105  
url: /tr/nodejs-cpp/delete-ranges-from-Excel/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel de aralıkları nasıl silip hücreleri sola veya yukarı kaydıracağınızı öğrenin.  
---  

## **Giriş**  

Excel'de bir aralık seçebilir, ardından onu silip diğer verileri sola veya yukarı kaydırabilirsiniz.  

**![Shift seçenekleri](delete-range.png)**  

## **Aspose.Cells for Node.js via C++ kullanarak Aralıkları Silme**  

Aspose.Cells, [Cells.deleteRange(number, number, number, number, ShiftType)](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRange-number-number-number-number-shifttype-) metodunu kullanarak bir aralık silmenizi sağlar.  

## **Aralıkları Sil ve Hücreleri Sola Kaydır**  

Aşağıdaki kodlar, Aspose.Cells for Node.js via C++ kullanarak bir aralığı silip hücreleri sola kaydırma örnekleridir:  

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

## **Aralıkları Sil ve Hücreleri Yukarı Kaydır**  

Aşağıdaki kodlar, Aspose.Cells for Node.js via C++ kullanarak bir aralığı silip hücreleri yukarı kaydırma örnekleridir:  

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


