---
title: Aspose.Cellsを使用してワードアートのウォーターマークをワークシートに追加する
type: docs
weight: 10
url: /ja/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---

## **Aspose.Cells - ワードアートのウォーターマークをワークシートに追加する**
WordArtを使用してスプレッドシートに特殊なテキスト効果を追加します。たとえば、ファイルの上部にタイトルを伸ばしたり、テキストを飾ったり、テキストを事前設定された形状に合わせたり、Excelシートに背景ウォーターマークとしてテキストを適用したりします。WordArtは移動や位置づけができるオブジェクトとなり、装飾を追加できます。

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook();

//Get the first default sheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Add Watermark

Shape wordart = sheet.getShapes().addTextEffect(MsoPresetTextEffect.TEXT_EFFECT_1,

"CONFIDENTIAL", "Arial Black", 50, false, true

, 18, 8, 1, 1, 130, 800);

//Get the shape's fill format

FillFormat wordArtFormat = wordart.getFill();

//Set the transparency

wordArtFormat.setTransparency(0.9);

//Make the line invisible

wordart.setHasLine(false);

//Save the file

workbook.save(dataDir + "AsposeWatermark_Out.xls");

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

詳細については、[ワードアートのウォーターマークをワークシートに追加する](/cells/ja/java/add-wordart-watermark-to-worksheet)を参照してください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
