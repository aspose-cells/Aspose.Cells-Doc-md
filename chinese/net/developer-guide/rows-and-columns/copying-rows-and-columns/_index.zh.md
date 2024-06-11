---
title: 复制行和列
type: docs
weight: 40
url: /zh/net/copying-rows-and-columns/
description: 本文章展示了如何通过 Aspose.Cells for .NET API 复制行和列。
keywords: C# 如何复制行和列、使用 C# 复制行、复制列、使用 Aspose.Cells for .NET 粘贴行和列、粘贴多行和多列、如何复制和粘贴单行或单列。
---

## **介绍**

有时，您需要在不复制整个工作表的情况下复制工作表中的行和列。使用Aspose.Cells，可以在工作簿内部或工作簿之间复制行和列。
复制行（或列）时，其中包含的数据，包括更新的引用的公式和值，注释，格式，隐藏单元格，图像以及其他绘图对象也会被复制。

## **使用Microsoft Excel如何复制行和列**

1. 选择要复制的行或列。
1. 要复制行或列，请单击 **标准** 工具栏上的 **复制**，或按 **CTRL**+**C**。
1. 选择要复制所选内容下方或右侧的行或列。
1. 复制行或列时，单击 **已复制的单元格** 在 **插入** 菜单上。

{{% alert color="primary" %}}

如果您在**标准**工具栏上单击**粘贴**，或者按**Ctrl**+**V**键，而不是在**插入**菜单上单击命令，则目标单元格的任何内容都将被替换。

{{% /alert %}}

## **如何使用Microsoft Excel的粘贴选项粘贴行和列**

1. 选择包含您要复制的数据或其他属性的单元格。
1. 在主页选项卡上，单击**复制**。
1. 单击要在其中**粘贴**所复制内容的区域中的第一个单元格。
1. 在主页选项卡上，单击**粘贴**旁边的箭头，然后选择**粘贴**特殊。
1. 选择您想要的**选项**。

## **如何使用 Aspose.Cells for .NET 复制行和列**

## **如何复制单行**

Aspose.Cells提供[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)类的[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)方法。此方法将所有类型的数据复制到目标行，包括公式，值，注释，单元格格式，隐藏单元格，图像和其他绘图对象。

[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) 方法接受以下参数：

- 来源 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 对象，
- 源行索引, 和
- 目标行索引.

使用此方法在工作表内或另一工作表之间复制一行。 [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) 方法的工作原理类似于 Microsoft Excel。例如，不需要明确设置目标行高度，该值也会被复制。

以下示例显示如何在工作表中复制一行。它使用一个模板 Microsoft Excel 文件，将第二行（包括数据、格式、注释、图像等）复制并粘贴到同一工作表的第12行。

您可以跳过使用 [**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) 方法获取源行高度然后使用 [**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) 方法设置目标行高度的步骤，因为 [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) 方法会自动处理行高度。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

在复制行时，重要的是注意相关的图像、图表或其他绘图对象，因为这与 Microsoft Excel 相同：

1. 如果源行索引为5，则如果它包含在三行内（起始行索引为4，结束行索引为6），则图像、图表等会被复制。
1. 目标行中现有的图像、图表等不会被移除。

{{% /alert %}}

## **如何复制多行**

您还可以在使用 [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) 方法将多行复制到新目标时，该方法需要一个额外的整数参数，用于指定要复制的源行数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **如何复制列**

Aspose.Cells 提供 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 类的 [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) 方法，此方法复制来自源列到目标列的各种数据，包括更新后的引用公式和数值、注释、单元格格式、隐藏单元格、图像和其他绘图对象。

[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) 方法接受以下参数：

- 来源 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 对象，
- 源列索引, 和
- 目标列索引.

使用 [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) 方法在工作表内或另一工作表中复制列。

该示例将一个工作表中的列复制到另一个工作簿的工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **如何复制多列**

与 [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) 方法类似，Aspose.Cells API 还提供 [**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index) 方法，用于将多个源列复制到新位置。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **如何粘贴行和列并设置粘贴选项**

Aspose.Cells 现在提供 [**PasteOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions)，使用函数 [**CopyRows**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) 和 [**CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1)。它允许设置类似于 Excel 的适当粘贴选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

