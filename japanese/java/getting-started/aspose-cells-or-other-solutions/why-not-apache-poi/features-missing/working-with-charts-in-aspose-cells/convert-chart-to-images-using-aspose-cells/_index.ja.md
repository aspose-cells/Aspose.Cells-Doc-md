---
title: Aspose.Cellsを使用してグラフを画像に変換する
type: docs
weight: 30
url: /ja/java/convert-chart-to-images-using-aspose-cells/
---

## **Aspose.Cells - グラフを画像に変換**
グラフは視覚的に魅力があり、ユーザーがデータの比較、パターン、傾向を見るのが簡単です。
Chart クラスの toImage メソッドは、チャートを画像ファイルに変換し、ディスクまたはストリームに保存できます。

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);

{{< /highlight >}}
## **ランニングコードのダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

{{% alert color="primary" %}} 

詳細については、[チャートを画像に変換する](/java/converting-chart-to-image) をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
