---
title: Calculate Formulas
type: docs
weight: 8
url: /java/calculate-formulas/
aliases:
    - /java/ways-to-calculate-formulas/
---

## **Adding Formulas & Calculating Results**

Aspose.Cells has an embedded formula calculation engine. It can not only re-calculate formulas imported from designer templates but also supports calculating the results of formulas added at runtime.

Aspose.Cells supports most of the formulas or functions that are part of Microsoft Excel. they can be used through the API or using designer spreadsheets. Aspose.Cells supports a huge set of mathematical, string, Boolean, date/time, statistical, database, lookup, and reference formulas.

Use the [**Formula**](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#Formula) property of the [**Cell**](https://apireference.aspose.com/cells/java/com.aspose.cells/Cell) class to add a formula to a cell. When applying a formula, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel and use a comma (,) to delimit function parameters.

To calculate the results of formulas, user may call the [**calculateFormula**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) method of the [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) class which processes all formulas embedded in an Excel file. Or, user may call the [**calculateFormula**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(com.aspose.cells.CalculationOptions,%20boolean)) method of the [**Worsheet**](https://apireference.aspose.com/cells/java/com.aspose.cells/Worksheet) class which processes all formulas embedded in a sheet. Or, user also may call the [**calculate**](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#calculate(com.aspose.cells.CalculationOptions)) method of the [**Cell**](https://apireference.aspose.com/cells/java/com.aspose.cells/Cell) class which processes the  formula of one Cell. Read [a list of the functions supported by the calculateFormula method](/cells/java/supported-formula-functions/).

{{% alert color="primary" %}}

Currently, Aspose.Cells supports the following operators: +, －, *, /, <, <=, =, >=, >, <>, &, %, ^.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Important to Know**

{{% alert color="primary" %}}

The [**Formula**](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#Formula) property of the [**Cell**](https://apireference.aspose.com/cells/java/com.aspose.cells/Cell) class works differently from the [**calculateFormula**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(boolean)) method of the [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) class. The [**Formula**](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#Formula) simply adds the formula to a cell but doesn't calculate the result at runtime, as the [**calculateFormula**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(boolean)) method does.

{{% /alert %}}

## **Direct Calculation of Formula**

Aspose.Cells has an embedded formula calculation engine. As well as calculating formulas imported from a designer file, Aspose.Cells can calculate formula results directly.

Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Aspose.Cells' formula calculation engine API ([**worksheet.calculateFormula(String formula, CalculationOptions opts)**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions))) to calculate the results of such formulas without adding them to the worksheet.

The code below produces the following output.

{{< highlight java >}}

Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50.0

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

## **Calculating Formulas repeatedly**

When there are lots of formulas in the workbook and user needs to calculate them repeatedly with modifying only a small part of them, it may be helpful for performance to enable the formula calculating chain: [**Workbook.getSettings().setCreateCalcChain(true)**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CreateCalcChain).
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}
By default the calculating chain is disabled. Because creating the chain also needs time, the first time of calculating formulas([**Workbook.calculateFormula()**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) may consume more CPU processing time and memory when comparing with calculating formulas without chain. If user does not need to calculate formulas repeatedly, the default behavior that calculating formula directly without the calculating chain should be the better way.
