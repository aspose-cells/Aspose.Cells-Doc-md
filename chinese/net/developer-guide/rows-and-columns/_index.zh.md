---
title: 设置行和列的格式
linktitle: 行和列
type: docs
weight: 100
url: /zh/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET 可以支持更改行高或列宽，以及在行或列上应用格式。
keywords: Set row height and column width, Adjust row height and column width, change the row height or column width, format rows and columns, how to set row height and column width.
---
{{% alert color="primary" %}}

使用电子表格并向行或列添加数据时，您可能需要更改行高或列宽。有时，在行或列上应用格式意味着需要更改当前高度或宽度才能显示数据。通常，用户使用 Microsoft Excel 在所见即所得环境中调整行高和列宽。但是，使用 Aspose.Cells 开发人员可以在运行时执行这些操作。

{{% /alert %}}

##  **使用行**

###  **如何调整行高**

Aspose.Cells提供一堂课，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表集合**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)允许访问 Excel 文件中的每个工作表。工作表由以下形式表示[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)代表工作表中所有单元格的集合。

这[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合提供了多种管理工作表中的行或列的方法。下面将更详细地讨论其中一些。

###  **如何设置行的高度**

可以通过调用来设置单行的高度[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏的[**设置行高**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)方法。这[**设置行高**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)方法采用以下参数：

- *行索引**，您要更改其高度的行的索引。
- *行高**，应用于行的行高。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

###  **如何设置工作表中所有行的高度**

如果开发人员需要为工作表中的所有行设置相同的行高，他们可以使用[**标准高度**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight)的财产[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。

**例子：**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

##  **使用列**

###  **如何设置列的宽度**

通过调用设置列的宽度[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏的[**设置列宽**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)方法。这[**设置列宽**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)方法采用以下参数：

- *列索引**，您要更改宽度的列的索引。
- *列宽**，所需的列宽。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

###  **如何设置列宽（以像素为单位）**

通过调用设置列的宽度[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏的[**设置列宽像素**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)方法。这[**设置列宽像素**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)方法采用以下参数：

- *列索引**，您要更改宽度的列的索引。
- *列宽**，所需的列宽（以像素为单位）。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

###  **如何设置工作表中所有列的宽度**

要为工作表中的所有列设置相同的列宽，请使用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏的[**标准宽度**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

##  **高级主题**
- [自动调整行和列](/cells/zh/net/autofit-rows-and-columns/)
- [使用 Aspose.Cells 将文本转换为列](/cells/zh/net/convert-text-to-columns-using-aspose-cells/)
- [复制行和列](/cells/zh/net/copying-rows-and-columns/)
- [删除工作表中的空白行和列](/cells/zh/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [对行和列进行分组和取消分组](/cells/zh/net/grouping-and-ungrouping-rows-and-columns/)
- [隐藏和显示行和列](/cells/zh/net/hiding-and-showing-rows-and-columns/)
- [在 Excel 工作表中插入或删除行](/cells/zh/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [插入和删除Excel文件的行和列](/cells/zh/net/inserting-and-deleting-rows-and-columns/)
- [删除工作表中的重复行](/cells/zh/net/remove-duplicate-rows-in-a-worksheet/)
- [删除工作表中的空白列和行时更新其他工作表中的引用](/cells/zh/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
