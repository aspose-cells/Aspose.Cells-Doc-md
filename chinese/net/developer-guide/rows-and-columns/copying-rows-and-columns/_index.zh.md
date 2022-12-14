---
title: 复制行和列
type: docs
weight: 40
url: /zh/net/copying-rows-and-columns/
---
## **介绍**

有时，您需要复制工作表中的行和列而不复制整个工作表。使用 Aspose.Cells，可以在工作簿内或工作簿之间复制行和列。
复制行（或列）时，其中包含的数据，包括公式（具有更新的引用）和值、注释、格式、隐藏的单元格、图像和其他绘图对象也会被复制。

## **使用 Microsoft Excel 复制行和列**

1. 选择要复制的行或列。
1. 要复制行或列，请单击**复制**在**标准**工具栏，或按**CTRL键**+**C**。
1. 选择要复制选择的位置下方或右侧的行或列。
1. 复制行或列时，单击**已复制 Cells**在**插入**菜单。

{{% alert color="primary" %}}

如果你点击**粘贴**在**标准**工具栏或按**CTRL键**+**V** 而不是单击命令**Insert** 菜单，目标单元格的任何内容都被替换。

{{% /alert %}}

## **在 Microsoft Excel 中使用粘贴选项粘贴行和列**

1. 选择包含要复制的数据或其他属性的单元格。
1. 在主页选项卡上，单击**复制**.
1. 单击要添加的区域中的第一个单元格**粘贴**你复制了什么。
1. 在主页选项卡上，单击旁边的箭头**粘贴** 然后选择**粘贴**特别的。
1. 选择**选项**你要。

## **使用 Aspose.Cells**

## **复制单行**

Aspose.Cells 提供了[**复制行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)班级。此方法将所有类型的数据（包括公式、值、注释、单元格格式、隐藏单元格、图像和其他绘图对象）从源行复制到目标行。

这[**复制行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)方法采用以下参数：

- 来源[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)目的，
- 源行索引，和
- 目标行索引。

使用此方法复制工作表中的一行，或复制到另一个工作表。这[**复制行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)方法的工作方式与 Microsoft Excel 类似。因此，例如，您不需要明确设置目标行的高度，该值也会被复制。

下面的示例演示如何复制工作表中的一行。它使用模板 Microsoft Excel 文件并复制第二行（包含数据、格式、注释、图像等）并将其粘贴到同一工作表中的第 12 行。

您可以跳过使用获取源行高的步骤[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight)方法，然后使用[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)方法作为[**复制行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)方法自动处理行高。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

复制行时，重要的是要注意相关的图像、图表或其他绘图对象，因为这与 Microsoft Excel 相同：

1. 如果源行索引为 5，则如果图像、图表等包含在三行中（起始行索引为 4，结束行索引为 6），则复制该图像、图表等。
1. 目标行中的现有图像、图表等不会被删除。

{{% /alert %}}

## **复制多行**

您还可以在使用[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)方法采用整数类型的附加参数来指定要复制的源行数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **复制列**

Aspose.Cells 提供了[**复制列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)类，此方法将所有类型的数据，包括公式（具有更新的引用）和值、注释、单元格格式、隐藏单元格、图像和其他绘图对象从源列复制到目标列。

这[**复制列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)方法采用以下参数：

- 来源[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)目的，
- 源列索引，和
- 目标列索引。

使用[**复制列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)在工作表中复制列或复制到另一个工作表的方法。

本示例从工作表复制一列并将其粘贴到另一个工作簿的工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **复制多列**

如同[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)方法，Aspose.Cells API 还提供了[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)方法以便将多个源列复制到新位置。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **使用粘贴选项粘贴行/列**

Aspose.Cells现在提供[**粘贴选项**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions)在使用功能时[**复制行**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2)和[**复制列**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1).它允许设置类似于 Excel 的适当粘贴选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

