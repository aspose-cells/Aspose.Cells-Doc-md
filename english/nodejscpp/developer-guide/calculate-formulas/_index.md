---
title: Calculate Formulas with Node.js via C++
linktitle: Calculate Formulas
description: This article introduces how to use Aspose.Cells library to calculate formulas in Microsoft Excel using Node.js via C++. By loading an existing Excel file or creating a new Excel file, we can use the methods provided by Aspose.Cells to calculate the formula and get the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, formulas, calculations, Direct Calculation of Formula, Calculate Formulas repeatedly, add formulas Node.js via C++
type: docs
weight: 125
url: /nodejs-cpp/calculate-formulas/
---

## **Adding Formulas & Calculating Results**

Aspose.Cells has an embedded formula calculation engine. Not only can it re-calculate formulas imported from designer templates, but it also supports calculating the results of formulas added at runtime.

Aspose.Cells supports most of the formulas or functions that are part of Microsoft Excel (Read [a list of the functions supported by the calculation engine](/cells/nodejs-cpp/supported-formula-functions/)). Those functions can be used through the APIs or designer spreadsheets. Aspose.Cells supports a huge set of mathematical, string, boolean, date/time, statistical, database, lookup, and reference formulas.

Use the [**Formula**](https://reference.aspose.com/cells/nodejs-cpp/cell/properties/formula) property or [**setFormula(...)**](https://reference.aspose.com/cells/nodejs-cpp/cell/setFormula/methods/2) methods of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class to add a formula to a cell. When applying a formula, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel and use a comma (,) to delimit function parameters.

To calculate the results of formulas, the user may call the [**calculateFormula**](https://reference.aspose.com/cells/nodejs-cpp/workbook/calculateFormula/methods/1) method of the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class which processes all formulas embedded in an Excel file. Or, the user may call the [**calculateFormula**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/methods/calculateFormula) method of the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class which processes all formulas embedded in a sheet. Or, the user may also call the [**calculate**](https://reference.aspose.com/cells/nodejs-cpp/cell/methods/calculate) method of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class which processes the formula of one Cell:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A4").setFormula("=SUM(A1:A3)");

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A4").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Important to Know for Formulas**

{{% alert color="primary" %}}

The **Formula** property and **setFormula(...)** methods of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class work differently from the **calculate** methods of the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet), and [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) classes. The **Formula** property and **setFormula(...)** methods simply add the formula to a cell but do not calculate the result at runtime. To get the result of the formulas, please call **calculate** methods.

{{% /alert %}}

## **Direct Calculation of Formula**

Aspose.Cells has an embedded formula calculation engine. As well as calculating formulas imported from a designer file, Aspose.Cells can calculate formula results directly.

Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet, and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Aspose.Cells' formula calculation engine APIs for [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) to [**calculate**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/calculateFormula/methods/3) the results of such formulas without adding them to the worksheet:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put 20 in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.putValue(20);

// Put 30 in cell A2
const cellA2 = worksheet.getCells().get("A2");
cellA2.putValue(30);

// Calculate the Sum of A1 and A2
const results = worksheet.calculateFormula("=Sum(A1:A2)");

// Print the output
console.log("Value of A1: " + cellA1.getStringValue());
console.log("Value of A2: " + cellA2.getStringValue());
console.log("Result of Sum(A1:A2): " + results.toString());
```

Above code produces the following output:
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **How to Calculate Formulas repeatedly**

When there are lots of formulas in the workbook, and the user needs to calculate them repeatedly while modifying only a small part of them, it may be helpful for performance to enable the formula calculation chain: [**formulaSettings.enableCalculationChain**](https://reference.aspose.com/cells/nodejs-cpp/formulaSettings/properties/enableCalculationChain).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load the template workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Print the time before formula calculation
console.log(new Date());

// Set the CreateCalcChain as true
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);

// Calculate the workbook formulas
workbook.calculateFormula();

// Print the time after formula calculation
console.log(new Date());

// Change the value of one cell
workbook.getWorksheets().get(0).getCells().get("A1").putValue("newvalue");

// Re-calculate those formulas which depend on cell A1
workbook.calculateFormula();
```

### **Important to Know**

{{% alert color="primary" %}}

By default, the calculation chain is disabled. Because creating the chain also needs extra time, the first time of calculating formulas ([**Workbook.calculateFormula(...)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/calculateFormula/methods/1)) may consume more CPU processing time and memory when compared with calculating formulas without a chain. If the user does not need to calculate formulas repeatedly, the default behavior (calculating the formula directly without creating a calculation chain) should be the better way.

{{% /alert %}}

## **Advance topics**
- [Add Cells to Microsoft Excel Formula Watch Window](/cells/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calculating IFNA function using Aspose.Cells](/cells/nodejs-cpp/calculating-ifna-function-using-aspose-cells/)
- [Calculation of Array Formula of Data Tables](/cells/nodejs-cpp/calculation-of-array-formula-of-data-tables/)
- [Calculation of Excel 2016 MINIFS and MAXIFS functions](/cells/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Decrease the Calculation Time of Cell.calculate method](/cells/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Detecting Circular Reference](/cells/nodejs-cpp/detecting-circular-reference/)
- [Direct calculation of custom function without writing it in a worksheet](/cells/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells](/cells/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrupt or Cancel the Formula Calculation of Workbook](/cells/nodejs-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Returning a Range of Values using AbstractCalculationEngine](/cells/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Returning a Range of Values using ICustomFunction](/cells/nodejs-cpp/returning-a-range-of-values-using-icustomfunction/)
- [Setting Formula Calculation Mode of Workbook](/cells/nodejs-cpp/setting-formula-calculation-mode-of-workbook/)
- [Using FormulaText function in Aspose.Cells](/cells/nodejs-cpp/using-formulatext-function-in-aspose-cells/)
- [Using ICustomFunction Feature](/cells/nodejs-cpp/using-icustomfunction-feature/)
