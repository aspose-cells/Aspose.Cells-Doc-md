---
title: 在透视表中对透视字段进行分组
type: docs
weight: 90
url: /zh/java/group-pivot-fields-in-the-pivot-table/
---

## **可能的使用场景**

Microsoft Excel允许您对数据透视表的数据进行分组。当与数据透视表相关的数据量较大时，将它们分组成节是很有用的。Aspose.Cells也提供了使用[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)方法来实现此功能。

## **在透视表中对透视字段进行分组**

以下示例代码加载了[示例Excel文件](64716838.xlsx)，并使用[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)方法对第一个数据透视表字段进行分组。然后刷新和计算数据透视表的数据，并将工作簿保存为[输出Excel文件](64716837.xlsx)。屏幕截图显示了示例代码对示例Excel文件的影响。正如您在屏幕截图中看到的，第一个数据透视表字段现在按月份和季度分组。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
