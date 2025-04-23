---
title: 在 Aspose.Cells 中显示或隐藏选项卡
type: docs
weight: 80
url: /zh/net/display-or-hide-tabs-in-aspose-cells/
---

{{% alert color="primary" %}} 

如果您仔细查看Microsoft Excel文件的底部，您会看到许多控件。其中包括:

- 工作表标签。
- 选项卡滚动按钮。

工作表标签代表Excel文件中的工作表。单击任何选项卡以切换到该工作表。工作簿中有更多的工作表，也会有更多的工作表标签。如果Excel文件有大量工作表，您需要按钮来进行导航。因此，Microsoft Excel提供了选项卡滚动按钮来滚动工作表标签。

**工作表标签和选项卡滚动按钮** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_1.png)

使用Aspose.Cells，开发人员可以控制Excel文件中工作表标签和选项卡滚动按钮的可见性。 

{{% /alert %}} 

下面是一个完整的示例，打开了一个Excel文件（book1.xls），隐藏其选项卡，并将修改后的文件保存为output.xls。

您可以在下图中看到Book1.xls文件包含选项卡。在执行示例代码后，选项卡被隐藏了，可以从下图中输出的output.xls文件的屏幕截图中看到。

**book1.xls：不进行任何修改的Excel文件** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: 修改后的Excel文件** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **控制选项卡栏宽度**
**C#**

{{< highlight csharp >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
