---
title: 复制行或范围时将图表的数据源更改为目标工作表
type: docs
weight: 440
url: /zh/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **可能的使用场景**

当您将包含图表的行或范围复制到新工作表时，图表的数据源不会更改。例如，如果图表的数据源为=Sheet1!$A$1:$B$4，则将行或范围复制到新工作表后，数据源将保持不变，即=Sheet1!$A$1:$B$4。它仍然指的是旧工作表，即 Sheet1。这也是 Microsoft Excel 中的行为。但是如果你想让它引用新的目标工作表，那么请使用[**复制选项.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)属性并将其设置为**真的**同时调用[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)方法。现在，如果您的目标工作表是 DestSheet，则图表的数据源将从 =Sheet1!$A$1:$B$4 更改为 =DestSheet!$A$1:$B$4。

## **复制行或范围时将图表的数据源更改为目标工作表**

下面的示例代码解释了[**复制选项.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)将包含图表的行或范围复制到新工作表时的属性。该代码使用[示例 excel 文件](5113699.xlsx)并生成[输出excel文件](5113697.xlsx).

![待办事项：图像_替代_文本](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
