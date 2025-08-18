---
title: Line Breaks and Text Wrapping with Golang via C++
description: How to implement text wrapping and word wrap using the Aspose.Cells library in C++. By using the Aspose.Cells library, you can easily insert text in cells and set the text wrapping method, such as manual word wrap, word wrap, etc. This document details how to implement these features and provides sample code for your reference.
keywords: Aspose.Cells, line breaks, text wraps, text layout
type: docs
weight: 60
url: /go-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

To ensure that text in a cell can be read, explicit line breaks and text wrapping can be applied. Text wrapping turns one line into several in a cell, which explicit line breaks put in breaks exactly where you want them.

{{% /alert %}}

## **To Wrap Text in a Cell**

To wrap text in a cell, use the [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) property.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-LineBreaksAndTextWrapping.go" >}}
## **To Use Explicit Line Breaks**

You can use ‘\n’ in C++ to insert explicit line breaks in a cell.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-LineBreaksAndTextWrapping-1.go" >}}