---
title: Get and Set Style for cells with Golang via C++
linktitle: Styles
type: docs
weight: 50
url: /go-cpp/styling-and-data-formatting/
description: Discover how to perform data formatting and styling in Aspose.Cells for C++, including text formatting, number formatting, date formatting, and other styling options. Our guide will help you create professional-looking spreadsheets with attractive formatting.
keywords: Aspose.Cells for C++, data formatting, styling, text formatting, number formatting, date formatting, styling options, spreadsheets, attractive formatting, professional-looking.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ introduced two new methods for formatting cells: `Cell.GetStyle` and `Cell.SetStyle`. This article examines the `Cell.GetStyle`/`SetStyle` approach to help you judge which technique best suits you.

{{% /alert %}}

## **Formatting Cells**
There are two ways to format a cell, illustrated below.

### **Using GetStyle()**
With the following piece of code, a `Style` object is initiated for each cell when formatting it. If a lot of cells are being formatted, a large amount of memory is consumed because the `Style` object is a large object. These `Style` objects won't be freed until the `Workbook.Save` method is called.

**C++**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-Styles.go" >}}
### **Using SetStyle()**
The first approach is easy and straightforward, so why did we add the second approach?

We added the second approach to optimize memory usage. After using the `Cell.GetStyle` method to retrieve a `Style` object, modify it and use the `Cell.SetStyle` method to set it back to this cell. This `Style` object won't be preserved, and the C++ runtime will collect it when it's not referenced.

When calling the `Cell.SetStyle` method, the `Style` object isn't saved for each cell. Instead, we compare this `Style` object to an internal `Style` object pool to see if it can be reused. Only `Style` objects that differ from the existing ones are kept for each `Workbook` object. This means that there are only several hundred `Style` objects for each Excel file instead of thousands. For each cell, only an index to the `Style` object pool is preserved.

**C++**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-Styles-1.go" >}}
## **Advanced Topics**
- [Create Style object using CellsFactory class](/cells/cpp/create-style-object-using-cellsfactory-class/)
- [Modify an Existing Style](/cells/cpp/modify-an-existing-style/)
- [Reusing Style Objects](/cells/cpp/reusing-style-objects/)
- [Using Built-in Styles](/cells/cpp/using-built-in-styles/)