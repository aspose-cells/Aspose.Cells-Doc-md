---
title: Aspose.Cells のワークシートにワードアートの透かしを追加する
type: docs
weight: 20
url: /ja/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---
{{% alert color="primary" %}}

ワードアートを使用して、スプレッドシートに特殊なテキスト効果を追加します。たとえば、タイトルをファイルの上部に引き延ばしたり、テキストを装飾したり、テキストをプリセットの形状に合わせたり、テキストを背景の透かしとして Excel シートに適用したりできます。ワードアートは、スプレッドシート内で移動または配置して装飾を追加できるオブジェクトになります。

{{% /alert %}}

次の例は、ワードアート図形を追加して、ワークシートの背景の透かしを設定する方法を示しています。

コードを実行すると、出力ファイルに淡い赤色のワードアートの透かしが含まれます。

**出力ファイル** 

![todo:画像_代替_文章](picture1.png)

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

## **サンプルコードをダウンロード**

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **実行例をダウンロード**

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
