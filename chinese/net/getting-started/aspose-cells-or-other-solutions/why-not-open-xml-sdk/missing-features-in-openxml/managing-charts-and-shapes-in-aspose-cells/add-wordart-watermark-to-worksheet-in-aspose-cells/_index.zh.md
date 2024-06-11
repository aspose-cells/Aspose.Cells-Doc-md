---
title: 在Aspose.Cells中为工作表添加WordArt水印
type: docs
weight: 20
url: /zh/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---

{{% alert color="primary" %}}

使用WordArt为电子表格添加特殊文本效果，例如，将标题横跨文件顶部，装饰文本，并使文本适应预设形状，或将文本应用于Excel工作表作为背景水印。 WordArt成为您可以在电子表格中移动或定位以添加装饰的对象。

{{% /alert %}}

以下示例显示如何添加文字艺术形状以设置工作表的背景水印。

运行代码后，输出文件包含淡红色的文字艺术水印。

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

## **下载运行示例**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
