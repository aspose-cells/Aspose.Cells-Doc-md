---
title: 在导出工作表数据时自动重命名重复列
type: docs
weight: 250
url: /zh/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: 使用Aspose.Cells for .NET API学习如何在导出工作表数据时自动重命名重复的列。
keywords: 导出工作表数据时重命名重复列，导出数据到数据表时自动重命名重复列
---

## **可能的使用场景**

有时用户在将工作表数据导出到数据表时会遇到重复列的问题。数据表不可以有重复列，因此在将工作表数据导出到数据表之前必须重命名重复列。Aspose.Cells可以根据您指定的策略自动重命名重复列，使用[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy)属性。如果指定[**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digit，列将重命名为column1、column2、column3等，如果指定[**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter，则列将重命名为columnA、columnB、columnC等。

## **导出工作表数据时自动重命名重复列**

以下示例代码将一些数据添加到工作表的前三列，但是所有列都具有相同的名称，即* People *。然后，通过指定 [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Letter 策略将工作表中的数据导出到数据表中。然后打印由 Aspose.Cells 生成的数据表的列名。以下屏幕截图显示了在可视化器中导出的数据表。如您所见，重复的列已更名为 PeopleA、PeopleB 等。

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **控制台输出**

以下是上述示例代码的控制台输出供参考。

{{< highlight java >}}

People

PeopleA

PeopleB

{{< /highlight >}}
