+++
title = "Using Formulas or Functions to Process Data" 
description = "" 
weight = 12231 
+++

Aspose.Cells for .NET : Using Formulas or Functions to Process Data  

# Aspose.Cells for .NET : Using Formulas or Functions to Process Data


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#UsingFormulasorFunctionstoProcessData-Introduction)
*   2 [Using Formulae and Functions](#UsingFormulasorFunctionstoProcessData-UsingFormulaeandFunctions)
*   3 [Using Built-in Functions](#UsingFormulasorFunctionstoProcessData-UsingBuilt-inFunctions)
*   4 [Using Add-in Functions](#UsingFormulasorFunctionstoProcessData-UsingAdd-inFunctions)
*   5 [Using Array Formula](#UsingFormulasorFunctionstoProcessData-UsingArrayFormula)
    *   5.1 [Using R1C1 Formula](#UsingFormulasorFunctionstoProcessData-UsingR1C1Formula)
{{< /panel >}}
 

## Introduction

One of the of Microsoft Excel's compelling features is its ability to process data with formulas and functions. Microsoft Excel provides a set of built-in functions and formulas that helps users to perform complex calculations quickly. Aspose.Cells also provides a huge set of built-in functions and formulas that help developers compute values easily. Aspose.Cells also supports add-in functions. Moroever, Aspose.Cells support array and R1C1 formulas in Aspose.Cells.

## Using Formulae and Functions

Aspose.Cells provides a class, `Workbook`, that represents a Microsoft Excel file. The `Workbook` class contains a `Worksheets` collection that allows access to each worksheet in the Excel file. A worksheet is represented by the `Worksheet` class. The `Worksheet` class provides a `Cells` collection. Each item in the `Cells` collection represents an object of the `Cell` class.

It is possible to apply formulas to cells using properties and methods offered by the `Cell` class, discussed in more detail below.

*   Using built-in functions.
*   Using add-in functions.
*   Working with array formulas.
*   Creating a R1C1 formula.

## Using Built-in Functions

Built-in functions or formulas are provided as ready-made functions to reduce developers' efforts and time. See [a list of built-in functions](https://docs2.aspose.com/cells/net/developerguide/formulas/supported+formula+functions) supported by Aspose.Cells. The functions are listed in alphabetical order. More functions will be supported in future.

Aspose.Cells supports most of the formulas or functions offered by Microsoft Excel. Developers can use these formulas through the API or [designer spreadsheet](https://docs2.aspose.com/cells/net/developerguide/introductionofasposecellsfornet/what+is+a+designer+spreadsheet). Aspose.Cells supports a huge set of mathematical, string, Boolean, date/time, statistical, database, lookup and reference formulas.

Use the `Cell` class' `Formula` property to add a formula to a cell. **Complex formulas**, for example

\= H7\*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

, are also supported in Aspose.Cells. When applying a formula to a cell, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel and use a comma (,) to delimit function parameters.

In the example below, a complex formula is applied to the first cell of a worksheet's `Cells` collection. The formula uses a built-in **IF** function provided by Aspose.Cells.

## Using Add-in Functions

We can have some user defined formulas that we want to include as an excel addin. When setting the cell.Formula function built-in functions work fine however there is a need to set the custom functions or formulas using the add-in functions. 

Aspose.Cells provides features to register add in functions using Worksheets.RegisterAddInFunction(). Afterwards when we set cell.Formula = anyFunctionFromAddIn, the output Excel file contains the calculated value from the AddIn function.

Following XLAM file shall be downloaded for registering the add in function in the below sample code. Similarly the output file "test\_udf.xlsx" can be downloaded to check the output.

[TestUDF.xlam](https://docs2.aspose.com/cells/net/attachments/5017210/81920908.xlam)

[test\_udf.xlsx](https://docs2.aspose.com/cells/net/attachments/5017210/81920909.xlsx)

## Using Array Formula

Array formulas are formulas that take arrays, instead of individual numbers, as arguments to the functions that make up the formula. When an array formula is displayed, it is surrounded by braces ({}).

Some Microsoft Excel functions return arrays of values. To calculate multiple results with an array formula, enter the array into a range of cells with the same number of rows and columns as the array arguments.

It is possible to apply an array formula to a cell by calling the `Cell` class' `ArrayFormula` method. The `ArrayFormula` method takes the following parameters:

*   **Array Formula**, the array formula.
*   **Number of Rows**, the number of rows to populate result of the array formula.
*   **Number of Columns**, the number of columns to populate result of the array formula.

#### Using R1C1 Formula

Add an **R1C1** reference style formula to a cell with the `Cell` class' `R1C1Formula` property.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [TestUDF.xlam](https://docs2.aspose.com/cells/net/attachments/5017210/81920908.xlam) (application/vnd.ms-excel.addin.macroenabled.12)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [test\_udf.xlsx](https://docs2.aspose.com/cells/net/attachments/5017210/81920909.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

