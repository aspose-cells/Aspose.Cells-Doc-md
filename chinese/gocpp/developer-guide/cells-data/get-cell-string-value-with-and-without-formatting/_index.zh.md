---
title: 通过C++用Golang获取带格式和不带格式的单元格字符串值
linktitle: 获取单元格字符串值
type: docs
weight: 240
url: /zh/go-cpp/get-cell-string-value-with-and-without-formatting/
description: 学习如何通过 Aspose.Cells for C++ API 获取带格式和不带格式的单元格字符串值。
keywords: 使用带有格式和不带格式的单元格字符串值，检索带格式和不带格式的单元格字符串值，获取带格式和不带格式的单元格字符串值
---

{{% alert color="primary" %}}

Aspose.Cells 提供了 [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) 方法，可以用来获取单元格的字符串值，无论是否带有任何格式。假设你有一个值为0.012345的单元格，并将其格式化为仅显示两位小数，那么在Excel中会显示为0.01。你可以使用 [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) 方法以字符串形式同时获取0.01和0.012345。它接受 [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) 枚举作为参数，具有以下值：

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

以下示例代码解释了使用[**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/)方法的用法。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellStringValueWithAndWithoutFormatting.go" >}}
