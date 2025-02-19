---
title: Get Validation Applied on a Cell with Node.js via C++
type: docs
weight: 200
url: /nodejs-cpp/get-validation-applied-on-a-cell/
description: This article shows how to apply validation on a Cell with Node.js via C++.
keywords: apply cell validation in excel with Node.js via C++, apply validation on a cell in excel with Node.js via C++, apply validation in excel with Node.js via C++, cell validation in excel with Node.js via C++, Node.js via C++ apply cell validation in excel, Node.js via C++ apply validation on a cell in excel, Node.js via C++ cell validation in excel
---

{{% alert color="primary" %}}

You can use Aspose.Cells for Node.js to get the validation applied to a cell. Aspose.Cells provides the [**Cell.getValidation()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidation) method for this purpose. If there is no validation applied on the cell, it returns null.

Similarly, you can use [**Worksheet.validations.getValidationInCell**](https://reference.aspose.com/cells/nodejs-cpp/validationcollection/#getValidationInCell-number-number-) method to acquire the validation applied to a cell by providing its row and column indices.

{{% /alert %}}

## Node.js code to get the validation applied on a Cell

Below code sample shows you how to get validation applied on a cell.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate the workbook from sample Excel file
const workbook = new AsposeCells.Workbook(dataDir + "sample.xlsx");

// Access its first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Cell C1 has the Decimal Validation applied on it. It can take only the values Between 10 and 20
const cell = worksheet.getCells().get("C1");

// Access the validation applied on this cell
const validation = cell.getValidation();

// Read various properties of the validation
console.log("Reading Properties of Validation");
console.log("--------------------------------");
console.log("Type: " + validation.getType());
console.log("Operator: " + validation.getOperator());
console.log("Formula1: " + validation.getFormula1());
console.log("Formula2: " + validation.getFormula2());
console.log("Ignore blank: " + validation.getIgnoreBlank());
```

## Related Articles

- [Data Validation](/cells/nodejs-cpp/data-validation/)
