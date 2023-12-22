---
title: 获取带格式和不带格式的 Cell 字符串值
type: docs
weight: 240
url: /zh/net/get-cell-string-value-with-and-without-formatting/
description: 了解如何通过 Aspose.Cells for .NET API 获取带或不带格式化的 Cell 字符串值。
keywords: Get Cell String Value with and without Formatting, Retrieve Cell String Value with and without Formatting, Obtain Cell String Value with and without Formatting
---
{{% alert color="primary" %}}

Aspose.Cells提供方法[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)它可用于获取单元格的字符串值（带或不带任何格式）。假设您有一个值为 0.012345 的单元格，并且您已将其格式化为仅显示两位小数。然后它将在 Excel 中显示为 0.01。您可以使用以下命令检索字符串值：0.01 和 0.012345[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法。它需要[**单元格值格式策略**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)enum 作为参数，具有以下值

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

下面的示例代码解释了使用[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
