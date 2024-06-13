---
title: 仅复制范围样式
type: docs
weight: 620
url: /zh/python-net/copy-range-style-only/
description: 本文介绍了如何在Python的Aspose.Cells via .NET库中仅复制范围样式。
keywords: Python Excel库，Python如何仅复制范围样式，Python如何使用python excel库仅复制范围样式。
---

{{% alert color="primary" %}}

[仅复制范围数据](/cells/zh/python-net/copy-range-data-only/)和[复制带样式的范围数据](/cells/zh/python-net/copy-range-data-with-style/)解释了如何单独复制数据范围到另一个范围时或完整包含格式时。也可以仅复制格式。本文展示了如何。

{{% /alert %}} 

此示例创建一个工作簿，填充数据并仅复制范围的样式。

1. 创建一个范围。
1. 使用指定的格式属性创建一个 [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) 对象。
1. 将样式格式应用于范围。
1. 创建第二个单元格范围。
1. 将第一个范围的格式复制到第二个范围。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeStyleOnly-1.py" >}}
