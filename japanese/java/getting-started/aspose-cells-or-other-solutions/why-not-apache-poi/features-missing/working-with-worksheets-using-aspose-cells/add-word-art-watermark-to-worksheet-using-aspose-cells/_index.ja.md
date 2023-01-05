---
title: Aspose.Cells を使用して Word Art の透かしをワークシートに追加する
type: docs
weight: 10
url: /ja/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---
## **Aspose.Cells - Word アートの透かしをワークシートに追加**
ワードアートを使用して、スプレッドシートに特殊なテキスト効果を追加します。たとえば、タイトルをファイルの上部に広げたり、テキストを装飾したり、テキストをプリセットの形状に合わせたり、テキストを背景の透かしとして Excel シートに適用したりできます。ワードアートは、スプレッドシート内で移動または配置して装飾を追加できるオブジェクトになります。

**Java**

{{< highlight "java" >}}

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
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[ワードアートの透かしをワークシートに追加する](/cells/ja/java/add-wordart-watermark-to-worksheet).

{{% /alert %}}
