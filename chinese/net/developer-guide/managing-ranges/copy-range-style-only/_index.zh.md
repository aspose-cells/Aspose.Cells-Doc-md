---
title: 仅复制范围样式
type: docs
weight: 620
url: /zh/net/copy-range-style-only/
---
{{% alert color="primary" %}}

[仅复制范围数据](/cells/zh/net/copy-range-data-only/)和[使用样式复制范围数据](/cells/zh/net/copy-range-data-with-style/)解释了如何将数据从一个范围复制到另一个范围或通过格式化完成。也可以只复制格式。本文展示了如何。

{{% /alert %}} 

此示例创建一个工作簿，用数据填充它并仅复制范围的样式。

1. 创建一个范围。
1. 创建一个[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)具有指定格式属性的对象。
1. 将样式格式应用于范围。
1. 创建第二个单元格区域。
1. 将第一个范围的格式复制到第二个范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeStyleOnly-1.cs" >}}
