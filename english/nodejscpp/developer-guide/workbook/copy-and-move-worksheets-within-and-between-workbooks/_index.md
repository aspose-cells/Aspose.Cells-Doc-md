---
title: Copy and Move Worksheets Within and Between Workbooks with Node.js via C++
linktitle: Copy and Move Worksheets Within and Between Workbooks
type: docs
weight: 80
url: /nodejs-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Learn how to copy and move worksheets within and between workbooks using Aspose.Cells for Node.js via C++. Efficiently manage your workbook structures.
---

{{% alert color="primary" %}}

Sometimes, you do need a number of worksheets with common formatting and data entry. For example, if you work with quarterly budgets, you might want to create a workbook with sheets that contain the same column headings, row headings, and formulas. There is a way to do this: by creating one sheet and then copying it three times.

Aspose.Cells for Node.js via C++ supports copying or moving worksheets within or between workbooks. Worksheets including data, formatting, tables, matrices, charts, images, and other objects are copied with the highest degree of precision.

{{% /alert %}}

## **Copying and Moving Worksheets**

### **Copying a Worksheet within a Workbook**

The initial steps are the same for all examples.

1. Create two workbooks with some data in Microsoft Excel. For the purposes of this example, we created two new workbooks in Microsoft Excel and input some data into the worksheets.

- FirstWorkbook.xlsx (3 worksheets).
- SecondWorkbook.xlsx (1 worksheet).

1. Download and install Aspose.Cells:
   1. [Download Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).
   1. Install it on your development computer.
      All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.
1. Create a project:
   1. Start your development environment.
   1. Create a new console application.
1. Add references:
   1. Add a reference to Aspose.Cells to the project.
      For example, add a reference to ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll
1. Copy the worksheet within a workbook
   The first example copies the first worksheet (Copy) within FirstWorkbook.xlsx.

When executing the code, the worksheet named Copy is copied within FirstWorkbook.xlsx with the name Last Sheet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open a file into the first book.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "FirstWorkbook.xlsx"));

// Copy the first sheet of the first book within the workbook
excelWorkbook1.getWorksheets().get(2).copy(excelWorkbook1.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "FirstWorkbookCopied_out.xlsx"));
```

### **Moving a Worksheet within a Workbook**

The code below shows how to move a worksheet from one position in a workbook to another. Executing the code moves the worksheet called Move from index 1 to index 2 in FirstWorkbook.xlsx.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "FirstWorkbook.xlsx");
// Open a file into the first book.
const excelWorkbook2 = new AsposeCells.Workbook(filePath);

// Move the sheet
const worksheets = excelWorkbook2.getWorksheets();
const worksheet = worksheets.get(0);
worksheet.moveTo(1);

// Save the file.
excelWorkbook2.save(path.join(dataDir, "FirstWorkbookMoved_out.xlsx"));
```

### **Copying a Worksheet between Workbooks**

Executing the code copies the worksheet named Copy into SecondWorkbook.xlsx with the name Sheet2.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const excelWorkbook3 = new AsposeCells.Workbook();
const excelWorkbook4 = new AsposeCells.Workbook();

// Create source worksheet
excelWorkbook3.getWorksheets().add("Copy");

// Add new worksheet into second Workbook
excelWorkbook4.getWorksheets().add();

// Copy the first sheet of the first book into second book.
excelWorkbook4.getWorksheets().get(1).copy(excelWorkbook3.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook4.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xlsx"));
```

### **Moving a Worksheet between Workbooks**

Executing the code moves the worksheet named Move from FirstWorkbook.xlsx to SecondWorkbook.xlsx with the name Sheet3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbooks instead of opening existing files
const excelWorkbook5 = new AsposeCells.Workbook();
const excelWorkbook6 = new AsposeCells.Workbook();

// Add New Worksheet
excelWorkbook6.getWorksheets().add();

// Copy the sheet from first book into second book.
excelWorkbook6.getWorksheets().get(0).copy(excelWorkbook5.getWorksheets().get(0));

// Remove the copied worksheet from first workbook
excelWorkbook5.getWorksheets().removeAt(0);

// Save the file.
excelWorkbook5.save(path.join(dataDir, "FirstWorkbookWithMove_out.xlsx"));

// Save the file.
excelWorkbook6.save(path.join(dataDir, "SecondWorkbookWithMove_out.xlsx"));
```
