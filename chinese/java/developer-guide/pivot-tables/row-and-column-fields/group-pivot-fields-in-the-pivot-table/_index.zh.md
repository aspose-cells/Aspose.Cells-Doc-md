---
title: 在透视表中对透视字段进行分组
type: docs
weight: 90
url: /zh/java/group-pivot-fields-in-the-pivot-table/
---

## **可能的使用场景**

Microsoft Excel 允许您对数据透视表的数据字段进行分组。当大量数据与数据透视表的数据字段相关时，将它们分组通常很有用。Aspose.Cells 也提供了使用 [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-) 方法的功能。

## **在透视表中对透视字段进行分组**

下面的示例代码加载了 [示例Excel文件](64716838.xlsx)，并使用 [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-) 方法对第一个数据透视字段进行分组。然后刷新和计算数据透视表的数据，并将工作簿保存为 [输出Excel文件](64716837.xlsx)。屏幕截图显示了示例代码对示例Excel文件的影响。如屏幕截图所示，第一个数据透视字段现在按月份和季度分组。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
