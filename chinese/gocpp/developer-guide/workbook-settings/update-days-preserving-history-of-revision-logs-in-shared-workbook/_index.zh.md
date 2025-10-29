---
title: 在共享工作簿中使用C++通过Golang更新保持历史的天数
linktitle: 在共享工作簿中保留修订日志的更新日志
type: docs
weight: 80
url: /zh/go-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: 学习如何使用C++通过Golang和Aspose.Cells更新共享工作簿中保留历史的天数
---

## **可能的使用场景**

当您分享一个工作簿时，您会得到一个选项***保留N天的更改历史***，如下截图所示。您可以使用Aspose.Cells的[**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/go-cpp/revisionlogcollection/getdayspreservinghistory/)属性来更新保留历史的天数。

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **在共享工作簿中保留修订日志的更新日志**

以下示例代码创建一个空白工作簿，然后共享它并将修订日志天数修改为7天，通常是30天。请参考代码生成的[输出Excel文件](60489773.xlsx)。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.go" >}}
