---
title: 工作表读写查询表
type: docs
weight: 560
url: /zh/java/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}} 

Aspose.Cells提供[工作表.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables)返回的集合[查询表集合](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection).得到一个特定的[查询表](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)， 使用[查询表集合.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\) ) 属性并传递 QueryTable 的索引。这[查询表](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)类具有以下两个用于调整QueryTable 的属性。

- [查询表.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [查询表.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

这些都是布尔值。您可以通过数据 > 连接 > 属性在 Microsoft Excel 中查看它们。

{{% /alert %}} 
## **工作表读写查询表**
下面的示例代码读取第一个[查询表](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)第一个工作表，然后打印两个[查询表](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)特性。然后它设置[查询表.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)至**真的**.

以下屏幕截图显示了[源文件](5472578.xlsx)在代码中使用，它的属性显示了[查询表](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)值。

![待办事项：图片_替代_文本](reading-and-writing-query-table-of-worksheet_1.png)

以下屏幕截图显示了[输出excel文件](5472574.xlsx)由代码生成，其属性显示了[查询表](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)值。如您所见，现在已选中保留格式复选框。

![待办事项：图片_替代_文本](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **控制台输出**
这是上面示例代码的控制台输出

{{< highlight "java" >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}
## **检索查询表结果范围**
Aspose.Cells 提供了读取地址的选项，即查询表的单元格结果范围。以下代码通过读取查询表的结果范围地址来演示此功能。可以下载示例文件[这里](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
