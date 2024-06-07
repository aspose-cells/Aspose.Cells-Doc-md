---
title: 复制行和列
type: docs
weight: 20
url: /zh/cpp/copying-rows-and-columns/
---

## **介绍**
有时，您需要在工作表中复制行和列，而不是复制整个工作表。使用 Aspose.Cells，可以在工作簿内或工作簿之间复制行和列。
当复制行（或列）时，其中包含的数据，包括公式、更新引用的值、注释、格式、隐藏单元格、图像和其他绘图对象也会被复制。
## **使用 Microsoft Excel 复制行和列**
1. 选择要复制的行或列。
1. 要复制行或列，单击**标准**工具栏上的**复制**，或按下**CTRL**+**C**。
1. 选择要复制所选内容下方或右侧的行或列。
1. 在复制行或列时，单击**插入**菜单上的**复制的单元格**。

{{% alert color="primary" %}} 

如果您点击 **Paste** 工具栏上的 **Standard**，或者按下 **CTRL**+**V**，而不是在 **Insert** 菜单上点击命令，那么目标单元格的任何内容都将被替换。

{{% /alert %}} 
## **使用Aspose.Cells**
### **复制行**
Aspose.Cells 提供了 Aspose::Cells::ICells 类的 CopyRow 方法。该方法从源行复制所有类型的数据，包括公式、值、注释、单元格格式、隐藏单元格、图像和其他绘图对象到目标行。

CopyRow 方法接受以下参数:

- 源 Cells 对象，
- 源行索引，以及
- 目标行索引。

使用此方法在工作表内复制行或到另一个工作表。 CopyRow 方法的工作方式类似于 Microsoft Excel。 例如，您无需显式设置目标行的高度，该值也会被复制。

下面的示例显示了如何在工作表中复制行。它使用一个模板 Microsoft Excel 文件，将第二行（包括数据、格式、注释、图像等）复制并粘贴到同一工作表的第12行。

您可以跳过使用 **GetRowHeigh** 方法获取源行高度然后使用 **SetRowHeight** 方法设置目标行高度的步骤，因为 **CopyRow** 方法会自动处理行高。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows-new.cpp" >}}

{{% alert color="primary" %}} 

在复制行时，重要的是注意相关图像、图表或其他绘图对象，这与 Microsoft Excel 相同:

1. 如果源行索引为5，且图像、图表等内容位于三行内 (起始行索引为4，结束行索引为6)，则其内容将被复制。
1. 目标行中现有的图像、图表等内容不会被移除。

{{% /alert %}} 
### **复制列**
Aspose.Cells 提供了 Aspose::Cells::ICells 类的 CopyColumn 方法，该方法可以从源列复制包括公式、更新引用、值、注释、单元格格式、隐藏单元格、图像和其他绘图对象等所有类型的数据到目标列。

CopyColumn 方法接受以下参数:

- 源 Cells 对象，
- 源列索引，以及
- 目标列索引。

使用 CopyColumn 方法在工作表内复制列或到另一个工作表。

此示例将工作表中的一列复制并粘贴到另一个工作簿的工作表中。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns-new.cpp" >}}
