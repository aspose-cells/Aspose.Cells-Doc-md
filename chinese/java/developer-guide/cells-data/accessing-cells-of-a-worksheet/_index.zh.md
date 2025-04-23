---
title: 访问工作表的单元格
type: docs
weight: 10
url: /zh/java/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

我们知道所有的工作表都可能包含基本存储在单元格中的数据（构成工作表的基本部分）。单元格是构成整个工作表的行和列的序列。在尝试从工作表中访问数据之前，我们需要先访问它的单元格。因此，在本主题中，我们将讨论一些基本的访问工作表单元格的方法，使用Aspose.Cells在运行时。

{{% /alert %}} 
## **访问单元格**
Aspose.Cells提供一个代表Microsoft Excel文件的Workbook类。Workbook类包含一个WorksheetCollection集合，允许访问Excel文件中的每个工作表。工作表由Worksheet类表示。Worksheet类提供了一个代表工作表中所有单元格的Cells集合。

我们可以使用Cells集合来访问工作表中的单元格。Aspose.Cells提供了不同的访问单元格的基本方法：

1. [使用单元格名称](/cells/zh/java/accessing-cells-of-a-worksheet/).
1. [使用行和列索引](/cells/zh/java/accessing-cells-of-a-worksheet/).
### **使用单元格名称**
开发人员可以通过将单元格名称传递给Worksheet类的Cells集合来访问任何特定单元格。

如果开头创建一个空白工作表，Cells集合的计数为零。当使用此方法访问单元格时，它会检查该单元格是否存在于集合中。如果存在，它会在集合中返回单元格对象，否则它会创建一个新的Cell对象，将对象添加到Cells集合中，然后返回对象。如果您熟悉Microsoft Excel，这种方法是访问单元格的最简单方式，但比其他方法更慢。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **使用单元格的行和列索引**
开发人员可以通过将单元格的行和列索引传递给Worksheet类的Cells集合来访问任何特定单元格。

这种方法的工作方式与第一种方法相同。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **相关文章**
{{% alert color="primary" %}} 

- [命名区域](/cells/zh/java/named-ranges/)

{{% /alert %}} 
## **访问工作表的最大显示范围**
Aspose.Cells允许开发人员访问工作表的最大显示范围。最大显示范围 - 带有内容的第一个和最后一个单元格之间的单元格范围 - 在需要复制、选择或显示工作表的全部内容时非常有用。

您可以使用[Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)来访问工作表的最大显示范围。

在下图中，所选工作表的最大显示范围为A1:G15。

**显示此工作表的最大显示范围** 

![todo:image_alt_text](accessing-cells-of-a-worksheet_1.png)

以下示例代码演示如何访问[MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)属性。代码将生成以下输出。

{{< highlight java >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
