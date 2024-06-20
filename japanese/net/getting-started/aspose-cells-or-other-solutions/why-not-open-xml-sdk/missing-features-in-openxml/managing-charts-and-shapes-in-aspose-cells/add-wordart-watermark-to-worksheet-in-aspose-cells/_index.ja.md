---
title: Aspose.Cellsでワードアートウォーターマークをワークシートに追加する
type: docs
weight: 20
url: /ja/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---

{{% alert color="primary" %}}

WordArtを使用してスプレッドシートに特殊なテキスト効果を追加できます。たとえば、タイトルをファイルの上に広げたり、テキストを装飾したり、テキストをプリセットの形状に合わせたり、Excelシートにテキストを背景ウォーターマークとして適用したりできます。WordArtは、スプレッドシートに追加するための移動や配置が可能なオブジェクトになります。

{{% /alert %}}

次の例では、ワークシートの背景ウォーターマークとしてワードアート形状を追加する方法を示します。

コードを実行すると、出力ファイルには薄い赤色の WordArt ウォーターマークが含まれています。

**出力ファイル** 

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

## **サンプルコードをダウンロード**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **実行例のダウンロード**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
