---  
title: Find or Search Data with Node.js via C++  
type: docs  
weight: 50  
url: /nodejs-cpp/find-or-search-data/  
description: Learn how to find or search cells in a worksheet that contains specified data through the Aspose.Cells for Node.js via C++ API.  
keywords: Find data Node.js via C++, Search data Node.js via C++, Find Cells Containing a Formula Node.js via C++, Search Cells Containing a Formula Node.js via C++, Find Data or Formulas using FindOptions Node.js via C++, Search Data or Formulas using FindOptions Node.js via C++, Find or Search Cells Containing Specified String Value or Number Node.js via C++, Find or Search cells contains specified data  
---  

{{% alert color="primary" %}}  
Microsoft Excel allows users to find cells in a worksheet that contain specified data.  
{{% /alert %}}  

## **Finding Cells Containing Specified Data**  

### **Using Microsoft Excel**  

Microsoft Excel allows users to find cells in a worksheet that contain specified data. If you select **Edit** from the **Find** menu in Microsoft Excel, you will see a dialog where you can specify the search value.  

Here, we are looking for the value "Oranges". Aspose.Cells also allows developers to find cells in the worksheet containing specified values.  

### **Using Aspose.Cells for Node.js via C++**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection provides several methods for finding cells in a worksheet containing user-specified data. A few of these methods are discussed below in more detail.  

{{% alert color="primary" %}}  
All Find methods return the references of the cells containing the specified data to search.  
{{% /alert %}}  

## **Finding Cells Containing a Formula**  

Developers can find a specified formula in the worksheet by calling the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection's [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-object-findoptions-) method. Typically, the [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-object-findoptions-) method accepts three parameters:  

- **Object:** The object to search for. The type should be int, double, DateTime, string, bool.  
- **Previous cell:** Previous cell with the same object. This parameter can be set to null if searching from the start.  
- **FindOptions:** Options for finding the required object.  

The examples below use worksheet data for practicing find methods:  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Opening the Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleFindingCellsContainingFormula.xlsx"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Instantiate FindOptions Object
const findOptions = new AsposeCells.FindOptions();
findOptions.setLookInType(AsposeCells.LookInType.Formulas);

// Finding the cell containing the specified formula
const cell = worksheet.getCells().find("=SUM(A5:A10)", null, findOptions);

// Printing the name of the cell found after searching worksheet
console.log("Name of the cell containing formula: " + cell.getName());
```  

## **Finding Data or Formulas using FindOptions**  

It is possible to find specified values using the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection's [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-object-findoptions-) method with various [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions). Typically, the [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-object-findoptions-) method accepts the following parameters:  

- **Search value**, the data or value to be searched for.  
- **Previous cell**, the last cell that contained the same value. This parameter can be set to null when searching from the start.  
- **Find options**, the find options.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");

// Instantiate the workbook object
const workbook = new AsposeCells.Workbook(sourceDir + "sampleFindingDataOrFormulasUsingFindOptions.xlsx");

workbook.calculateFormula();

// Get Cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Instantiate FindOptions Object
const findOptions = new AsposeCells.FindOptions();

// Create a Cells Area
const ca = new AsposeCells.CellArea();
ca.setStartRow(8);
ca.setStartColumn(2);
ca.setEndRow(17);
ca.setEndColumn(13);

// Set cells area for find options
findOptions.setRange(ca);

// Set searching properties
findOptions.setSearchBackward(false);
findOptions.setSearchOrderByRows(true);

// Set the lookintype, you may specify, values, formulas, comments etc.
findOptions.setLookInType(AsposeCells.LookInType.Values);

// Set the lookattype, you may specify Match entire content, endswith, starwith etc.
findOptions.setLookAtType(AsposeCells.LookAtType.EntireContent);

// Find the cell with value
const cell = cells.find(341, null, findOptions);

if (cell !== null) {
    console.log("Name of the cell containing the value: " + cell.getName());
} else {
    console.log("Record not found ");
}
```  

## **Finding Cells Containing Specified String Value or Number**  

It is possible to find specified string values by calling the same [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-object-findoptions-) method found in the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection with various [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions).  

Specify the [**FindOptions.LookInType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#lookintype) and [**FindOptions.LookAtType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#lookattype) properties. The following example code illustrates how to use these properties to find cells with various number of strings at the **beginning** or at the **center** or at the **end** of the cell's string.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate the workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get Cells collection
const cells = workbook.getWorksheets().get(0).getCells();

const opts = new AsposeCells.FindOptions();
opts.setLookInType(AsposeCells.LookInType.Values);
opts.setLookAtType(AsposeCells.LookAtType.EntireContent);

// Find the cell with the input integer or double
let cell1 = cells.find(205, null, opts);

if (cell1 !== null) {
    console.log("Name of the cell containing the value: " + cell1.getName());
} else {
    console.log("Record not found ");
}

// Find the cell with the input string
let cell2 = cells.find("Items A", null, opts);

if (cell2 !== null) {
    console.log("Name of the cell containing the value: " + cell2.getName());
} else {
    console.log("Record not found ");
}

// Find the cell containing the input string
opts.setLookAtType(AsposeCells.LookAtType.Contains);
let cell3 = cells.find("Data", null, opts);

if (cell3 !== null) {
    console.log("Name of the cell containing the value: " + cell3.getName());
} else {
    console.log("Record not found ");
}
```  

## **Advance topics**  
- [Find Cells with Specific Style](https://reference.aspose.com/cells/nodejs-cpp/find-cells-with-specific-style/)  
- [Find if the cell value starts with single quote mark](https://reference.aspose.com/cells/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Search Data using Original Values](https://reference.aspose.com/cells/nodejs-cpp/search-data-using-original-values/)  
  