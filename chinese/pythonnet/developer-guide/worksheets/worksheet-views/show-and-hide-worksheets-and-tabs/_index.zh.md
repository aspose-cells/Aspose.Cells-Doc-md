---
title: 显示和隐藏工作表和选项卡
type: docs
weight: 10
url: /zh/python-net/show-and-hide-worksheets-and-tabs/
description: 本文提供了使用 Aspose.Cells for Python via .NET API 编程显示和隐藏 Excel 工作表的示例代码。此外，还介绍了如何显示和隐藏 Excel 工作簿标签。
keywords: Python Excel库，Python显示和隐藏工作表，Python显示和隐藏标签，Python控制标签栏宽度。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 允许用户显示和隐藏工作簿元素，包括工作表和标签。

{{% /alert %}}

## **显示和隐藏工作表**

一个Excel文件可以有一个或多个工作表。每次创建Excel文件时，我们会添加工作表到文件中。每个工作表彼此独立，拥有自己的数据和格式设置。有时开发者可能需要将部分工作表隐藏，其他的保持可见，以满足需求。所以，**Aspose.Cells for Python via .NET** 允许开发者控制工作表在Excel文件中的显示状态。

Aspose.Cells for Python via .NET 提供一个类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，代表一个 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) 集合，可以访问 Excel 文件中的每个工作表。

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

在使用 Aspose.Cells for Python via .NET 时，开发者可以控制Excel文件中工作表标签和标签滚动按钮的显示。

Aspose.Cells for Python via .NET 提供了一个类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，代表一个 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类提供了丰富的属性和方法用于管理Excel文件。要控制工作表标签的显示，开发者可以使用 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类的 [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) 属性。[**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) 是一个布尔属性，只能存储 **true** 或 ** false** 的值。

### **使选项卡可见**

使用[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类的[**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)属性将标签设置为**true**来使标签可见。

### **隐藏选项卡**

通过将[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类的[**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)属性设置为false来隐藏Excel文件中的选项卡。

下面是一个完整的示例，打开一个Excel文件（book1.xls），隐藏其标签并将修改后的文件保存为output.xls。代码执行后，您将看到工作簿的标签被隐藏了。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **控制选项卡栏宽度**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
