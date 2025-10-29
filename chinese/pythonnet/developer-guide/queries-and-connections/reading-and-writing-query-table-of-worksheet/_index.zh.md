---
title: 工作表的查询表读取和写入
type: docs
weight: 40
url: /zh/python-net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET提供Worksheet.QueryTables集合，该集合通过索引返回QueryTable对象。它具有以下两个属性

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

这两个都是布尔值。你可以在Microsoft Excel中通过数据 > 连接 > 属性查看它们。

{{% /alert %}}

## 工作表的查询表读取和写入

以下示例代码读取第一个工作表的第一个查询表，并打印出两个查询表属性。然后将QueryTable.PreserveFormatting设置为true。

您可以从以下链接下载用于此代码的源Excel文件和代码生成的输出Excel文件。

- [源Excel文件](5115533.xlsx)
- [输出Excel文件](5115537.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAndWritingQueryTable.py" >}}

### 控制台输出

这是上述示例代码的控制台输出

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## 检索查询表结果范围

Aspose.Cells for Python via .NET提供读取查询表结果范围地址的选项。以下代码演示了如何读取查询表的结果范围地址。示例文件可在[此处](72417290.xlsx)下载。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAddressOfResultRange.py" >}}

{{< app/cells/assistant language="python-net" >}}
