---
title: 显示和隐藏行列和滚动条
type: docs
weight: 20
url: /zh/net/show-and-hide-rows-columns-and-scroll-bars/
---
{{% alert color="primary" %}}

Aspose.Cells 提供了控制工作表行、列和滚动条可见性的方法。

{{% /alert %}}

## **显示和隐藏行和列**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许开发人员访问 Excel 文件中的每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)代表工作表中所有单元格的集合。这[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection 提供了多种方法来管理工作表中的行或列。下面讨论其中的一些。

### **显示行和列**

开发人员可以通过调用[**取消隐藏行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow)和[**取消隐藏列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)分别收藏。两种方法都有两个参数：

- **行或列索引** 用于显示特定行或列的行或列的索引。
- **行高或列宽** 取消隐藏后分配给行或列的行高或列宽。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

在使隐藏的列可见时，如果您需要将其恢复到先前分配的宽度或原始宽度，请取消隐藏宽度为负的列。例如：worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **隐藏行和列**

开发人员可以通过调用[**隐藏行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow)和[**隐藏列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)分别收藏。这两种方法都将行和列索引作为参数来隐藏特定的行或列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

也可以通过将行高或列宽分别设置为 0 来隐藏行或列。

{{% /alert %}}

### **隐藏多行多列**

开发人员可以通过调用[**隐藏行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows)和[**隐藏列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)分别收藏。这两种方法都将起始行或列索引以及应隐藏的行数或列数作为参数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **显示和隐藏滚动条**

滚动条用于导航任何文件的内容。通常，有两种滚动条：

- 垂直滚动条
- 水平滚动条

Microsoft Excel 还提供水平和垂直滚动条，以便用户可以滚动浏览工作表内容。使用 Aspose.Cells，开发人员可以控制 Excel 文件中两种滚动条的可见性。

### **控制滚动条的可见性**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示一个 Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类提供了广泛的属性和方法来管理 Excel 文件。要控制滚动条的可见性，请使用[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级'[**工作簿设置.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)和[**工作簿设置.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)特性。[**工作簿设置.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)和[**工作簿设置.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)是布尔属性，这意味着这些属性只能存储**真的**或者**错误的**值。

#### **使滚动条可见**

通过设置滚动条可见[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级'[**工作簿设置.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)或者[**工作簿设置.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)财产给**真的**.

#### **隐藏滚动条**

通过设置隐藏滚动条[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级'[**工作簿设置.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)或者[**工作簿设置.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)财产给**错误的**.

**示例代码**

下面是打开 Excel 文件 book1.xls 的完整代码，隐藏两个滚动条，然后将修改后的文件保存为 output.xls。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
