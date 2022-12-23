---
title: 为数据透视表创建切片器
type: docs
weight: 10
url: /zh/java/create-slicer-to-a-pivot-table/
---
## **可能的使用场景**
切片器用于快速过滤数据。它可用于过滤表格或数据透视表中的数据。 Microsoft Excel 允许您通过选择表格或数据透视表然后单击*插入 > 切片器*Aspose.Cells 还允许您使用[工作表.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)） 方法。
## **为数据透视表创建切片器**
请参阅以下示例代码。它加载了[示例 Excel 文件](67338498.xlsx)包含数据透视表。然后它根据第一个基本数据透视字段创建切片器。最后，它将工作簿保存在[输出 XLSX](67338497.xlsx)和[输出 XLSB](67338496.xlsb)格式。以下屏幕截图显示了 Aspose.Cells 在输出 Excel 文件中创建的切片器。

![待办事项：图片_替代_文本](create-slicer-to-a-pivot-table_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
