---
title: 显示和隐藏行、列和滚动条
type: docs
weight: 20
url: /zh/net/show-and-hide-rows-columns-and-scroll-bars/
description: 本文演示了如何使用C#语言和.NET API或库来以编程方式显示和隐藏Excel工作表的行和列。可以调整滚动条的可见性，并且可以隐藏多行和列。
---

{{% alert color="primary" %}}

Aspose.Cells提供了一种控制工作表的行、列和滚动条可见性的方法。

{{% /alert %}}

## **显示和隐藏行和列**

Aspose.Cells提供了一个表示Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许开发人员访问Excel文件中的每个工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合，代表工作表中的所有单元格。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合提供了若干用于管理工作表中的行或列的方法。其中一些将在下面讨论。

### **显示行和列**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow)和[**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn)方法，分别显示任何隐藏的行或列。两种方法都需要两个参数：

- 行或列索引 - 用于显示特定行或列的索引。
- 行高或列宽 - 在取消隐藏后分配给行或列的行高或列宽。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

在使隐藏的列可见时，如果需要恢复其先前分配的宽度或其原始宽度，请使用负宽度取消隐藏列。例如：worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **隐藏行和列**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow)和[**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn)方法，分别隐藏行或列。两种方法都以行索引或列索引作为参数，以隐藏特定的行或列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

还可以通过将行高或列宽设置为0来隐藏行或列。

{{% /alert %}}

### **隐藏多个行和列**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows)和[**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns)方法，分别一次隐藏多行或列。两种方法都需要起始行或列索引和应该隐藏的行数或列数作为参数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **显示和隐藏滚动条**

滚动条用于浏览任何文件的内容。通常有两种类型的滚动条：

- 垂直滚动条
- 水平滚动条

Microsoft Excel还提供水平和垂直滚动条，以便用户可以滚动工作表内容。使用Aspose.Cells，开发人员可以控制Excel文件中两种类型滚动条的可见性。

### **控制滚动条的可见性**

Aspose.Cells 提供了代表 Excel 文件的一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类提供了一系列用于管理 Excel 文件的属性和方法。要控制滚动条的可见性，请使用 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类的 [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) 和 [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) 属性。[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) 和 [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) 都是布尔属性，这意味着这些属性只能存储 **true** 或 **false** 值。

#### **显示滚动条**

通过将 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类的 [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) 或 [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) 属性设置为 **true** 来使滚动条可见。

#### **隐藏滚动条**

通过将 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类的 [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) 或 [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) 属性设置为 **false** 来隐藏滚动条。

**示例代码**

下面是一个完整的代码，打开一个Excel文件book1.xls，隐藏两个滚动条，然后将修改后的文件保存为output.xls。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
