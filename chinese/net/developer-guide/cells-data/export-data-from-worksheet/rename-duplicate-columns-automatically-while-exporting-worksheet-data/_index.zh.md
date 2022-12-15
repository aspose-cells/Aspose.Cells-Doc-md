---
title: 导出工作表数据时自动重命名重复列
type: docs
weight: 250
url: /zh/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
---
## **可能的使用场景**

有时，用户在将工作表中的数据导出到数据表时会遇到重复列的问题。 DataTable 不能有重复的列，因此必须先重命名重复的列，然后才能将工作表数据导出到数据表中。 Aspose.Cells 可以根据您指定的策略自动重命名重复的列[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy)财产。如果您指定[**重命名策略**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digit，列将被重命名为 column1、column2、column3 等，如果您指定[**重命名策略**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter，然后列将被重命名为columnA，columnB，columnC等。

## **导出工作表数据时自动重命名重复列**

以下示例代码在工作表的前三列中添加了一些数据，但所有列都具有相同的名称，即*人们*.然后通过指定将工作表中的数据导出到数据表中[**重命名策略**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).信策略。然后它打印由 Aspose.Cells 生成的数据表的列名称。下面的屏幕截图显示了可视化工具中导出数据的数据表。如您所见，重复的列已重命名为 PeopleA、PeopleB 等。

![待办事项：图像_替代_文本](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **控制台输出**

以下是上述示例代码的控制台输出，供参考。

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
