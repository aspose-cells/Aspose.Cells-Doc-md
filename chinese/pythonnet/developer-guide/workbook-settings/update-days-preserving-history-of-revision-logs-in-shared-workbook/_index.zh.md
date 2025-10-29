---
title: 在共享工作簿中保留修订日志的更新日志
type: docs
weight: 80
url: /zh/python-net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **可能的使用场景**

当你共享工作簿时，会出现一个选项，显示 ***保留变更历史 N 天***，如下图所示。你可以使用 Aspose.Cells for Python via .NET 的 [**WorksheetCollection.revision_logs.days_preserving_history**](https://reference.aspose.com/cells/python-net/aspose.cells.revisions/revisionlogcollection/days_preserving_history) 属性，更新保存历史的天数。

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **在共享工作簿中保留修订日志的更新日志**

以下示例代码创建一个空白工作簿，然后共享它并将修订日志天数修改为7天，通常是30天。请参考代码生成的[输出Excel文件](60489773.xlsx)。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
