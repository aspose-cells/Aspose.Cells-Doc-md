---
title : "Ways to Calculate Formulas" 
description : "" 
weight : 12039 
toc : false
type: docs
url: /cpp/developerguide/formulas/ways+to+calculate+formulas/
---

# Aspose.Cells for C++ : Ways to Calculate Formulas


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#introduction)
*   2 [Adding Formulas & Calculating Results](#adding-formulas-&-calculating-results)
*   3 [Direct Calculation of Formula](#direct-calculation-of-formula)
*   4 [Calculating Formulas Once Only](#calculating-formulas-once-only)
{{< /panel >}}
 

## Introduction

Aspose.Cells has an embedded formula calculation engine. It can not only re-calculate formulas imported from designer templates but also supports calculating the results of formulas added at runtime.

## Adding Formulas & Calculating Results

Aspose.Cells supports most of the formulas or functions that are the part of Microsoft Excel. they can be used through the API or using designer spreadsheets. Aspose.Cells supports a huge set of mathematical, string, boolean, date/time, statistical, lookup and reference formulas.

Use the `Cell.Formula` method to add a formula to a cell. When applying a formula to a cell, always begin the string with an equal sign `(=)` as you do when creating a formula in Microsoft Excel. Use a comma `(,)` to delimit function parameters.

To calculate the results of formulas, call the `Workbook.CalculateFormula()` method which processes all the formulas embedded in an Excel file. Please see the following sample code that adds the formula and calculates its results. Please check the [output excel file](https://docs2.aspose.com/cells/cpp/attachments/37978115/38109185.xlsx) generated with this code.

**Sample Code**

## Direct Calculation of Formula

Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use `Worksheet.CalculateFormula(String formula)` method to calculate the results of such formulas without adding them to worksheet.

The code below produces the following output.

{{< code lang="cs" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50
{{< /code >}}

**Sample Code**

## Calculating Formulas Once Only

When `Workbook.CalculateFormula()` is called to calculate the values of formulas in a workbook template, Aspose.Cells creates a calculating chain. It increases performance when formulas are calculated for the second or third time.

However, if the template contains lots of formulas, the first time the formula is calculated can consume a lot of CPU processing time and memory.

Aspose.Cells allows you to turn off creating a calculating chain which is useful when you want to calculate formulas only once.

Please call `Workbook.GetISettings().SetCreateCalcChain()` with false parameter. You can use the [provided excel file](https://docs2.aspose.com/cells/cpp/attachments/37978115/38109186.xlsx) to test this code.

**Sample Code**

