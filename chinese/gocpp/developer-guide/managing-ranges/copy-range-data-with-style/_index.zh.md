---
title: 使用C++复制范围数据并保持样式
linktitle: 仅复制范围数据和样式
type: docs
weight: 610
url: /zh/go-cpp/copy-range-data-with-style/
description: 使用Aspose.Cells for C++在Excel文件中复制范围数据，包括单元格样式
---

{{% alert color="primary" %}}

[仅复制范围数据](/cells/zh/cpp/copy-range-data-only/) 说明如何在范围之间复制单元格数据。本文展示如何在复制单元格范围时同时保持其格式样式，使用Aspose.Cells for C++。

{{% /alert %}}

Aspose.Cells提供可以操作范围的类和方法，包括[**CreateRange()**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/)、[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)和[**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)。

本示例演示了如何：

1. 创建一个工作簿
1. 填充单元格数据
1. 创建一个[**Range**](https://reference.aspose.com/cells/go-cpp/range/)
1. 创建并配置一个[**Style**](https://reference.aspose.com/cells/go-cpp/style/)对象
1. 对范围应用样式
1. 创建第二个范围
1. 在范围之间复制格式化数据

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeDataWithStyle.go" >}}
