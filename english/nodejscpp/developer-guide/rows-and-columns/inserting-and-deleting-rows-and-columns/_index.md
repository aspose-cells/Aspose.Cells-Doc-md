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

Aspose.Cells for Node.js via C++ provides a class [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), which represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection that represents all cells in the worksheet.

The [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection provides several methods for managing rows and columns in a worksheet. Some of these are discussed below.

{{% alert color="primary" %}}

When rows or columns are added, the content in the worksheet is shifted down or to the right, and if rows or columns are removed, the content is shifted up or to the left.

{{% /alert %}}


## **Insert Rows and Columns**

### **How to Insert a Row**

Insert a row into the worksheet at any location by calling the [**insertRow**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/insertrow) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection. The [**insertRow**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/insertrow) method takes the index of the row where the new row will be inserted.

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

// Closing the file stream to free all resources
fstream.close();
```

### **How to Insert Multiple Rows**

To insert multiple rows into a worksheet, call the [**insertRows**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/insertrows) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection. The [**insertRows**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/insertrows) method takes two parameters:

- Row index, the index of the row from where the new rows will be inserted.
- Number of rows, the total number of rows that need to be inserted.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting 10 rows into the worksheet starting from 3rd row
worksheet.getCells().insertRows(2, 10);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```

### **How to Insert a Row with Formatting**

To insert a row with formatting options, use the [**insertRows**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/insertrows) overload that takes [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) as a parameter. Set the [**copyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions/properties/copyformattype) property of [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) class with [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions/properties/copyformattype) Enumeration. The [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions/properties/copyformattype) Enumeration has three members as listed below.

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

// Closing the file stream to free all resources
fstream.close();
```

### **How to Insert a Column**

Developers can also insert a column into the worksheet at any location by calling the [**insertColumn**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/insertcolumn) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection. The [**insertColumn**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/insertcolumn) method takes the index of the column where the new column will be inserted.

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

// Closing the file stream to free all resources
fileStream.close();
```

## **Delete Rows and Columns**

### **How to Delete Multiple Rows**

To delete multiple rows from a worksheet, call the [**deleteRows**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/deleterows) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection. The [**deleteRows**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/deleterows) method takes two parameters:

- Row index, the index of the row from where the rows will be deleted.
- Number of rows, the total number of rows that need to be deleted.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting 10 rows from the worksheet starting from 3rd row
worksheet.getCells().deleteRows(2, 10);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));

// Closing the file stream to free all resources
fstream.close();
```


### **How to Delete a Column**

To delete a column from the worksheet at any location, call the [**deleteColumn**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/deletecolumn) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection. The [**deleteColumn**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/deletecolumn) method takes the index of the column to delete.

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
