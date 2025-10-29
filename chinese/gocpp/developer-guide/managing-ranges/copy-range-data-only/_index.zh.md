---
title: 仅复制范围内的数据，使用C++中的Golang
linktitle: 仅复制范围的数据
type: docs
weight: 600
url: /zh/go-cpp/copy-range-data-only/
description: 学习如何仅复制范围数据而不复制格式，使用Aspose.Cells结合Golang通过C++。
---

{{% alert color="primary" %}}

有时，您需要将数据从一个单元格范围复制到另一个范围，仅复制数据，而不是格式。Aspose.Cells提供了这一功能。

本文提供了一个使用Aspose.Cells复制数据范围的示例代码。

{{% /alert %}}

此示例演示如何：

1. 创建一个工作簿。
1. 在第一个工作表中的单元格中添加数据。
1. 创建[**Range**](https://reference.aspose.com/cells/go-cpp/range/)。
1. 使用指定的格式属性创建一个 [**Style**](https://reference.aspose.com/cells/go-cpp/style/) 对象。
1. 将样式格式应用于范围。
1. 创建另一个单元格范围。
1. 将第一个范围的数据复制到这个第二个范围。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeDataOnly.go" >}}
