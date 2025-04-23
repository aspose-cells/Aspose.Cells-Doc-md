---
title: 在 Aspose.Cells 中在工作表之间复制形状
type: docs
weight: 30
url: /zh/net/copy-shapes-between-worksheets-in-aspose-cells/
---

{{% alert color="primary" %}} 

有时候，您需要在工作表之间复制元素，比如图片、图表和其他绘图对象。Aspose.Cells 支持该功能。图表、图片和其他对象可以以最高精度进行复制。

本文详细介绍了如何在工作表之间复制形状。举例说明，在 Visual Studio.Net 中创建一个控制台应用程序，并使用 Aspose.Cells 复制图片、图表和其他绘图对象在工作表之间。

{{% /alert %}} 

以下是从一个工作表复制图表到另一个工作表的代码

**C#**

{{< highlight csharp >}}

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

**注意：**如果要了解更多关于复制多个形状的细节，需访问[此处](/cells/zh/net/copy-shapes-between-worksheets/)
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **下载运行示例**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
