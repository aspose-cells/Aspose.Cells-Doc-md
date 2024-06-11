---
title: 在透视表中对透视字段进行分组
type: docs
weight: 80
url: /zh/python-net/group-pivot-fields-in-the-pivot-table/
description: 如何使用Aspose.Cells for Python via .NET在数据透视表中对字段进行分组。
keywords: 使用Aspose.Cells for Python Excel库，在数据透视表中对字段进行分组。
---

## **可能的使用场景**

Microsoft Excel允许您对数据透视表中的字段进行分组。当与数据透视表相关的数据量较大时，将它们分组为不同的部分通常很有用。Aspose.Cells for Python via .NET也提供了使用[**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float)方法实现此功能。

## **在数据透视表中对字段进行分组**

以下示例代码加载[示例Excel文件](64716818.xlsx)，并使用[**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float)方法对第一个透视字段执行分组。然后刷新和计算透视表的数据，并将工作簿保存为[输出Excel文件](64716817.xlsx)。屏幕截图显示了示例代码对示例Excel文件的效果。如屏幕截图所示，第一个透视字段现在按月份和季度分组。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.py" >}}
