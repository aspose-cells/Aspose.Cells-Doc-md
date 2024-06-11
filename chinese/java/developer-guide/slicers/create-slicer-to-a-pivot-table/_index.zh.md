---
title: 创建到数据透视表的切片器
type: docs
weight: 10
url: /zh/java/create-slicer-to-a-pivot-table/
---

## **可能的使用场景**
切片器可用于快速过滤数据。它可以用于表格或数据透视表中的数据过滤。Microsoft Excel允许您通过选择表格或数据透视表，然后点击*插入 > 切片器*来创建切片器。Aspose.Cells也允许您使用[Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\))方法创建切片器。
## **为数据透视表创建切片器**
请查看以下示例代码。它加载包含数据透视表的[sample Excel file](67338498.xlsx)，然后基于第一个基本数据透视表字段创建切片器。最后，将工作簿保存为[output XLSX](67338497.xlsx)和[output XLSB](67338496.xlsb)格式。以下截图显示了Aspose.Cells在输出Excel文件中创建的切片器。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
