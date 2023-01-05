---
title: Grafiği xlsx4j'de Resme Dönüştür
type: docs
weight: 10
url: /tr/java/convert-chart-to-image-in-xlsx4j/
---
## **Aspose.Cells - Grafiği Resme Dönüştür**
Grafikler görsel olarak çekicidir ve kullanıcıların verilerdeki karşılaştırmaları, kalıpları ve eğilimleri görmesini kolaylaştırır.
Chart sınıfı toImage yöntemi, grafiği diske veya akışa kaydedilebilen bir görüntü dosyasına dönüştürür.

**Java**

{{< highlight "java" >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Grafiği Resme Dönüştürme](/java/converting-chart-to-image).

{{% /alert %}}
