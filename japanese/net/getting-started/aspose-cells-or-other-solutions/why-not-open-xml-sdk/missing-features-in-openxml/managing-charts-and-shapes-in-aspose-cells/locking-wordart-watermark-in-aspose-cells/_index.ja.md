---
title: Aspose.Cells でワードアートの透かしをロックする
type: docs
weight: 40
url: /ja/net/locking-wordart-watermark-in-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells API を使用すると、ワードアートがワークシート上で移動および配置できるオブジェクトになる方法で、ワークシートにワードアートの透かしを追加できます。編集、移動、選択などの操作に対してワードアート オブジェクトをロックすることもできます。この記事では、透かしのいくつかの側面をロックするための Shape.SetLockedProperty メソッドの使用法について説明します。

{{% /alert %}} 

Aspose.Cells API を使用すると、透かしの特定の側面をロックして、ユーザーの操作を制限または完全にブロックできます。次のコード スニペットは、Aspose.Cells for .NET API を使用して、スプレッドシートを最初から作成することにより、透かしの選択、移動、編集、およびサイズ変更をロックする方法を示しています。

**C#**

{{< highlight "csharp" >}}

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
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **実行例をダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
