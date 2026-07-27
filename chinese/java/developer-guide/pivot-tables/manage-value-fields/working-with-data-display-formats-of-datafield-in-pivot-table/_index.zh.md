---
title: 在数据透视表中处理数据字段的数据显示格式
type: docs
weight: 150
url: /zh/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells支持数据透视表中所有数据字段的数据显示格式。

{{% /alert %}}

## **“从最小到最大的排名”和“从最大到最小的排名”显示格式选项**

Aspose.Cells提供了设置数据透视表字段显示格式选项的功能。为此，API提供了[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat)属性。要按最大到最小排名，您可以将[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat)属性设置为[**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK-LARGEST-TO-SMALLEST)。以下代码片段演示了设置显示格式选项。

可从此处下载示例源文件和输出文件以测试示例代码:

[源Excel文件](PivotTableSample.xlsx)

[输出Excel文件](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
{{< app/cells/assistant language="java" >}}
