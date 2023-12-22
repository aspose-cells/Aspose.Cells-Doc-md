---
title: 对数据透视表中的数据透视字段进行分组
type: docs
weight: 80
url: /zh/python-net/group-pivot-fields-in-the-pivot-table/
description: 如何使用 Aspose.Cells for Python via .NET 对数据透视表中的数据透视字段进行分组。
keywords: Group Pivot Fields in the Pivot Table.
---
##  **可能的使用场景**

Microsoft Excel 允许您对数据透视表的数据透视字段进行分组。当存在大量与数据透视字段相关的数据时，将它们分组通常很有用。 Aspose.Cells for Python via .NET 也提供此功能，使用[**数据透视表.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float)方法。

##  **对数据透视表中的数据透视字段进行分组**

以下示例代码加载[Excel 文件示例](64716818.xlsx)并使用第一个数据透视字段执行分组[**数据透视表.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float)方法。然后刷新并计算数据透视表的数据并将工作簿保存为[输出Excel文件](64716817.xlsx)。屏幕截图显示了示例代码对示例 Excel 文件的效果。正如您在屏幕截图中看到的，第一个数据透视字段现在按月份和季度分组。

![待办事项：图像_替代_文本](group-pivot-fields-in-the-pivot-table_1.png)

##  **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.py" >}}
