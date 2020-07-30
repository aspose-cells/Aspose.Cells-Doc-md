---
title : "Precedents and Dependents" 
description : "" 
weight : 12035 
toc : false
type: docs
url: /cpp/developerguide/data/precedents+and+dependents/
---

# Aspose.Cells for C++ : Precedents and Dependents


Complex financial worksheets, especially ones developed in collaboration, can hide the most embarrassing errors. Checking formulas for accuracy and finding the source of an error can be difficult when the formula uses precedent cells and dependent cells.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#introduction)
*   2 [Tracing Precedent and Dependent Cells: Microsoft Excel](#tracing-precedent-and-dependent-cells:-microsoft-excel)
*   3 [Tracing Precedent and Dependent Cells: Aspose.Cells](#tracing-precedent-and-dependent-cells:-aspose.cells)
    *   3.1 [Tracing Precedents](#tracing-precedents)
    *   3.2 [Tracing Dependents](#tracing-dependents)
{{< /panel >}}
 

## Introduction

*   **Precedent cells** are cells that are referred to by a formula in another cell. For example, if cell D10 contains the formula =B5, cell B5 is a precedent to cell D10.

*   **Dependent cells** contain formulas that refer to other cells. For example, if cell D10 contains the formula =B5, cell D10 is dependent of cell B5.

To make the spreadsheet easy to read, you might want to clearly show which cells on a spreadsheet are used in a formula. Similarly, you may want to extract the dependent cells of other cells.

Aspose.Cells allows you to trace cells and find out which are linked.

## Tracing Precedent and Dependent Cells: Microsoft Excel

Formulas may change based on modifications made by a client. For example, if cell C1 is dependent on C3 and C4 containing a formula, and C1 is changed (so the formula is overridden), C3 and C4, or other cells, need to change to balance the spreadsheet based on business rules.

Similarly, suppose C1 contains the formula "=(B1\*22)/(M2\*N32)". I want to find the cells that C1 depends on, that is the precedent cells B1, M2, and N32.

You might need to trace the dependency of a particular cell to other cells. If business rules are embedded in formulas, we would like to find out the dependency and execute some rules based on it. Similarly, if the value of a particular cell is modified, which cells in the worksheet are impacted by that change?

Microsoft Excel allows users to trace precedents and dependents.

1.  On the **View Toolbar**, select **Formula Auditing**
2.  Trace Precedents:
    1.  Select the cell that contains the formula for which you want to find precedent cells.
    2.  To display a tracer arrow to each cell that directly provides data to the active cell, click **Trace Precedents** on the **Formula Auditing** toolbar.
3.  Trace formulas that reference a particular cell (dependents)
    1.  Select the cell for which you want to identify the dependent cells.
    2.  To display a tracer arrow to each cell that is dependent on the active cell, click Trace Dependents on the Formula Auditing toolbar.

## Tracing Precedent and Dependent Cells: Aspose.Cells

### Tracing Precedents

Aspose.Cells makes it easy to get precedent cells. Not only can it retrieve cells that provide data to simple formula precedents but also find cells that provide data to complex formula precedents with named ranges.

### Tracing Dependents

Aspose.Cells lets you get dependent cells in spreadsheets. Aspose.Cells can not only retrieve cells that provide data regarding a simple formula but also find cells that provide data to complex formula dependents with named ranges.

