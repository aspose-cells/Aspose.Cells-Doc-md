---
title: Managing Page Breaks
type: docs
weight: 30
url: /net/managing-page-breaks/
description: This article provides sample code and explains how to add page breaks, clear page breaks, or delete specific page breaks in Excel worksheets programmatically using the C# API or .NET Library.
keywords: page breaks c#, excel page breaks c#, clear page break c#, delete specific page break c#
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

According to the definition, a page break is a place in a flow of text where one page ends and the next begins. Microsoft Excel lets users add page breaks into any selected cell of a worksheet.

When the page break is added at a cell, the page ends and the rest of the data after the page break is printed on the next page while printing. In simple words, page breaks divide your worksheet into multiple pages according to your specifications. You can also add page breaks to your worksheets at runtime using Aspose.Cells. Aspose.Cells allows developers to add two kinds of page breaks:

- Horizontal page break
- Vertical page break

In the rest of the discussion, we will describe how you can add horizontal or vertical page breaks into your worksheets using Aspose.Cells.

{{% /alert %}}

## **Page Breaks**

Aspose.Cells provides a [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a wide range of properties and methods used to manage a worksheet.

To add the page breaks, use the Worksheet class' [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) and [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) properties.

The [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) and [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) properties are collections that may contain several page breaks. Each collection contains several methods for managing horizontal and vertical page breaks.

### **Adding Page Breaks**

To add a page break in a worksheet, insert vertical and horizontal page breaks at the specified cell by calling the [**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) and [**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) methods. Each **Add** method takes the name of the cell where the break should be added.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

In Page Break Preview or Print Preview modes, you can see how these page breaks work.

{{% /alert %}}

### **Clearing All Page Breaks**

To clear all page breaks in a worksheet, call the **Clear()** methods of the [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) and [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) collections.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **Removing a Specific Page Break**

To remove a specific page break, call the [**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) and [**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) methods. Each **RemoveAt** method takes the index of the page break to be removed.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **Important to Know**

When you set **FitToPages** properties (that is [**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) and [**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) in page‑setup settings, the page‑break settings are affected, so if you print the worksheet, the page‑break settings are not considered although they are still set.
{{< app/cells/assistant language="csharp" >}}
