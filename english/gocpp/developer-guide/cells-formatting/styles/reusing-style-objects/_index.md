---
title: Reusing Style Objects with Golang via C++
linktitle: Reusing Style Objects
description: In Aspose.Cells for C++, by creating and using reusable style objects, you can simplify style management and improve code efficiency. Our guide will help you leverage the advantages of reusable style objects and implement them in your application.
keywords: Aspose.Cells for C++, Reusing Style Objects, Style Management, Code Efficiency, Reusable Styles, Application Development, API Reference, Example Code, Download, Support.
type: docs
weight: 3000
url: /go-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

Reusing style objects can save memory and make a program faster.

{{% /alert %}}

To apply some formatting to a large range of cells in a worksheet:

1. Create a style object.  
2. Specify the attributes.  
3. Apply the style to the cells in the range.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReusingStyleObjects.go" >}}
{{% alert color="primary" %}}

Because the **Cell.GetStyle**/​**Cell.SetStyle** approach uses far less memory and is efficient, the older **Cell.Style** property, which consumed a lot of unnecessary memory, was removed with the release of Aspose.Cells 7.1.0.

{{% /alert %}}