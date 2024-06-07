---
title: 带样式复制范围数据
type: docs
weight: 610
url: /zh/net/copy-range-data-with-style/
---

{{% alert color="primary" %}}

[仅复制区域数据](/cells/zh/net/copy-range-data-only/)解释了如何将一系列单元格的数据复制到另一个区域。具体地，该过程为复制的单元格应用了一组新样式。Aspose.Cells也可以复制带有格式的范围。本文说明了如何进行操作。

{{% /alert %}}

Aspose.Cells提供一系列用于处理范围的类和方法，例如[**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)、[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)和[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle)。

本例：

1. 创建一个工作簿。
1. 在第一个工作表中的多个单元格中填充数据。
1. 创建[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)。
1. 使用指定格式属性创建[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象。
1. 将样式应用到数据范围。
1. 创建第二个单元格范围。
1. 将第一个范围的数据与格式复制到第二个范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
