---
title: 访问工作表的单元格
type: docs
weight: 10
url: /zh/python-net/accessing-cells-of-a-worksheet/
description: 本文展示了如何通过Aspose.Cells for Python via .NET API获取工作表的最大显示范围并访问单元格。
keywords: Python Excel库，获取单元格对象，访问单元格，如何通过单元格的行和列索引获取单元格对象，如何通过单元格集合中的单元格索引获取单元格对象，如何通过单元格的行和列索引获取单元格对象，获取工作表的最大显示范围。 
---

{{% alert color="primary" %}}

我们知道，所有工作表可能包含基本存储在单元格中的数据（构成工作表的基本部分）。单元格是工作表的基本部分，用于构造整个工作表作为行和列的序列。在我们尝试从工作表获取数据之前，需要访问其单元格。因此，在本主题中，我们将讨论使用Aspose.Cells for Python via .NET在运行时访问工作表单元格的一些基本方法。

{{% /alert %}}

## **如何访问单元格**

Aspose.Cells for Python via .NET提供一个代表Excel文件的[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，可访问Excel文件中的每个工作表。工作表由[**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)类表示。[**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)类提供一个[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)集合，表示工作表中的所有单元格。

我们可以使用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合访问工作表中的单元格。Aspose.Cells for Python via .NET提供三种访问工作表单元格的基本方法：

1. 使用单元格名称。
1. 使用单元格的行和列索引。
1. 使用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合中的单元格索引

**重要提示：**我们已经提到第3种方法是最快的，第1种方法是最慢的。这些方法之间的性能差异非常小，因此无论使用哪种方法，都不用担心性能下降。

### **如何通过单元格名称获取单元格对象**

开发人员可以通过将单元格名称作为索引传递给[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)类的[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)集合来访问任何特定单元格。

如果在开始时创建空白工作表，则[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合的计数为零。当您使用这种方法访问单元格时，它将检查该单元格是否存在于集合中。如果是，它将在集合中返回单元格对象，否则，它将创建一个新的[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)对象，将对象添加到[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合然后返回该对象。如果您熟悉Microsoft Excel，这种方法是访问单元格的最简单方式，但相对于其他方法来说速度是最慢的。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellName-1.py" >}}

### **如何通过单元格的行和列索引获取单元格对象**

开发人员可以通过将其行和列的索引传递给[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)类的[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)集合来访问任何指定的单元格。

这种方法的工作方式与第一种方法相同。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.py" >}}

### **如何通过单元格索引在单元格集合中获取单元格对象**

也可以通过将单元格的数值索引传递给[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合来访问单元格。

如果使用这种方法访问单元格，如果单元格的数值索引超出范围，则可能会引发异常。这种方法是最快的访问单元格的方法，但需要注意的一点是，如果使用这种方法访问单元格对象，那么当新单元格添加到[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)的集合中时，数值索引可能会改变。[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合中的单元格对象是按行和列索引进行内部排序的。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.py" >}}

## **如何获取工作表的最大显示范围**

Aspose.Cells for Python via .NET 允许开发人员访问工作表的最大显示范围。最大显示范围 - 指内容第一个和最后一个单元格之间的单元格范围 - 在您需要在图像中复制、选择或显示工作表的全部内容时非常有用。

您可以使用[**Worksheet.cells.max_display_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/)来访问工作表的最大显示范围。以下示例代码说明了如何访问[**MaxDisplayRange**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/)属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.py" >}}
