---
title: Line Breaks and Text Wrapping
description: How to implement text wrapping and word wrap using the Aspose.Cells library in C#. By using the Aspose.Cells library, you can easily insert text in cells and set the text wrapping method, such as manual word wrap, word wrap, etc. This document details how to implement these features and provides sample code for your reference.
keywords: Aspose.Cells, line breaks, text wraps, text layout
type: docs
weight: 60
url: /python-net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

To ensure that text in a cell can be read, explicit line breaks and text wrapping can be applied. Text wrapping turns one line into several in a cell, which explicit line breaks put in breaks exactly where you want them.

{{% /alert %}}

## **To Wrap Text in a Cell**

To wrap text in a cell, use the [**Aspose.Cells.Style.is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **To Use Explicit Line Breaks**

You can use ‘\n’ in C# and ‘ vbLf’ in VB.NET to insert explicit line breaks in a cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
