---
title: 复制行或范围时将图表的数据源更改为目标工作表
description: 了解如何在复制行或范围时将图表的数据源更改为目标工作表 Aspose.Cells for .NET。我们的指南将向您展示如何更新图表的数据范围并将其链接到目标工作表，确保复制的行或范围范围准确地反映在图表中。
keywords: Aspose.Cells for .NET, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /zh/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
##  **可能的使用场景**

将包含图表的行或区域复制到新工作表时，图表的数据源不会更改。例如，如果图表的数据源为=Sheet1!$A$1:$B$4，则将行或范围复制到新工作表后，数据源将保持不变，即=Sheet1!$A$1:$B$4。它仍然引用旧工作表，即 Sheet1。这也是 Microsoft Excel 中的行为。但如果您希望它引用新的目标工作表，那么请使用[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)属性并将其设置为**真的**打电话时[**Cells.复制行()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)方法。现在，如果您的目标工作表是 DestSheet，则图表的数据源将从 =Sheet1!$A$1:$B$4 更改为 =DestSheet!$A$1:$B$4。

##  **复制行或范围时将图表的数据源更改为目标工作表**

下面的示例代码解释了其用法[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)属性，同时将包含图表的行或范围复制到新工作表。该代码使用[示例 Excel 文件](5113699.xlsx)并生成[输出Excel文件](5113697.xlsx).

![待办事项：图像_替代_文本](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
