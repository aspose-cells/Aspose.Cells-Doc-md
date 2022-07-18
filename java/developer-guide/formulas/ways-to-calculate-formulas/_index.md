---
title: Calculate Formulas
type: docs
weight: 8
url: /java/calculate-formulas/
aliases:
    - /java/ways-to-calculate-formulas/
---

## **Adding Formulas & Calculating Results**

Aspose.Cells has an embedded formula calculation engine. Not only it can re-calculate formulas imported from designer templates but also it supports to calculate the results of formulas added at runtime.

Aspose.Cells supports most of the formulas or functions that are part of Microsoft Excel(Read [a list of the functions supported by the calculation engine](/cells/java/supported-formula-functions/)). Those functions can be used through the APIs or designer spreadsheets. Aspose.Cells supports a huge set of mathematical, string, boolean, date/time, statistical, database, lookup, and reference formulas.

Use the [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) property or [**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula(java.lang.String,%20com.aspose.cells.FormulaParseOptions,%20java.lang.Object)) methods of the [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) class to add a formula to a cell. When applying a formula, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel and use a comma (,) to delimit function parameters.

To calculate the results of formulas, user may call the [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) method of the [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) class which processes all formulas embedded in an Excel file. Or, user may call the [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(com.aspose.cells.CalculationOptions,%20boolean)) method of the [**Worsheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class which processes all formulas embedded in a sheet. Or, user also may call the [**Calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate(com.aspose.cells.CalculationOptions)) method of the [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) class which processes the  formula of one Cell:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Important to Know**

{{% alert color="primary" %}}

The **Formula** property and **SetFormula(...)** methods of the [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) class work differently from the **Calculate** methods of the [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) and [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) classes. The **Formula** property and **SetFormula(...)** methods simply add the formula to a cell but do not calculate the result at runtime. To get the result of the formulas, please call **Calculate** methods.

{{% /alert %}}

## **Direct Calculation of Formula**

Aspose.Cells has an embedded formula calculation engine. As well as calculating formulas imported from a designer file, Aspose.Cells can calculate formula results directly.

Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Aspose.Cells' formula calculation engine APIs for [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) to [**calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions)) the results of such formulas without adding them to the worksheet:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Above code produces the following output:
{{< highlight java >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Calculating Formulas repeatedly**

When there are lots of formulas in the workbook and user needs to calculate them repeatedly with modifying only a small part of them, it may be helpful for performance to enable the formula calculation chain: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Important to Know**

{{% alert color="primary" %}}

By default the calculation chain is disabled. Because creating the chain also needs extra time, the first time of calculating formulas([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))) may consume more CPU processing time and memory when comparing with calculating formulas without chain. If user does not need to calculate formulas repeatedly, the default behavior(calculating formula directly without creating calculation chain) should be the better way.

{{% /alert %}}
