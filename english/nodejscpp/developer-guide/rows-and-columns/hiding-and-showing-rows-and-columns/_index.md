---
title: Hiding and Showing Rows and Columns with Node.js via C++
linktitle: Hiding and Showing Rows and Columns
type: docs
weight: 60
url: /nodejs-cpp/hiding-and-showing-rows-and-columns/
description: Learn how to hide and show rows and columns in a worksheet using Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, it makes sense to hide certain rows or columns in a worksheet and display them later. Microsoft Excel provides this feature and so does Aspose.Cells.

{{% /alert %}}

## **Controlling the Visibility of Rows and Columns**

Aspose.Cells for Node.js via C++ provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection provides several methods for managing rows or columns in a worksheet. A few of these are discussed below.

### **Hiding Rows and Columns**

Developers can hide a row or column by calling the [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) and [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) methods of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection respectively. Both methods take the row and column index as a parameter to hide the specific row or column.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with Uint8Array
const workbook = new AsposeCells.Workbook(new Uint8Array(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the 3rd row of the worksheet
worksheet.getCells().hideRow(2);

// Hiding the 2nd column of the worksheet
worksheet.getCells().hideColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

{{% alert color="primary" %}}

It is also possible to hide a row or column by setting the row height or column width to 0 respectively.

{{% /alert %}}

### **Showing Rows and Columns**

Developers can show any hidden row or column by calling the [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) and [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) methods of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection respectively. Both methods take two parameters:

- **Row or column index** - the index of a row or column that is used to show the specific row or column.
- **Row height or column width** - the row height or column width assigned to the row or column after unhiding.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Read the Excel file into a Buffer (Uint8Array)
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

{{% alert color="primary" %}}

While making a hidden column visible, if you need to restore it to previously assigned width or to its original width, please unhide the column with a negative width. For example: worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **Hiding Multiple Rows and Columns**

Developers can hide multiple rows or columns at once by calling the [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) and [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) methods of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection respectively. Both methods take the starting row or column index and the number of rows or columns that should be hidden as parameters.

```javascript
const fs = require("fs");
const path = require("path");
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

// Hiding 3, 4, and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));
```

{{% alert color="primary" %}}

It is also possible to use the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) class' [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) and [**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) methods to make multiple rows and columns visible.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
