---
title: 访问工作表的单元格
type: docs
weight: 10
url: /zh/java/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

我们知道所有工作表可能包含基本存储在单元格中的数据（用于构成工作表的部分）。单元格是构建整个工作表的基本部分，用于构建行和列的序列。在尝试从工作表访问数据之前，我们需要访问其单元格。因此，在本主题中，我们将讨论一些在运行时访问工作表单元格的基本方法。使用Aspose.Cells。

{{% /alert %}} 
## **访问单元格**
Aspose.Cells提供了一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，表示一个Microsoft Excel文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含了一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)集合，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了一个[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合，表示工作表中的所有单元格。

我们可以使用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合来访问工作表中的单元格。Aspose.Cells提供了不同的基本方法来访问单元格:

1. [使用单元格名称](/cells/zh/java/accessing-cells-of-a-worksheet/).
1. [使用行和列索引](/cells/zh/java/accessing-cells-of-a-worksheet/).
### **使用单元格名称**
开发人员可以通过将单元格名称传递给[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类的[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合来访问任何特定单元格。

如果您在开始时创建一个空白工作表，[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的计数为零。当您使用这种方法来访问单元格时，它会检查该单元格是否存在于集合中。如果是，则返回集合中的单元格对象，否则它会创建一个新的[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)对象，将对象添加到[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合中，然后返回对象。这种方法是访问单元格的最简单方式，如果您熟悉Microsoft Excel但比其他方法慢。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **使用单元格的行和列索引**
开发人员可以通过将单元格的行和列的索引传递给[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类的[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合来访问任何特定单元格。

这种方法与第一种方法的工作方式相同。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **相关文章**
{{% alert color="primary" %}} 

- [命名区域](/cells/zh/java/named-ranges/)

{{% /alert %}} 
## **访问工作表的最大显示范围**
Aspose.Cells 允许开发人员访问工作表的最大显示范围。最大显示范围是指第一个和最后一个具有内容的单元格之间的单元格范围，当您需要在图像中复制、选择或显示工作表的全部内容时，这很有用。

您可以使用[Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)访问工作表的最大显示范围。

在下图中，所选工作表的最大显示范围为A1:G15。

**显示该工作表的最大显示范围** 

![todo:image_alt_text](accessing-cells-of-a-worksheet_1.png)

以下示例代码说明如何访问[MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)属性。该代码会生成以下输出。

{{< highlight java >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
