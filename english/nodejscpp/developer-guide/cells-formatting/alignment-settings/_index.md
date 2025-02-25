---
title: Alignment Settings with Node.js via C++
linktitle: Alignment Settings
description: In the Aspose.Cells library, you can use cell alignment settings to adjust the layout and display of text using Node.js via C++. This document provides detailed steps and sample code for using Aspose.Cells for cell alignment settings.
keywords: Aspose.Cells, cell alignment, horizontal alignment, vertical alignment, text wrapping Node.js via C++
type: docs
weight: 20
url: /nodejs-cpp/cells-alignment-settings/
---

## **Configuring Alignment Settings**

### **Alignment settings in Microsoft Excel**

Anyone who has used Microsoft Excel to format cells will be familiar with the alignment settings in Microsoft Excel.

As you can see from the above figure, there are different kinds of alignment options:

- Text alignment(horizontal & vertical)
- Indentation.
- Orientation.
- Text control.
- Text direction.

All of these alignment settings are fully supported by Aspose.Cells and are discussed in more detail below.

### **Alignment settings in Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class.

Aspose.Cells provides [**GetStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/methods/getstyle) and [**SetStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/methods/setstyle) methods for the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class that are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) class provides useful properties for configuring alignment settings.

Select any text alignment type using the [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) enumeration. The pre-defined text alignment types in the [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) enumeration are:

|**Text Alignment Types**|**Description**|
| :- | :- |
|Bottom|Represents bottom text alignment|
|Center|Represents center text alignment|
|CenterAcross|Represents center across text alignment|
|Distributed|Represents distributed text alignment|
|Fill|Represents fill text alignment|
|General|Represents general text alignment|
|Justify|Represents justify text alignment|
|Left|Represents left text alignment|
|Right|Represents right text alignment|
|Top|Represents top text alignment|
|JustifiedLow|Aligns the text with an adjusted kashida length for Arabic text.|
|ThaiDistributed|Distributes Thai text especially, because each character is treated as a word.|

{{% alert color="primary" %}}

You can also apply the justify distributed setting using the [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/isjustifydistributed) property.

{{% /alert %}}

#### **Horizontal Alignment**

Use the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**HorizontalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/horizontalalignment) property to align the text horizontally.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the horizontal alignment of the text in the "A1" cell
const style = cell.getStyle();
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

#### **Vertical Alignment**

Similar to horizontal alignment, use the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**VerticalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/verticalalignment) property to align the text vertically.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Clearing all the worksheets
workbook.getWorksheets().clear();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the horizontal alignment of the text in the "A1" cell
const style = cell.getStyle();

// Setting the vertical alignment of the text in a cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

#### **Indentation**

It is possible to set the indentation level of the text in a cell with the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**IndentLevel**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/indentlevel) property.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the horizontal alignment of the text in the "A1" cell
const style = cell.getStyle();

// Setting the indentation level of the text (inside the cell) to 2
style.setIndentLevel(2);

cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

#### **Orientation**

Set the orientation (rotation) of the text in a cell with the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**RotationAngle**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/rotationangle) property.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the horizontal alignment of the text in the "A1" cell
const style = cell.getStyle();

// Setting the rotation of the text (inside the cell) to 25
style.setRotationAngle(25);

cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

#### **Text Control**

The following section discusses how to control text by setting text wrapping, shrink to fit and other formatting options.

##### **Wrapping Text**

Wrapping text in a cell makes it easier to read: the height of the cell adjusts to fit all the text, instead of cutting it off or spilling over into adjacent cells. Set text wrapping on or off with the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**IsTextWrapped**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/istextwrapped) property.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create Workbook Object
const wb = new AsposeCells.Workbook();

// Open first Worksheet in the workbook
const ws = wb.getWorksheets().get(0);

// Get Worksheet Cells Collection
const cell = ws.getCells();

// Increase the width of First Column Width
cell.setColumnWidth(0, 35);

// Increase the height of first row
cell.setRowHeight(0, 36);

// Add Text to the First Cell
cell.checkCell(0, 0).putValue("I am using the latest version of Aspose.Cells to test this functionality");

// Make Cell's Text wrap
const style = cell.checkCell(0, 0).getStyle();
style.setIsTextWrapped(true);
cell.checkCell(0, 0).setStyle(style);

// Save Excel File
wb.save(path.join(dataDir, "WrappingText.out.xlsx"));
```

##### **Shrinking to Fit**

An option to wrapping text in a field is to shrink the text size to fit a cell's dimensions. This is done by setting the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**IsTextWrapped**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/istextwrapped) property to **true**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the horizontal alignment of the text in the "A1" cell
const style = cell.getStyle();

// Shrinking the text to fit according to the dimensions of the cell
style.setShrinkToFit(true);

cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

##### **Merging Cells**

Like Microsoft Excel, Aspose.Cells supports merging several cells into one. Aspose.Cells provides two approaches to this task. One way is to call the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection's [**Merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/merge/index) method. The [**Merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/merge/index) method takes the following parameters to merge the cells:

- First row: the first row from where to start merging.
- First column: the first column from where to start merging.
- Number of rows: the number of rows to merge.
- Number of columns: the number of columns to merge.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

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

The other way is to first call the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection's [**CreateRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/createrange/index) method to create a range of the cells to be merged. The [**CreateRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/createrange/index) method takes the same set of parameters as that of the [**Merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/merge/index) method discussed above and returns a [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) object. The [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) object also provides a [**Merge**](https://reference.aspose.com/cells/nodejs-cpp/range/methods/merge) method that merges the range specified in the [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) object.

##### **Text Direction**

It is possible to set the reading order of text in cells. The reading order is the visual order in which characters, words, etc. are displayed. For example, English is a left to right language while Arabic is a right to left language.

The reading order is set with the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**TextDirection**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/textdirection) property. Aspose.Cells provides pre-defined text direction types in the [**TextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/textdirectiontype) enumeration.

|**Text Direction Types**|**Description**|
| :- | :- |
|Context|The reading order consistent with the language of the first entered character|
|LeftToRight|Left to right reading order|
|RightToLeft|Right to left reading order|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Instantiating a Workbook object
// Obtaining the reference of first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("I am using the latest version of Aspose.Cells to test this functionality.");

// Gets style in the "A1" cell
const style = cell.getStyle();

// Shrinking the text to fit according to the dimensions of the cell
style.setTextDirection(AsposeCells.TextDirectionType.LeftToRight);

cell.setStyle(style);
// Saving the Excel file
workbook.save("book1.xlsx");
```

## **Advance topics**
- [Change Cells Alignment and Keep Existing Formatting](/cells/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Line Breaks and Text Wrapping](/cells/nodejs-cpp/line-breaks-and-text-wrapping/)

