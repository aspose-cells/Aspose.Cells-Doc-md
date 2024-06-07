---
title: 复制行和列
type: docs
weight: 40
url: /zh/net/copying-rows-and-columns/
description: 此文章展示了如何通过Aspose.Cells for .NET API复制行和列。
keywords: C#如何复制行和列，使用C#复制行，使用C#复制列，如何使用Aspose.Cells for .NET粘贴多行和列，如何复制并粘贴单行或单列。
---

## **介绍**

有时，您需要在工作表中复制行和列，而无需复制整个工作表。使用Aspose.Cells，可以在工作簿内部或之间复制行和列。
复制行（或列）时，其中包含的数据，包括更新后的引用、值、注释、格式、隐藏单元格、图片和其他绘图对象也会被复制。

## **如何在Microsoft Excel中复制行和列**

1. 选择要复制的行或列。
1. 要复制行或列，单击**标准**工具栏上的**复制**，或按下**CTRL**+**C**。
1. 选择要复制所选内容下方或右侧的行或列。
1. 在复制行或列时，单击**插入**菜单上的**复制的单元格**。

{{% alert color="primary" %}}

如果您单击**标准**工具栏上的**粘贴**，或按**CTRL**+**V**，而不是在**插入**菜单上单击命令，则目标单元格的任何内容都将被替换。

{{% /alert %}}

## **如何使用 Microsoft Excel 的粘贴选项来复制行和列**

1. 选择包含要复制的数据或其他属性的单元格。
1. 在“开始”选项卡上，单击“复制”。
1. 单击要在其中粘贴复制内容的区域的第一个单元格。
1. 在“开始”选项卡上，单击“粘贴”旁边的箭头，然后选择“特粘贴”选项。
1. 选择所需的选项。

## **如何使用 Aspose.Cells for .NET 复制行和列**

## **如何复制单行**

Aspose.Cells 提供 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 类的 [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) 方法。该方法从源行复制包括公式、数值、注释、单元格格式、隐藏单元格、图像和其他绘图对象等所有类型的数据到目标行。

[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) 方法接受以下参数：

- 源 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 对象，
- 源行索引，以及
- 目标行索引。

使用该方法在同一工作表内或到另一个工作表内复制行。该方法与 Microsoft Excel 的工作方式类似。例如，您不需要显式设置目标行的高度，该值也会被复制。

以下示例显示了如何在工作表中复制一行。它使用一个模板 Microsoft Excel 文件，将第二行（包括数据、格式、注释、图像等等）复制并粘贴到同一工作表的第12行。

您可以跳过使用 [**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) 方法获取源行高度以及使用 [**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) 方法设置目标行高度的步骤，因为 [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) 方法会自动处理行高。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

在复制行时，重要注意相关图像、图表或其他绘图对象，因为这与 Microsoft Excel 相同：

1. 如果源行索引为 5，则图像、图表等会被复制，如果它们在三行中（起始行索引为 4，结束行索引为 6）。
1. 目标行中现有的图像、图表等不会被移除。

{{% /alert %}}

## **如何复制多行**

您还可以使用 [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) 方法复制多行到新的目标，该方法接受整数类型的额外参数以指定要复制的源行数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **如何复制列**

Aspose.Cells 提供 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 类的 [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) 方法，该方法从源列复制包括更新引用的公式和数值、注释、单元格格式、隐藏单元格、图像和其他绘图对象等所有类型的数据到目标列。

[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) 方法接受以下参数：

- 源 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 对象，
- 源列索引，以及
- 目标列索引。

使用 [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) 方法在同一工作表内或到另一个工作表内复制一列。

此示例将工作表中的一列复制并粘贴到另一个工作簿的工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **如何复制多列**

类似于 [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) 方法，Aspose.Cells API 还提供 [**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index) 方法，以便将多个源列复制到新位置。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **如何使用粘贴选项粘贴行和列**

在使用函数 [**CopyRows**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) 和 [**CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1) 时，Aspose.Cells 现在提供 [**PasteOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions)。它允许设置类似于 Excel 的适当粘贴选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

