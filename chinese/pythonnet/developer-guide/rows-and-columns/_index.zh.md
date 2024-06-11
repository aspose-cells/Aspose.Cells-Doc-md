---
title: 格式化行和列
linktitle: 行和列
type: docs
weight: 100
url: /zh/python-net/adjusting-row-height-and-column-width/
description: 使用Aspose.Cells for Python通过.NET可以支持更改行高或列宽，并在行或列上应用格式。
keywords: Python Excel库，Python设置行高和列宽，Python调整行高和列宽，Python更改行高或列宽，Python格式化行和列，Python如何设置行高和列宽。
---


{{% alert color="primary" %}}

在处理电子表格并向行或列添加数据时，可能需要更改行高或列宽。有时，在行或列上应用格式意味着当前的高度或宽度需要改变以显示数据。通常，用户在Microsoft Excel的所见即所得环境中调整行高和列宽。但是，使用Aspose.Cells for Python通过.NET，开发人员可以在运行时执行这些操作。

{{% /alert %}}

## **处理行**

### **如何调整行高**

Aspose.Cells for Python通过.NET提供了一个类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，代表了Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合，表示工作表中的所有单元格。

[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合提供了多种管理工作表中行或列的方法。下面详细讨论其中一些。

### **如何设置行高**

可以通过调用 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合的 [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) 方法来设置单行的高度。[**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) 方法接受以下参数：

- **row**，要更改高度的行索引。
- **height**，应用在行上的行高。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightOfRow-1.py" >}}

### **如何设置工作表中所有行的高度**

如果开发人员需要为工作表中的所有行设置相同的行高，他们可以使用 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合的 [**standard_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_height) 属性。

**示例：**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightAllRows-1.py" >}}

## **处理列**

### **如何设置列宽**

通过调用 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合的 [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) 方法设置列的宽度。[**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) 方法接受以下参数：

- **column**，要更改宽度的列索引。
- **width**，期望的列宽。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.py" >}}

### **如何以像素为单位设置列宽**

通过调用 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合的 [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) 方法设置列的宽度。[**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) 方法接受以下参数：

- **column**，要更改宽度的列索引。
- **pixels**，期望的列宽（以像素为单位）。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.py" >}}

### **如何设置工作表中所有列的宽度**

要为工作表中的所有列设置相同的列宽，使用 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合的 [**standard_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_width) 属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.py" >}}

## **高级主题**
- [自适应行和列](/cells/zh/python-net/autofit-rows-and-columns/)
- [使用 Aspose.Cells 将文本转换为列](/cells/zh/python-net/convert-text-to-columns-using-aspose-cells/)
- [复制行和列](/cells/zh/python-net/copying-rows-and-columns/)
- [在工作表中删除空白行和列](/cells/zh/python-net/delete-blank-rows-and-columns-in-a-worksheet/)
- [分组和取消分组行和列](/cells/zh/python-net/grouping-and-ungrouping-rows-and-columns/)
- [隐藏和显示行和列](/cells/zh/python-net/hiding-and-showing-rows-and-columns/)
- [在 Excel 工作表中插入或删除行](/cells/zh/python-net/insert-or-delete-rows-in-an-excel-worksheet/)
- [插入和删除 Excel 文件的行和列](/cells/zh/python-net/inserting-and-deleting-rows-and-columns/)
- [在工作表中删除重复行](/cells/zh/python-net/remove-duplicate-rows-in-a-worksheet/)
- [在删除工作表中的空白列和行时更新其他工作表中的引用](/cells/zh/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
