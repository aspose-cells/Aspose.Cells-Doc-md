---
title: Precedents and Dependents
type: docs
weight: 230
url: /net/precedents-and-dependents/
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

Aspose.Cells provides the [Cell](https://apireference.aspose.com/cells/net/aspose.cells/cell) class' [GetPrecedents](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedents) method used to trace a cell's precedents. It returns a [ReferredAreaCollection](https://apireference.aspose.com/cells/net/aspose.cells/referredareacollection). As you can see above, in Book1.xls, cell B7 contains a formula "=SUM(A1:A3)". So cells A1:A3 are the precedent cells to cell B7. The following example demonstrates the tracing precedents feature using the template file Book1.xls.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingPrecedents-1.cs" >}}
### **Tracing Dependents**
Aspose.Cells lets you get dependent cells in spreadsheets. Aspose.Cells can not only can retrieve cells that provide data regarding a simple formula but also find cells that provide data to a complex formula dependents with named ranges.

Aspose.Cells provides the [Cell](https://apireference.aspose.com/cells/net/aspose.cells/cell) class' [GetDependents](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/getdependents) method used to trace a cell's dependents. For example, in Book1.xlsx there are formulas: "=A1+20" and "=A1+30" in the B2 and C2 cells respectively. The following example demonstrates how to trace the dependents for the A1 cell using the template file Book1.xlsx.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependents-1.cs" >}}
