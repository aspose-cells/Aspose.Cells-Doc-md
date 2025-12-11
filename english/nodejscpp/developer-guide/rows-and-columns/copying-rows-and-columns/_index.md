---  
title: Copying Rows and Columns with Node.js via C++  
linktitle: Copying Rows and Columns  
type: docs  
weight: 40  
url: /nodejs-cpp/copying-rows-and-columns/  
description: This article shows how to copy rows and columns through the Aspose.Cells for Node.js via C++ API.  
keywords: Node.js via C++, How to Copy Rows and Columns, Copy Rows in Node.js, Copy Columns using Node.js, How to Paste Rows and Columns using Aspose.Cells for Node.js via C++, Paste multiple rows and columns, How to Copy and paste Single Row or Column.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Introduction**  

Sometimes, you need to copy rows and columns in a worksheet without copying the entire worksheet. With Aspose.Cells, it is possible to copy rows and columns within or between workbooks.  
When a row (or column) is copied, the data contained in it, including formulas—with updated references—and values, comments, formatting, hidden cells, images, and other drawing objects are copied too.  

## **How to Copy Rows and Columns with Microsoft Excel**  

1. Select the row or column that you want to copy.  
2. To copy rows or columns, click **Copy** on the **Standard** toolbar, or press **CTRL**+**C**.  
3. Select a row or column below or to the right of where you want to copy your selection.  
4. When you are copying rows or columns, click **Copied Cells** on the **Insert** menu.  

{{% alert color="primary" %}}  
If you click **Paste** on the **Standard** toolbar or press **CTRL**+**V** instead of clicking a command on the **Insert** menu, any contents of the destination cells are replaced.  
{{% /alert %}}  

## **How to Paste Rows and Columns using Paste Options with Microsoft Excel**  

1. Select the cells that contain the data or other attributes that you want to copy.  
2. On the Home tab, click **Copy**.  
3. Click the first cell in the area where you want to **paste** what you copied.  
4. On the Home tab, click the arrow next to **Paste**, and then select **Paste Special**.  
5. Select the **options** you want.  

## **How to Copy Rows and Columns Using Aspose.Cells for Node.js via C++**  

## **How to Copy Single Rows**  

Aspose.Cells provides the [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) class. This method copies all types of data, including formulas, values, comments, cell formats, hidden cells, images, and other drawing objects, from the source row to the destination row.  

The [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) method takes the following parameters:  

- the source [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) object,  
- the source row index, and  
- the destination row index.  

Use this method to copy a row within a sheet, or to another sheet. The [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) method works in a similar way to Microsoft Excel. So, for example, you don't need to set the height of the destination row explicitly; that value is copied too.  

The following example shows how to copy a row in a worksheet. It uses a template Microsoft Excel file and copies the second row (complete with data, formatting, comments, images, and so on) and pastes it to the 12th row in the same worksheet.  

You can skip the step that gets the source row height using the [**Cells.getRowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRowHeight-number-boolean-cellsunittype-) method and then set the destination row height using the [**Cells.setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) method, as the [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) method automatically takes care of the row height.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the first worksheet in the workbook.
const wsTemplate = excelWorkbook1.getWorksheets().get(0);

// Copy the second row with data, formatting, images and drawing objects
// To the 16th row in the worksheet.
wsTemplate.getCells().copyRow(wsTemplate.getCells(), 1, 15);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
When copying rows, it is important to note related images, charts, or other drawing objects, as is the case with Microsoft Excel:  

1. If the source row index is 5, the image, chart, etc., is copied if it is contained in the three rows (the starting row index is 4 and the ending row index is 6).  
2. The existing images, charts, etc., in the destination row will not be removed.  
{{% /alert %}}  

## **How to Copy Multiple Rows**  

You can also copy multiple rows onto a new destination while using the [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) method, which takes an additional integer parameter to specify the number of source rows to be copied.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Copy the first 3 rows to 7th row
cells.copyRows(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **How to Copy Columns**  

Aspose.Cells provides the [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) class. This method copies all types of data, including formulas—with updated references—and values, comments, cell formats, hidden cells, images, and other drawing objects, from the source column to the destination column.  

The [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) method takes the following parameters:  

- the source [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) object,  
- source column index, and  
- the destination column index.  

Use the [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) method to copy a column within a sheet or to another sheet.  

This example copies a column from a worksheet and pastes it into a worksheet in another workbook.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook(filePath);

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Copy the first column from the first worksheet of the first workbook into
// the first worksheet of the second workbook.
ws1.getCells().copyColumn(ws1.getCells(), ws1.getCells().getColumns().get(0).getIndex(), ws1.getCells().getColumns().get(2).getIndex());

// Autofit the column.
ws1.autoFitColumn(2);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

## **How to Copy Multiple Columns**  

Similar to the [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) method, the Aspose.Cells APIs also provide the [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) method to copy multiple source columns to a new location.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));

// Get the first worksheet's cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Copy the first 3 columns to the 7th column
cells.copyColumns(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **How to Paste Rows and Columns with Paste Options**  

Aspose.Cells now provides [**PasteOptions**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/) while using the functions [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) and [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-). It allows you to set the appropriate paste options similar to Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeChartDataSource.xlsx"));

// Access the first sheet which contains chart
const source = workbook.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = workbook.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Set PasteOptions
const pasteOptions = new AsposeCells.PasteOptions();
pasteOptions.setPasteType(AsposeCells.PasteType.Values);
pasteOptions.setOnlyVisibleCells(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options, pasteOptions);

// Save workbook in xlsx format
workbook.save(path.join(outputDir, "outputChangeChartDataSource.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
