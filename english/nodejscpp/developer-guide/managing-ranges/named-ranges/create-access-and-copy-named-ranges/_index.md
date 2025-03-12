---  
title: Create Access and Copy Named Ranges with Node.js via C++  
linktitle: Create Access and Copy Named Ranges  
type: docs  
weight: 200  
url: /nodejs-cpp/create-access-and-copy-named-ranges/  
description: Learn how to create, access, and copy named ranges in Excel using Aspose.Cells for Node.js via C++.  
---  

## **Introduction**  

Normally, column and row labels are used to refer to individual cells. It is possible to create descriptive names to represent cells, ranges of cells, formulas, or constant values. The word **name** may refer to a string of characters that represents a cell, range of cells, formula, or constant value. Assigning a name to a range means that range of cells can be referred to by its name. Use easy-to-understand names, such as Products, to refer to hard-to-understand ranges, such as Sales!C20:C30. Labels can be used in formulas that refer to data on the same worksheet; if you want to represent a range on another worksheet, you may use a name. *Named ranges are among the most powerful features of Microsoft Excel, especially when used as the source range for list controls, pivot tables, charts, and so on.*  

## **Working with Named Range Using Microsoft Excel**  

### **Create Named Ranges**  

The following steps describe how to name a cell or range of cells using **MS Excel**. This method applies to **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000**, and **2002**.  

1. Select the cell or range of cells that you want to name.  
2. Click the **Name Box** at the left end of the formula bar.  
3. Type the name for the cells.  
4. Press ENTER.  

{{% alert color="primary" %}}  
You cannot name a cell while you are changing the contents of the cell.  
{{% /alert %}}  

## **Working with Named Range Using Aspose.Cells**  

Here, we use the Aspose.Cells API to do the task.  
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection.  

### **Create Named Range**  

It is possible to create a named range by calling the overloaded [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection. A typical version of [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) method takes the following parameters:  

- Name of the upper left cell, the name of the top left cell in the range.  
- Name of the lower right cell, the name of the bottom right cell in the range.  

When the [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) method is called, it returns the newly created range as an instance of the [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) class. Use this [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) object to configure the named range. For example, set the name of the range using the [**getName()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getName--) property. The following example shows how to create a named range of cells that extends over B4:G14.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating a named range
const range = worksheet.getCells().createRange("B4", "G14");

// Setting the name of the named range
range.setName("TestRange");

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Input Data into the Cells in the Named Range**  

You can insert data into the individual cells of a range following the pattern  

- **JavaScript**: Range[row,column]  

Say you have a named range of cells that spans A1:C4. The matrix makes 4 * 3 = 12 cells. The individual range cells are arranged sequentially: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

Use the following properties to identify the cells in the range:  

- firstRow returns the index of the first row in the named range.  
- firstColumn returns the index of the first column in the named range.  
- rowCount returns the total number of rows in the named range.  
- columnCount returns the total number of columns in the named range.  

The following example shows how to input some values into the cells of a specified range.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir);
}

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet in the workbook.
const worksheet1 = workbook.getWorksheets().get(0);

// Create a range of cells based on H1:J4.
const range = worksheet1.getCells().createRange("H1", "J4");

// Name the range.
range.setName("MyRange");

// Input some data into cells in the range.
range.get(0, 0).setValue("USA");
range.get(0, 1).setValue("SA");
range.get(0, 2).setValue("Israel");
range.get(1, 0).setValue("UK");
range.get(1, 1).setValue("AUS");
range.get(1, 2).setValue("Canada");
range.get(2, 0).setValue("France");
range.get(2, 1).setValue("India");
range.get(2, 2).setValue("Egypt");
range.get(3, 0).setValue("China");
range.get(3, 1).setValue("Philipine");
range.get(3, 2).setValue("Brazil");

// Save the excel file.
workbook.save(path.join(dataDir, "rangecells.out.xls"));
```  

### **Identify Cells in the Named Range**  

You can insert data into the individual cells of a range following the pattern:  

- **JavaScript**: Range[row,column]  

If you have a named range that spans A1:C4. The matrix makes 4 * 3 = 12 cells. The individual range cells are arranged sequentially: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

Use the following properties to identify the cells in the range:  

- firstRow returns the index of the first row in the named range.  
- firstColumn returns the index of the first column in the named range.  
- rowCount returns the total number of rows in the named range.  
- columnCount returns the total number of columns in the named range.  

The following example shows how to input some values into the cells of a specified range.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

// Identify range cells.
console.log("First Row : " + range.getFirstRow());
console.log("First Column : " + range.getFirstColumn());
console.log("Row Count : " + range.getRowCount());
console.log("Column Count : " + range.getColumnCount());
```  

### **Access Named Ranges**  

#### **Access a Specific Named Range**  

Call the [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) collection's [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) method to get a range by the specified name. A typical [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) method takes the name of the named range and returns the specified named range as an instance of the [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) class. The following example shows how to access a specified range by its name.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

if (range !== null) {
    console.log("Named Range : " + range.getRefersTo());
}
```  

#### **Access All the Named Ranges in a Spreadsheet**  

Call the [**worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) collection's [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) method to get all named ranges in a spreadsheet. The [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) method returns an array of all named ranges in the [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) collection.  

The following example shows how to access all the named ranges in a workbook.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting all named ranges
const ranges = workbook.getWorksheets().getNamedRanges();

if (ranges != null) {
    console.log("Total Number of Named Ranges: " + ranges.length);
}
```  

### **Copy Named Ranges**  

Aspose.Cells provides [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-) method to copy a range of cells with formatting into another range.  

The following example shows how to copy a source range of cells to another named range.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const range1 = worksheet.getCells().createRange("E12", "I12");

// Name the range.
range1.setName("MyRange");

// Set the outline border to the range.
range1.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));

// Input some data with some formattings into
// A few cells in the range.
range1.get(0, 0).putValue("Test");
range1.get(0, 4).putValue("123");

// Create another range of cells.
const range2 = worksheet.getCells().createRange("B3", "F3");

// Name the range.
range2.setName("testrange");

// Copy the first range into second range.
range2.copy(range1);

// Save the excel file.
workbook.save(path.join(dataDir, "copyranges.out.xls"));
```  
  