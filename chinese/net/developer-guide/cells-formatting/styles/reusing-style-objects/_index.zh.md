---
title: 重用样式对象
type: docs
weight: 3000
url: /zh/net/reusing-style-objects/
---
{{% alert color="primary" %}}

重用样式对象可以节省内存并使程序更快。

{{% /alert %}}

将某些格式应用于工作表中的大范围单元格：

1. 创建样式对象。
1. 指定属性。
1. 将样式应用于范围内的单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

因为[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)方法使用的内存少得多，而且效率高，旧的 Cell.Style 属性消耗了大量不必要的内存，随着 Aspose.Cells 7.1.0 的发布被删除。

{{% /alert %}}
