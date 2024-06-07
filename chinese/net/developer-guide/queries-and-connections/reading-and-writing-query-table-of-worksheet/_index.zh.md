---
title: 读取和写入工作表的查询表
type: docs
weight: 40
url: /zh/net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells提供了Worksheet.QueryTables集合，通过索引返回QueryTable类型的对象。它具有以下两个属性

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

这都是布尔值。您可以通过Microsoft Excel中的数据 > 连接 > 属性查看它们。

{{% /alert %}}

## 读取和写入工作表的查询表

以下示例代码读取第一个工作表的第一个查询表，然后打印两个查询表属性。然后将QueryTable.PreserveFormatting设置为true。

您可以从以下链接下载此代码中使用的源Excel文件和代码生成的输出Excel文件。

- [源Excel文件](5115533.xlsx)
- [输出Excel文件](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### 控制台输出

这是上述示例代码的控制台输出

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## 检索查询表结果范围

Aspose.Cells提供了读取查询表的结果范围地址的选项。以下代码演示了通过读取查询表的结果范围地址来查看此功能。示例文件可以从[这里](72417290.xlsx)下载。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
