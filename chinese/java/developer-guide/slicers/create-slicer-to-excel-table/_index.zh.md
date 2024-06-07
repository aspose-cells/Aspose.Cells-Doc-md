---
title: 为Excel表创建切片器
type: docs
weight: 15
url: /zh/java/create-slicer-to-excel-table/
---

## **可能的使用场景**

切片器用于快速过滤数据。它可以用于在表或数据透视表中过滤数据。Microsoft Excel允许您通过选择表或数据透视表，然后单击*插入 > 切片器*来创建切片器。Aspose.Cells也允许您使用[**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add(com.aspose.cells.ListObject,%20com.aspose.cells.ListColumn,%20int,%20int)) 方法来创建切片器。

## **为Excel表创建分割器**

请参阅以下示例代码。它加载包含表格的[示例Excel文件](sampleCreateSlicerToExcelTable.xlsx)。然后基于第一列创建分割器。最后，将工作簿另存为[输出XLSX](outputCreateSlicerToExcelTable.xlsx)格式。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Slicers-CreateSlicerToExcelTable-1.java" >}}
