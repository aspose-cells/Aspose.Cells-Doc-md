---
title: 分组和取消分组行和列
type: docs
weight: 40
url: /zh/java/grouping-and-ungrouping-rows-and-columns/
---
## **介绍**
在 Microsoft Excel 文件中，您可以为数据创建一个大纲，以便通过单击鼠标来显示和隐藏详细信息级别。

点击**大纲符号**、1、2、3、+ 和 - 快速仅显示工作表中为各部分提供摘要或标题的行或列，或者您可以使用符号查看单个摘要或标题下的详细信息，如下图所示:

行和列的分组

![待办事项：图像_替代_文本](grouping-and-ungrouping-rows-and-columns_1.png)
## **行列分组管理**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中每个工作表的集合。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)代表工作表中所有单元格的集合。

这[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection 提供了多种方法来管理工作表中的行或列，下面将详细讨论其中的一些方法。
### **分组行和列**
可以通过调用[组行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\)） 和[组列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\) 的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这两种方法都采用以下参数：

- 第一行/列索引，组中的第一行或第一列。
- 最后一行/列索引，组中的最后一行或最后一列。
- is hidden，布尔型参数，指定分组后是否隐藏行/列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **群组设置**
Microsoft Excel 还允许配置用于显示的组设置：

- 详细信息下方的摘要行。
- 详细信息右侧的摘要列。

**群组设置** 

![待办事项：图像_替代_文本](grouping-and-ungrouping-rows-and-columns_2.png)

可以使用 Worksheet 类的 Outline 属性配置这些组设置。
### **详细信息下方的汇总行**
开发人员可以控制在详细信息下方显示摘要行，方法是使用[大纲](https://reference.aspose.com/cells/java/com.aspose.cells/Outline)班级'[汇总行下方](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow)方法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **详细信息右侧的摘要列**
可以控制摘要列是否显示在详细信息的右侧[大纲](https://reference.aspose.com/cells/java/com.aspose.cells/Outline)班级'[摘要列右](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)方法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **取消分组行和列**
通过调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏的[解组行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\)） 和[取消组合列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)） 方法。两种方法都采用相同的参数：

- 第一行或第一列索引，要取消分组的第一行/列。
- 最后一行或最后一列索引，要取消分组的最后一行/列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
