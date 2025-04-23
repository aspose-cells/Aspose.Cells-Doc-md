---
title: 获取带格式和不带格式的单元格字符串值
type: docs
weight: 240
url: /zh/net/get-cell-string-value-with-and-without-formatting/
description: 学习如何通过 Aspose.Cells for .NET API 获取带有和不带有格式的单元格字符串值。
keywords: 使用带有格式和不带格式的单元格字符串值，检索带格式和不带格式的单元格字符串值，获取带格式和不带格式的单元格字符串值
---

{{% alert color="primary" %}}

Aspose.Cells提供一个方法[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)，它可用于获取单元格的字符串值，带有或不带有任何格式。假设您有一个单元格，其值为0.012345，并对其进行格式化以仅显示两位小数。那么在Excel中，它将显示为0.01。您可以使用[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法检索字符串值，它会显示为0.01或者0.012345。它接受[**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy/) 枚举作为参数，该枚举具有以下值。

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

以下示例代码解释了使用[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法的用法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
{{< app/cells/assistant language="csharp" >}}
