---
title: 读取和写入工作表的查询表
type: docs
weight: 560
url: /zh/java/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}} 

Aspose.Cells提供 [Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) 集合，它返回 [QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection)。要获取特定的 [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)，请使用 [QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\)) 属性并传递QueryTable的索引。 [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) 类有以下两个属性来调整QueryTable。

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

这两个值都是布尔值。您可以通过Microsoft Excel的数据 > 连接 > 属性查看它们。

{{% /alert %}} 
## **读取和写入工作表的查询表**
以下示例代码读取第一个工作表的第一个 [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)，然后打印两个 [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) 属性。然后将 [QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) 设置为 **true**。

以下屏幕截图显示了代码中使用的 [源excel文件](5472578.xlsx) 及其显示了两个 [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) 值的属性。

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_1.png)

以下屏幕截图显示了代码生成的 [输出excel文件](5472574.xlsx) 及其显示了两个 [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) 值的属性。如您所见，保留的格式复选框现在已经选中。

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **控制台输出**
这是上述示例代码的控制台输出

{{< highlight java >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}
## **检索查询表结果范围**
Aspose.Cells提供了一种读取查询表的结果范围地址（即单元格的地址）的选项。以下代码演示了通过读取查询表的结果范围地址来实现此功能。示例文件可以从 [此处](QueryTXT.xlsx) 下载。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
