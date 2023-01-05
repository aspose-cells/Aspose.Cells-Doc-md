---
title: 为 Excel 表创建切片器
type: docs
weight: 15
url: /zh/java/create-slicer-to-excel-table/
---
## **可能的使用场景**

切片器用于快速过滤数据。它可用于过滤表格或数据透视表中的数据。 Microsoft Excel 允许您通过选择表格或数据透视表然后单击*插入 > 切片器*Aspose.Cells 还允许您使用[**工作表.Slicers.Add()**](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add(com.aspose.cells.ListObject,%20com.aspose.cells.ListColumn,%20int,%20int)） 方法。

## **为 Excel 表创建切片器**

请参阅以下示例代码。它加载了[示例 Excel 文件](sampleCreateSlicerToExcelTable.xlsx)包含一个表。然后它根据第一列创建切片器。最后，它将工作簿保存在[输出 XLSX](outputCreateSlicerToExcelTable.xlsx)格式。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Slicers-CreateSlicerToExcelTable-1.java" >}}
