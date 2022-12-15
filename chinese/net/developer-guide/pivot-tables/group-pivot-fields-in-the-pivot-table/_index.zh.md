---
title: 数据透视表中的分组数据透视字段
type: docs
weight: 80
url: /zh/net/group-pivot-fields-in-the-pivot-table/
---
## **可能的使用场景**

Microsoft Excel 允许您对数据透视表的数据透视字段进行分组。当有大量数据与数据透视字段相关时，将它们分组到部分通常很有用。 Aspose.Cells 也使用[**数据透视表.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)方法。

## **数据透视表中的分组数据透视字段**

下面的示例代码加载[示例 Excel 文件](64716818.xlsx)并使用[**数据透视表.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)方法。然后它刷新并计算数据透视表的数据并将工作簿另存为[输出Excel文件](64716817.xlsx).屏幕截图显示了示例代码对示例 Excel 文件的影响。正如您在屏幕截图中看到的，第一个数据透视字段现在按月和季度分组。

![待办事项：图像_替代_文本](group-pivot-fields-in-the-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
