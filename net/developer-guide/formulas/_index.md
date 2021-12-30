---
title: Manage and Calculate formulas of Excel files
linktitle: Formulas
type: docs
weight: 120
url: /net/using-formulas-or-functions-to-process-data/
aliases: [/net/formulas/]
description: Aspose.Cells can simply get, set and calculate formulas of excel files.
---

## **Introduction**

One of the of Microsoft Excel's compelling features is its ability to process data with formulas and functions. Microsoft Excel provides a set of built-in functions and formulas that helps users to perform complex calculations quickly. Aspose.Cells also provides a huge set of built-in functions and formulas that help developers compute values easily. Aspose.Cells also supports add-in functions. Moreover, Aspose.Cells support array and R1C1 formulas in Aspose.Cells.

## **Using Formulae and Functions**

Aspose.Cells provides a class, [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. Each item in the Cells collection represents an object of the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class.

It is possible to apply formulas to cells using properties and methods offered by the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class, discussed in more detail below.

- Using built-in functions.
- Using add-in functions.
- Working with array formulas.
- Creating a R1C1 formula.

## **Using Built-in Functions**

Built-in functions or formulas are provided as ready-made functions to reduce developers' efforts and time. See [a list of built-in functions](/cells/net/supported-formula-functions/) supported by Aspose.Cells. The functions are listed in alphabetical order. More functions will be supported in future.

Aspose.Cells supports most of the formulas or functions offered by Microsoft Excel. Developers can use these formulas through the API or [designer spreadsheet](/cells/net/what-is-a-designer-spreadsheet/). Aspose.Cells supports a huge set of mathematical, string, Boolean, date/time, statistical, database, lookup and reference formulas.

Use the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class' [**Formula**](https://apireference.aspose.com/cells/net/aspose.cells/cell/properties/formula) property to add a formula to a cell. **Complex formulas**, for example

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, are also supported in Aspose.Cells. When applying a formula to a cell, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel and use a comma (,) to delimit function parameters.

In the example below, a complex formula is applied to the first cell of a worksheet's [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/cells) collection. The formula uses a built-in **IF** function provided by Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Using Add-in Functions**

We can have some user defined formulas that we want to include as an excel add-in. When setting the cell.Formula function built-in functions work fine however there is a need to set the custom functions or formulas using the add-in functions.

Aspose.Cells provides features to register add in functions using [**Worksheets.RegisterAddInFunction()**](https://apireference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Afterwards when we set cell.Formula = anyFunctionFromAddIn, the output Excel file contains the calculated value from the AddIn function.

Following XLAM file shall be downloaded for registering the add in function in the below sample code. Similarly the output file "test_udf.xlsx" can be downloaded to check the output.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Using Array Formula**

Array formulas are formulas that take arrays, instead of individual numbers, as arguments to the functions that make up the formula. When an array formula is displayed, it is surrounded by braces ({}).

Some Microsoft Excel functions return arrays of values. To calculate multiple results with an array formula, enter the array into a range of cells with the same number of rows and columns as the array arguments.

It is possible to apply an array formula to a cell by calling the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class' [**SetArrayFormula**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) method. The [**SetArrayFormula**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) method takes the following parameters:

- **Array Formula**, the array formula.
- **Number of Rows**, the number of rows to populate result of the array formula.
- **Number of Columns**, the number of columns to populate result of the array formula.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Using R1C1 Formula**

Add an **R1C1** reference style formula to a cell with the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class' [**R1C1Formula**](https://apireference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Advance topics**
- [Add Cells to Microsoft Excel Formula Watch Window](/cells/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Detecting Circular Reference](/cells/net/detecting-circular-reference/)
- [Interrupt or Cancel the Formula Calculation of Workbook](/cells/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Specify Maximum Rows of Shared Formula](/cells/net/specify-maximum-rows-of-shared-formula/)
- [Supported Formula Functions](/cells/net/supported-formula-functions/)
- [Ways to Calculate Formulas](/cells/net/ways-to-calculate-formulas/)



