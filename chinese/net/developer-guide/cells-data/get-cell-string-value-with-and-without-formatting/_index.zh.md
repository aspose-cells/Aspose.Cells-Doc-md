---
title: 获取单元格字符串值及其格式化值
type: docs
weight: 240
url: /zh/net/get-cell-string-value-with-and-without-formatting/
description: 通过Aspose.Cells for .NET API 学习如何获取单元格字符串值及其格式化值。
keywords: 获取具有和不具有格式化的单元格字符串值
---

{{% alert color="primary" %}}

Aspose.Cells提供了一个[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法，可用于获取单元格的字符串值，无论是否有任何格式化。假设您有一个值为0.012345的单元格，您已将其格式化为仅显示两位小数。在Excel中会显示为0.01。您可以使用[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法检索字符串值，同时显示0.01和0.012345。它将[**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy/)枚举作为参数，该枚举具有以下值

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

以下示例代码解释了[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法的用法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
