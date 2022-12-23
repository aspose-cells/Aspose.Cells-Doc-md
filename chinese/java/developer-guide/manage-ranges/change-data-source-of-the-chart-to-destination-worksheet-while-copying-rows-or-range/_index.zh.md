---
title: 复制行或范围时将图表的数据源更改为目标工作表
type: docs
weight: 850
url: /zh/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **可能的使用场景**
当您将包含图表的行或范围复制到新工作表时，图表的数据源不会改变。例如，如果图表的数据源为=Sheet1!$A$1:$B$4，则将行或范围复制到新工作表后，数据源将保持不变，即=Sheet1!$A$1:$B$4。它仍然指的是旧工作表，即 Sheet1。这也是 Microsoft Excel 行为。但是，如果您希望它引用新的目标工作表，请使用 CopyOptions.ReferToDestinationSheet 属性并在调用 Cells.CopyRows() 方法时将其设置为 true。现在，如果您的目标工作表是 DestSheet，则图表的数据源将从 =Sheet1!$A$1:$B$4 更改为 =DestSheet!$A$1:$B$4。
## **复制行或范围时将图表的数据源更改为目标工作表**
以下示例代码解释了在将包含图表的行或范围复制到新工作表时 CopyOptions.ReferToDestinationSheet 属性的用法。该代码使用[示例 excel 文件](5472284.xlsx)并生成[输出excel文件](5472283.xlsx).截图显示chart的数据源在[输出excel文件](5472283.xlsx)现在指的是 DestSheet 而不是 Sheet1。

![待办事项：图片_替代_文本](change-data-source-of-the-chart_1.png)







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






