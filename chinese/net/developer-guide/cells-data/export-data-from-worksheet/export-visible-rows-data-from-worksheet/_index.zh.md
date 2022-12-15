---
title: 从工作表导出可见行数据
type: docs
weight: 10
url: /zh/net/export-visible-rows-data-from-worksheet/
---
{{% alert color="primary" %}}

您可以使用 Aspose.Cells 将工作表中的数据导出到数据表中。有时您只想导出可见行的数据。 Aspose.Cells 提供了实现此目的的方法。使用[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)指定您只想导出可见行数据。

{{% /alert %}}

此示例说明如何从以下工作表中导出数据。第 5、6 和 7 行被隐藏。

|**工作表中的样本数据，第 5、6 和 7 行被隐藏**|
|:- |
|![待办事项：图像_替代_文本](export-visible-rows-data-from-worksheet_1.png)|

使用数据导出到数据表后[**工作表.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)方法与[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)选项，它看起来像这样。隐藏行被绘制为空行

|**隐藏行作为空白行导出到数据表**|
|:- |
|![待办事项：图像_替代_文本](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
