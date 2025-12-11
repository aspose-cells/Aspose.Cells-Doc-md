---
title: Add and Reference Named Ranges
type: docs
weight: 120
url: /net/aspose-cells-gridweb/add-and-reference-named-ranges/
keywords: GridWeb,GridName,Names
description: This article introduces how to work with named ranges in GridWeb. 
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Normally, column and row labels are used to uniquely refer to cells, but you can create descriptive names to represent cells, a range of cells, formulas, or constant values. The word **Name** may refer to a string of characters that represents a cell, a range of cells, a formula, or a constant value. For example, use easy‑to‑understand names, such as **Products**, to refer to hard‑to‑understand ranges, such as **Sales!C20:C30**. Labels can be used in formulas that refer to data on the same worksheet; if you want to represent a range on another worksheet, you may use a name. **Named ranges** are one of the most powerful features of Microsoft Excel. Users can assign a name to a range and use that name in formulas. Aspose.Cells.GridWeb supports this feature.

{{% /alert %}} 
## **Adding/Referencing Named Ranges in Formulas**
The GridWeb control provides two classes (GridName and GridNameCollection) for working with named ranges. The following code snippet will help you understand how to create a named range and access it in formulas.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
