---
title: xlsx4j でチャートを画像に変換する
type: docs
weight: 10
url: /ja/java/convert-chart-to-image-in-xlsx4j/
---

## **Aspose.Cells - チャートを画像に変換する**
グラフは視覚的に魅力があり、ユーザーがデータの比較、パターン、傾向を見るのが簡単です。
Chart クラスの toImage メソッドは、チャートを画像ファイルに変換し、ディスクやストリームに保存できます。

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

詳細については、[チャートを画像に変換する](/java/converting-chart-to-image) をご覧ください。

{{% /alert %}}
