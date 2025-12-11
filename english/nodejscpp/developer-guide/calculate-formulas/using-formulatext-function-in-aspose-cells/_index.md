---
title: Using FormulaText function in Aspose.Cells for Node.js via C++
linktitle: Using FormulaText function in Aspose.Cells
description: This article introduces how to use the FormulaText function in Aspose.Cells library to process formulas in Microsoft Excel. Learn to get and set the formula text of cells and save modified Excel files using Node.js via C++.
keywords: Aspose.Cells, Excel, FormulaText functions Node.js via C++
type: docs
weight: 60
url: /nodejs-cpp/using-formulatext-function-in-aspose-cells/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

FormulaText is an Excel 2013 and later function. It is not supported by previous versions like Excel 2010 or 2007, etc. As its name suggests, it prints the text of the formula which is present in a given cell. This article will show you how to make use of this function using Aspose.Cells for Node.js via C++.

{{% /alert %}} 

The following sample code shows the usage of FormulaText with Aspose.Cells for Node.js via C++. The code first writes a formula in cell A1 and then prints the text of the formula using FormulaText in cell A2.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create a workbook object
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put a formula in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.setFormula("=Sum(B1:B10)");

// Get the text of the formula in cell A2 using FORMULATEXT function
const cellA2 = worksheet.getCells().get("A2");
cellA2.setFormula("=FormulaText(A1)");

// Calculate the workbook
workbook.calculateFormula();

// Print the result of A2; it will now print the text of the formula inside cell A1
console.log(cellA2.getStringValue());
```
## **Console Output**
Here is the console output of the above sample code.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
