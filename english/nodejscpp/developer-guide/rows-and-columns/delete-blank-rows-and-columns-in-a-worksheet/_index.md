---  
title: Delete Blank Rows and Columns in a Worksheet with Node.js via C++  
linktitle: Delete Blank Rows and Columns in a Worksheet  
type: docs  
weight: 300  
url: /nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/  
description: Learn how to delete all blank rows and columns from a worksheet using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

{{% alert color="primary" %}}

It is possible to delete all blank rows and columns from a worksheet. This is useful when, for example, generating a PDF file from a Microsoft Excel file and you want to convert only rows and columns that contain data or related objects.

Use the following Aspose.Cells methods to delete empty rows and columns:

1. To delete blank rows, use the [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankRows--) method. Please note, for blank rows to be deleted, it is not only required that [**Row.isBlank()**](https://reference.aspose.com/cells/nodejs-cpp/row/#isBlank--) be true, but also that there be no visible comment defined for any cell in those rows, and no pivot table whose range intersects with them.  
2. To delete blank columns, use the [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankColumns--) method.

{{% /alert %}}

## Node.js code to delete Blank Rows

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Open an existing Excel file.
const wb = new AsposeCells.Workbook(filePath);

// Create a Worksheets object with reference to
// the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get the first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the blank rows from the worksheet
sheet.getCells().deleteBlankRows();

// Save the Excel file.
wb.save(path.join(dataDir, "mybook.out.xlsx"));
```

## Node.js code to Delete Blank Columns

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an existing Excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleInput.xlsx"));

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = workbook.getWorksheets();

// Get the first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the blank columns from the worksheet
sheet.getCells().deleteBlankColumns();

// Save the Excel file.
workbook.save(path.join(dataDir, "mybook.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
