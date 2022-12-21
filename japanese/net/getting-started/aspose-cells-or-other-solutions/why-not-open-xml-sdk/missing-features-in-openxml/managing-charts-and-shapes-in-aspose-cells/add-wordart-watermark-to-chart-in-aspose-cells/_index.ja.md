---
title: Aspose.Cells のグラフにワードアートの透かしを追加する
type: docs
weight: 10
url: /ja/net/add-wordart-watermark-to-chart-in-aspose-cells/
---
{{% alert color="primary" %}} 

ワードアートを使用して、スプレッドシートに特殊なテキスト効果を追加できます。たとえば、タイトルを拡大したり、テキストを装飾したり、テキストをプリセットの形状に合わせたり、影響を受けるテキストを透かしとしてグラフのプロット エリアに適用したりします。ワードアートは、スプレッドシート内で移動または配置して装飾を追加できるオブジェクトになります。

{{% /alert %}} 

次の例は、既存のグラフのプロット エリアの透かしとしてワードアート図形を追加する方法を示しています。この例では、グラフが既に含まれているテンプレート Excel ファイルを使用します。

**入力ファイル** 

![todo:画像_代替_文章](picture1.png)

**出力ファイル**

![todo:画像_代替_文章](picture2.png)

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

## **サンプルコードをダウンロード**

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)

## **実行例をダウンロード**

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
