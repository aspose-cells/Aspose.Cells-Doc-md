---
title: 访问工作表的 Cells
type: docs
weight: 10
url: /zh/net/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}}

我们知道所有工作表都可能包含基本上存储在单元格中的数据（工作表由单元格组成）。单元格是工作表的基本部分，用于将整个工作表构建为一系列行和列。在我们尝试从工作表访问数据之前，我们需要访问其单元格。因此，在本主题中，我们将讨论使用 Aspose.Cells 在运行时访问工作表单元格的一些基本方法。

{{% /alert %}}

## **访问 Cells**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示一个 Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表集合**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)允许访问 Excel 文件中的每个工作表。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)代表工作表中所有单元格的集合。

我们可以用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合以访问工作表中的单元格。 Aspose.Cells 提供了访问工作表中单元格的三种基本方法：

1. 使用单元名称。
1. 使用单元格的行和列索引。
1. 在中使用单元格索引[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏

**重要的：**我们已经提到第三种方法是最快的，而第一种方法是最慢的。两种方法之间的性能差异非常小，因此无论您使用哪种方法，都不必担心性能下降。

### **使用 Cell 名称**

开发人员可以通过将其单元名称传递给[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)的集合[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类作为索引。

如果您在开始时创建一个空白工作表，则计数[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏为零。当您使用这种方法访问一个单元格时，它会检查该单元格是否存在于集合中。如果是，它返回集合中的单元格对象，否则，它创建一个新的[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)对象，将对象添加到[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合，然后返回对象。如果您熟悉 Microsoft Excel，此方法是访问单元格的最简单方法，但与其他方法相比，它是最慢的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **使用 Cell 的行和列索引**

开发人员可以通过将其行和列的索引传递给[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)的集合[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。

这种方法的工作方式与第一种方法相同。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **在 Cells 集合中使用 Cell 索引**

也可以通过将单元格的数字索引传递给[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。

如果您使用此方法访问单元格，则如果单元格的数字索引超出范围，则会引发异常。这种方法是访问单元格最快的方法，但需要知道的重要一点是，如果您使用这种方法访问单元格对象，则数字索引可能会在新单元格添加到[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。中的单元格对象[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合在内部按行和列索引排序。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **访问工作表的最大显示范围**

Aspose.Cells 允许开发人员访问工作表的最大显示范围。最大显示范围 - 第一个和最后一个有内容的单元格之间的单元格范围 - 当您需要复制、选择或在图像中显示工作表的全部内容时非常有用。

您可以使用访问工作表的最大显示范围[**工作表.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) .下面的示例代码说明了如何访问[**最大显示范围**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
