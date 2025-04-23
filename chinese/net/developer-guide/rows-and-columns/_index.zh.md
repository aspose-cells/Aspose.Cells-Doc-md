---
title: 格式化行和列
linktitle: 行和列
type: docs
weight: 100
url: /zh/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET可以支持更改行高或列宽，并对行或列应用格式。
keywords: 设置行高和列宽，调整行高和列宽，更改行高或列宽，格式化行和列，如何设置行高和列宽。
---


{{% alert color="primary" %}}

在处理电子表格并向行或列添加数据时，您可能需要更改行的高度或列的宽度。有时，对行或列应用格式意味着当前的高度或宽度需要更改以显示数据。通常，用户在Microsoft Excel中使用所见即所得的环境来调整行高和列宽。但是，使用Aspose.Cells，开发人员可以在运行时执行这些操作。

{{% /alert %}}

## **处理行**

### **如何调整行高**

Aspose.Cells提供了一个表示Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合，表示工作表中的所有单元格。

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合提供了几种方法来管理工作表中的行或列。以下将更详细讨论其中的一些。

### **如何设置行的高度**

可以通过调用 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合的 [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) 方法来设置单行的高度。[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) 方法采用以下参数：

- **行索引**，要更改高度的行的索引。
- **行高**，要应用于该行的行高。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **如何设置工作表中所有行的高度**

如果开发人员需要为工作表中的所有行设置相同的行高，可以使用 [**StandardHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) 集合的 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 属性。

**示例：**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **使用列**

### **如何设置列的宽度**

通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合的[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)方法设置列的宽度。[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)方法接受以下参数：

- **列索引**，要更改其宽度的列的索引。
- **列宽度**，所需的列宽度。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **如何以像素设置列宽**

通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合的[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)方法设置列的宽度。[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)方法接受以下参数：

- **列索引**，要更改其宽度的列的索引。
- **列宽**，以像素为单位的期望列宽。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **如何设置工作表中所有列的宽度**

要为工作表中所有列设置相同的列宽，请使用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合的[**StandardWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **高级主题**
- [自动调整行和列](/cells/zh/net/autofit-rows-and-columns/)
- [使用Aspose.Cells将文本转换为列](/cells/zh/net/convert-text-to-columns-using-aspose-cells/)
- [复制行和列](/cells/zh/net/copying-rows-and-columns/)
- [在工作表中删除空白行和列](/cells/zh/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [分组和取消分组行和列](/cells/zh/net/grouping-and-ungrouping-rows-and-columns/)
- [隐藏和显示行和列](/cells/zh/net/hiding-and-showing-rows-and-columns/)
- [在Excel工作表中插入或删除行](/cells/zh/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [插入和删除Excel文件的行和列](/cells/zh/net/inserting-and-deleting-rows-and-columns/)
- [在工作表中删除重复行](/cells/zh/net/remove-duplicate-rows-in-a-worksheet/)
- [删除工作表中的空白列和行时更新其他工作表中的引用](/cells/zh/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
{{< app/cells/assistant language="csharp" >}}
