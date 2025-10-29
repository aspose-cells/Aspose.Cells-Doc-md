---  
title: حذف النطاقات باستخدام Node.js عبر C++  
linktitle: حذف المجموعات  
type: docs  
weight: 105  
url: /ar/nodejs-cpp/delete-ranges-from-Excel/  
description: تعلم كيفية حذف النطاقات في Excel وتحريك الخلايا إلى اليسار أو الأعلى باستخدام Aspose.Cells for Node.js via C++.  
---  

## **مقدمة**  

في Excel، يمكنك تحديد مجموعة، ثم حذفها وتحريك البيانات الأخرى يسارًا أو لأعلى.  

**![خيارات التحريك](delete-range.png)**  

## **حذف النطاقات باستخدام Aspose.Cells for Node.js via C++**  

 توفر Aspose.Cells طريقة [Cells.deleteRange(number, number, number, number, ShiftType)](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRange-number-number-number-number-shifttype-) لحذف مدى.  

## **حذف النطاقات وتحريك الخلايا لليسار**  

حذف مدى وتحريك الخلايا إلى اليسار كما في الأكواد التالية باستخدام Aspose.Cells for Node.js via C++:  

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

## **حذف النطاقات وتحريك الخلايا لأعلى**  

حذف مدى وتحريك الخلايا إلى الأعلى كما في الأكواد التالية باستخدام Aspose.Cells for Node.js via C++:  

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
