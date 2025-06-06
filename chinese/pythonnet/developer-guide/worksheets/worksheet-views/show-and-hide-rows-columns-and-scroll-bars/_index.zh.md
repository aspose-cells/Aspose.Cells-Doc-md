---
title: 显示和隐藏行、列和滚动条
type: docs
weight: 20
url: /zh/python-net/show-and-hide-rows-columns-and-scroll-bars/
description: 本文演示如何使用 Aspose.Cells for Python via .NET API 编程式地显示和隐藏 Excel 工作表的行和列。可以调节滚动条的可见性，并隐藏多个行和列。
keywords: Python Excel库，Python显示行和列，Python隐藏行和列，Python显示垂直滚动条，Python显示水平滚动条，Python隐藏垂直滚动条，Python隐藏水平滚动条，Python显示和隐藏行列及滚动条。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 提供了控制工作表的行、列和滚动条可见性的方法。

{{% /alert %}}

## **显示和隐藏行和列**

Aspose.Cells for Python via .NET 提供了一个类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类含有一个 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) 集合，允许开发者访问每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供一个 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合，表示工作表中的所有单元格。[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合提供了管理工作表中行或列的若干方法，部分内容如下。

### **显示行和列**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)集合的[**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/)和[**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/)方法，分别显示任何隐藏的行或列。两种方法都需要两个参数：

- 行或列索引 - 用于显示特定行或列的索引。
- 行高或列宽 - 在取消隐藏后分配给行或列的行高或列宽。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

在使隐藏的列可见时，如果需要恢复其先前分配的宽度或其原始宽度，请使用负宽度取消隐藏列。例如：worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **隐藏行和列**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)集合的[**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/)和[**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/)方法，分别隐藏行或列。两种方法都以行索引或列索引作为参数，以隐藏特定的行或列。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

还可以通过将行高或列宽设置为0来隐藏行或列。

{{% /alert %}}

### **隐藏多个行和列**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)集合的[**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/)和[**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns)方法，分别一次隐藏多行或列。两种方法都需要起始行或列索引和应该隐藏的行数或列数作为参数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

## **显示和隐藏滚动条**

滚动条用于浏览任何文件的内容。通常有两种类型的滚动条：

- 垂直滚动条
- 水平滚动条

Microsoft Excel 还提供水平和垂直滚动条，用户可以滚动浏览工作表内容。使用 Aspose.Cells for Python via .NET，开发者可以控制这两种滚动条的可见性。

### **控制滚动条的可见性**

Aspose.Cells for Python via .NET 提供一个类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，代表一个 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类提供了丰富的属性和方法用于管理 Excel 文件。要控制滚动条的可见性，使用 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类的 [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) 和 [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) 属性。[**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) 和 [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) 是布尔属性，只能存储 **true** 或 **false**。

#### **显示滚动条**

通过将 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类的 [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) 或 [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) 属性设置为 **true** 来使滚动条可见。

#### **隐藏滚动条**

通过将 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类的 [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) 或 [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) 属性设置为 **false** 来隐藏滚动条。

**示例代码**

下面是一个完整的代码，打开一个Excel文件book1.xls，隐藏两个滚动条，然后将修改后的文件保存为output.xls。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Worksheets-Display-DisplayHideScrollBars-1.py" >}}
