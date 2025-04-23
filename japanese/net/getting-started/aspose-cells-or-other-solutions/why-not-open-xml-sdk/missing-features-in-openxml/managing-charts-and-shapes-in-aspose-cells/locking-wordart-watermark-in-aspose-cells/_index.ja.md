---
title: Aspose.Cells で WordArt ウォーターマークをロックする
type: docs
weight: 40
url: /ja/net/locking-wordart-watermark-in-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells API は、ワークシート上に WordArt ウォーターマークを追加することを可能にし、WordArt をワークシート上で移動および配置可能なオブジェクトにします。また、編集、移動、選択などの WordArt オブジェクトをロックすることも可能です。この記事では、Shape.SetLockedProperty メソッドの使用方法を説明します。

{{% /alert %}} 

Aspose.Cells API では、ユーザーの操作を制限したり完全にブロックしたりするために、ウォーターマークの特定の側面をロックすることができます。次のコードスニペットは、Aspose.Cells for .NET API の使用方法を示しており、スプレッドシートをゼロから作成してウォーターマークの選択、移動、編集、サイズ変更をロックしています。

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
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **実行例のダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
