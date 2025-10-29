---
title: 格式化行和列
linktitle: 行和列
type: docs
weight: 100
url: /zh/python-net/adjusting-row-height-and-column-width/
description: Aspose.Cells for Python via .NET 可以支持更改行高或列宽，并对行或列应用格式。
keywords: Python Excel 库，Python 设置行高和列宽，Python 调整行高和列宽，Python 更改行高或列宽，Python 格式化行和列，Python 如何设置行高和列宽。
---


{{% alert color="primary" %}}

在处理电子表格并向行或列添加数据时，有时需要更改行高或列宽。有时，应用对行或列的格式意味着当前的高度或宽度需要更改以显示数据。通常，用户在 Microsoft Excel 中使用所见即所得的环境调整行高和列宽。但是，使用 Aspose.Cells for Python via .NET，开发人员可以在运行时执行这些操作。

{{% /alert %}}

## **处理行**

### **如何调整行高**

Aspose.Cells for Python via .NET 提供一个代表 Microsoft Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，该类允许访问 Excel 文件中的每个工作表。工作表由 [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) 类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供了 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 集合，该集合表示工作表中的所有单元格。

[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合提供了几种方法来管理工作表中的行或列。以下将更详细讨论其中的一些。

### **如何设置行的高度**

可以通过调用 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合的 [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) 方法来设置单行的高度。[**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) 方法采用以下参数：

- **row**，您要更改其高度的行的索引。
- **height**，要在行上应用的行高。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightOfRow-1.py" >}}

### **如何设置工作表中所有行的高度**

如果开发人员需要为工作表中的所有行设置相同的行高，可以使用 [**standard_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_height) 集合的 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 属性。

**示例：**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightAllRows-1.py" >}}

## **使用列**

### **如何设置列的宽度**

通过调用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合的[**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float)方法设置列的宽度。[**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float)方法接受以下参数：

- **column**，要更改宽度的列的索引。
- **width**，所需的列宽。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.py" >}}

### **如何以像素设置列宽**

通过调用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合的[**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int)方法设置列的宽度。[**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int)方法接受以下参数：

- **column**，要更改宽度的列的索引。
- **pixels**，以像素表示的所需列宽。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.py" >}}

### **如何设置工作表中所有列的宽度**

要为工作表中所有列设置相同的列宽，请使用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合的[**standard_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_width)属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.py" >}}

## **高级主题**
- [自动调整行和列](/cells/zh/python-net/autofit-rows-and-columns/)
- [使用Aspose.Cells将文本转换为列](/cells/zh/python-net/convert-text-to-columns-using-aspose-cells/)
- [复制行和列](/cells/zh/python-net/copying-rows-and-columns/)
- [在工作表中删除空白行和列](/cells/zh/python-net/delete-blank-rows-and-columns-in-a-worksheet/)
- [分组和取消分组行和列](/cells/zh/python-net/grouping-and-ungrouping-rows-and-columns/)
- [隐藏和显示行和列](/cells/zh/python-net/hiding-and-showing-rows-and-columns/)
- [在Excel工作表中插入或删除行](/cells/zh/python-net/insert-or-delete-rows-in-an-excel-worksheet/)
- [插入和删除Excel文件的行和列](/cells/zh/python-net/inserting-and-deleting-rows-and-columns/)
- [在工作表中删除重复行](/cells/zh/python-net/remove-duplicate-rows-in-a-worksheet/)
- [删除工作表中的空白列和行时更新其他工作表中的引用](/cells/zh/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
{{< app/cells/assistant language="python-net" >}}
