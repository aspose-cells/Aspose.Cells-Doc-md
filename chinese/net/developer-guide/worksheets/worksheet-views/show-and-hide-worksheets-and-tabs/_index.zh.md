---
title: 显示和隐藏工作表和选项卡
type: docs
weight: 10
url: /zh/net/show-and-hide-worksheets-and-tabs/
description: 本文提供了使用 C# API 或 .NET 库以编程方式显示和隐藏 Excel 工作表的示例代码。此外，如何显示和隐藏 Excel 工作簿选项卡。
---
{{% alert color="primary" %}}

Aspose.Cells 允许用户显示和隐藏工作簿的元素，包括工作表和选项卡。

{{% /alert %}}

## **显示和隐藏工作表**

一个 Excel 文件可以有一个或多个工作表。每当我们创建 Excel 文件时，我们都会将工作表添加到我们工作的 Excel 文件中。 Excel 文件中的每个工作表都独立于其他工作表，具有自己的数据和格式设置等。有时，开发人员可能出于自己的兴趣需要隐藏一些工作表，而其他工作表在 Excel 文件中可见。所以，**Aspose.Cells**允许开发人员控制工作表在其 Excel 文件中的可见性。

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , 表示一个 Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要控制工作表的可见性，请使用[**可见**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible)的财产[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。[**可见**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible)是一个布尔属性，这意味着它只能存储一个**真的**要么**错误的**价值。

### **使工作表可见**

通过设置使工作表可见[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级'[**可见**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible)财产给**真的**

### **隐藏工作表**

通过设置隐藏工作表[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级'[**可见**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible)财产给**错误的**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **显示和隐藏标签**

如果仔细查看 Microsoft Excel 文件的底部，您会看到许多控件。这些包括：

- 工作表标签。
- 选项卡滚动按钮。

工作表选项卡代表 Excel 文件中的工作表。单击任何选项卡以切换到该工作表。工作簿中的工作表越多，工作表标签就越多。如果 Excel 文件有大量工作表，您需要按钮来浏览它们。因此，Microsoft Excel 提供了用于滚动工作表选项卡的选项卡滚动按钮。

使用 Aspose.Cells，开发人员可以控制 Excel 文件中工作表选项卡和选项卡滚动按钮的可见性。

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , 表示一个 Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类提供了广泛的属性和方法来管理 Excel 文件。要控制 Excel 文件中选项卡的可见性，开发人员可以使用[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)财产。[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)是一个布尔属性，这意味着它只能存储一个**真的**要么**错误的**价值。

### **使选项卡可见**

使选项卡可见[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)财产给**真的**.

### **隐藏标签**

通过设置隐藏 Excel 文件中的选项卡[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)属性为假。

下面是打开 Excel 文件 (book1.xls)、隐藏其选项卡并将修改后的文件保存为 output.xls 的完整示例。代码执行后，您会看到工作簿的选项卡被隐藏了。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **控制标签栏宽度**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
