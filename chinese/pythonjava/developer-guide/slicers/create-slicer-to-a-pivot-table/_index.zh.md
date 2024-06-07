---
title: 为数据透视表创建切片器
type: docs
weight: 10
url: /zh/python-java/create-slicer-to-a-pivot-table/
---

## **可能的使用场景**
切片器用于快速过滤数据。它们可以用来过滤表或数据透视表中的数据。Microsoft Excel允许您通过选择表或数据透视表，然后单击*插入 > 切片器*来创建切片器。通过Java的Aspose.Cells for Python提供了Worksheet.getSlicers().add()方法来创建切片器。
## **为数据透视表创建分割器**
以下代码片段加载包含数据透视表的[示例Excel文件](106364966.xlsx)。然后，根据第一个基本数据透视表字段创建切片器。最后，将工作簿保存为[输出XLSX](106364967.xlsx)格式。下面的屏幕截图显示了Aspose.Cells在生成的Excel文件中创建的切片器。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
