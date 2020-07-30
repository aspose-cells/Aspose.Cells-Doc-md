---
title : "Show and Hide Worksheets and Tabs" 
description : "" 
weight : 16149 
toc : false
type: docs
url: /net/developerguide/worksheets/displayfeatures/show+and+hide+worksheets+and+tabs/
---

# Aspose.Cells for .NET : Show and Hide Worksheets and Tabs


Aspose.Cells allows the user to show and hide elements of a workbook including worksheets and tabs.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Show and Hide a Worksheet](#show-and-hide-a-worksheet)
    *   1.1 [Making a Worksheet Visible](#making-a-worksheet-visible)
    *   1.2 [Hiding a Worksheet](#hiding-a-worksheet)
*   2 [Show and Hide Tabs](#show-and-hide-tabs)
    *   2.1 [Making Tabs Visible](#making-tabs-visible)
    *   2.2 [Hiding Tabs](#hiding-tabs)
    *   2.3 [Controlling the Tab Bar Width](#controlling-the-tab-bar-width)
{{< /panel >}}
 

## Show and Hide a Worksheet

An Excel file can have one or more than one worksheets. Whenever we create an Excel file, we add worksheets to the Excel file in which we work. Each worksheet in an Excel file is independent from the other worksheet by having its own data and formatting settings etc. Sometimes, developers may require to make few worksheets hidden and others visible in the Excel file for their own interest. So, **Aspose.Cells** allows developers to control the visibility of the worksheets in their Excel files.

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook), that represents an Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a wide range of properties and methods to manage worksheets. To control a worksheet's visibility, use the [IsVisible](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/isvisible) property of the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. [IsVisible](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/isvisible) is a Boolean property, which means that it can only store a **true** or **false** value.

### Making a Worksheet Visible

Make a worksheet visible by setting the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class' [IsVisible](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/isvisible) property to **true**

### Hiding a Worksheet

Hide a worksheet by setting the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class' [IsVisible](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/isvisible) property to **false**.

## Show and Hide Tabs

If you closely look at the bottom of a Microsoft Excel file, you will see a number of controls. These include:

*   Sheet tabs.
*   Tab scrolling buttons.

Sheet tabs represent the worksheets in the Excel file. Click any tab to switch to that worksheet. The more worksheets in the workbook, the more sheet tabs there are. If the Excel file has a good number of worksheets you need buttons to navigate through them. So, Microsoft Excel provides tab scrolling buttons for scrolling through the sheet tabs.

Using Aspose.Cells, developers can control the visibility of sheet tabs and tabs scrolling buttons in Excel files.

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook), that represents an Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class provides a wide range of properties and methods to manage an Excel file. To control the visibility of tabs in an Excel file, developers can use the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class' [WorkbookSettings.ShowTabs](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/showtabs) property. [WorkbookSettings.ShowTabs ](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/showtabs)is a Boolean property, which means that it can only store a **true** or **false** value.

### Making Tabs Visible

Make tabs visible with the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class' [WorkbookSettings.ShowTabs](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/showtabs) property to **true**.

### Hiding Tabs

Hide tabs in an Excel file by setting the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class' [WorkbookSettings.ShowTabs](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/showtabs) property to false.

Below is a complete example that opens an Excel file (book1.xls), hides its tabs and saves the modified file as output.xls. After the code execution, you will see that the tabs of the workbook are hidden.

### Controlling the Tab Bar Width

