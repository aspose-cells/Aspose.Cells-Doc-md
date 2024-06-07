---
title: 导出工作表数据时自动重命名重复列
type: docs
weight: 250
url: /zh/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: 通过Aspose.Cells for .NET API学习如何在导出工作表数据时自动重命名重复列。
keywords: 导出工作表数据时重命名重复列，将数据导出到数据表时自动重命名重复列
---

## **可能的使用场景**

有时，用户在从工作表导出数据到数据表时会遇到重复列的问题。数据表不能有重复列，因此在导出工作表数据到数据表之前必须将重复列重命名。Aspose.Cells可以根据您指定的策略自动重命名重复列，使用[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy)属性。如果指定[**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).数字，列将被重命名为列1、列2、列3等，如果指定[**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).字母，则列将被重命名为列A、列B、列C等。

## **导出工作表数据时自动重命名重复列**

以下示例代码在工作表的前三列中添加一些数据，但所有列的名称均为*People*。然后，通过指定[**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).字母策略将数据从工作表导出到数据表。然后打印由Aspose.Cells生成的数据表的列名。以下截图显示了数据表中导出数据的可视化器。正如您所见，重复列已被重命名为PeopleA、PeopleB等。

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **控制台输出**

这是上述示例代码的控制台输出，供参考。

{{< highlight java >}}

People

PeopleA

PeopleB

{{< /highlight >}}
