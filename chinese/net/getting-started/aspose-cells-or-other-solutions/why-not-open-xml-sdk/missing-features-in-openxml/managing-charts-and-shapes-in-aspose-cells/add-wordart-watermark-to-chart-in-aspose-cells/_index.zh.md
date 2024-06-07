---
title: 在Aspose.Cells中为图表添加WordArt水印
type: docs
weight: 10
url: /zh/net/add-wordart-watermark-to-chart-in-aspose-cells/
---

{{% alert color="primary" %}} 

您可以使用文字艺术将特殊文本效果添加到电子表格中。例如，拉伸标题，装饰文本，使文本适合预设形状，或者将受影响的文本应用于图表的绘图区域作为水印。文字艺术变成一个对象，您可以将其移动或定位在电子表格中以添加装饰。

{{% /alert %}} 

以下示例显示了如何将WordArt形状作为现有图表的绘图区域水印。示例使用已包含图表的模板Excel文件。

**输入文件** 

![todo:image_alt_text](picture1.png)

**输出文件**

![todo:image_alt_text](picture2.png)

**C#**

{{< highlight csharp >}}

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

## **下载示例**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
