---
title: 在Aspose.Cells中显示或隐藏滚动条
type: docs
weight: 70
url: /zh/net/display-or-hide-scroll-bars-in-aspose-cells/
---

{{% alert color="primary" %}}

滚动条非常适用于导航任何文件的内容。通常有两种滚动条：

- 垂直滚动条
- 水平滚动条

Microsoft Excel 还提供水平和垂直滚动条，以便用户可以滚动工作表内容。使用 Aspose.Cells，开发人员可以控制 Excel 文件中两种类型滚动条的可见性。

{{% /alert %}}

Aspose.Cells提供了一个代表Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类提供了一系列属性和方法用于管理Excel文件。要控制滚动条的可见性，请使用[**WorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings)类的[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)和[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)属性。[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)和[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)是布尔属性，这意味着这些属性只能存储**true**或**false**值。

以下是一个完整的代码，打开一个Excel文件book1.xls，隐藏两个滚动条，然后将修改后的文件保存为output.xls。

下面的截图显示了Book1.xls文件包含两个滚动条。修改后的文件保存为output.xls文件，如下所示。

**Book1.xls：任何修改前的Excel文件**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls：修改后的Excel文件**

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
