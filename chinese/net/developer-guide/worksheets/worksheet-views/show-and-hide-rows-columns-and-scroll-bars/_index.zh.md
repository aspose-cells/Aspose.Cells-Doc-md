---
title: 显示和隐藏行、列和滚动条
type: docs
weight: 20
url: /zh/net/show-and-hide-rows-columns-and-scroll-bars/
description: 本文演示了如何使用 C# 语言和 .NET API 或库来以编程方式显示和隐藏 Excel 工作表的行和列。滚动条的可见性可以调整，可以隐藏几行和几列。
---

{{% alert color="primary" %}}

Aspose.Cells 提供了控制工作表的行、列和滚动条可见性的方法。

{{% /alert %}}

## **显示和隐藏行和列**

Aspose.Cells 提供一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许开发人员访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供一个 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合，表示工作表中的所有单元格。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合提供几种管理工作表中的行或列的方法。以下讨论了其中的一些。

### **显示行和列**

开发人员可以通过调用 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合的 [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) 和 [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) 方法来显示任何隐藏的行或列。这两种方法都有两个参数:

- **行或列索引** - 用于显示特定行或列的行或列索引。
- **行高或列宽** - 在取消隐藏后分配给行或列的行高或列宽。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

将隐藏的列显示出来时，如果需要将其恢复为先前分配的宽度或其原始宽度，请以负宽度取消隐藏列。例如：worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **隐藏行和列**

开发人员可以通过调用 [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) 和 [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) 方法来隐藏 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合中的行或列。这两种方法都将行和列索引作为参数，以隐藏特定的行或列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

还可以将行高或列宽分别设置为 0 来隐藏行或列。

{{% /alert %}}

### **隐藏多行和列**

开发人员可以通过调用 [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) 和 [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) 方法一次隐藏多行或列，分别将起始行或列索引和应该隐藏的行或列数作为参数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **显示和隐藏滚动条**

滚动条用于浏览任何文件的内容。通常，有两种类型的滚动条：

- 垂直滚动条
- 水平滚动条

Microsoft Excel 还提供水平和垂直滚动条，以便用户可以滚动工作表内容。使用 Aspose.Cells，开发人员可以控制 Excel 文件中两种类型滚动条的可见性。

### **控制滚动条的可见性**

Aspose.Cells 提供了一个代表 Excel 文件的类 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类提供了广泛的属性和方法来管理 Excel 文件。要控制滚动条的可见性，请使用 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类的 [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) 和 [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) 属性。[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) 和 [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) 是布尔属性，这意味着这些属性只能存储 **true** 或 **false** 值。

#### **使滚动条可见**

通过将 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类的 [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) 或 [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) 属性设置为 **true** 来使滚动条可见。

#### **隐藏滚动条**

通过将 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类的 [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) 或 [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) 属性设置为 **false** 来隐藏滚动条。

**示例代码**

以下是完整代码，打开一个 Excel 文件，book1.xls，隐藏两个滚动条，然后将修改后的文件保存为 output.xls。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
