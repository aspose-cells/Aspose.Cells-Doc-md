---
title: 在 Aspose.Cells 中显示或隐藏选项卡
type: docs
weight: 80
url: /zh/net/display-or-hide-tabs-in-aspose-cells/
---
{{% alert color="primary" %}} 

如果仔细查看 Microsoft Excel 文件的底部，您会看到许多控件。这些包括：

- 工作表标签。
- 选项卡滚动按钮。

工作表选项卡代表 Excel 文件中的工作表。单击任何选项卡以切换到该工作表。工作簿中的工作表越多，工作表标签就越多。如果 Excel 文件有大量工作表，您需要按钮来浏览它们。因此，Microsoft Excel 提供了用于滚动工作表选项卡的选项卡滚动按钮。

**工作表标签和标签滚动按钮** 

![待办事项：图像_替代_文本](display-or-hide-tabs-in-aspose-cells_1.png)

使用 Aspose.Cells，开发人员可以控制 Excel 文件中工作表选项卡和选项卡滚动按钮的可见性。

{{% /alert %}} 

下面是打开 Excel 文件 (book1.xls)、隐藏其选项卡并将修改后的文件保存为 output.xls 的完整示例。

您可以看到 Book1.xls 文件包含下图中的选项卡。示例代码执行后，选项卡被隐藏，您可以从下面的 output.xls 文件的屏幕截图中看到。

**book1.xls：修改前的Excel文件** 

![待办事项：图像_替代_文本](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls：修改后的Excel文件** 

![待办事项：图像_替代_文本](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **控制标签栏宽度**
**C#**

{{< highlight "csharp" >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
