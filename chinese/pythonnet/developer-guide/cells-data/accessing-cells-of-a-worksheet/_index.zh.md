---
title: 访问工作表的单元格
type: docs
weight: 10
url: /zh/python-net/accessing-cells-of-a-worksheet/
description: 本文展示了如何通过 Aspose.Cells for Python 通过 .NET API 获取工作表的最大显示范围并访问单元格。
keywords: Python Excel 库，获取单元格对象，访问单元格，如何通过 Aspose.Cells for Python 通过 .NET API 的行和列索引获取单元格对象，如何通过单元格集合的单元格索引获取单元格对象，如何通过行和列索引获取单元格对象，获取工作表的最大显示范围。 
---

{{% alert color="primary" %}}

我们知道所有工作表可能包含基本存储在单元格中的数据（工作表由单元格构成）。 单元格是工作表的基本部分，用于构造整个工作表作为行和列的序列。 在尝试从工作表中访问数据之前，我们需要访问其单元格。 因此，在本主题中，我们将通过 Aspose.Cells for Python 通过 .NET 讨论在运行时访问工作表单元格的一些基本方法。

{{% /alert %}}

## **如何访问单元格**

通过 .NET 的 Aspose.Cells for Python 提供了一个代表 Excel 文件的 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类。 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) ，允许访问 Excel 文件中的每个工作表。 工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供一个 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合，表示工作表中的所有单元格。

我们可以使用 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合在工作表中访问单元格。 Aspose.Cells for Python 通过 .NET 提供了三种基本方法来访问工作表中的单元格

1. 使用单元格名称。
1. 使用单元格的行列索引。
1. 在[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合中使用单元格索引

**重要:** 我们已经提到第3种方法是最快的，第1种方法是最慢的。这些方法之间的性能差异非常小，所以不用担心性能下降，无论您使用哪种方法。

### **如何通过单元格名称获取单元格对象**

开发人员可以通过将单元格名称传递给 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类的 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合作为索引，访问任何特定单元格。

如果您在开始时创建一个空白工作表，[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合的计数为零。当您使用此方法访问单元格时，它将检查该单元格是否存在于集合中。若是，则返回集合中的单元格对象，否则，创建一个新的 [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 对象，将对象添加到 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合，然后返回对象。如果您熟悉 Microsoft Excel，则此方法是访问单元格的最简单方式，但相比其他方法，速度是最慢的。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellName-1.py" >}}

### **如何通过行和列索引获取单元格对象**

开发人员可以通过将其行和列的索引传递给 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类的 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合，访问任何特定单元格。

这种方法与第一种方法的工作方式相同。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.py" >}}

### **如何通过单元格索引在单元格集合中获取单元格对象**

也可以通过将单元格的数字索引传递给 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合，访问单元格。

如果您使用此方法访问单元格，当单元格的数字索引超出范围时，可能会抛出异常。此方法是访问单元格最快的方式，但需要注意的是，如果使用此方法访问单元格对象，当向 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合中添加新单元格后，数字索引可能会发生变化。[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合中的单元格对象是按行和列索引内部排序的。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.py" >}}

## **如何获取工作表的最大显示范围**

通过 .NET 的 Aspose.Cells for Python 允许开发人员访问工作表的最大显示范围。 最大显示范围 - 具有内容的第一个单元格和最后一个单元格之间的单元格范围 - 在您需要将工作表的全部内容复制、选择或显示为图像时非常有用。

您可以使用 [**Worksheet.cells.max_display_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/) 访问工作表的最大显示范围。以下示例代码展示了如何访问 [**MaxDisplayRange**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/) 属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.py" >}}
