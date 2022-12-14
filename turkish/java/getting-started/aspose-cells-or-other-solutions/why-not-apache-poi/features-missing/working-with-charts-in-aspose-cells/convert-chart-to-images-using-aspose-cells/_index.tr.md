---
title: Aspose.Cells'i kullanarak Grafiği Görüntülere Dönüştür
type: docs
weight: 30
url: /tr/java/convert-chart-to-images-using-aspose-cells/
---
## **Aspose.Cells - Grafiği Görüntülere Dönüştür**
Grafikler görsel olarak çekicidir ve kullanıcıların verilerdeki karşılaştırmaları, kalıpları ve eğilimleri görmesini kolaylaştırır.
Chart sınıfı toImage yöntemi, grafiği diske veya akışa kaydedilebilen bir görüntü dosyasına dönüştürür.

**Java**

{{< highlight "java" >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Grafiği Resme Dönüştürme](/java/converting-chart-to-image).

{{% /alert %}}
