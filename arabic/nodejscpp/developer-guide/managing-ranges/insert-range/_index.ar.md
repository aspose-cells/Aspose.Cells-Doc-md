---
title: إدراج النطاقات باستخدام Node.js عبر C++
linktitle: إدراج المجالات
type: docs
weight: 105
url: /ar/nodejs-cpp/insert-ranges-to-excel/
description: تعلم كيفية إدراج نطاقات في Excel وتحويل البيانات الأخرى باستخدام Aspose.Cells for Node.js via C++. 
---

## **مقدمة**

في Excel ، يمكنك تحديد مجال ، ثم إدراج مجال ونقل البيانات الأخرى يمينًا أو لأسفل.

**![خيارات النقل](InsertRange.png)**

## **إدراج النطاقات باستخدام Aspose.Cells for Node.js via C++**

يوفر Aspose.Cells for Node.js via C++ طريقة [Cells.insertRange(CellArea, number, ShiftType, boolean)] لإدراج نطاق.

## **إدراج مجموعات ونقل الخلايا إلى اليمين**

إدراج نطاق وتحريك الخلايا إلى اليمين كما في الرموز التالية مع Aspose.Cells:

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

## **إدراج مجموعات ونقل الخلايا للأسفل**

إدراج نطاق وتحريك الخلايا إلى الأسفل كما في الرموز التالية مع Aspose.Cells:

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

