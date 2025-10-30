---
title: Node.js kullanarak C++ ile Aralıklar Ekleme
linktitle: Aralıkları Ekle
type: docs
weight: 105
url: /tr/nodejs-cpp/insert-ranges-to-excel/
description: Excel de aralıklar nasıl eklenir ve diğer veriler nasıl kaydırılır öğrenin, Aspose.Cells for Node.js via C++ kullanılarak. 
---

## **Giriş**

Excel'de bir aralığı seçebilir, ardından sağa veya aşağıya diğer verileri kaydırarak bir aralık ekleyebilirsiniz.

**![Kaydırma seçenekleri](InsertRange.png)**

## **Aspose.Cells for Node.js via C++ kullanarak Aralıklar Ekle**

Aspose.Cells for Node.js via C++, [Cells.insertRange(HücreAlanı, sayı, KaydırmaTipi, boolean)] metodunu sağlar ve aralık ekler.

## **Aralıkları Ekleyip Hücreleri Sağa Kaydırmak**

Aşağıdaki kodlar ile aspose.cells kullanarak bir aralık ekleyin ve hücreleri sağa kaydırın:

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

## **Aralıkları Ekleyin ve Hücreleri Aşağı Kaydırın**

Aşağıdaki kodlar ile aspose.cells kullanarak bir aralık ekleyin ve hücreleri aşağı kaydırın:

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
