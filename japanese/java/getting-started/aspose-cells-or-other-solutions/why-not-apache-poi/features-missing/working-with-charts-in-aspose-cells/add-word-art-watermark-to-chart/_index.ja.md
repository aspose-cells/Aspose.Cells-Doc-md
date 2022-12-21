---
title: ワード アートの透かしをグラフに追加する
type: docs
weight: 10
url: /ja/java/add-word-art-watermark-to-chart/
---
## **Aspose.Cells - Word アートの透かしをチャートに追加**
ワードアートを使用して、スプレッドシートに特殊なテキスト効果を追加できます。たとえば、タイトルを拡大したり、テキストを装飾したり、テキストをプリセットの形状に合わせたり、影響を受けるテキストを透かしとしてグラフのプロット エリアに適用したりします。ワードアートは、スプレッドシート内で移動または配置して装飾を追加できるオブジェクトになります。

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook.

//Open the existing excel file.

Workbook workbook = new Workbook(dataDir + "AsposeChart.xls");

//Get the chart in the first worksheet.

com.aspose.cells.Chart chart = workbook.getWorksheets().get(0).getCharts().get(0);

//Add a WordArt watermark (shape) to the chart's plot area.

com.aspose.cells.Shape wordart = chart.getShapes().addTextEffectInChart(MsoPresetTextEffect.TEXT_EFFECT_2,

"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

//Get the shape's fill format.

FillFormat wordArtFormat = wordart.getFill();

//Set the transparency.

wordArtFormat.setTransparency(0.9);

//Make the line invisible.

wordart.setHasLine(false);

//Save the excel file.

workbook.save(dataDir + "AsposeChartWatermarked_Out.xls", SaveFormat.EXCEL_97_TO_2003);

{{< /highlight >}}
## **実行中のコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[ワードアートの透かしをグラフに追加する](/cells/ja/java/add-wordart-watermark-to-chart).

{{% /alert %}}
