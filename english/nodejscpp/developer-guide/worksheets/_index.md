---  
title: Manage Worksheets of Microsoft Excel files with Node.js via C++  
linktitle: Worksheets  
type: docs  
weight: 90  
url: /nodejs-cpp/manage-worksheets/  
description: Add, remove, and activate worksheets using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
Developers can easily create and manage worksheets in Microsoft Excel files programmatically using Aspose.Cells' flexible API. This topic describes approaches for adding and removing worksheets in Microsoft Excel files.  
{{% /alert %}}  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows access to each worksheet in the Excel file.  

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a wide range of properties and methods for managing worksheets.  

## **Adding Worksheets to a New Excel File**  

To create a new Excel file programmatically:  

1. Create an object of the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class.  
1. Call the [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#add-sheettype-) method of the [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) class. An empty worksheet is added to the Excel file automatically. It can be referenced by passing the sheet index of the new worksheet to the [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection.  
1. Obtain a worksheet reference.  
1. Perform work on the worksheets.  
1. Save the new Excel file with new worksheets by calling the [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) method of the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().getCount();
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Adding Worksheets to a Designer Spreadsheet**  

The process of adding worksheets to a designer spreadsheet is the same as that of adding a new worksheet, except that the Excel file already exists and should be opened before worksheets are added. A designer spreadsheet can be opened by the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

## **Accessing Worksheets using Sheet Name**  

Access any worksheet by specifying its name or index.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing a worksheet using its sheet name
const worksheet = workbook.getWorksheets().get("Sheet1");
const cell = worksheet.getCells().get("A1");
console.log(cell.getValue());
```  

## **Removing Worksheets using Sheet Name**  

To remove worksheets from a file, call the [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) method of the [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) class. Pass the sheet name to the [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) method to remove a specific worksheet.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Removing a worksheet using its sheet name
workbook.getWorksheets().removeAt("Sheet1");

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Removing Worksheets using Sheet Index**  

Removing worksheets by name works well when the name of the worksheet is known. If you don't know the worksheet's name, use an overloaded version of the [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) method that takes the sheet index of the worksheet instead of its sheet name.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Removing a worksheet using its sheet index
workbook.getWorksheets().removeAt(0);

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Activating Sheets and Making an Active Cell in the Worksheet**  

Sometimes, you need a specific worksheet to be active and displayed when a user opens a Microsoft Excel file in Excel. Similarly, you might want to activate a specific cell and set the scrollbars to show the active cell. Aspose.Cells is capable of doing all these tasks.  

An **active sheet** is a sheet you're working on: the active sheet's name on the tab is bold by default.  

An **active cell** is a selected cell, the cell into which data is entered when you begin typing. Only one cell is active at a time. The active cell is highlighted by a heavy border.  

### **Activating Sheets and Making a Cell Active**  

Aspose.Cells provides specific API calls for activating a sheet and a cell. For example, the [**WorksheetCollection.getActiveSheetIndex()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getActiveSheetIndex--) property is useful for setting the active sheet in a workbook. Similarly, [**Worksheet.getActiveCell()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getActiveCell--) property is used to set and get an active cell in the worksheet.  

To make sure that the horizontal or vertical scrollbars are at the row and column index position you want to show specific data, use the [**Worksheet.getFirstVisibleRow()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleRow--) and [**Worksheet.getFirstVisibleColumn()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleColumn--) properties.  

The following example shows how to activate a worksheet and make an active cell in it. In the generated output, the scrollbars will be scrolled to make the 2nd row and 2nd column as their first visible row and column.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Add a worksheet if collection is empty
const worksheets = workbook.getWorksheets();
if (worksheets.getCount() === 0) {
worksheets.add();
}

// Get the first worksheet in the workbook.
const worksheet1 = worksheets.get(0);

// Get the cells in the worksheet.
const cells = worksheet1.getCells();

// Input data into B2 cell.
cells.get(1, 1).putValue("Hello World!");

// Set the first sheet as an active sheet.
workbook.getWorksheets().setActiveSheetIndex(0);

// Set B2 cell as an active cell in the worksheet.
worksheet1.setActiveCell("B2");

// Set the B column as the first visible column in the worksheet.
worksheet1.setFirstVisibleColumn(1);

// Set the 2nd row as the first visible row in the worksheet.
worksheet1.setFirstVisibleRow(1);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Advance topics**  
- [Copying and Moving Worksheets](/cells/nodejs-cpp/copying-and-moving-worksheets/)  
- [Count number of cells in the Worksheet](/cells/nodejs-cpp/count-number-of-cells-in-the-worksheet/)  
- [Detecting Empty Worksheets](/cells/nodejs-cpp/detecting-empty-worksheets/)  
- [Find if the Worksheet is Dialog Sheet](/cells/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [Get worksheet unique id](/cells/nodejs-cpp/get-worksheet-unique-id/)  
- [Create, Manipulate or Remove Scenarios from Worksheets](/cells/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [Managing Page Breaks](/cells/nodejs-cpp/managing-page-breaks/)  
- [Page Setup Features](/cells/nodejs-cpp/page-setup-features/)   
- [Utilize Sheet.SheetId property of OpenXml using Aspose.Cells](/cells/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [Worksheet Views](/cells/nodejs-cpp/worksheet-views/)  

  
{{< app/cells/assistant language="nodejs-cpp" >}}
