---
title: 访问工作表的单元格
type: docs
weight: 10
url: /zh/cpp/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

我们知道所有的工作表都可能包含基本存储在单元格中的数据（构成工作表的基本部分）。单元格是构成整个工作表的行和列的序列。在尝试从工作表中访问数据之前，我们需要先访问它的单元格。因此，在本主题中，我们将讨论一些基本的访问工作表单元格的方法，使用Aspose.Cells在运行时。

{{% /alert %}} 
## **访问单元格**
Aspose.Cells提供一个代表Excel文件的 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类包含一个 [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合，允许访问Excel文件中的每个工作表。工作表由 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供一个 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合，表示工作表中的所有单元格。

我们可以使用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合来访问工作表中的单元格。Aspose.Cells提供了三种基本方法来访问工作表中的单元格：

1. 使用单元格名称。
1. 使用单元格的行和列索引。
1. 在 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合中使用单元格索引

{{% alert color="primary" %}} 

我们已经提到第3种方法是最快的，第1种方法是最慢的。三种方法之间的性能差异非常小，因此无论您使用哪种方法，都不用担心性能降级。

{{% /alert %}} 
### **使用单元格名称**
开发人员可以通过将单元格名称传递给 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类的 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合作为索引来访问任何特定单元格。

如果在开始时创建一个空白工作表，那么 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的计数为零。当您使用这种方法访问单元格时，它会检查该单元格是否存在于集合中。如果存在，则返回集合中的单元格对象，否则将创建一个新的 [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) 对象，将对象添加到 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合中，然后返回该对象。这种方法是在熟悉 Microsoft Excel 的情况下访问单元格的最简单方法，但与其他方法相比，它是最慢的。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
### **使用单元格的行和列索引**
开发人员可以通过将其行和列的索引传递给 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类的 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合来访问任何特定单元格。该方法与第一种方法的工作方式相同。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
## **访问工作表的最大显示范围**
Aspose.Cells 允许开发人员访问工作表的最大显示范围。最大显示范围 - 即内容的第一个单元格与最后一个单元格之间的单元格范围 - 在您需要复制、选择或显示工作表的全部内容时非常有用。

您可以使用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [MaxDisplayRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) 方法访问工作表的最大显示范围。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
