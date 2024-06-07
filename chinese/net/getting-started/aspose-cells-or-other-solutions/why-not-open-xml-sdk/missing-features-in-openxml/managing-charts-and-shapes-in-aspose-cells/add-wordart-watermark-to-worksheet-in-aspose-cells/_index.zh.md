---
title: 在Aspose.Cells中为工作表添加WordArt水印
type: docs
weight: 20
url: /zh/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---

{{% alert color="primary" %}}

使用WordArt添加特殊文本效果到电子表格中。例如，将标题跨越文件顶部，装饰文本，并将文本适配预设形状，或将文本应用为Excel表中的背景水印。WordArt变为一个对象，您可以在电子表格中移动或定位以添加装饰。

{{% /alert %}}

以下示例展示如何添加WordArt形状以设置背景水印。

运行代码后，输出文件包含淡红色的WordArt水印。

**输出文件** 

![todo:image_alt_text](picture1.png)

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Add WordArt Watermark to Worksheet.xlsx";

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Get the first default sheet

Worksheet sheet = workbook.Worksheets[0];

//Add Watermark

Aspose.Cells.Drawing.Shape wordart = sheet.Shapes.AddTextEffect(MsoPresetTextEffect.TextEffect1,

"CONFIDENTIAL", "Arial Black", 50, false, true

, 18, 8, 1, 1, 130, 800);

//Get the fill format of the word art

MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the color

wordArtFormat.ForeColor = System.Drawing.Color.Red;

//Set the transparency

wordArtFormat.Transparency = 0.9;

//Make the line invisible

MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the file

workbook.Save(FileName);

{{< /highlight >}}

## **下载示例代码**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **下载示例**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
