---
title: 仅复制范围样式
type: docs
weight: 620
url: /zh/net/copy-range-style-only/
---

{{% alert color="primary" %}}

[仅复制范围数据](/cells/zh/net/copy-range-data-only/) 和 [仅复制范围样式](/cells/zh/net/copy-range-style-only/) 解释了如何单独复制范围数据或包括格式。也可以仅复制格式。本文展示了如何做到。

{{% /alert %}} 

此示例创建一个工作簿，填充数据并仅复制范围的样式。

1. 创建一个范围。
1. 使用指定的格式属性创建一个 [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) 对象。
1. 将样式格式应用于范围。
1. 创建第二个单元格范围。
1. 将第一个范围的格式复制到第二个范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeStyleOnly-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
