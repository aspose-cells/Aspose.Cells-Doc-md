---
title: 工作表的查询表读取和写入
type: docs
weight: 560
url: /zh/java/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}} 

Aspose.Cells提供[Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables)集合，返回[QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection)。要获取特定的[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)，使用[QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\))属性，并传递QueryTable的索引。[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)类有用于调整QueryTable的两个属性。

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

这两个值都是布尔值。您可以通过Microsoft Excel中的数据 > 连接 > 属性查看它们。

{{% /alert %}} 
## **读取和写入工作表的查询表**
以下示例代码读取第一个工作表的第一个[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)，然后打印两个[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)属性。然后将[QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)设置为**true**。

以下屏幕截图显示了代码中使用的源Excel文件[5472578.xlsx](5472578.xlsx)及其显示了两个[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)的属性。

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_1.png)

以下屏幕截图显示了代码生成的输出Excel文件[5472574.xlsx](5472574.xlsx)及其显示了两个[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)的属性。如您所见，现在已勾选保存格式复选框。

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **控制台输出**
这是上述示例代码的控制台输出

{{< highlight java >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}

## **检索查询表结果范围**
Aspose.Cells提供了读取查询表的地址，即单元格的结果范围的选项。下面的代码演示了通过读取查询表的结果范围地址来实现此功能。示例文件可以[在这里](QueryTXT.xlsx)下载。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
