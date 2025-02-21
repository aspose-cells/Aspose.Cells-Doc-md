---
title: Get Text Width of Cell Value with Node.js via C++
type: docs
weight: 50
url: /nodejs-cpp/get-text-width-of-cell-value/
description: Learn how to Get Text Width of Cell Value through Aspose.Cells for Node.js via C++ API.
keywords: Get Text Width of Cell Value Node.js via C++, Obtain Text Width of Cell Value Node.js via C++
---

## **Get Text Width of Cell Value**

Sometimes, developers might need to calculate the width of the cell's value for arranging data in some layout. Aspose.Cells for Node.js via C++ provides the [**CellsHelper.getTextWidth**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getTextWidth-string-number-) method, which allows developers to get the text width of the cell's value. The following sample code illustrates how to use [**CellsHelper.getTextWidth**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getTextWidth-string-number-) to access the text width of the cell's value.

The Source file used in the following code snippet is attached for your reference.

[Source File](96928090.xlsx)

## Sample Code

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
let workbook = new AsposeCells.Workbook(sourceDir + "GetTextWidthSample.xlsx");

console.log("Text width: " + AsposeCells.CellsHelper.getTextWidth(workbook.getWorksheets().get(0).getCells().get("A1").getStringValue(), workbook.getDefaultStyle().getFont(), 1));
```
