---
title: 创建到数据透视表的切片器
type: docs
weight: 10
url: /zh/python-java/create-slicer-to-a-pivot-table/
---

## **可能的使用场景**
分层切片器用于快速过滤数据。它们可用于在表或数据透视表中过滤数据。Microsoft Excel允许您通过选择表或数据透视表然后单击*插入 > 分层切片器* 来创建一个分层切片器。Aspose.Cells for Python via Java提供了Worksheet.getSlicers().add()方法来创建分层切片器。
## **为数据透视表创建切片器**
以下代码段加载包含数据透视表的[样本Excel文件](106364966.xlsx)，然后根据第一个基本数据透视字段创建分层切片器。最后，将工作簿保存为[输出XLSX](106364967.xlsx)格式。以下屏幕截图显示了Aspose.Cells在输出Excel文件中创建的分层切片器。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
