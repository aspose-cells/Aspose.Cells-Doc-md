---
title: 设置数据透视表格式
type: docs
weight: 10
url: /zh/net/formatting-pivot-table/
description: 如何使用 Aspose.Cells for Python via .NET 格式化数据透视表。
keywords: Format pivot table.
---
##  **数据透视表外观**

如何创建数据透视表解释了如何创建简单的数据透视表。本文介绍如何通过设置各种属性来自定义数据透视表的外观：

- 数据透视表格式选项
- 数据透视表字段格式选项
- 数据字段格式选项

###  **设置数据透视表格式选项**

这[**数据透视表**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)类控制整个数据透视表，并且可以通过多种方式进行格式化。

####  **设置自动套用格式类型**

Microsoft Excel 提供了多种不同的预设报告格式。 Aspose.Cells for Python via .NET 也支持这些格式化选项。要访问它们：

1. 放[**数据透视表.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/)为*真**。
1. 从指定格式选项[**数据透视表自动格式类型**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/)枚举。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

####  **设置格式选项**

下面的代码示例展示了如何设置数据透视表的格式以显示行和列的总计，以及如何设置报表的字段顺序。它还演示了如何为空值设置客户字符串。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

####  **手动格式化外观**

要手动格式化数据透视表报告的外观，请使用[**数据透视表.format_all(样式)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/)和[**数据透视表.format(行、列、样式)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/)方法。为您所需的格式创建一个样式对象，例如：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

###  **设置数据透视字段格式选项**

这[**数据透视字段**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)类表示数据透视表中的字段，可以通过多种方式进行格式化。下面的代码示例展示了如何：

- 访问行字段。
- 设置小计。
- 设置自动排序。
- 设置自动显示。

####  **设置行/列/页字段格式**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

###  **设置数据字段格式**

下面的代码示例展示了如何设置数据字段的显示格式和数字格式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

###  **清除数据透视表字段**

这[**数据透视字段集合**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/)有一个名为[**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#)这允许您清除数据透视表字段。当您想要清除区域中的所有数据透视字段（例如页面、列、行或数据）时，请使用它。
下面的代码示例显示了如何清除数据区域中的所有数据透视字段。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
