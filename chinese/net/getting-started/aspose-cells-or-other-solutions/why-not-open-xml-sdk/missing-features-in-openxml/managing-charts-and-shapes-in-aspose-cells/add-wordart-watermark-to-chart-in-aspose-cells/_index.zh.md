---
title: 在 Aspose.Cells 中为图表添加艺术字水印
type: docs
weight: 10
url: /zh/net/add-wordart-watermark-to-chart-in-aspose-cells/
---
{{% alert color="primary" %}} 

您可以使用艺术字向电子表格添加特殊文本效果。例如，拉伸标题、装饰文本、使文本适合预设形状，或将受影响的文本作为水印应用到图表的绘图区域。艺术字成为一个对象，您可以在电子表格中移动或放置它以添加装饰。

{{% /alert %}} 

以下示例显示如何将艺术字形状添加为现有图表绘图区域的水印。该示例使用已包含图表的模板 Excel 文件。

**输入文件** 

![待办事项：图片_替代_文本](picture1.png)

**输出文件**

![待办事项：图片_替代_文本](picture2.png)

**C#**

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Add WordArt Watermark to Chart.xlsx";

//Open the existing excel file.

Workbook workbook = new Workbook(FileName);

//Get the chart in the first worksheet.

Aspose.Cells.Charts.Chart chart = workbook.Worksheets[0].Charts[0];

//Add a WordArt watermark (shape) to the chart's plot area.

Aspose.Cells.Drawing.Shape wordart = chart.Shapes.AddTextEffectInChart(MsoPresetTextEffect.TextEffect2,

"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

//Get the shape's fill format.

Aspose.Cells.Drawing.MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the transparency.

wordArtFormat.Transparency = 0.9;

//Get the line format and make it invisible.

Aspose.Cells.Drawing.MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the excel file.

workbook.Save(FileName);

{{< /highlight >}}

## **下载示例代码**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)

## **下载运行示例**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
