---
title: 通过格式化策略获取单元格字符串值
type: docs
weight: 240
url: /zh/python-net/get-cell-string-value-with-format-strategy/
description: 了解如何通过 Aspose.Cells for Python via .NET API 使用带格式和不带格式获取单元格字符串值的方法。
keywords: Python Excel 库，Python 获取带格式和不带格式的单元格字符串值，Python 获取带格式和不带格式的单元格字符串值，Python 获取带格式和不带格式的单元格字符串值
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 提供了一个方法 [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/)，可用于获取带有或没有任何格式的单元格的字符串值。假设您有一个值为 0.012345 的单元格，并且已将其格式化为只显示两位小数。在 Excel 中，它将显示为 0.01。您可以使用 [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) 方法检索字符串值，值可以是 0.01 也可以是 0.012345。它接受 [**CellValueFormatStrategy**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvalueformatstrategy/) 枚举作为参数，该枚举具有以下值：

- CellValueFormatStrategy.CELL_STYLE
- CellValueFormatStrategy.DISPLAY_STYLE
- CellValueFormatStrategy.DISPLAY_STRING
- CellValueFormatStrategy.NONE

{{% /alert %}}

以下示例代码解释了使用[**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/)方法的用法。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetStringValueWithOrWithoutFormatting.py" >}}
{{< app/cells/assistant language="python-net" >}}
