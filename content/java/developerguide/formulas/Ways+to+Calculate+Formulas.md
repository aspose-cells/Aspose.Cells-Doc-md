+++
title = "Ways to Calculate Formulas" 
description = "" 
weight = 12193 
+++

Aspose.Cells for Java : Ways to Calculate Formulas  

# Aspose.Cells for Java : Ways to Calculate Formulas



{{< panel title="Contents Summary" style="primary" >}}
*   1 [Adding Formulas & Calculating Results](#WaystoCalculateFormulas-AddingFormulas&CalculatingResults)
    *   1.1 [Important to Know](#WaystoCalculateFormulas-ImportanttoKnow)
*   2 [Direct Calculation of Formula](#WaystoCalculateFormulas-DirectCalculationofFormula)
*   3 [Calculating Formulas Once Only](#WaystoCalculateFormulas-CalculatingFormulasOnceOnly)
{{< /panel >}}
 

## Adding Formulas & Calculating Results

Aspose.Cells has an embedded formula calculation engine. It can not only re-calculate formulas imported from designer templates but also supports calculating the results of formulas added at runtime.

Aspose.Cells supports most of the formulas or functions that are part of Microsoft Excel. they can be used through the API or using designer spreadsheets. Aspose.Cells supports a huge set of mathematical, string, Boolean, date/time, statistical, database, lookup, and reference formulas.

Use the [Formula](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#Formula) property of the [Cell](https://apireference.aspose.com/java/cells/com.aspose.cells/Cell) class to add a formula to a cell. When applying a formula, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel and use a comma (,) to delimit function parameters.

To calculate the results of formulas, call the [calculateFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#calculateFormula(boolean)) method of the [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/Workbook) class which processes all formulas embedded in an Excel file. Read [a list of the functions supported by the calculateFormula method](https://docs2.aspose.com/cells/java/developerguide/formulas/supported+formula+functions).

Currently, Aspose.Cells supports the following operators: +, －, \*, /, <, <=, =, >=, >, <>, &, %, ^.

### Important to Know

The [Formula](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#Formula) property of the [Cell](https://apireference.aspose.com/java/cells/com.aspose.cells/Cell) class works differently from the [calculateFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#calculateFormula(boolean)) method of the [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/Workbook) class. The `Formula` [Formula](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#Formula)simply adds the formula to a cell but doesn't calculate the result at runtime, as the [calculateFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#calculateFormula(boolean))method does.

## Direct Calculation of Formula

Aspose.Cells has an embedded formula calculation engine. As well as calculating formulas imported from a designer file, Aspose.Cells can calculate formula results directly.

Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Aspose.Cells' formula calculation engine API ([worksheet.calculateFormula(String formula)](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#calculateFormula(java.lang.String))) to calculate the results of such formulas without adding them to the worksheet.

The code below produces the following output.

{{< code lang="cs" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /code >}}

## Calculating Formulas Once Only

When [Workbook.calculateFormula()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#calculateFormula(boolean)) is called to calculate the values of formulas in a workbook template, Aspose.Cells creates a calculating chain. This increases performance when formulas are calculated for the second or third time.

However, if the template contains lots of formulas, the first time the formula is calculated can consume a lot of CPU processing time and memory.

Aspose.Cells allows you to turn off creating a calculating chain which is useful when you want to calculate formulas only once.

To improve Aspose.Cell's formula calculation performance and when you do not want to create a formula calculating chain, set [Workbook.getSettings().setCreateCalcChain()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#CreateCalcChain) to **false**. By default, it is set to **true**.

