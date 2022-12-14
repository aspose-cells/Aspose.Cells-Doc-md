---
title: 工作表读写查询表
type: docs
weight: 40
url: /zh/net/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells 提供Worksheet.QueryTables集合，通过索引返回QueryTable类型的对象。它具有以下两个属性

- QueryTable.AdjustColumnWidth
- 查询表.PreserveFormatting

这些都是布尔值。您可以通过数据 > 连接 > 属性在 Microsoft Excel 中查看它们。

{{% /alert %}}

## 工作表读写查询表

下面的示例代码读取第一个工作表的第一个 QueryTable，然后打印两个 QueryTable 属性。然后它将 QueryTable.PreserveFormatting 设置为 true。

您可以从以下链接下载此代码中使用的源 Excel 文件和代码生成的输出 Excel 文件。

- [源 Excel 文件](5115533.xlsx)
- [输出 Excel 文件](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### 控制台输出

这是上面示例代码的控制台输出

{{< highlight "java" >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## 检索查询表结果范围

 Aspose.Cells 提供了读取地址的选项，即查询表的单元格结果范围。以下代码通过读取查询表的结果范围地址来演示此功能。可以下载示例文件[这里](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
