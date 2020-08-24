---
title: Using Formulas or Functions to Process Data
type: docs
weight: 50
url: /java/using-formulas-or-functions-to-process-data/
---

{{% alert color="primary" %}} 

One of Microsoft Excel's compelling features is its ability to process data with formulas and functions. Microsoft Excel provides a set of built-in functions and formulas that helps users to perform complex calculations quickly. Aspose.Cells also provides a huge set of built-in functions and formulas that help developers compute values easily. Aspose.Cells also supports add-in functions. Moreover, Aspose.Cells support array and R1C1 formulas in Aspose.Cells.

{{% /alert %}} 
#### **Using Formulas and Functions**
Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#Worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection. Each item in the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection represents an object of the [Cell](https://apireference.aspose.com/java/cells/com.aspose.cells/cell) class.

It is possible to apply formulas to cells using properties and methods offered by the [Cell](https://apireference.aspose.com/java/cells/com.aspose.cells/cell) class, discussed in more detail below.

- [Using built-in functions](/cells/java/using-formulas-or-functions-to-process-data/).
- [Using add-in functions](/cells/java/using-formulas-or-functions-to-process-data/).
- [Working with array formulas](/cells/java/using-formulas-or-functions-to-process-data/).
- [Creating a R1C1 formula](/cells/java/using-formulas-or-functions-to-process-data/).
#### **Using Built-in Functions**
Built-in functions or formulas are provided as ready-made functions to reduce developers' efforts and time. See [a list of built-in functions](/cells/java/supported-formula-functions/). The functions are listed in alphabetical order. More functions will be supported in the future.

Aspose.Cells supports most of the formulas or functions offered by Microsoft Excel. Developers can use these formulas through the API or [designer spreadsheet](/cells/java/what-is-a-designer-spreadsheet/). Aspose.Cells supports a huge set of mathematical, string, Boolean, date/time, statistical, database, lookup, and reference formulas.

Use the [Formula](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#Formula) property of the [Cell](https://apireference.aspose.com/java/cells/com.aspose.cells/cell) class to add a formula to a cell. **Complex formulas**, for example

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, are also supported in Aspose.Cells. When applying a formula to a cell, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel and use a comma (,) to delimit function parameters.

In the example below, a complex formula is applied to the first cell of a worksheet's [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection. The formula uses a built-in **IF** function provided by Aspose.Cells.

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}
#### **Using Add-in Functions**
We can have some user-defined formulas that we want to include as an excel addin. When setting the [cell.Formula](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#Formula) function built-in functions work fine however there is a need to set the custom functions or formulas using the add-in functions. 

Aspose.Cells provides features to register add in functions using [Worksheets.RegisterAddInFunction()](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheetcollection#registerAddInFunction\(java.lang.String,%20java.lang.String,%20boolean\)). Afterwards when we set [cell.Formula](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#Formula) = anyFunctionFromAddIn, the output Excel file contains the calculated value from the AddIn function.

Following the XLAM file shall be downloaded for registering the add-in function in the below sample code. Similarly, the output file "test_udf.xlsx" can be downloaded to check the output.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}
#### **Using Array Formula**
Array formulas are formulas that work with arrays, instead of individual numbers, as arguments to the functions that make up the formula. When an array formula is displayed, it is surrounded by braces ({}) as shown below.

**Setting an array formula on cell G2** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

Some Microsoft Excel functions return arrays of values. To calculate multiple results with an array formula, enter the array into a range of cells with the same number of rows and columns as the array arguments.

It is possible to apply an array formula to a cell by calling the [Cell](https://apireference.aspose.com/java/cells/com.aspose.cells/cell) class' [setArrayFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#setArrayFormula\(java.lang.String,%20int,%20int\)) method. The [setArrayFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#setArrayFormula\(java.lang.String,%20int,%20int\)) method takes the following parameters:

- **Array Formula**, the array formula.
- **Number of Rows**, the number of rows to populate result of the array formula.
- **Number of Columns**, the number of columns to populate the result of the array formula.

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}
#### **Using R1C1 Formula**
Apply an **R1C1** reference style formula to a cell with the [Cell](https://apireference.aspose.com/java/cells/com.aspose.cells/cell) class' [setR1C1Formula](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#R1C1Formula) property.

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}
