---
title: 使用格式策略获取单元格字符串值
type: docs
weight: 240
url: /zh/python-net/get-cell-string-value-with-format-strategy/
description: 学习如何通过Aspose.Cells for Python通过.NET API获取带格式和不带格式的单元格字符串值。
keywords: Python Excel库，Python获取带格式和不带格式的单元格字符串值，Python检索带格式和不带格式的单元格字符串值，Python获取带格式和不带格式的单元格字符串值
---

{{% alert color="primary" %}}

Aspose.Cells for Python通过.NET提供一个方法[**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/)，可用于获取单元格的字符串值，无论是否有任何格式。 假设您有一个带有值0.012345的单元格，并将其格式化为仅显示两位小数。 它将在Excel中显示为0.01。 您可以使用[**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/)方法检索0.01和0.012345两种字符串值。 它接受[**CellValueFormatStrategy**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvalueformatstrategy/) 枚举作为参数，该枚举具有以下值

- CellValueFormatStrategy.CELL_STYLE
- CellValueFormatStrategy.DISPLAY_STYLE
- CellValueFormatStrategy.DISPLAY_STRING
- CellValueFormatStrategy.NONE

{{% /alert %}}

以下示例代码解释了[**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/)方法的用法。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetStringValueWithOrWithoutFormatting.py" >}}
