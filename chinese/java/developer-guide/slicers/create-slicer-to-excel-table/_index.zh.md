---
title: 创建到Excel表格的切片器
type: docs
weight: 15
url: /zh/java/create-slicer-to-excel-table/
---

## **可能的使用场景**

切片器用于快速过滤数据。它可用于在表格或数据透视表中过滤数据。Microsoft Excel允许您通过选择表格或数据透视表，然后单击*插入 > 切片器* 来创建切片器。Aspose.Cells也允许您使用[**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add-com.aspose.cells.ListObject-com.aspose.cells.ListColumn-int-int-)方法创建切片器。

## **为Excel表创建切片器**

请查看以下示例代码。它加载包含数据表的[sample Excel file](sampleCreateSlicerToExcelTable.xlsx)，然后基于第一列创建切片器。最后，将工作簿保存为[output XLSX](outputCreateSlicerToExcelTable.xlsx)格式。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Slicers-CreateSlicerToExcelTable-1.java" >}}
{{< app/cells/assistant language="java" >}}
