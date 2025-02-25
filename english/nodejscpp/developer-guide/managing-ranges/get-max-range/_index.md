---  
title: Get Max Range In A Worksheet with Node.js via C++  
linktitle: Get Max Range In A Worksheet  
type: docs  
weight: 360  
url: /nodejs-cpp/get-max-range-in-a-worksheet/  
description: This article describes how to get the max range, max data range, and max display range of Excel files using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

When reading data from the worksheet, we need to know the maximum area.  

When copying all data from a worksheet, we need to know the maximum area.  

When exporting a specified area to HTML and PDF, we need to know the maximum area.  

Aspose.Cells for Node.js via C++ contains different ways to find the max range in a worksheet.  

{{% /alert %}}  

## **Getting max range**  
In Aspose.Cells, if the [**row**](https://reference.aspose.com/cells/nodejs-cpp/row/) and [**column**](https://reference.aspose.com/cells/nodejs-cpp/column/) objects are initialized, these rows and columns will be counted to the maximum area, even if there is no data in empty rows or columns.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxRow();
let maxColumn = sheet.getCells().getMaxColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxRow();
maxColumn = sheet.getCells().getMaxColumn();
// The range is updated to A1:B10.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **Getting max data range**  
In most cases, we only need to obtain all the ranges containing all the data, even if the empty cells outside the range are formatted.  
And the settings about shapes, tables, and pivot tables will be ignored.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxDataRow();
let maxColumn = sheet.getCells().getMaxDataColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxDataRow();
maxColumn = sheet.getCells().getMaxDataColumn();
// The range is still A1:B3.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **Getting max display range**  
When we export all data from the worksheet to HTML, PDF, or images, we need to obtain an area containing all visible objects, including data, styles, graphics, tables, and pivot tables.  
The following codes show how to render the max display range to HTML:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Gets the max display range.
const range = worksheets.get(0).getCells().getMaxDisplayRange();

// Save the range to html
const saveOptions = new AsposeCells.HtmlSaveOptions();
saveOptions.setExportActiveWorksheetOnly(true);
saveOptions.setExportArea(AsposeCells.CellArea.createCellArea(range.getFirstRow(), range.getFirstColumn(), range.getFirstRow() + range.getRowCount() - 1, range.getFirstColumn() + range.getColumnCount() - 1));

// Save the range.
workbook.save("html.html", saveOptions);
```  

Here is [source excel file](Book1.xlsx).  
  