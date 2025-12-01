---
title: Precedents and Dependents
type: docs
weight: 230
url: /java/precedents-and-dependents/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Complex financial worksheets, especially ones developed in collaboration, can hide the most embarrassing errors. Checking formulas for accuracy and finding the source of an error can be difficult when the formula uses precedent cells and dependent cells.

{{% /alert %}} 
## **Introduction**
- **Precedent cells** are cells that are referred to by a formula in another Cell. For example, if cell D10 contains the formula =B5, cell B5 is a precedent to cell D10.
- **Dependent cells** contain formulas that refer to other cells. For example, if cell D10 contains the formula =B5, cell D10 is dependent of cell B5.

To make the spreadsheet easy to read, you might want to clearly show which cells on a spreadsheet are used in a formula. Similarly, you may want to extract the dependent cells of other cells.

Aspose.Cells allows you to trace cells and find out which are linked.
## **Tracing Precedent and Dependent Cells: Microsoft Excel**
Formulas may change based on modifications made by a client. For example, if cell C1 is dependent on C3 and C4 containing a formula, and C1 is changed (so the formula is overridden), C3 and C4, or other cells, need to change to balance the spreadsheet based on business rules.

Similarly, suppose C1 contains the formula "=(B1*22)/(M2*N32)". I want to find the cells that C1 depends on, that is the precedent cells B1, M2, and N32.

You might need to trace the dependency of a particular cell to other cells. If business rules are embedded in formulas, we would like to find out the dependency and execute some rules based on it. Similarly, if the value of a particular cell is modified, which cells in the worksheet are impacted by that change?

Microsoft Excel allows users to trace precedents and dependents.

1. On the **View Toolbar**, select **Formula Auditing**. The Formula Auditing dialog will be displayed.
1. Trace Precedents:
   1. Select the cell that contains the formula for which you want to find precedent cells.
   1. To display a tracer arrow to each cell that directly provides data to the active cell, click **Trace Precedents** on the **Formula Auditing** toolbar.
1. Trace formulas that reference a particular cell (dependents)
   1. Select the cell for which you want to identify the dependent cells.
   1. To display a tracer arrow to each cell that is dependent on the active cell, click Trace Dependents on the Formula Auditing toolbar.
## **Tracing Precedent and Dependent Cells: Aspose.Cells**
### **Tracing Precedents**
Aspose.Cells makes it easy to get precedent cells. Not only can it retrieve cells that provide data to simple formula precedents but also find cells that provide data to complex formula precedents with named ranges.

In the example below, a template excel file, Book1.xls, is used. The spreadsheet has data and formulas on the first Worksheet.

Aspose.Cells provides the [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) class' [GetPrecedents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedents--) method used to trace a cell's precedents. It returns a [ReferredAreaCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredAreaCollection). As you can see above, in Book1.xls, cell B7 contains a formula "=SUM(A1:A3)". So cells A1:A3 are the precedent cells to cell B7. The following example demonstrates the tracing precedents feature using the template file Book1.xls.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingPrecedents.java" >}}
### **Tracing Dependents**
Aspose.Cells lets you get dependent cells in spreadsheets. Aspose.Cells not only can retrieve cells that provide data regarding a simple formula but also find cells that provide data to a complex formula dependents with named ranges.

Aspose.Cells provides the [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) class' [GetDependents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependents-boolean-) method used to trace a cell's dependents. For example, in Book1.xlsx there are formulas: "=A1+20" and "=A1+30" in the B2 and C2 cells respectively. The following example demonstrates how to trace the dependents for the A1 cell using the template file Book1.xlsx.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependents.java" >}}
### **Tracing Precedent and Dependent cells according to calculation chain**
Above apis of tracing precedents and dependents are according to the formula expression itself. They simply provide convenient way for user to trace interdependencies for a few formulas. If there are large amount of formulas in the workbook and user needs to trace precedents and dependents for every cell, they will give poor performance. For such situation, user should consider to use [GetPrecedentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedentsInCalculation--) and [GetDependentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependentsInCalculation-boolean-) methods. These two methods trace dependencies according to the calculation chain. So, to use them, firstly you need to enable the calculation chain by [Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/java/com.aspose.cells/FormulaSettings#EnableCalculationChain). Then you should perform full calculation for the Workbook by [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions-). After that, you can trace precedents or dependents for all those cells you need.

For some formulas, the resultant precedents may be different for GetPrecedents and GetPrecedentsInCalculation, and the resultant dependents may be different for GetDependents and GetDependentsInCalculation. For example, if cell A1's formula is "=IF(TRUE,B2,C3)", GetPrecedents will provide B2 and C3 as A1's precedent. Accordingly, B2 and C3 both have the dependent A1 when checking by GetDependents. However, for the  calculation of this formula, it is obvious that only B2 can affect the calculated result. So GetPrecedentsInCalculation will not provide C3 for A1, and GetDependentsInCalculation will not provide A1 for C3. Sometimes user may just has the requirement of tracing those interdependencies that actually affect the calculated result of formulas based on current data of the Workbook, then they also need to use GetDependentsInCalculation/GetPrecedentsInCalculation instead of GetDependents/GetPrecedents.

The following example demonstrates how to trace the precedents and dependents according to calculation chain for cells:


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependenciesInCalculation.java" >}}
{{< app/cells/assistant language="java" >}}
