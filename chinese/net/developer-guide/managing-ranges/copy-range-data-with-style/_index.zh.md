---
title: 使用样式复制范围数据
type: docs
weight: 610
url: /zh/net/copy-range-data-with-style/
---
{{% alert color="primary" %}}

[仅复制范围数据](/cells/zh/net/copy-range-data-only/)解释了如何将数据从一个单元格区域复制到另一个区域。具体来说，它会将一组新样式应用于复制的单元格。 Aspose.Cells 还可以复制带格式的范围。这篇文章解释了如何。

{{% /alert %}}

Aspose.Cells 提供了一系列用于处理范围的类和方法，例如，[**创建范围()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**风格旗帜**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)和[**应用样式()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

这个例子：

1. 创建工作簿。
1. 用数据填充第一个工作表中的多个单元格。
1. 创建一个[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. 创建一个[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)具有指定格式属性的对象。
1. 将样式应用于数据范围。
1. 创建第二个单元格区域。
1. 将具有格式的数据从第一个范围复制到第二个范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
