---
title: 在共享工作簿中保留修订日志的更新日志
type: docs
weight: 90
url: /zh/java/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **可能的使用场景**

当您共享工作簿时，会出现一个选项说***保留N天的更改历史记录***，如下截图所示。您可以使用Aspose.Cells和[**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/java/com.aspose.cells/revisionlogcollection#DaysPreservingHistory)属性更新保留历史记录的天数。

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **在共享工作簿中保留修订日志的更新日志**

以下示例代码创建一个空工作簿，然后共享它，并将修订日志天数保留历史记录更新为7天，通常是30天。请参考代码生成的[输出Excel文件](60489784.xlsx)。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.java" >}}
