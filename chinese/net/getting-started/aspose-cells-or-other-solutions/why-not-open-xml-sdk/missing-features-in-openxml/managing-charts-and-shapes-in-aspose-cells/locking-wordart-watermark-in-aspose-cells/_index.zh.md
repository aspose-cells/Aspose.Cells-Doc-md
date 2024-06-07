---
title: 在Aspose.Cells中锁定WordArt水印
type: docs
weight: 40
url: /zh/net/locking-wordart-watermark-in-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells API允许在工作表上添加WordArt水印，使WordArt成为可以移动和定位在工作表上的对象。还可以锁定WordArt对象，以限制任何交互，例如编辑、移动和选择。本文解释了使用Shape.SetLockedProperty方法锁定水印的一些方面。

{{% /alert %}} 

Aspose.Cells API允许锁定水印的某些方面，以便限制或完全阻止用户交互。下面的代码片段演示了使用Aspose.Cells for .NET API锁定水印的选择、移动、编辑和调整大小，从而创建一个新电子表格。

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Locking WordArt Watermark.xlsx";

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Get the first default sheet

Worksheet sheet = workbook.Worksheets[0];

//Add Watermark

Aspose.Cells.Drawing.Shape wordart = sheet.Shapes.AddTextEffect(MsoPresetTextEffect.TextEffect1,

"CONFIDENTIAL", "Arial Black", 50, false, true

, 18, 8, 1, 1, 130, 800);

//Lock Shape Aspects

wordart.IsLocked = true;

wordart.SetLockedProperty(ShapeLockType.Selection, true);

wordart.SetLockedProperty(ShapeLockType.ShapeType, true);

wordart.SetLockedProperty(ShapeLockType.Move, true);

wordart.SetLockedProperty(ShapeLockType.Resize, true);

wordart.SetLockedProperty(ShapeLockType.Text, true);

//Get the fill format of the word art

MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the color

wordArtFormat.ForeColor = Color.Red;

//Set the transparency

wordArtFormat.Transparency = 0.9;

//Make the line invisible

MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the file

workbook.Save(FileName);

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **下载示例**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
