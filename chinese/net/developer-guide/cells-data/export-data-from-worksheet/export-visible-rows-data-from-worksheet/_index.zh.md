---
title: 从工作表导出可见行数据
type: docs
weight: 10
url: /zh/net/export-visible-rows-data-from-worksheet/
description: 通过Aspose.Cells for .NET API学习如何通过工作表导出可见行数据。
keywords: 将可见行数据导出到数据表，将可见行数据导出到数据表，将行数据导出到数据表并排除隐藏行，导出工作表数据到数据表时忽略隐藏行
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells将工作表中的数据导出到数据表。有时您只想导出可见行的数据。Aspose.Cells提供了实现这一目标的方法。使用[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)指定您只想导出可见行数据。

{{% /alert %}}

此示例显示如何从以下工作表导出数据。行5、6和7被隐藏。

|**工作表中的示例数据，行5、6和7被隐藏**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

将数据导出到数据表使用[**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)方法，[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)选项，它看起来像这样。隐藏行被绘制为空行

|**将隐藏行导出到数据表作为空行**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
