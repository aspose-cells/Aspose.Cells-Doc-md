---
title: 在数据透视表中对数据透视字段进行分组
type: docs
weight: 80
url: /zh/net/group-pivot-fields-in-the-pivot-table/
---

## **可能的使用场景**

Microsoft Excel允许您对数据透视表的数据透视字段进行分组。当与数据透视字段相关联的数据量很大时，将它们分组为部分通常很有用。Aspose.Cells也提供了使用[**PivotTable.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)方法来实现此功能。

## **在数据透视表中对数据透视字段进行分组**

以下示例代码加载了[示例Excel文件](64716818.xlsx)，并使用[**PivotTable.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)方法对第一个数据透视字段进行分组。然后刷新和计算数据透视表的数据，并将工作簿保存为[输出Excel文件](64716817.xlsx)。屏幕截图显示了示例代码对示例Excel文件的影响。从屏幕截图可以看出，第一个数据透视字段现在按月份和季度分组。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
