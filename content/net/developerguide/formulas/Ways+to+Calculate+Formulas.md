+++
title = "Ways to Calculate Formulas" 
description = "" 
weight = 12232 
+++

Aspose.Cells for .NET : Ways to Calculate Formulas  

# Aspose.Cells for .NET : Ways to Calculate Formulas


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#WaystoCalculateFormulas-Introduction)
*   2 [Adding Formulas & Calculating Results](#WaystoCalculateFormulas-AddingFormulas&CalculatingResults)
*   3 [Direct Calculation of Formula](#WaystoCalculateFormulas-DirectCalculationofFormula)
*   4 [Calculating Formulas Once Only](#WaystoCalculateFormulas-CalculatingFormulasOnceOnly)
{{< /panel >}}
 

## Introduction

Aspose.Cells has an embedded formula calculation engine. It can not only re-calculate formulas imported from designer templates but also supports calculating the results of formulas added at runtime.

## Adding Formulas & Calculating Results

Aspose.Cells supports most of the formulas or functions that are the part of Microsoft Excel. they can be used through the API or using designer spreadsheets. Aspose.Cells supports a huge set of mathematical, string, Boolean, date/time, statistical, database, lookup and reference formulas.

Use the `Cell` class' `Formula` property to add a formula to a cell. When applying a formula to a cell, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel. Use a comma (,) to delimit function parameters.

To calculate the results of formulas, call the `Excel` class' `CalculateFormula` method which processes all the formulas embedded in an Excel file. Read \[a list of the functions supported by the `CalculateFormula` method.

Currently, Aspose.Cells supports the following operators: +, －, \*, /, <, <=, =, >=, >, <>, &, %, ^.

The the `Cell` class' `Formula` property works differently from the `Excel` class' `CalculateFormula` method. The `Formula` property simply adds the formula to a cell but doesn't calculate the formula results at runtime, as the `CalculateFormula` method does.

## Direct Calculation of Formula

Aspose.Cells has an embedded formula calculation engine. As well as calculating formulas imported from a designer file, Aspose.Cells can calculate formula results directly.

Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Aspose.Cells' formula calculation engine API (`worksheet.CalculateFormula(string formula)`) to calculate the results of such formulas without adding them to worksheet.

The code below produces the following output.

{{< code lang="cs" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50
{{< /code >}}

## Calculating Formulas Once Only

When `Workbook.CalculateFormula()` is called to calculate the values of formulas in a workbook template, Aspose.Cells creates a calculating chain. It increases performance when formulas are calculated for the second or third time.

However, if the template contains lots of formulas, the first time the formula is calculated can consume a lot of CPU processing time and memory.

Aspose.Cells allows you to turn off creating a calculating chain which is useful when you want to calculate formulas only once.

To improve Aspose.Cell's formula calculation performance and when you do not want to create a formula calculating chain, set `Workbook.Settings.CreateCalcChain` to `false`. By default, it is set to `true`.

