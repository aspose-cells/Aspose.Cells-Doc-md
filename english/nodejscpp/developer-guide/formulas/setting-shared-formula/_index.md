---
title: Setting Shared Formula with Node.js via C++
linktitle: Setting Shared Formula
type: docs
weight: 10
url: /nodejs-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

If you want to add a function in a worksheet which will do some calculations, this article explains how to achieve this task using Aspose.Cells for Node.js via C++.

{{% /alert %}}

## Setting Shared Formula using Aspose.Cells for Node.js via C++

Suppose you have a worksheet filled with data in the format that looks like the following sample worksheet.

|**Input file with one column of data**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

You want to add a function in B2 that will calculate the sales tax for the first row of data. The tax is **9%**. The formula that calculates the sales tax is: **"=A2*0.09"**. This article explains how to apply this formula with Aspose.Cells.

Aspose.Cells lets you specify a formula using the [**Cell.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) property. There are two options for adding formulas to the other cells (B3, B4, B5, and so on) in the column.

Either do what you did for the first cell, effectively setting the formula for each cell, updating the cell reference accordingly (A3*0.09, A4*0.09, A5*0.09 and so on). This requires the cell references for each row to be updated. It also requires Aspose.Cells to parse each formula individually, which can be time-consuming for large spreadsheets and complex formulas. It also adds extra lines of code although loops can cut them down somewhat.

Another approach is to use a **shared formula**. With a shared formula, the formulas are automatically updated for the cell references in each row so that the tax would be calculated properly. The [**Cell.setSharedFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setSharedFormula-string-number-number-) method is more efficient than the first method.

The following example demonstrates how to use it.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook from existing file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Get the cells collection in the first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Apply the shared formula in the range i.e.., B2:B14
cells.get("B2").setSharedFormula("=A2*0.09", 13, 1);

// Save the excel file
workbook.save(path.join(dataDir, "Output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}