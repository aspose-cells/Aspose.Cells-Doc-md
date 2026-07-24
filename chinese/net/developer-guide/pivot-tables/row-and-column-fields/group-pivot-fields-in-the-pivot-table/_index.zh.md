---
title: 在透视表中对透视字段进行分组
type: docs
weight: 80
url: /zh/net/group-pivot-fields-in-the-pivot-table/
---

## **可能的使用场景**

Microsoft Excel允许您对透视表的透视字段进行分组。当与透视字段相关的数据量很大时，通常将它们分组成部分很有用。Aspose.Cells也提供使用[**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/)方法的此功能。

## **在透视表中对透视字段进行分组**

以下示例代码加载[示例Excel文件](64716818.xlsx)，并使用[**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/)方法对第一个透视字段执行分组。然后刷新和计算透视表的数据，并将工作簿保存为[输出Excel文件](64716817.xlsx)。屏幕截图显示了示例代码对示例Excel文件的效果。如屏幕截图所示，第一个透视字段现在按月份和季度分组。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}
