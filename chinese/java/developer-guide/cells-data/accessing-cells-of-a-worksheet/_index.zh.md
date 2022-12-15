---
title: 访问工作表的 Cells
type: docs
weight: 10
url: /zh/java/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

我们知道所有工作表都可能包含基本上存储在单元格中的数据（工作表由单元格组成）。单元格是工作表的基本部分，用于将整个工作表构建为一系列行和列。在我们尝试从工作表访问数据之前，我们需要访问其单元格。因此，在本主题中，我们将讨论使用 Aspose.Cells 在运行时访问工作表单元格的一些基本方法。

{{% /alert %}} 
## **访问 Cells**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中每个工作表的集合。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)代表工作表中所有单元格的集合。

我们可以使用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合以访问工作表中的单元格。 Aspose.Cells 提供了访问单元格的不同基本方法：

1. [使用单元名称](/cells/zh/java/accessing-cells-of-a-worksheet/).
1. [使用行和列索引](/cells/zh/java/accessing-cells-of-a-worksheet/).
### **使用 Cell 名称**
开发人员可以通过将其单元名称传递给[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)的集合[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。

如果您在开始时创建一个空白工作表，则计数[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏为零。当您使用这种方法访问一个单元格时，它会检查该单元格是否存在于集合中。如果是，它返回集合中的单元格对象，否则，它创建一个新的[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)对象，将对象添加到[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合，然后返回对象。如果您熟悉 Microsoft Excel，此方法是访问单元格的最简单方法，但它比其他方法慢。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **使用 Cell 的行和列索引**
开发人员可以通过将其行和列的索引传递给[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)的集合[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。

这种方法的工作方式与第一种方法相同。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **相关文章**
{{% alert color="primary" %}} 

- [命名范围](/cells/zh/java/named-ranges/)

{{% /alert %}} 
## **访问工作表的最大显示范围**
Aspose.Cells 允许开发人员访问工作表的最大显示范围。最大显示范围 - 第一个和最后一个有内容的单元格之间的单元格范围 - 当您需要复制、选择或在图像中显示工作表的全部内容时非常有用。

您可以使用访问工作表的最大显示范围[工作表.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

下图中，选中的工作表最大显示范围为A1:G15。

**显示此工作表的最大显示范围** 

![待办事项：图像_替代_文本](accessing-cells-of-a-worksheet_1.png)

下面的示例代码说明了如何访问[最大显示范围](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)财产。该代码生成以下输出。

{{< highlight "java" >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
