---
title: Show and Hide Worksheets and Tabs
type: docs
weight: 10
url: /python-net/show-and-hide-worksheets-and-tabs/
description: This article provides sample code for using the Aspose.Cells for Python via .NET API to programmatically display and hide an Excel worksheet. Additionally, how to show and hide Excel workbook tabs.
keywords: Python Excel Library, Python Show and Hide a Worksheet, Python Show and Hide Tabs, Python Control the Tab Bar Width.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET allows the user to show and hide elements of a workbook including worksheets and tabs.

{{% /alert %}}

## **Show and Hide a Worksheet**

An Excel file can have one or more than one worksheets. Whenever we create an Excel file, we add worksheets to the Excel file in which we work. Each worksheet in an Excel file is independent from the other worksheet by having its own data and formatting settings etc. Sometimes, developers may require to make few worksheets hidden and others visible in the Excel file for their own interest. So, **Aspose.Cells for Python via .NET** allows developers to control the visibility of the worksheets in their Excel files.

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a wide range of properties and methods to manage worksheets. To control a worksheet's visibility, use the [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) property of the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) is a Boolean property, which means that it can only store a **true** or **false** value.

### **Making a Worksheet Visible**

Make a worksheet visible by setting the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class' [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) property to **true**

### **Hiding a Worksheet**

Hide a worksheet by setting the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class' [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) property to **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideUnhideWorksheet-1.py" >}}

## **Show and Hide Tabs**

If you closely look at the bottom of a Microsoft Excel file, you will see a number of controls. These include:

- Sheet tabs.
- Tab scrolling buttons.

Sheet tabs represent the worksheets in the Excel file. Click any tab to switch to that worksheet. The more worksheets in the workbook, the more sheet tabs there are. If the Excel file has a good number of worksheets you need buttons to navigate through them. So, Microsoft Excel provides tab scrolling buttons for scrolling through the sheet tabs.

Using Aspose.Cells for Python via .NET, developers can control the visibility of sheet tabs and tabs scrolling buttons in Excel files.

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class provides a wide range of properties and methods to manage an Excel file. To control the visibility of tabs in an Excel file, developers can use the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class' [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) property. [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) is a Boolean property, which means that it can only store a **true** or **false** value.

### **Making Tabs Visible**

Make tabs visible with the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class' [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) property to **true**.

### **Hiding Tabs**

Hide tabs in an Excel file by setting the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class' [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) property to false.

Below is a complete example that opens an Excel file (book1.xls), hides its tabs and saves the modified file as output.xls. After the code execution, you will see that the tabs of the workbook are hidden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **Controlling the Tab Bar Width**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
