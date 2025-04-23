---
title: xlsx4j de Grafikleri Görüntüye Dönüştürme
type: docs
weight: 10
url: /tr/java/convert-chart-to-image-in-xlsx4j/
---

## **Aspose.Cells - Grafikleri Görüntüye Dönüştürme**
Grafikler görsel açıdan çekicidir ve kullanıcıların verilerde karşılaştırmaları, desenleri ve trendleri görmelerini kolaylaştırır.
Chart sınıfının toImage yöntemi, grafikleri bir resim dosyasına dönüştürür, bu dosya diskte veya akışta saklanabilir.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

Daha fazla ayrıntı için [Grafiği Resme Dönüştürme](/java/converting-chart-to-image) sayfasını ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
