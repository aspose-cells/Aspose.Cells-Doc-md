---
title: 仅复制范围数据和样式
type: docs
weight: 610
url: /zh/net/copy-range-data-with-style/
---

{{% alert color="primary" %}}

[仅复制范围数据](/cells/zh/net/copy-range-data-only/) 解释了如何将数据从一个单元格范围复制到另一个范围。具体来说，它处理了对复制单元格应用的新样式集。Aspose.Cells还可以复制带有格式的范围。本文解释了如何做到这一点。

{{% /alert %}}

Aspose.Cells提供了一系列用于处理范围的类和方法，例如 [**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)、[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) 和 [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle)。

此示例：

1. 创建一个工作簿。
1. 在第一个工作表中填充多个单元格的数据。
1. 创建一个 [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)。
1. 使用指定的格式属性创建一个 [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) 对象。
1. 将样式应用到数据范围。
1. 创建第二个单元格范围。
1. 将第一个范围的带有格式的数据复制到第二个范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
