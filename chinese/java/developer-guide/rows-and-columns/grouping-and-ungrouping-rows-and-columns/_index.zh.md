---
title: 行和列的分组和取消分组
type: docs
weight: 40
url: /zh/java/grouping-and-ungrouping-rows-and-columns/
---

## **介绍**
在 Microsoft Excel 文件中，您可以创建一个数据大纲，以便通过单击鼠标来显示和隐藏不同级别的细节。

单击**大纲符号**1、2、3、+和- 快速显示工作表中仅提供摘要或标题部分的行或列，或者您可使用符号查看摘要或标题下的详细信息，如下图所示:

行和列的分组 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)
## **行和列的分组管理**
Aspose.Cells提供了一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，它表示Microsoft Excel文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)集合，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了一个[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合，表示工作表中的所有单元格。

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合提供了几种用于管理工作表中的行或列的方法，以下是其中的一些方法。
### **分组行和列**
可以通过调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合的 [groupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows-int-int-boolean-) 和 [groupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns-int-int-boolean-) 方法对行或列进行分组。这两个方法都接受以下参数：

- 第一个行/列索引，即组中的第一行或列。
- 最后一个行/列索引，即组中的最后一行或列。
- 是否隐藏，一个布尔参数，指定是否在分组后隐藏行/列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **分组设置**
Microsoft Excel还允许配置用于显示的分组设置：

- 详细信息下面的摘要行。
- 明细右侧的汇总列。

**分组设置** 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_2.png)

可以使用Worksheet类的Outline属性来配置这些分组设置。
### **明细下方的汇总行**
开发人员可以通过使用[Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline)类的[SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow)方法来控制在明细下方显示汇总行。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **将摘要列显示在详细信息右侧**
可以使用[Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline)类的[SummaryColumnRight](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)方法来控制是否在明细右侧显示汇总列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **取消行和列的分组**
通过调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合的 [UngroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows-int-int-) 和 [UngroupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns-int-int-) 方法取消分组。两者都接受相同的参数：

- 第一个行或列索引，即要取消分组的第一行/列。
- 最后一个行或列索引，即要取消分组的最后一行/列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
{{< app/cells/assistant language="java" >}}
