---
title: 在 Aspose.Cells 中的工作表之间复制形状
type: docs
weight: 30
url: /zh/net/copy-shapes-between-worksheets-in-aspose-cells/
---
{{% alert color="primary" %}} 

有时，您需要在工作表之间复制工作表上的元素，例如图片、图表和其他绘图对象。 Aspose.Cells 支持此功能。可以最高精度复制图表、图像和其他对象。

本文让您详细了解如何在工作表之间复制形状。为了说明，它在 Visual Studio.Net 中创建了一个控制台应用程序，使用 Aspose.Cells 在工作表之间复制图片、图表和其他绘图对象。

{{% /alert %}} 

下面是将图表从工作表复制到另一个的代码

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Copy Shapes between Worksheets.xlsx";

//Open the template file

Workbook workbook = new Workbook(FileName);

//Get the Chart from the "Chart" worksheet.

Aspose.Cells.Charts.Chart source = workbook.Worksheets["Chart"].Charts[0];

Aspose.Cells.Drawing.ChartShape cshape = source.ChartObject;

//Copy the Chart to the Result Worksheet

workbook.Worksheets["Result"].Shapes.AddCopy(cshape, 20, 0, 2, 0);

//Save the Worksheet

workbook.Save(FileName);



{{< /highlight >}}

**笔记：**有关复制多个形状的更多详细信息，您需要访问[这里](/cells/zh/net/copy-shapes-between-worksheets/)
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **下载运行示例**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
