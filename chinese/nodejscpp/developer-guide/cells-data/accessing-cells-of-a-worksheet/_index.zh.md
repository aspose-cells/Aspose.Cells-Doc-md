---
title: 访问工作表的单元格
type: docs
weight: 10
url: /zh/nodejs-cpp/accessing-cells-of-a-worksheet/
description: 本文介绍如何通过 Aspose.Cells for Node.js via C++ 获取工作表的最大显示范围并访问单元格。
keywords: 获取单元格对象，访问单元格，获取工作表的最大显示范围。 
---

{{% alert color="primary" %}}

我们知道所有工作表可能包含存储在单元格中的数据（工作表由这些单元格组成）。单元格是工作表的基本组成部分，用于构建完整的工作表，按照行和列的顺序排列。在尝试访问工作表中的数据之前，需要获取其单元格。因此，本主题将讨论在运行时通过 Aspose.Cells for Node.js via C++ 访问工作表单元格的一些基本方法。

{{% /alert %}}

## **如何访问单元格**

Aspose.Cells for Node.js via C++ 提供了一个名为 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 的类，用于表示一个 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类拥有一个 [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)，允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类提供一个 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合，代表工作表中的所有单元格。

可以使用 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合访问工作表中的单元格。Aspose.Cells for Node.js via C++ 提供了三种基本方法来访问工作表中的单元格：

1. 使用单元格名称。
1. 使用单元格的行和列索引。
1. 使用[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合中的单元格索引

**重要提示：**我们已经提到第3种方法是最快的，第1种方法是最慢的。这些方法之间的性能差异非常小，因此无论使用哪种方法，都不用担心性能下降。

### **如何通过单元格名称获取单元格对象**

开发人员可以通过将单元格名称作为索引传递给[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)类的[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)集合来访问任何特定单元格。

如果在开始时创建空白工作表，则[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合的计数为零。当您使用这种方法访问单元格时，它将检查该单元格是否存在于集合中。如果是，它将在集合中返回单元格对象，否则，它将创建一个新的[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)对象，将对象添加到[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合然后返回该对象。如果您熟悉Microsoft Excel，这种方法是访问单元格的最简单方式，但相对于其他方法来说速度是最慢的。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellName-1.js" >}}

### **如何通过单元格的行和列索引获取单元格对象**

开发人员可以通过将其行和列的索引传递给[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)类的[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)集合来访问任何指定的单元格。

这种方法的工作方式与第一种方法相同。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.js" >}}

### **如何通过单元格索引在单元格集合中获取单元格对象**

也可以通过将单元格的数值索引传递给[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合来访问单元格。

如果使用这种方法访问单元格，如果单元格的数值索引超出范围，则可能会引发异常。这种方法是最快的访问单元格的方法，但需要注意的一点是，如果使用这种方法访问单元格对象，那么当新单元格添加到[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)的集合中时，数值索引可能会改变。[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合中的单元格对象是按行和列索引进行内部排序的。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.js" >}}

## **如何获取工作表的最大显示范围**

Aspose.Cells for Node.js via C++ for Node.js via C++ 允许开发者访问工作表的最大显示范围。最大显示范围是指第一个和最后一个有内容的单元格之间的范围，当你需要复制、选择或显示整个工作表内容到图像中时非常实用。

您可以使用[**Cells.getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--)来访问工作表的最大显示范围。以下示例代码说明了如何访问[**getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--)属性。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
