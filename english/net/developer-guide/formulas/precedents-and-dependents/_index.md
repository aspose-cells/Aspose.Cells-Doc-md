---
title: Precedents and Dependents
type: docs
weight: 230
url: /net/precedents-and-dependents/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Complex financial worksheets, especially ones developed in collaboration, can hide the most embarrassing errors. Checking formulas for accuracy and finding the source of an error can be difficult when the formula uses precedent cells and dependent cells.

{{% /alert %}} 

## **Introduction**
- **Precedent cells** are cells that are referred to by a formula in another cell. For example, if cell D10 contains the formula `=B5`, cell B5 is a precedent to cell D10.  
- **Dependent cells** contain formulas that refer to other cells. For example, if cell D10 contains the formula `=B5`, cell D10 is dependent on cell B5.  

To make the spreadsheet easy to read, you might want to clearly show which cells on a spreadsheet are used in a formula. Similarly, you may want to extract the dependent cells of other cells.

Aspose.Cells allows you to trace cells and find out which are linked.

## **Tracing Precedent and Dependent Cells: Microsoft Excel**
Formulas may change based on modifications made by a client. For example, if cell C1 depends on C3 and C4, and C1 is changed (so the formula is overridden), C3 and C4—or other cells—need to change to balance the spreadsheet based on business rules.

Similarly, suppose C1 contains the formula `=(B1*22)/(M2*N32)`. I want to find the cells that C1 depends on, that is, the precedent cells B1, M2, and N32.

You might need to trace the dependency of a particular cell to other cells. If business rules are embedded in formulas, we would like to find out the dependency and execute some rules based on it. Likewise, if the value of a particular cell is modified, which cells in the worksheet are impacted by that change?

Microsoft Excel allows users to trace precedents and dependents.

1. On the **View Toolbar**, select **Formula Auditing**. The Formula Auditing dialog will be displayed.  
2. **Trace Precedents**:  
   1. Select the cell that contains the formula for which you want to find precedent cells.  
   2. To display a tracer arrow to each cell that directly provides data to the active cell, click **Trace Precedents** on the **Formula Auditing** toolbar.  
3. **Trace Dependents**:  
   1. Select the cell for which you want to identify the dependent cells.  
   2. To display a tracer arrow to each cell that is dependent on the active cell, click **Trace Dependents** on the **Formula Auditing** toolbar.

## **Tracing Precedent and Dependent Cells: Aspose.Cells**
### **Tracing Precedents**
Aspose.Cells makes it easy to get precedent cells. Not only can it retrieve cells that provide data to simple‑formula precedents, but it can also find cells that provide data to complex‑formula precedents with named ranges.

In the example below, a template Excel file, **Book1.xls**, is used. The spreadsheet has data and formulas on the first worksheet.

Aspose.Cells provides the [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) class's [GetPrecedents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedents) method, which returns a [ReferredAreaCollection](https://reference.aspose.com/cells/net/aspose.cells/referredareacollection). As you can see, in **Book1.xls** cell **B7** contains the formula `=SUM(A1:A3)`. Thus, cells **A1:A3** are the precedent cells to cell **B7**. The following example demonstrates the tracing‑precedents feature using the template file **Book1.xls**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingPrecedents-1.cs" >}}

### **Tracing Dependents**
Aspose.Cells lets you get dependent cells in spreadsheets. Not only can it retrieve cells that provide data for a simple formula, but it can also find cells that provide data for a complex‑formula dependent with named ranges.

Aspose.Cells provides the [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) class's [GetDependents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependents) method. For example, in **Book1.xlsx** there are formulas `=A1+20` and `=A1+30` in cells **B2** and **C2**, respectively. The following example demonstrates how to trace the dependents for cell **A1** using the template file **Book1.xlsx**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependents-1.cs" >}}

### **Tracing Precedent and Dependent Cells According to the Calculation Chain**
The above APIs for tracing precedents and dependents are based on the formula expression itself. They simply provide a convenient way for the user to trace inter‑dependencies for a few formulas. If there are a large number of formulas in the workbook and the user needs to trace precedents and dependents for every cell, performance may suffer. In such situations, the user should consider using the [GetPrecedentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedentsincalculation/) and [GetDependentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependentsincalculation/) methods.

These two methods trace dependencies according to the calculation chain. To use them:

1. Enable the calculation chain by setting `Workbook.Settings.FormulaSettings.EnableCalculationChain`.  
2. Perform a full calculation for the workbook by calling `Workbook.CalculateFormula()`.  
3. After that, you can trace precedents or dependents for any cells you need.

For some formulas, the resultant precedents may differ between **GetPrecedents** and **GetPrecedentsInCalculation**, and the resultant dependents may differ between **GetDependents** and **GetDependentsInCalculation**. For example, if cell **A1**'s formula is `=IF(TRUE,B2,C3)`, **GetPrecedents** will return **B2** and **C3** as A1's precedents. Accordingly, both **B2** and **C3** have the dependent **A1** when checked by **GetDependents**. However, for the actual calculation of this formula, only **B2** can affect the result. Therefore, **GetPrecedentsInCalculation** will not return **C3** for **A1**, and **GetDependentsInCalculation** will not return **A1** for **C3**.

Sometimes a user may simply have the requirement to trace only those inter‑dependencies that actually affect the calculated result of formulas based on the current data in the workbook; in such cases, they should use **GetDependentsInCalculation**/**GetPrecedentsInCalculation** instead of **GetDependents**/**GetPrecedents**.

The following example demonstrates how to trace precedents and dependents according to the calculation chain for specific cells:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependenciesInCalculation.cs" >}}
{{< app/cells/assistant language="csharp" >}}
