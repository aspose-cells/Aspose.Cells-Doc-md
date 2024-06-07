---
title: 在复制行或区域时将图表的数据源更改为目标工作表
description: 学习如何在Aspose.Cells for .NET中复制行或区域时将图表的数据源更改为目标工作表。我们的指南将向您展示如何更新图表的数据范围，并将其链接到目标工作表，确保复制的行或区域在图表中准确反映。
keywords: Aspose.Cells for .NET，图表，数据源，目标工作表，行，区域，复制，更新，数据范围，链接。
type: docs
weight: 440
url: /zh/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **可能的使用场景**

当您复制包含图表的行或区域到新工作表时，图表的数据源不会更改。例如，如果图表的数据源为=Sheet1!$A$1:$B$4，则在将行或区域复制到新工作表后，数据源仍将保持不变，即=Sheet1!$A$1:$B$4。它仍然指向旧工作表即Sheet1。这也是Microsoft Excel中的行为。但如果您希望将其引用新的目标工作表，则请使用[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)属性，并在调用[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)方法时将其设置为true。现在如果您的目标工作表是DestSheet，则您的图表的数据源将从=Sheet1!$A$1:$B$4更改为=DestSheet!$A$1:$B$4。

## **将图表的数据源更改为目标工作表，同时复制行或范围**

以下示例代码解释了在将包含图表的行或区域复制到新工作表时使用[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)属性的用法。该代码使用[sample excel file](5113699.xlsx)并生成[output excel file](5113697.xlsx)。

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
