---
title: Get and Set Style for cells
description: Discover how to perform data formatting and styling in Aspose.Cells for JavaScript via C++, including text formatting, number formatting, date formatting, and other styling options. Our guide will help you create professional-looking spreadsheets with attractive formatting.
keywords: Aspose.Cells for JavaScript via C++, data formatting, styling, text formatting, number formatting, date formatting, styling options, spreadsheets, attractive formatting, professional-looking.
linktitle: Styles
type: docs
weight: 50
url: /javascript-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for JavaScript via C++ introduced two new methods for formatting cells: Cell.style and Cell.style. This article examines the Cell.style/style approach to help you judge which technique best suits you.

{{% /alert %}} 
## **Formatting Cells**
There are two ways to format a cell, illustrated below.
### **Using style**
With the following piece of code, a Style object is initiated for each cell when formatting it. If a lot of cells are being formatted, a large amount of memory is consumed because the Style object is a large object. These Style objects won't be freed until the Workbook.save method is called.

**JavaScript**

{{< highlight javascript >}}
cell.style.font.isBold = true;
{{< /highlight >}}
### **Using style**
The first approach is easy and straight-forward so why did we add the second approach?

We added the second approach to optimize memory usage. After using the Cell.style property to retrieve a Style object, modify it and assign it back using the Cell.style property to this cell. This Style object won't be preserved and JavaScript's garbage collector will collect it when it's not referenced.

When assigning the Cell.style property, the Style object isn't saved for each cell. Instead, we compare this Style object to an internal Style object pool to see if it can be reused. Only Style objects that differ from the existing ones are kept for each Workbook object. This means that there are only several hundred Style objects for each Excel file instead of thousands. For each cell, only an index to the Style object pool is preserved.

**JavaScript**

{{< highlight javascript >}}
let style = cell.style;

style.font.isBold = true;

cell.style = style;
{{< /highlight >}}

## **Advance topics**
- [Create Style object using CellsFactory class](/cells/javascript-cpp/create-style-object-using-cellsfactory-class/)
- [Modify an Existing Style](/cells/javascript-cpp/modify-an-existing-style/)
- [Reusing Style Objects](/cells/javascript-cpp/reusing-style-objects/)
- [Using Built-in Styles](/cells/javascript-cpp/using-built-in-styles/)