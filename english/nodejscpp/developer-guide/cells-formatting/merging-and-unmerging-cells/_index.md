---
title: Merging and Unmerging Cells with Node.js via C++
linktitle: Merging and Unmerging Cells
description: Aspose.Cells is a Node.js library for working with spreadsheet files, which supports merging and unmerging cells. This article will introduce how to merge and unmerge cells using the Aspose.Cells library, with options for customizing the merged cell style.
keywords: Aspose.Cells, Node.js library, spreadsheet, merge cells, unmerge cells, style settings, custom styles
type: docs
weight: 190
url: /nodejs-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells supports this feature and can also merge cells in a worksheet. You may unmerge, or split, the merged cells too. A merged cell's cell reference is the reference for the top left cell in the original selected range.

{{% /alert %}} 
## **Introduction**
You don't always want the same number of cells in every row or column. For example, you might want to put a title in a cell that spans several columns. Or, if creating an invoice, you might want fewer columns for the total. To make one cell from two or more cells, merge them. Microsoft Excel lets users select files and merge them to structure the spreadsheet the way they want.

{{% alert color="primary" %}} 

Note that when cells are merged, only the data in the top left cells is retained. If there is data in the other cells in the range, this data is deleted. Formatting, likewise, is based on the reference cell so that when you merge cells, the formatting settings of the top left cell in the range are applied on the merged cell. When the cell is split, the new cells keep their original format settings.

{{% /alert %}} 
## **Merging Cells in a Worksheet**
### **Merging Cells in Microsoft Excel**
The following steps describe how to merge cells in the worksheet using MS Excel.

1. Copy the data you want into the upper-leftmost cell within the range.
1. Select the cells you want to merge.
1. To merge cells in a row or column and center the cell contents, click **Merge and Center** icon on the **Formatting** toolbar.

### **Merging Cells with Aspose.Cells**
The Aspose.Cells.Cells Class has some useful methods for the task. For example, the method `merge()` merges the cells into a single cell within a specified range.

The following example shows how to merge cells (C6:E7) in a worksheet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
const wbk = new AsposeCells.Workbook();

// Create a Worksheet and get the first sheet.
const worksheet = wbk.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Merge some Cells (C6:E7) into a single C6 Cell.
cells.merge(5, 2, 2, 3);

// Input data into C6 Cell.
cells.get(5, 2).putValue("This is my value");

// Create a Style object to fetch the Style of C6 Cell.
const style = cells.get(5, 2).getStyle();

// Create a Font object
const font = style.getFont();

// Set the name.
font.setName("Times New Roman");

// Set the font size.
font.setSize(18);

// Set the font color
font.setColor(AsposeCells.Color.Blue);

// Bold the text
font.setIsBold(true);

// Make it italic
font.setIsItalic(true);

// Set the background color of C6 Cell to Red
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Apply the Style to C6 Cell.
cells.get(5, 2).setStyle(style);

// Save the Workbook.
wbk.save(path.join(dataDir, "mergingcells.out.xls"));
```

## **Unmerging (Splitting) Merged Cells**
### **Using Microsoft Excel**
The following steps describe how to split merged cells using Microsoft Excel.

1. Select the merged cell.
   When cells have been combined, **Merge and Center** is selected on the **Formatting** toolbar.
1. Click **Merge and Center** on the **Formatting** toolbar.

### **Using Aspose.Cells**
The class Aspose.Cells.Cells has a method named `unmerge()` that splits the cells into their original state. The method unmerges the cells using the cell's reference in the merged cell range.

The following example shows how to split the merged cells (C6). The example uses the file created in the previous example and splits the merged cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
// Open the excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "mergingcells.xls"));

// Create a Worksheet and get the first sheet.
const worksheet = workbook.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Unmerge the cells.
cells.unMerge(5, 2, 2, 3);

// Save the file.
workbook.save(path.join(dataDir, "unmergingcells.out.xls"));
```

## **Advance topics**
- [Detect Merged Cells in a Worksheet](/cells/nodejs-cpp/detect-merged-cells-in-a-worksheet/)
