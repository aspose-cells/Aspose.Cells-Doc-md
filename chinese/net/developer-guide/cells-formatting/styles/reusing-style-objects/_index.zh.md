---
title: 重用样式对象
description: Aspose.Cells for .NET中，通过创建和使用可重用的样式对象，可以简化样式管理，提高代码效率。我们的指南将帮助您利用可重用样式对象的优势并在您的应用程序中实现它们。
keywords: Aspose.Cells for .NET, Reusing Style Objects, Style Management, Code Efficiency, Reusable Styles, Application Development, API Reference, Example Code, Download, Support.
type: docs
weight: 3000
url: /zh/net/reusing-style-objects/
---
{{% alert color="primary" %}}

重用样式对象可以节省内存并使程序更快。

{{% /alert %}}

要将某些格式应用于工作表中的大范围单元格：

1. 创建一个样式对象。
1. 指定属性。
1. 将样式应用到范围内的单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

因为[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)该方法使用的内存少得多，而且效率高，旧的 Cell.Style 属性消耗了大量不必要的内存，随着 Aspose.Cells 7.1.0 的发布而被删除。

{{% /alert %}}
