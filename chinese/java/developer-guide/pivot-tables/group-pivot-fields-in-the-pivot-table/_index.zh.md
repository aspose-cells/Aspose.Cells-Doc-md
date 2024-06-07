---
title: 在数据透视表中对数据透视字段进行分组
type: docs
weight: 90
url: /zh/java/group-pivot-fields-in-the-pivot-table/
---

## **可能的使用场景**

Microsoft Excel允许您分组数据透视表的数据字段。当存在大量数据关联到数据透视表字段时，通常将它们分组为多个部分是有益的。Aspose.Cells也使用[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)）方法提供了此功能。

## **在数据透视表中对数据透视字段进行分组**

以下示例代码加载了[sample Excel文件](64716838.xlsx)，并使用[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)）方法对第一个数据透视表字段进行分组。然后刷新和计算数据透视表的数据，并将工作簿另存为[output Excel文件](64716837.xlsx)。屏幕截图显示了样本代码对样本Excel文件的影响。从截图中可以看出，数据透视表的第一个数据字段现在按月份和季度分组。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
