---
title: 仅复制范围样式
type: docs
weight: 620
url: /zh/net/copy-range-style-only/
---

{{% alert color="primary" %}}

[仅复制区域数据](/cells/zh/net/copy-range-data-only/)和[复制区域数据及样式](/cells/zh/net/copy-range-data-with-style/)解释了如何将数据从一个范围复制到另一个范围，可以单独进行操作或一起复制包括格式在内。也可以只复制格式。本文展示了操作方法。

{{% /alert %}} 

本例会创建工作簿，填充数据并仅复制范围的样式。

1. 创建一个范围。
1. 使用指定格式属性创建[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象。
1. 应用样式格式到范围。
1. 创建第二个单元格范围。
1. 将第一个范围的格式复制到第二个范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeStyleOnly-1.cs" >}}
