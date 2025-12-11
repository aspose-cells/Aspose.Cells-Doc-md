---
title: Calculate Formulas with Golang via C++
linktitle: Calculate Formulas
description: This article introduces how to use the Aspose.Cells library to calculate formulas in Microsoft Excel with Golang via C++. By loading an existing Excel file or creating a new Excel file, we can use the methods provided by Aspose.Cells to calculate the formula and get the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, formulas, calculations, Direct Calculation of Formula, Calculate Formulas repeatedly, add formulas.
type: docs
weight: 125
url: /go-cpp/calculate-formulas/
---

## **Adding Formulas & Calculating Results**

Aspose.Cells has an embedded formula calculation engine. Not only can it re‑calculate formulas imported from designer templates, but it also supports calculating the results of formulas added at runtime.

Aspose.Cells supports most of the formulas or functions that are part of Microsoft Excel (Read [a list of the functions supported by the calculation engine](/cells/cpp/supported-formula-functions/)). Those functions can be used through the APIs or designer spreadsheets. Aspose.Cells supports a huge set of mathematical, string, boolean, date/time, statistical, database, lookup, and reference formulas.

Use the [**GetFormula**](https://reference.aspose.com/cells/go-cpp/cell/getformula/) property or [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) methods of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class to add a formula to a cell. When applying a formula, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel and use a comma (,) to delimit function parameters.

To calculate the results of formulas, the user may call the [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) method of the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class, which processes all formulas embedded in an Excel file. Alternatively, the user may call the [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) method of the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class, which processes all formulas embedded in a sheet. The user may also call the [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) method of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class, which processes the formula of a single cell:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas.go" >}}

### **Important to Know for Formulas**

{{% alert color="primary" %}}

The **GetFormula** property and **SetFormula(...)** methods of the [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) class work differently from the **Calculate** methods of the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/), and [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) classes. The **GetFormula** property and **SetFormula(...)** methods simply add the formula to a cell but do not calculate the result at runtime. To get the result of the formulas, please call the **Calculate** methods.

{{% /alert %}}

## **Direct Calculation of Formulas**

Aspose.Cells has an embedded formula calculation engine. As well as calculating formulas imported from a designer file, Aspose.Cells can calculate formula results directly.

Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet, and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula to a worksheet.

You can use Aspose.Cells' formula calculation engine APIs for [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) to [**calculate**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula/) the results of such formulas without adding them to the worksheet:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-1.go" >}}
Above code produces the following output:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **How to Calculate Formulas Repeatedly**

When there are many formulas in the workbook and the user needs to calculate them repeatedly while modifying only a small part of them, it may be helpful for performance to enable the formula calculation chain: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getenablecalculationchain/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-2.go" >}}

### **Important to Know**

{{% alert color="primary" %}}

By default, the calculation chain is disabled. Because creating the chain also requires extra time, the first calculation of formulas ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)) may consume more CPU processing time and memory compared with calculating formulas without a chain. If the user does not need to calculate formulas repeatedly, the default behavior (calculating formulas directly without creating a calculation chain) should be the better approach.

{{% /alert %}}

## **Advanced Topics**
- [Add Cells to Microsoft Excel Formula Watch Window](/cells/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calculating IFNA function using Aspose.Cells](/cells/cpp/calculating-ifna-function-using-aspose-cells/)
- [Calculation of Array Formula of Data Tables](/cells/cpp/calculation-of-array-formula-of-data-tables/)
- [Calculation of Excel 2016 MINIFS and MAXIFS functions](/cells/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Decrease the Calculation Time of Cell.Calculate method](/cells/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Direct calculation of custom function without writing it in a worksheet](/cells/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells](/cells/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Returning a Range of Values using AbstractCalculationEngine](/cells/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Setting Formula Calculation Mode of Workbook](/cells/cpp/setting-formula-calculation-mode-of-workbook/)
- [Using FormulaText function in Aspose.Cells](/cells/cpp/using-formulatext-function-in-aspose-cells/)