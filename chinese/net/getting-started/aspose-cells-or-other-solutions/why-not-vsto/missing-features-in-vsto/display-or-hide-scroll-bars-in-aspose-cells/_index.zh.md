---
title: 在 Aspose.Cells 中显示或隐藏滚动条
type: docs
weight: 70
url: /zh/net/display-or-hide-scroll-bars-in-aspose-cells/
---

{{% alert color="primary" %}}

滚动条非常适用于浏览任何文件的内容。通常有两种滚动条：

- 垂直滚动条
- 水平滚动条

Microsoft Excel还提供水平和垂直滚动条，以便用户可以滚动工作表内容。使用Aspose.Cells，开发人员可以控制Excel文件中两种类型滚动条的可见性。

{{% /alert %}}

Aspose.Cells 提供了一个代表 Excel 文件的 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类提供了许多属性和方法，用于管理 Excel 文件。要控制滚动条的可见性，请使用 [**WorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings) 类的 [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) 和 [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) 属性。 [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) 和 [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) 是布尔属性，表示这些属性只能存储 **true** 或 **false** 值。

下面是一个完整的代码示例，打开一个 Excel 文件，book1.xls，隐藏滚动条，然后将修改后的文件保存为 output.xls。

下面的屏幕截图显示了包含两个滚动条的Book1.xls文件。修改后的文件保存为output.xls文件，也显示在下面。

**Book1.xls: 在做出任何修改之前的Excel文件**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: 修改后的Excel文件**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Hiding the vertical scroll bar of the Excel file

workbook.Settings.IsVScrollBarVisible = false;

//Hiding the horizontal scroll bar of the Excel file

workbook.Settings.IsHScrollBarVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **下载运行代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **下载示例代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
