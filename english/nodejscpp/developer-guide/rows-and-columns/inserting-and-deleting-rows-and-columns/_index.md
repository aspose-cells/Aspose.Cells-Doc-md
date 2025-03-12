---
title: Inserting and Deleting Rows and Columns of Excel file
linktitle: Inserting and Deleting Rows and Columns
type: docs
weight: 70
url: /nodejs-cpp/inserting-and-deleting-rows-and-columns/
description: This article shows how to insert and delete rows and columns by the Aspose.Cells for Node.js via C++ API.
keywords: Aspose.Cells Node.js via C++ manage rows and columns, insert rows and columns, delete rows and columns
---

## **Introduction**

Whether creating a new worksheet from scratch or working on an existing worksheet, we may need to add extra rows or columns to accommodate more data. Inversely, we may also need to delete rows or columns from specified positions in the worksheet. 
To fulfill these requirements, Aspose.Cells for Node.js via C++ provides a very simplest set of classes and methods, discussed below.

### **Manage Rows and Columns**

Aspose.Cells for Node.js via C++ provides a class [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), which represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection that represents all cells in the worksheet.

The [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection provides several methods for managing rows and columns in a worksheet. Some of these are discussed below.

{{% alert color="primary" %}}

When rows or columns are added, the content in the worksheet is shifted down or to the right, and if rows or columns are removed, the content is shifted up or to the left.

{{% /alert %}}


## **Insert Rows and Columns**

### **How to Insert a Row**

Insert a row into the worksheet at any location by calling the [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) method of the [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection. The [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) method takes the index of the row where the new row will be inserted.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRow(2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

### **How to Insert Multiple Rows**

To insert multiple rows into a worksheet, call the [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) method of the [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection. The [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) method takes two parameters:

- Row index, the index of the row from where the new rows will be inserted.
- Number of rows, the total number of rows that need to be inserted.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileData = fs.readFileSync(filePath);
const workbook = new AsposeCells.Workbook(fileData);

const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().insertRows(2, 10);

workbook.save(path.join(dataDir, "output.out.xls"));
```

### **How to Insert a Row with Formatting**

To insert a row with formatting options, use the [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) overload that takes [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) as a parameter. Set the [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) property of [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) class with [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) Enumeration. The [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) Enumeration has three members as listed below.

- SameAsAbove: Formats the row same as the above row.
- SameAsBelow:  Formats the row same as below row.
- Clear: Clears the formatting.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting Formatting options
const insertOptions = new AsposeCells.InsertOptions();
insertOptions.setCopyFormatType(AsposeCells.CopyFormatType.SameAsAbove);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2, 1, insertOptions);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "InsertingARowWithFormatting.out.xls"));
```

### **How to Insert a Column**

Developers can also insert a column into the worksheet at any location by calling the [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) method of the [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection. The [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) method takes the index of the column where the new column will be inserted.

```javascript
const fs = require('fs');
const path = require('path');
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fileStream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fileStream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a column into the worksheet at 2nd position
worksheet.getCells().insertColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Delete Rows and Columns**

### **How to Delete Multiple Rows**

To delete multiple rows from a worksheet, call the [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) method of the [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection. The [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) method takes two parameters:

- Row index, the index of the row from where the rows will be deleted.
- Number of rows, the total number of rows that need to be deleted.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Read file contents as Uint8Array
const fileContent = fs.readFileSync(filePath);
const fileBuffer = new Uint8Array(fileContent);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting 10 rows from the worksheet starting from 3rd row
worksheet.getCells().deleteRows(2, 10);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```


### **How to Delete a Column**

To delete a column from the worksheet at any location, call the [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) method of the [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection. The [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) method takes the index of the column to delete.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting a column from the worksheet at 5th position
worksheet.getCells().deleteColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));

// Closing resources is handled automatically by Node.js, no specific close needed.
```
