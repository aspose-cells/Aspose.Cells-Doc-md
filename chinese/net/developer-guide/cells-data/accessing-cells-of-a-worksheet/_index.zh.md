---
title: 访问工作表的单元格
type: docs
weight: 10
url: /zh/net/accessing-cells-of-a-worksheet/
description: 本文介绍了如何通过Aspose.Cells for .NET API获得工作表的最大显示范围并访问单元格。
keywords: 获取单元格对象，访问单元格，获取工作表的最大显示范围。 
---

{{% alert color="primary" %}}

我们知道所有工作表可能包含基本存储在单元格中的数据（用于构成工作表的部分）。单元格是构建整个工作表的基本部分，用于构建行和列的序列。在尝试从工作表访问数据之前，我们需要访问其单元格。因此，在本主题中，我们将讨论一些在运行时访问工作表单元格的基本方法。使用Aspose.Cells。

{{% /alert %}}

## **如何访问单元格**

Aspose.Cells提供了一个表示Excel文件的[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合，表示工作表中的所有单元格。

我们可以使用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合访问工作表中的单元格。Aspose.Cells提供了三种基本方法来访问工作表中的单元格:

1. 使用单元格名称。
1. 使用单元格的行列索引。
1. 在[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合中使用单元格索引

**重要:** 我们已经提到第3种方法是最快的，第1种方法是最慢的。这些方法之间的性能差异非常小，所以不用担心性能下降，无论您使用哪种方法。

### **如何通过单元格名称获取单元格对象**

开发人员可以通过将单元格名称传递给 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合作为索引，访问任何特定单元格。

如果您在开始时创建一个空白工作表，[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合的计数为零。当您使用此方法访问单元格时，它将检查该单元格是否存在于集合中。若是，则返回集合中的单元格对象，否则，创建一个新的 [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 对象，将对象添加到 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合，然后返回对象。如果您熟悉 Microsoft Excel，则此方法是访问单元格的最简单方式，但相比其他方法，速度是最慢的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **如何通过行和列索引获取单元格对象**

开发人员可以通过将其行和列的索引传递给 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合，访问任何特定单元格。

这种方法与第一种方法的工作方式相同。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **如何通过单元格索引在单元格集合中获取单元格对象**

也可以通过将单元格的数字索引传递给 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合，访问单元格。

如果您使用此方法访问单元格，当单元格的数字索引超出范围时，可能会抛出异常。此方法是访问单元格最快的方式，但需要注意的是，如果使用此方法访问单元格对象，当向 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合中添加新单元格后，数字索引可能会发生变化。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合中的单元格对象是按行和列索引内部排序的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **如何获取工作表的最大显示范围**

Aspose.Cells 允许开发人员访问工作表的最大显示范围。最大显示范围是指第一个和最后一个具有内容的单元格之间的单元格范围，当您需要在图像中复制、选择或显示工作表的全部内容时，这很有用。

您可以使用 [**Worksheet.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) 访问工作表的最大显示范围。以下示例代码展示了如何访问 [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) 属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
