---
title: Line Breaks and Text Wrapping
description: How to implement text wrapping and word wrap using the Aspose.Cells for Python via .NET library. By using the Aspose.Cells for Python via .NET library, you can easily insert text in cells and set the text wrapping method, such as manual word wrap, word wrap, etc. This document details how to implement these features and provides sample code for your reference.
keywords: Aspose.Cells for Python via .NET, line breaks, text wraps, text layout
type: docs
weight: 60
url: /python-net/line-breaks-and-text-wrapping/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

To ensure that text in a cell can be read, explicit line breaks and text wrapping can be applied. Text wrapping turns one line into several in a cell, which explicit line breaks put in breaks exactly where you want them.

{{% /alert %}}

## **To Wrap Text in a Cell**

To wrap text in a cell, use the [**Style.is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) property.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

## **To Use Explicit Line Breaks**

You can use ‘\n’ in C# and ‘ vbLf’ in VB.NET to insert explicit line breaks in a cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-UseExplicitLineBreaks-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
