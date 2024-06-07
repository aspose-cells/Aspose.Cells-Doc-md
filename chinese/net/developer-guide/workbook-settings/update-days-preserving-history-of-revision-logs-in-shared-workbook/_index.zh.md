---
title: 更新在共享工作簿中保留修订日志历史的天数
type: docs
weight: 80
url: /zh/net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **可能的使用场景**

当您分享一个工作簿时，您会看到一个选项，***保留 N 天的更改历史***，如下截图所示。您可以使用 Aspose.Cells 的 [**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/net/aspose.cells.revisions/revisionlogcollection/properties/dayspreservinghistory) 属性更新保留历史的天数。

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **更新天数保留共享工作簿中修订日志的历史记录**

以下示例代码创建一个空的工作簿，然后共享它并将修订日志天数保留历史记录更新为7天，通常是30天。请查看代码生成的[输出Excel文件](60489773.xlsx)以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.cs" >}}
