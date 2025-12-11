---
title: Ways to Calculate Formulas
type: docs
weight: 30
url: /cpp/ways-to-calculate-formulas/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**
Aspose.Cells has an embedded formula calculation engine. It can not only re‑calculate formulas imported from designer templates but also supports calculating the results of formulas added at runtime.

## **Adding Formulas & Calculating Results**
Aspose.Cells supports most of the formulas or functions that are part of Microsoft Excel. They can be used through the API or using designer spreadsheets. Aspose.Cells supports a huge set of mathematical, string, boolean, date/time, statistical, lookup and reference formulas.

Use the `Cell.SetFormula` method to add a formula to a cell. When applying a formula to a cell, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel. Use a comma (,) to delimit function parameters.

To calculate the results of formulas, call the `Workbook.CalculateFormula()` method, which processes all the formulas embedded in an Excel file. See the following sample code that adds the formula and calculates its results. Check the [output Excel file](38109185.xlsx) generated with this code.

**Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults-new.cpp" >}}
<!---## **Direct Calculation of Formula**
Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Worksheet.CalculateFormula(String formula) method to calculate the results of such formulas without adding them to worksheet.

The code below produces the following output.

{{< highlight java >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}   --->

## **Calculating Formulas Once Only**
When `Workbook.CalculateFormula()` is called to calculate the values of formulas in a workbook template, Aspose.Cells creates a calculation chain. This increases performance when formulas are calculated for the second or third time.

However, if the template contains many formulas, the first time the formulas are calculated can consume a lot of CPU processing time and memory.

Aspose.Cells allows you to turn off creating a calculation chain, which is useful when you want to calculate formulas only once.

Please call `Workbook.GetISettings().SetCreateCalcChain()` with a false parameter. You can use the [provided Excel file](38109186.xlsx) to test this code.

**Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
