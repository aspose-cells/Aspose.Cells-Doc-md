---
title: Copy Ranges of Excel with Node.js via C++
linktitle: Copy Ranges
type: docs
weight: 105
url: /nodejs-cpp/copy-ranges-of-Excel/
---

## **Introduction**

In Excel, you can select a range, copy the range, then paste it with specific options to the same worksheet, other worksheets or other files.

## **Copy Ranges Using Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ provides some overload [Range.copy](https://reference.aspose.com/cells/nodejs-cpp/range/#copy) methods to copy the range. And [Range.copyStyle(Range)](https://reference.aspose.com/cells/nodejs-cpp/range/#copyStyle-range-) only the copy style of the range; [Range.copyData(Range)](https://reference.aspose.com/cells/nodejs-cpp/range/#copyData-range-) only the copy value of the range.

## **Copy Range**

Creating two ranges: the source range, the target range, then copying the source range to the target range with the `Range.copy` method.

See the following code:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
let worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
let worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
let sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
let targetRange = worksheet.getCells().createRange("B1", "B2");

// Copy source range to target range in the same worksheet 
targetRange.copy(sourceRange);

// Create target range of cells.
workbook.getWorksheets().add();
worksheet = workbook.getWorksheets().get(1);

targetRange = worksheet.getCells().createRange("A1", "A2");
// Copy source range to target range in another worksheet 
targetRange.copy(sourceRange);

// Copy to another workbook
const anotherWorkbook = new AsposeCells.Workbook();

worksheet = workbook.getWorksheets().get(0);

targetRange = worksheet.getCells().createRange("A1", "A2");
// Copy source range to target range in another workbook 
targetRange.copy(sourceRange);
```

## **Paste Range With Options**

Aspose.Cells for Node.js via C++ supports pasting the range with specific types.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
const targetRange = worksheet.getCells().createRange("B1", "B2");

// Init paste options.
const options = new AsposeCells.PasteOptions();
// Set paste type.
options.setPasteType(AsposeCells.PasteType.ValuesAndFormats);
options.setSkipBlanks(true);
// Copy source range to target range
targetRange.copy(sourceRange, options);
```

## **Only Copy Data Of The Range**

Also, you can copy the data with the `Range.copyData` method as shown in the following code:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = worksheets.get(0);

// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
const targetRange = worksheet.getCells().createRange("B1", "B2");

// Copy the data of source range to target range
targetRange.copyData(sourceRange);
```

## **Advance topics**
- [Copy Row Heights of Source Range to Destination Range](/cells/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/)

