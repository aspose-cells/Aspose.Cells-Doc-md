---
title: 复制行和列
type: docs
weight: 40
url: /zh/net/copying-rows-and-columns/
description: 本文介绍如何通过 Aspose.Cells for .NET API 复制行和列。
keywords: C# How to Copy Rows and Columns, Copy Rows in C#, Copy Columns using C#, How to Paste Rows and Columns using Aspose.Cells for .NET, Paste multiple rows and columns, How to Copy and paste Single Row or Column.
---
##  **介绍**

有时，您需要复制工作表中的行和列，而不复制整个工作表。使用 Aspose.Cells，可以在工作簿内或工作簿之间复制行和列。
复制行（或列）时，其中包含的数据（包括公式（带有更新的引用）以及值、注释、格式、隐藏单元格、图像和其他绘图对象）也会被复制。

##  **如何使用 Microsoft Excel 复制行和列**

1. 选择要复制的行或列。
1. 要复制行或列，请单击**复制**于**标准**工具栏，或按**CTRL**+*C**。
1. 选择要复制选择的位置下方或右侧的行或列。
1. 当您复制行或列时，单击**复制Cells**于**插入**菜单。

{{% alert color="primary" %}}

如果您点击**粘贴**于**标准**工具栏或按**CTRL**+**V** 而不是单击 **Insert 上的命令**菜单中，目标单元格的所有内容都会被替换。

{{% /alert %}}

##  **如何使用 Microsoft Excel 的粘贴选项粘贴行和列**

1. 选择包含要复制的数据或其他属性的单元格。
1. 在“主页”选项卡上，单击“*复制**”。
1. 单击您想要的区域中的第一个单元格**粘贴**你复制的内容。
1. 在“主页”选项卡上，单击旁边的箭头**粘贴**，然后选择**粘贴**特别的。
1. 选择**选项**你要。

##  **如何使用 Aspose.Cells for .NET 复制行和列**

##  **如何复制单行**

 Aspose.Cells 提供[**复制行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)班级。此方法将所有类型的数据（包括公式、值、注释、单元格格式、隐藏单元格、图像和其他绘图对象）从源行复制到目标行。

这[**复制行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)方法采用以下参数：

- 来源[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)目的，
- 源行索引，以及
- 目标行索引。

使用此方法可将一个工作表中的行复制到另一个工作表中。这[**复制行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)该方法的工作原理与 Microsoft Excel 类似。因此，例如，您不需要显式设置目标行的高度，该值也会被复制。

以下示例显示如何复制工作表中的行。它使用模板 Microsoft Excel 文件并复制第二行（包含数据、格式、注释、图像等）并将其粘贴到同一工作表中的第 12 行。

您可以使用以下命令跳过获取源行高的步骤[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight)方法，然后使用设置目标行高[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)方法如[**复制行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)方法自动处理行高。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

复制行时，请务必注意相关图像、图表或其他绘图对象，因为这与 Microsoft Excel 相同：

1. 如果源行索引为 5，则如果图像、图表等包含在三行（起始行索引为 4，结束行索引为 6）中，则复制该图像、图表等。
1. 目标行中现有的图像、图表等不会被删除。

{{% /alert %}}

##  **如何复制多行**

您还可以在使用时将多行复制到新目标[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)方法，它采用整数类型的附加参数来指定要复制的源行数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


##  **如何复制列**

 Aspose.Cells 提供[**复制列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)类，此方法复制所有类型的数据，包括公式（带有更新的引用）以及值、注释、单元格格式、隐藏单元格、图像和其他绘图对象从源列到目标列。

这[**复制列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)方法采用以下参数：

- 来源[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)目的，
- 源列索引，以及
- 目标列索引。

使用[**复制列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)将一个工作表中的列复制到另一个工作表的方法。

此示例从工作表复制一列并将其粘贴到另一个工作簿的工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

##  **如何复制多列**

如同[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)方法，Aspose.Cells API 还提供[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)方法，以便将多个源列复制到新位置。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


##  **如何使用粘贴选项粘贴行和列**

 Aspose.Cells现提供[**粘贴选项**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions)使用函数时[**复制行**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2)和[**复制列**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1)。它允许设置适当的粘贴选项，类似于 Excel。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

