---
title: Get and Set Style for cells
linktitle: Styles
type: docs
weight: 50
url: /net/styling-and-data-formatting/
aliases: [/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/]
---

{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 introduced two new methods for formatting cells: Cell.GetStyle and Cell.SetStyle. This article examines the Cell.GetStyle/SetStyle approach to help you judge which technique best suits you.

{{% /alert %}} 
## **Formatting Cells**
There are two ways to format a cell, illustrated below.
### **Using GetStyle()**
With following piece of code, a Style object is initiated for each cell when formatting it. If ta lot of cells are being formatted, a large amount of memory is consumed because the Style object is a large object. These Style objects won't be freed until the Workbook.Save method is called.



**C#**

{{< highlight csharp >}}

 cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **Using SetStyle()**
The first approach is easy and straight-forward so why did we add the second approach?

We added the second approach to optimize memory usage. After using the Cell.GetStyle method to retrieve a Style object, modify it and use the Cell.SetStyle method to set the it back to this cell. This Style object won't be preserved and .NET GC collect it when it's not referenced.

When calling the Cell.SetStyle method, the Style object isn't saved for each cell. Instead, we compare this Style object to an internal Style object pool to see if it can be reused. Only Style objects that differ from the existing ones are kept for each Workbook object. This means that there are only several hundred Style objects for each Excel file instead of thousands. For each cell, only an index to the Style object pool is preserved.



**C#**

{{< highlight csharp >}}

 Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);


## **Advance topics**
- [Create Style object using CellsFactory class](/cells/net/create-style-object-using-cellsfactory-class/)
- [Modify an Existing Style](/cells/net/modify-an-existing-style/)
- [Reusing Style Objects](/cells/net/reusing-style-objects/)
- [Using Built-in Styles](/cells/net/using-built-in-styles/)




