---
title: 复制行和列
type: docs
weight: 20
url: /zh/cpp/copying-rows-and-columns/
---
##  **介绍**
有时您需要复制工作表中的行和列，而不复制整个工作表。使用 Aspose.Cells，可以在工作簿内或工作簿之间复制行和列。
复制行（或列）时，其中包含的数据（包括公式（带有更新的引用）以及值、注释、格式、隐藏单元格、图像和其他绘图对象）也会被复制。
##  **使用 Microsoft Excel 复制行和列**
1. 选择要复制的行或列。
1. 要复制行或列，请单击**复制**于**标准**工具栏，或按**CTRL**+*C**。
1. 选择要复制选择的位置下方或右侧的行或列。
1. 当您复制行或列时，单击**复制Cells**于**插入**菜单。

{{% alert color="primary" %}} 

如果您点击**粘贴**于**标准**工具栏或按**CTRL**+**V** 而不是单击 **Insert 上的命令**菜单中，目标单元格的任何内容都会被替换。

{{% /alert %}} 
##  **使用Aspose.Cells**
###  **复制行**
Aspose.Cells 提供 Aspose::Cells::ICells 类的 CopyRow 方法。此方法将所有类型的数据（包括公式、值、注释、单元格格式、隐藏单元格、图像和其他绘图对象）从源行复制到目标行。

CopyRow 方法采用以下参数：

- 源 Cells 对象，
- 源行索引，以及
- 目标行索引。

使用此方法可将一个工作表中的行复制到另一个工作表中。 CopyRow 方法的工作方式与 Microsoft Excel 类似。因此，例如，您不需要显式设置目标行的高度，该值也会被复制。

以下示例显示如何复制工作表中的行。它使用模板 Microsoft Excel 文件并复制第二行（包含数据、格式、注释、图像等）并将其粘贴到同一工作表中的第 12 行。

您可以使用以下命令跳过获取源行高的步骤**获取行高**方法，然后使用设置目标行高**设置行高**方法如**复制行**方法自动处理行高。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows-new.cpp" >}}

{{% alert color="primary" %}} 

复制行时，请务必注意相关图像、图表或其他绘图对象，因为这与 Microsoft Excel 相同：

1. 如果源行索引为 5，则如果图像、图表等包含在三行中（起始行索引为 4，结束行索引为 6），则复制该图像、图表等。
1. 目标行中的现有图像、图表等不会被删除。

{{% /alert %}} 
###  **复制列**
Aspose.Cells 提供 Aspose::Cells::ICells 类的 CopyColumn 方法，此方法从源复制所有类型的数据，包括公式（带有更新的引用）以及值、注释、单元格格式、隐藏单元格、图像和其他绘图对象列到目标列。

CopyColumn 方法采用以下参数：

- 源 Cells 对象，
- 源列索引，以及
- 目标列索引。

使用 CopyColumn 方法将工作表中的列复制到另一个工作表。

此示例从工作表复制一列并将其粘贴到另一个工作簿的工作表中。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns-new.cpp" >}}
