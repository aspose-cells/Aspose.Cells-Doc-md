---
title: 对行和列进行分组和取消分组
type: docs
weight: 40
url: /zh/java/grouping-and-ungrouping-rows-and-columns/
---

## **介绍**
在 Microsoft Excel 文件中，您可以为数据创建概要，让您单击一次鼠标即可显示和隐藏详细级别。

单击**概要符号**，1、2、3、+ 和 - ，即可快速显示仅提供摘要或标题用于工作表中的节的行或列，或者您可以使用符号查看摘要或标题下的详细信息，如下图所示：

行和列的分组 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)
## **行和列的分组管理**
Aspose.Cells 提供了一个 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类，代表 Microsoft Excel 文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类包含一个 [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) 集合，允许访问 Excel 文件中的每个工作表。工作表由 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类提供一个 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合，表示工作表中的所有单元格。

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合提供了几种方法来管理工作表中的行或列，下面将详细讨论其中的一些。
### **分组行和列**
通过调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合的 [groupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\)) 和 [groupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\)) 方法，可以对行或列进行分组。这两种方法接受以下参数：

- 第一个行/列索引，组中的第一个行或列。
- 最后一个行/列索引，组中的最后一个行或列。
- 是否隐藏，一个布尔参数，指定在分组后是否隐藏行/列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **分组设置**
Microsoft Excel 也允许配置用于显示的分组设置：

- 详细下面的摘要行。
- 在详细数据右侧显示汇总列。

**分组设置** 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_2.png)

可以使用 Worksheet 类的 Outline 属性配置这些分组设置。
### **详细数据下方显示汇总行**
开发人员可以使用 [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) 类的 [SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) 方法控制在详细数据下方显示汇总行。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **将摘要列放在详细信息右侧**
可以控制在详细数据右侧显示汇总列与 [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) 类的 [SummaryColumnRight](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight) 方法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **取消分组行和列**
通过调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合的 [UngroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\)) 和 [UngroupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) 方法可以取消组合分组的行或列。这两种方法使用相同的参数：

- 第一行或列索引，要取消分组的第一行/列。
- 最后一行或列索引，要取消分组的最后一行/列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
