---
title: Ways to Calculate Formulas
type: docs
weight: 30
url: /go-cpp/ways-to-calculate-formulas/
---

## **Introduction**

Aspose.Cells has an embedded formula calculation engine. It can not only re‑calculate formulas imported from designer templates but also supports calculating the results of formulas added at runtime.

## **Adding Formulas & Calculating Results**

Aspose.Cells supports most of the formulas or functions that are part of Microsoft Excel. **They** can be used through the API or using designer spreadsheets. Aspose.Cells supports a huge set of mathematical, string, boolean, date/time, statistical, lookup and reference formulas.

Use the `Cell.SetFormula` method to add a formula to a cell. When applying a formula to a cell, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel. Use a comma (,) to delimit function parameters.

To calculate the results of formulas, call the `Workbook.CalculateFormula()` method, which processes all the formulas embedded in an **Excel** file. See the following sample code that adds the formula and calculates its results. Please check the [output Excel file](38109185.xlsx) generated with this code.

**Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingFormulasAndCalculatingResults.go" >}}

## **Calculating Formulas Once Only**

When `Workbook.CalculateFormula()` is called to calculate the values of formulas in a workbook template, Aspose.Cells creates a **calculation chain**. It increases performance when formulas are calculated for the second or third time.

However, if the template contains lots of formulas, the first time the **formulas** are calculated can consume significant CPU processing time and memory.

Aspose.Cells allows you to turn off creating a **calculation chain**, which is useful when you want to calculate formulas only once.

Please call `Workbook.GetISettings().SetCreateCalcChain()` with **a** false parameter. You can use the [provided Excel file](38109186.xlsx) to test this code.

**Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculatingFormulasOnceOnly.go" >}}