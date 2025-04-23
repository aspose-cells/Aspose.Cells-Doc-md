---
title: 在数据透视表中处理数据字段的数据显示格式
type: docs
weight: 140
url: /zh/net/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells支持数据透视表中所有数据字段的数据显示格式。

{{% /alert %}}

## **“从最小到最大的排名”和“从最大到最小的排名”显示格式选项**

ASpose.Cells提供了设置数据透视字段显示格式选项的功能。为此，API提供了[**PivotField.ShowValuesSetting.CalculationType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotshowvaluessetting/calculationtype/)属性。为了从最大到最小排名，您可以将[**PivotField.ShowValuesSetting.CalculationType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotshowvaluessetting/calculationtype/)属性设置为[**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfielddatadisplayformat)。以下代码片段演示了设置显示格式选项。

可从此处下载示例源文件和输出文件以测试示例代码:

[源 Excel 文件]（101089332.xlsx）

[输出 Excel 文件]（101089333.xlsx）

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTables-PivotTableDataDisplayFormatRanking-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
