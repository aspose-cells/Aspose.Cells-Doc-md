---
title: 在复制行或范围时将图表的数据源更改为目标工作表
type: docs
weight: 850
url: /zh/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **可能的使用场景**
当您将包含图表的行或范围复制到新工作表时，图表的数据源不会更改。例如，如果图表的数据源为=Sheet1!$A$1:$B$4，则在将行或范围复制到新工作表后，数据源将保持不变，即=Sheet1!$A$1:$B$4。它仍然指向旧工作表即Sheet1。这也是Microsoft Excel的行为。但如果要使其指向新的目标工作表，请在调用Cells.CopyRows()方法时使用CopyOptions.ReferToDestinationSheet属性，并将其设置为true。现在，如果您的目标工作表是DestSheet，则图表的数据源将从=Sheet1!$A$1:$B$4更改为=DestSheet!$A$1:$B$4。
## **复制行或区域时更改图表的数据源到目标工作表**
以下示例代码解释了在将包含图表的行或范围复制到新工作表时使用CopyOptions.ReferToDestinationSheet属性。该代码使用[示例Excel文件](5472284.xlsx)并生成[输出Excel文件](5472283.xlsx)。屏幕截图显示了[输出Excel文件](5472283.xlsx)中图表的数据源现在指向DestSheet而不是Sheet1。

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






