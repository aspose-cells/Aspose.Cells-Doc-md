---
title: 在Aspose.Cells中显示或隐藏标签页
type: docs
weight: 80
url: /zh/net/display-or-hide-tabs-in-aspose-cells/
---

{{% alert color="primary" %}} 

如果仔细查看 Microsoft Excel 文件底部，您会看到许多控件。这包括:

- 工作表选项卡。
- 选项卡滚动按钮。

工作表选项卡代表Excel文件中的工作表。单击任何选项卡切换到该工作表。工作簿中有更多工作表时，就会有更多的工作表选项卡。如果Excel文件有大量工作表，需要按钮来在它们之间进行导航。因此，Microsoft Excel提供了选项卡滚动按钮，用于滚动工作表选项卡。

**工作表标签和标签滚动按钮** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_1.png)

使用Aspose.Cells，开发人员可以控制Excel文件中的工作表选项卡的可见性和选项卡滚动按钮。 

{{% /alert %}} 

以下是一个完整的示例，打开一个Excel文件（book1.xls），隐藏其标签页并将修改后的文件保存为output.xls。

您可以从下面的截图中看到Book1.xls文件包含标签页。示例代码执行后，标签页被隐藏了，您可以从下面的output.xls文件的截图中看到。

**book1.xls：任何修改之前的Excel文件** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls：修改后的Excel文件** 

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
## **控制选项卡栏宽度。**
**C#**

{{< highlight csharp >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
