---
title: 隐藏和显示行和列
type: docs
weight: 60
url: /zh/python-net/hiding-and-showing-rows-and-columns/
description: 本文介绍了如何通过 Aspose.Cells for Python 通过 .NET API 隐藏和显示行和列。
keywords: Python Excel库，Aspose.Cells Python 隐藏和显示行，Python 隐藏和显示列，Python 隐藏行和列，Python 显示行和列。
---

{{% alert color="primary" %}}

有时，在工作表中隐藏某些行或列并稍后显示它们是有道理的。Microsoft Excel 提供了此功能，Aspose.Cells for Python 通过 .NET 也提供了。

{{% /alert %}}

## **控制行和列的可见性**

Aspose.Cells for Python 通过 .NET 提供了一个表示 Microsoft Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)，允许开发人员访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供了一个 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)，表示工作表中的所有单元格。[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合提供了几种用于管理工作表中行或列的方法。以下是其中的一些讨论。

## **如何隐藏行和列**

开发人员可以通过调用 [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) 和 [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) 方法来隐藏 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合中的行或列。这两种方法都将行和列索引作为参数，以隐藏特定的行或列。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

还可以将行高或列宽分别设置为 0 来隐藏行或列。

{{% /alert %}}

## **如何显示行和列**

开发人员可以通过调用 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合的 [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) 和 [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) 方法来显示任何隐藏的行或列。这两种方法都有两个参数:

- **行或列索引** - 用于显示特定行或列的行或列索引。
- **行高或列宽** - 在取消隐藏后分配给行或列的行高或列宽。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

将隐藏的列显示出来时，如果需要将其恢复为先前分配的宽度或其原始宽度，请以负宽度取消隐藏列。例如：worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

## **如何隐藏多行和列**

开发人员可以通过调用 [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) 和 [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns/) 方法一次隐藏多行或列，分别将起始行或列索引和应该隐藏的行或列数作为参数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

也可以使用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)类的[**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows/)和[**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns/)方法使多行和列可见。

{{% /alert %}}
