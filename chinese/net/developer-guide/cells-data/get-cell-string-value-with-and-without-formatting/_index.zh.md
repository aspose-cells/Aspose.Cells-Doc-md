---
title: 获取 Cell 带格式和不带格式的字符串值
type: docs
weight: 240
url: /zh/net/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}}

Aspose.Cells提供方法[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)可用于获取带或不带任何格式的单元格的字符串值。假设您有一个值为 0.012345 的单元格，并且您已将其格式化为仅显示两位小数。然后它将在 Excel 中显示为 0.01。您可以使用 0.01 和 0.012345 检索字符串值[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法。它需要[**CellValueFormat策略**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)枚举作为具有以下值的参数

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

下面的示例代码解释了使用[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
