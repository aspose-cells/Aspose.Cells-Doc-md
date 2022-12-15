---
title: 数据透视表中的分组数据透视字段
type: docs
weight: 90
url: /zh/java/group-pivot-fields-in-the-pivot-table/
---
## **可能的使用场景**

Microsoft Excel 允许您对数据透视表的数据透视字段进行分组。当有大量数据与数据透视字段相关时，将它们分组到部分通常很有用。 Aspose.Cells 也使用[**数据透视表.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)） 方法。

## **数据透视表中的分组数据透视字段**

下面的示例代码加载[示例 Excel 文件](64716838.xlsx)并使用[**数据透视表.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)） 方法。然后刷新并计算数据透视表的数据，并将工作簿保存为[输出Excel文件](64716837.xlsx).屏幕截图显示了示例代码对示例 Excel 文件的影响。正如您在屏幕截图中看到的，第一个数据透视字段现在按月和季度分组。

![待办事项：图像_替代_文本](group-pivot-fields-in-the-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
