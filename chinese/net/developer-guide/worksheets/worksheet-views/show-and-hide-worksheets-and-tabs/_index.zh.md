---
title: 显示和隐藏工作表和标签
type: docs
weight: 10
url: /zh/net/show-and-hide-worksheets-and-tabs/
description: 本文提供使用 C# API 或 .NET 库的示例代码，以通过编程方式显示和隐藏 Excel 工作表。此外，如何显示和隐藏 Excel 工作簿标签。
---

{{% alert color="primary" %}}

Aspose.Cells 允许用户显示和隐藏工作簿中的元素，包括工作表和标签。

{{% /alert %}}

## **显示和隐藏工作表**

Excel 文件可以有一个或多个工作表。每当创建一个 Excel 文件时，我们向其中添加工作表。Excel 文件中的每个工作表通过具有自己的数据和格式设置等独立于其他工作表来。有时，开发人员可能需要将某些工作表隐藏，而将其他工作表对于他们自己的兴趣设为可见。因此，**Aspose.Cells** 允许开发人员控制其 Excel 文件中工作表的可见性。

Aspose.Cells 提供了一个代表 Excel 文件的类 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个集合 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)，允许访问 Excel 文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供了广泛的属性和方法来管理工作表。要控制工作表的可见性，请使用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) 属性。[**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) 是布尔属性，这意味着它只能存储一个 **true** 或 **false** 值。

### **使工作表可见**

通过将 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) 属性设置为 **true** 来使工作表可见。

### **隐藏工作表**

通过将 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) 属性设置为 **false** 来隐藏工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **显示和隐藏标签**

如果仔细查看 Microsoft Excel 文件底部，您会看到许多控件。这包括:

- 工作表选项卡。
- 选项卡滚动按钮。

工作表选项卡代表Excel文件中的工作表。单击任何选项卡切换到该工作表。工作簿中有更多工作表时，就会有更多的工作表选项卡。如果Excel文件有大量工作表，需要按钮来在它们之间进行导航。因此，Microsoft Excel提供了选项卡滚动按钮，用于滚动工作表选项卡。

使用Aspose.Cells，开发人员可以控制Excel文件中的工作表选项卡的可见性和选项卡滚动按钮。

Aspose.Cells提供了一个类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，表示一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类提供了广泛的属性和方法来管理Excel文件。要控制Excel文件中选项卡的可见性，开发人员可以使用[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)属性。[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)是一个布尔属性，只能存储**true**或**false**值。

### **使选项卡可见。**

使用[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)属性将选项卡设置为**true**以显示。

### **隐藏选项卡。**

通过将[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)属性设置为false来隐藏Excel文件中的选项卡。

以下是一个完整的示例，打开一个Excel文件（book1.xls），隐藏其选项卡，并将修改后的文件保存为output.xls。代码执行后，您会看到工作簿的选项卡已隐藏。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **控制选项卡栏宽度。**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
