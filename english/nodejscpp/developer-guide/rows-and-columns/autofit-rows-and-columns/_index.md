---  
title: AutoFit Rows and Columns with Node.js via C++  
linktitle: AutoFit Rows and Columns  
type: docs  
weight: 20  
url: /nodejs-cpp/autofit-rows-and-columns/  
description: This article shows how to autoFit rows, columns, rows of merged cells, and row in a range of cells using Aspose.Cells for Node.js via C++.  
keywords: Autofit rows Node.js via C++, autofit columns Node.js via C++, autofit row in a range of cells Node.js via C++, autofit rows of merged cells Node.js via C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel lets users auto-size the width and height of cells according to their content. This feature is also available through Aspose.Cells for Node.js via C++, so developers can auto-size the dimensions of a cell at runtime.  
{{% /alert %}}  

## **Auto Fitting**  

Aspose.Cells provides a [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a wide range of properties and methods for managing a worksheet. This article looks at using the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class to autofit rows or columns.  

### **AutoFit Row - Simple**  

The most straightforward approach to auto-sizing the width and height of a row is to call the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) method. The [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) method takes a row index (of the row to be resized) as a parameter.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileBuffer = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1);

// Saving the modified Excel file
const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath);
```  

### **How to AutoFit Row in a Range of Cells**  

A row is composed of many columns. Aspose.Cells allows developers to auto-fit a row based on the content in a range of cells within the row by calling an overloaded version of the [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-) method. It takes the following parameters:  

- **Row index**, the index of the row about to be auto-fitted.  
- **First column index**, the index of the row's first column.  
- **Last column index**, the index of the row's last column.  

The [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-) method checks the contents of all the columns in the row and then auto-fits the row.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileData = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1, 0, 5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **How to AutoFit Column in a Range of Cells**  

A column is composed of many rows. It is possible to auto-fit a column based on the content in a range of cells in the column by calling an overloaded version of [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) method that takes the following parameters:  

- **Column index**, the index of the column about to be auto-fitted.  
- **First row index**, the index of the column's first row.  
- **Last row index**, the index of the column's last row.  

The [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) method checks the contents of all rows in the column and then auto-fits the column.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const workbook = new AsposeCells.Workbook(fs.readFileSync(inputPath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the Column of the worksheet
worksheet.autoFitColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **How to AutoFit Rows for Merged Cells**  

With Aspose.Cells, it is possible to autofit rows even for cells that have been merged using the [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) API. The [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) class provides [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) property that can be used to autofit rows for merged cells. [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) accepts [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype) enumerable which has the following members.  

- None: Ignore merged cells.  
- FirstLine: Only expands the height of the first row.  
- LastLine: Only expands the height of the last row.  
- EachLine: Only expands the height of each row.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first (default) worksheet
const worksheet = wb.getWorksheets().get(0);

// Create a range A1:B1
const range = worksheet.getCells().createRange(0, 0, 1, 2);

// Merge the cells
range.merge();

// Insert value to the merged cell A1
worksheet.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style = worksheet.getCells().get(0, 0).getStyle();

// Set wrapping text on
style.setIsTextWrapped(true);

// Apply the style to the cell
worksheet.getCells().get(0, 0).setStyle(style);

// Create an object for AutoFitterOptions
const options = new AsposeCells.AutoFitterOptions();

// Set auto-fit for merged cells
options.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.EachLine);

// Autofit rows in the sheet (including the merged cells)
worksheet.autoFitRows(options);

// Save the Excel file
wb.save(path.join(outputDir, "AutofitRowsforMergedCells.xlsx"));
```  

{{% alert color="primary" %}}  
You may also try to use the overloaded versions of [**autoFitRows**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) & [**autoFitColumns**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) methods accepting a range of rows/columns and an instance of [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) to auto-fit the selected rows/columns with your desired [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) accordingly.  

The signatures of the aforesaid methods are as follows:  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **Important to Know**  

{{% alert color="primary" %}}  
If a cell is merged then the autoFit methods will not be applied, which is the same behavior as in Microsoft Excel. You can get around this by using the autofilter API. Moreover, if the text in a cell is wrapped, the [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) method will not be applied either. Another thing you need to know is that the *autoFit* methods are time-consuming. So, you should call these methods as seldom as possible to ensure the efficiency of your application.  
{{% /alert %}}  

## **Advance topics**  
- [AutoFit Rows for Merged Cells](/cells/nodejs-cpp/autofit-rows-for-merged-cells/)  
  
{{< app/cells/assistant language="nodejs-cpp" >}}