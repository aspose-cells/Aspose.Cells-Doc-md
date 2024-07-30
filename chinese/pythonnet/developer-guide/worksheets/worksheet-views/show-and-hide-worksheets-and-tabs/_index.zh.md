---
title: 显示和隐藏工作表和选项卡
type: docs
weight: 10
url: /zh/python-net/show-and-hide-worksheets-and-tabs/
description: 本文提供了使用Aspose.Cells for Python via .NET API的示例代码，以编程方式显示和隐藏Excel工作表。此外，还介绍了如何显示和隐藏Excel工作簿选项卡。
keywords: Python Excel库，Python显示和隐藏工作表，Python显示和隐藏选项卡，Python控制选项卡栏宽度。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET允许用户显示和隐藏工作簿的元素，包括工作表和选项卡。

{{% /alert %}}

## **显示和隐藏工作表**

Excel文件可能包含一个或多个工作表。每当我们创建一个Excel文件时，在我们工作的Excel文件中添加工作表。Excel文件中的每个工作表都是独立的，具有自己的数据和格式设置等。有时，开发人员可能需要在他们的Excel文件中使几个工作表隐藏，而其他工作表可见。因此，“Aspose.Cells for Python via .NET”允许才开发人员控制工作表在Excel文件中的可见性。

Aspose.Cells for Python via .NET提供了一个表示Excel文件的类[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供了广泛的属性和方法来管理工作表。要控制工作表的可见性，请使用 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类的 [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) 属性。[**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) 是一个布尔属性，这意味着它只能存储 **true** 或 **false** 值。

### **使工作表可见**

通过将 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类的 [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) 属性设置为 **true** 来使工作表可见

### **隐藏工作表**

通过将[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类的[**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible)属性设置为**false**来隐藏工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideUnhideWorksheet-1.py" >}}

## **显示和隐藏标签**

如果您仔细查看Microsoft Excel文件的底部，您会看到许多控件。其中包括:

- 工作表标签。
- 选项卡滚动按钮。

工作表标签代表Excel文件中的工作表。单击任何选项卡以切换到该工作表。工作簿中有更多的工作表，也会有更多的工作表标签。如果Excel文件有大量工作表，您需要按钮来进行导航。因此，Microsoft Excel提供了选项卡滚动按钮来滚动工作表标签。

使用Aspose.Cells for Python via .NET，开发人员可以控制Excel文件中工作表选项卡和选项卡滚动按钮的可见性。

Aspose.Cells for Python via .NET提供了一个表示Excel文件的类[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类提供了一系列属性和方法来管理Excel文件。要控制Excel文件中选项卡的可见性，开发人员可以使用[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类的[**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)属性。[**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)是一个布尔属性，意味着它只能存储true或false值。

### **使选项卡可见**

使用[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类的[**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)属性将标签设置为**true**来使标签可见。

### **隐藏选项卡**

通过将[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类的[**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)属性设置为false来隐藏Excel文件中的选项卡。

下面是一个完整的示例，打开一个Excel文件（book1.xls），隐藏其标签并将修改后的文件保存为output.xls。代码执行后，您将看到工作簿的标签被隐藏了。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **控制选项卡栏宽度**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
