---
title: 重用样式对象
description: 在 Aspose.Cells for .NET 中，通过创建和使用可重用的样式对象，您可以简化样式管理并提高代码效率。我们的指南将帮助您利用可重用样式对象的优势，并将它们在您的应用中实现。
keywords: Aspose.Cells for .NET，重用样式对象，样式管理，代码效率，可重用样式，应用开发，API 参考，示例代码，下载，支持。
type: docs
weight: 3000
url: /zh/net/reusing-style-objects/
---

{{% alert color="primary" %}}

重用样式对象可以节省内存并加快程序运行速度。

{{% /alert %}}

若要对工作表中的大范围单元格应用一些格式设置：

1. 创建一个样式对象。
1. 指定属性。
1. 将样式应用于范围中的单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

由于 [**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) 方法占用的内存明显较少，并且效率更高，旧的 Cell.Style 属性在 Aspose.Cells 7.1.0 版本中已被移除，因为它消耗了大量不必要的内存。

{{% /alert %}}
