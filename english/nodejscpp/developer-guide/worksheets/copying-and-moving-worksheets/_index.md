---
title: Copying and Moving Worksheets with Node.js via C++
linktitle: Copying and Moving Worksheets
type: docs
weight: 10
url: /nodejs-cpp/copying-and-moving-worksheets/
description: This article includes sample code and describes how to copy and move worksheets programmatically both within an Excel workbook and across Excel workbooks using the Node.js API with C++.
keywords: copy worksheet Node.js, move worksheet Node.js
---

{{% alert color="primary" %}}

Sometimes, you do need a number of worksheets with common formatting and data. For example, if you work with quarterly budgets, you might want to create a workbook with sheets that contain the same column headings, row headings, and formulas. There is a way to do this: by creating one sheet and then copying it.

Aspose.Cells for Node.js via C++ supports copying and moving worksheets within or between workbooks. Worksheet, complete with data, formatting, tables, matrices, charts, images and other objects, are copied with the highest degree of precision.

{{% /alert %}}

## **Moving or Copying Sheets using Microsoft Excel**

Following are the steps involved for copying and moving worksheets within or between workbooks in Microsoft Excel.

1. To move or copy sheets to another workbook, open the workbook that will receive the sheets.
1. Switch to the workbook that contains the sheets you want to move or copy, and then select the sheets.
1. On the **Edit** menu, click **Move or Copy Sheet**.
1. In the **To book** dialog, click the workbook to receive the sheets.
1. To move or copy the selected sheets to a new workbook, click **New Book**.
1. In the **Before sheet** box, click the sheet before which you want to insert the moved or copied sheets.
1. To copy the sheets instead of moving them, select the **Create a copy** checkbox.

### **Copy Worksheets within a Workbook with Aspose.Cells for Node.js via C++**

Aspose.Cells provides an overloaded method, [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#addCopy-number-), that is used to add a worksheet to the collection and copy data from an existing worksheet. One version of the method takes the index of the source worksheet as a parameter. The other version takes the name of the source worksheet.

The following example shows how to copy an existing worksheet within a workbook.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Open an existing Excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to
// the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Copy data to a new sheet from an existing
// sheet within the Workbook.
sheets.addCopy("Sheet1");

// Save the Excel file.
wb.save(path.join(dataDir, "CopyWithinWorkbook_out.xls"));
```

### **Copy Worksheets between Workbooks**

Aspose.Cells provides a method, [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-), used to copy data and formatting from a source worksheet to another worksheet within or between workbooks. The method takes the source worksheet object as a parameter.

The following example shows how to copy a worksheet from one workbook to another workbook.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Create a Workbook.
// Open a file into the first book.
const excelWorkbook0 = new AsposeCells.Workbook(inputPath);

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Copy the first sheet of the first book into second book.
excelWorkbook1.getWorksheets().get(0).copy(excelWorkbook0.getWorksheets().get(0));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xls"));
```

The following example shows how to copy a worksheet from one workbook to another.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook.
const excelWorkbook0 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws0 = excelWorkbook0.getWorksheets().get(0);

// Put some data into header rows (A1:A4)
for (let i = 0; i < 5; i++) {
ws0.getCells().get(i, 0).putValue(`Header Row ${i}`);
}

// Put some detail data (A5:A999)
for (let i = 5; i < 1000; i++) {
ws0.getCells().get(i, 0).putValue(`Detail Row ${i}`);
}

// Define a pagesetup object based on the first worksheet.
const pagesetup = ws0.getPageSetup();

// The first five rows are repeated in each page...
// It can be seen in print preview.
pagesetup.setPrintTitleRows("$1:$5");

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Name the worksheet.
ws1.setName("MySheet");

// Copy data from the first worksheet of the first workbook into the
// first worksheet of the second workbook.
ws1.copy(ws0);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetFromWorkbookToOther_out.xls"));
```

### **Move Worksheets within Workbook**

Aspose.Cells provides a method [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#moveto-number-) which is used to move a worksheet to another location in the same spreadsheet. The method takes the target worksheet index as a parameter.

The following example shows how to move a worksheet to another location within the workbook.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get the first worksheet.
const worksheet = sheets.get(0);

// Move the first sheet to the third position in the workbook.
worksheet.moveTo(2);

// Save the excel file.
wb.save(path.join(dataDir, "MoveWorksheet_out.xls"));
```
