---
title: 复制行和列
type: docs
weight: 20
url: /zh/cpp/copying-rows-and-columns/
---

## **介绍**
有时，您需要在工作表中复制行和列，而不是复制整个工作表。使用Aspose.Cells，可以在工作簿内或之间复制行和列。
当复制行（或列）时，其中包含的数据，包括公式 - 具有更新的引用 - 和值，批注，格式，隐藏单元格，图像和其他绘图对象也会被复制。
## **使用Microsoft Excel复制行和列**
1. 选择要复制的行或列。
1. 要复制行或列，请单击 **标准** 工具栏上的 **复制**，或按 **CTRL**+**C**。
1. 选择要复制所选内容下方或右侧的行或列。
1. 复制行或列时，单击 **已复制的单元格** 在 **插入** 菜单上。

{{% alert color="primary" %}} 

如果您单击 **标准** 工具栏上的 **粘贴**，或者按 **CTRL**+**V** 而不是单击 **插入** 菜单上的命令，则目标单元格的任何内容都将被替换。

{{% /alert %}} 
## **使用Aspose.Cells**
### **复制行**
Aspose.Cells 提供了 Aspose::Cells::ICells 类的 CopyRow 方法。该方法从源行复制所有类型的数据，包括公式，值，批注，单元格格式，隐藏单元格，图像和其他绘图对象到目标行。

CopyRow方法接受以下参数:

- 源Cells 对象,
- 源行索引, 和
- 目标行索引.

使用该方法可在工作表内或者不同工作表之间复制一行。CopyRow方法的工作方式类似于Microsoft Excel。例如，你不需要显式设置目标行的高度，该值也会被复制。

以下示例展示了如何在工作表中复制一行。它使用一个模板Microsoft Excel文件，复制第二行（包括数据、格式、批注、图片等）并粘贴到同一工作表的第12行。

你可以跳过使用**GetRowHeigh**方法获取源行高度然后使用**SetRowHeight**方法设置目标行高度的步骤，因为**CopyRow**方法会自动处理行高度。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows-new.cpp" >}}

{{% alert color="primary" %}} 

在复制行时，重要注意相关图片、图表或其他绘图对象，这与Microsoft Excel相同:

1. 如果源行索引为5，图像、图表等将被复制，如果它在三行中（起始行索引为4，结束行索引为6）内。
1. 目标行中的现有图片、图表等不会被删除。

{{% /alert %}} 
### **复制列**
Aspose.Cells提供Aspose::Cells::ICells类的CopyColumn方法，该方法从源列复制包括更新引用的公式和数值、批注、单元格格式、隐藏单元格、图片和其他绘图对象等所有类型的数据到目标列。

CopyColumn方法接受以下参数:

- 源Cells 对象,
- 源列索引, 和
- 目标列索引.

使用CopyColumn方法在工作表内或者不同工作表之间复制一列。

该示例将一个工作表中的列复制到另一个工作簿的工作表中。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns-new.cpp" >}}
