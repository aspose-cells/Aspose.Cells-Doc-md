---
title: Managing Ranges with Node.js via C++
linktitle: Ranges
type: docs
weight: 105
url: /nodejs-cpp/managing-ranges/
description: Learn how to manage ranges in Excel using Aspose.Cells for Node.js via C++. Create ranges, set values, styles, and perform various operations.
---

## **Introduction**

In Excel, you can select multiple cells with a mouse box selection; the set of selected cells is called "Range".

For example, you can click the left mouse button in Cell "A1" of Excel and then drag to cell "C4". The rectangular area you selected can also be easily created as an object by using Aspose.Cells for Node.js via C++.

Here is how to create a range, put a value, set a style, and perform more operations on the "Range" object.

## **Managing Ranges Using Aspose.Cells for Node.js via C++**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection.

### **Create Range**

When you want to create a rectangular area that extends over A1:C4, you can use the following code:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
```

### **Put value into the Cells of the Range**

Say you have a range of cells that extends over A1:C4. The matrix makes 4 * 3 = 12 cells. The individual range cells are arranged sequentially: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

The following example shows how to input some values into the cells of the Range.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "RangeValueTest.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook();
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
// Put value
range.get(0, 0).setValue("A1");
range.get(0, 1).setValue("B1");
range.get(0, 2).setValue("C1");
range.get(3, 0).setValue("A4");
range.get(3, 1).setValue("B4");
range.get(3, 2).setValue("C4");
// Save the Workbook
workbook.save(filePath);
```

### **Set style of the Cells of the Range**

The following example shows how to set the style of the cells of the Range.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Creates a Workbook
const workbook = new AsposeCells.Workbook();
// Gets Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Creates Range
const range = cells.createRange("A1:C4");
// Puts value
range.get(0, 0).setValue("A1");
range.get(3, 2).setValue("C4");
// Sets Style
let style00 = workbook.createStyle();
style00.setPattern(AsposeCells.BackgroundType.Solid);
style00.setForegroundColor(new AsposeCells.Color(255, 0, 0)); // Red
range.get(0, 0).setStyle(style00);
let style32 = workbook.createStyle();
style32.setPattern(AsposeCells.BackgroundType.HorizontalStripe);
style32.setForegroundColor(new AsposeCells.Color(0, 255, 0)); // Green
range.get(3, 2).setStyle(style32);
// Saves the Workbook
workbook.save("RangeStyleTest.xlsx");
```

### **Get CurrentRegion of the Range**

CurrentRegion is a property that returns a Range object that represents the current region. 

The current region is a range bounded by any combination of blank rows and blank columns. Read-only.

In Excel, you can get the CurrentRegion area by:
1. Select an area (range1) with the mouse box.
2. Click "Home - Editing - Find & Select - Go To Special - Current region", or use "Ctrl+Shift+*", you will see Excel automatically helps you select an area (range2). Now you made it, range2 is the CurrentRegion of range1.

Please download the following test file, open it in Excel, use the mouse box to select an area "A1:D7", then click "Ctrl+Shift+*", you will see area "A1:C3" selected.

[current_region.xlsx](current_region.xlsx)

Now please run the following example to see how it works in Aspose.Cells:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "current_region.xlsx");
// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("A1:D7");
// Get CurrentRegion
const A1C3 = src.getCurrentRegion();
```


## **Advance topics**
- [AutoFill range of Excel file](/cells/nodejs-cpp/autofill-ranges/)
- [Copy Ranges of Excel](/cells/nodejs-cpp/copy-ranges-of-Excel/)
- [Copy Range Data Only](/cells/nodejs-cpp/copy-range-data-only/)
- [Copy Range Data with Style](/cells/nodejs-cpp/copy-range-data-with-style/)
- [Copy Range Style Only](/cells/nodejs-cpp/copy-range-style-only/)
- [Create Union Range](/cells/nodejs-cpp/create-union-range/)
- [Cut and Paste Range](/cells/nodejs-cpp/cut-and-paste-cells/)
- [Delete Ranges](/cells/nodejs-cpp/delete-ranges-from-Excel/)
- [Get Address Cell Count Offset Entire Column and Entire Row of the Range](/cells/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insert Ranges](/cells/nodejs-cpp/insert-ranges-to-Excel/)
- [Merge or Unmerge Range of Cells](/cells/nodejs-cpp/merge-or-unmerge-range-of-cells/)
- [Move Range of Cells in a Worksheet](/cells/nodejs-cpp/move-range-of-cells-in-a-worksheet/)
- [Create Workbook and Worksheet Scoped Named Ranges](/cells/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Search and Replace Data in a Range](/cells/nodejs-cpp/search-and-replace-data-in-a-range/)
