---
title: Aspose.Cells 工作表添加艺术字水印
type: docs
weight: 20
url: /zh/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---
{{% alert color="primary" %}}

使用艺术字为电子表格添加特殊文本效果。例如，在文件顶部拉伸标题、修饰文本并使文本适合预设形状，或将文本作为背景水印应用于 Excel 工作表。艺术字成为一个对象，您可以在电子表格中移动或定位以添加装饰。

{{% /alert %}}

下面的示例演示如何添加艺术字形状来为工作表设置背景水印。

运行代码后，输出文件包含淡红色艺术字水印。

**输出文件** 

![待办事项：图像_替代_文本](picture1.png)

**C#**

{{< highlight "csharp" >}}

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
