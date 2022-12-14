---
title: 复制行和列
type: docs
weight: 20
url: /zh/cpp/copying-rows-and-columns/
---
## **介绍**
有时您需要复制工作表中的行和列而不复制整个工作表。使用 Aspose.Cells，可以在工作簿内或工作簿之间复制行和列。
复制行（或列）时，其中包含的数据，包括公式（具有更新的引用）和值、注释、格式、隐藏的单元格、图像和其他绘图对象也会被复制。
## **使用 Microsoft Excel 复制行和列**
1. 选择要复制的行或列。
1. 要复制行或列，请单击**复制**在**标准**工具栏，或按**CTRL键**+**C**。
1. 选择要复制选择的位置下方或右侧的行或列。
1. 复制行或列时，单击**已复制 Cells**在**插入**菜单。

{{% alert color="primary" %}} 

如果你点击**粘贴**在**标准**工具栏或按**CTRL键**+**V** 而不是单击命令**Insert** 菜单，目标单元格的任何内容都被替换。

{{% /alert %}} 
## **使用 Aspose.Cells**
### **复制行**
Aspose.Cells提供Aspose::Cells::ICells类的CopyRow方法。此方法将所有类型的数据（包括公式、值、注释、单元格格式、隐藏单元格、图像和其他绘图对象）从源行复制到目标行。

CopyRow 方法采用以下参数：

- 源 Cells 对象，
- 源行索引，和
- 目标行索引。

使用此方法复制工作表中的一行，或复制到另一个工作表。 CopyRow 方法的工作方式与 Microsoft Excel 类似。因此，例如，您不需要明确设置目标行的高度，该值也会被复制。

下面的示例演示如何复制工作表中的一行。它使用模板 Microsoft Excel 文件并复制第二行（包含数据、格式、注释、图像等）并将其粘贴到同一工作表中的第 12 行。

您可以跳过使用获取源行高的步骤**获取行高**方法，然后使用**设置行高**方法作为**复制行**方法自动处理行高。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows.cpp" >}}

{{% alert color="primary" %}} 

复制行时，重要的是要注意相关的图像、图表或其他绘图对象，因为这与 Microsoft Excel 相同：

1. 如果源行索引为 5，则如果图像、图表等包含在三行中（起始行索引为 4，结束行索引为 6），则复制该图像、图表等。
1. 目标行中的现有图像、图表等不会被删除。

{{% /alert %}} 
### **复制列**
Aspose.Cells 提供 Aspose::Cells::ICells 类的 CopyColumn 方法，该方法从源中复制所有类型的数据，包括公式 - 更新引用 - 和值、注释、单元格格式、隐藏单元格、图像和其他绘图对象列到目标列。

CopyColumn 方法采用以下参数：

- 源 Cells 对象，
- 源列索引，和
- 目标列索引。

使用 CopyColumn 方法将列复制到工作表中或复制到另一个工作表。

本示例从工作表复制一列并将其粘贴到另一个工作簿的工作表中。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns.cpp" >}}
