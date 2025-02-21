---
title: Get Cell String Value with and without Formatting in Node.js via C++
type: docs
weight: 240
url: /nodejs-cpp/get-cell-string-value-with-and-without-formatting/
description: Learn how to get cell string value with and without formatting through the Aspose.Cells for Node.js via C++ API.
keywords: Get Cell String Value with and without Formatting Node.js via C++, Retrieve Cell String Value with and without Formatting Node.js via C++, Obtain Cell String Value with and without Formatting Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells provides a method [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue) which can be used to get the string value of the cell with or without any formatting. Suppose, you have a cell with value 0.012345 and you have formatted it to display two decimal places only. It will then display as 0.01 in Excel. You can retrieve string values both as 0.01 and as 0.012345 using the [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue) method. It takes [**CellValueFormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy/) enum as a parameter which has the following values

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

The following sample code explains the use of [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue) method.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const cell = worksheet.getCells().get("A1");

// Put value inside the cell
cell.putValue(0.012345);

// Format the cell that it should display 0.01 instead of 0.012345
const style = cell.getStyle();
style.setNumber(2);
cell.setStyle(style);

// Get string value as Cell Style
let value = cell.getStringValue(AsposeCells.CellValueFormatStrategy.CellStyle);
console.log(value);

// Get string value without any formatting
value = cell.getStringValue(AsposeCells.CellValueFormatStrategy.None);
console.log(value);
```
