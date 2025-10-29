---
title: 仅复制Golng via C++的范围样式
linktitle: 仅复制范围样式
type: docs
weight: 620
url: /zh/go-cpp/copy-range-style-only/
description: 学习如何使用Aspose.Cells结合Golang通过C++仅复制Excel中的样式。
---

{{% alert color="primary" %}}

[只复制范围数据](/cells/zh/cpp/copy-range-data-only/)和[复制范围数据并带样式](/cells/zh/cpp/copy-range-data-with-style/)讲解了如何单独或完整复制范围中的数据及格式，也可以只复制格式。

{{% /alert %}} 

此示例创建一个工作簿，填充数据并仅复制范围的样式。

1. 创建一个范围。
1. 使用指定的格式属性创建一个 [**Style**](https://reference.aspose.com/cells/go-cpp/style/) 对象。
1. 将样式格式应用于范围。
1. 创建第二个单元格范围。
1. 将第一个范围的格式复制到第二个范围。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeStyleOnly.go" >}}
