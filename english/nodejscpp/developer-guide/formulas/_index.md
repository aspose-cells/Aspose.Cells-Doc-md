---
title: Manage formulas of Excel files with Node.js via C++
linktitle: Formulas
type: docs
weight: 122
url: /nodejs-cpp/using-formulas-or-functions-to-process-data/
description: Learn how to Manage formulas of Excel files through the Aspose.Cells for Node.js via C++. Aspose.Cells can simply get, set and calculate formulas of excel files.
keywords: How to calculate formulas in Node.js via C++, Formulas and Functions using Node.js via C++, Node.js via C++ Manage Built-in Functions, How to Use Add-in Functions with Node.js via C++, How to Use Array Formula via Node.js via C++, How to Use R1C1 Formula in Node.js via C++.
---

## **Introduction**

One of the of Microsoft Excel's compelling features is its ability to process data with formulas and functions. Microsoft Excel provides a set of built-in functions and formulas that helps users to perform complex calculations quickly. Aspose.Cells also provides a huge set of built-in functions and formulas that help developers compute values easily. Aspose.Cells also supports add-in functions. Moreover, Aspose.Cells supports array and R1C1 formulas.

## **How to Use Formulas and Functions**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection. Each item in the Cells collection represents an object of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class.

It is possible to apply formulas to cells using properties and methods offered by the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class, discussed in more detail below.

- Using built-in functions.
- Using add-in functions.
- Working with array formulas.
- Creating a R1C1 formula.

## **How to Use Built-in Functions**

Built-in functions or formulas are provided as ready-made functions to reduce developers' efforts and time. See [a list of built-in functions](/cells/nodejs-cpp/supported-formula-functions/) supported by Aspose.Cells. The functions are listed in alphabetical order. More functions will be supported in future.

Aspose.Cells supports most of the formulas or functions offered by Microsoft Excel. Developers can use these formulas through the API or [designer spreadsheet](/cells/nodejs-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells supports a huge set of mathematical, string, Boolean, date/time, statistical, database, lookup and reference formulas.

Use the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class' [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) property to add a formula to a cell. **Complex formulas**, for example

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, are also supported in Aspose.Cells. When applying a formula to a cell, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel and use a comma (,) to delimit function parameters.

In the example below, a complex formula is applied to the first cell of a worksheet's [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection. The formula uses a built-in **IF** function provided by Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

## **How to Use Add-in Functions**

We can have some user defined formulas that we want to include as an excel add-in. When setting the cell.Formula function built-in functions work fine however there is a need to set the custom functions or formulas using the add-in functions.

Aspose.Cells provides features to register add in functions using [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). Afterwards when we set cell.Formula = anyFunctionFromAddIn, the output Excel file contains the calculated value from the AddIn function.

Following XLAM file shall be downloaded for registering the add in function in the below sample code. Similarly the output file "test_udf.xlsx" can be downloaded to check the output.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Register macro enabled add-in along with the function name
const id = workbook.getWorksheets().registerAddInFunction(path.join(dataDir, "TESTUDF.xlam"), "TEST_UDF", false);

// Register more functions in the file (if any)
workbook.getWorksheets().registerAddInFunction(id, "TEST_UDF1"); // in this way you can add more functions that are in the same file

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first cell
const cell = worksheet.getCells().get("A1");

// Set formula name present in the add-in
cell.setFormula("=TEST_UDF()");

// Save workbook to output XLSX format.
workbook.save(path.join(outputDir, "test_udf.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **How to Use Array Formula**

Array formulas are formulas that take arrays, instead of individual numbers, as arguments to the functions that make up the formula. When an array formula is displayed, it is surrounded by braces ({}).

Some Microsoft Excel functions return arrays of values. To calculate multiple results with an array formula, enter the array into a range of cells with the same number of rows and columns as the array arguments.

It is possible to apply an array formula to a cell by calling the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class' [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) method. The [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) method takes the following parameters:

- **Array Formula**, the array formula.
- **Number of Rows**, the number of rows to populate result of the array formula.
- **Number of Columns**, the number of columns to populate result of the array formula.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

// Adding a value to B1
worksheet.getCells().get("B1").putValue(4);

// Adding a value to "B2" cell
worksheet.getCells().get("B2").putValue(5);

// Adding a value to "B3" cell
worksheet.getCells().get("B3").putValue(6);

// Adding a value to C1
worksheet.getCells().get("C1").putValue(7);

// Adding a value to "C2" cell
worksheet.getCells().get("C2").putValue(8);

// Adding a value to "C3" cell
worksheet.getCells().get("C3").putValue(9);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A6").setArrayFormula("=LINEST(A1:A3,B1:C3,TRUE,TRUE)", 5, 3);

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A6").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **How to Use R1C1 Formula**

Add an **R1C1** reference style formula to a cell with the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class' [**getR1C1Formula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getR1C1Formula--) property.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Setting an R1C1 formula on the "A11" cell, 
// Row and Column indices are relative to destination index
worksheet.getCells().get("A11").setR1C1Formula("=SUM(R[-10]C[0]:R[-7]C[0])");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Advance topics**
- [Precedents and Dependents](/cells/nodejs-cpp/precedents-and-dependents/)
- [Set External Links in Formulas](/cells/nodejs-cpp/set-external-links-in-formulas/)
- [Propagate Formula in Table or List Object automatically while entering data in new rows](/cells/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Setting Formula for Named Range](/cells/nodejs-cpp/setting-formula-for-named-range/)
- [Setting Formulas - Notice for Non English Users](/cells/nodejs-cpp/setting-formulas-notice-for-non-english-users/)
- [Setting Shared Formula](/cells/nodejs-cpp/setting-shared-formula/)
- [Specify Maximum Rows of Shared Formula](/cells/nodejs-cpp/specify-maximum-rows-of-shared-formula/)
- [Supported Excel Functions](/cells/nodejs-cpp/supported-formula-functions/)

