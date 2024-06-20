---
title: Aspose.Cells Kullanarak Grafikleri Görüntüye Dönüştürme
type: docs
weight: 30
url: /tr/java/convert-chart-to-images-using-aspose-cells/
---

## **Aspose.Cells - Grafiği Görüntüye Dönüştürme**
Grafikler görsel açıdan çekicidir ve kullanıcıların verilerde karşılaştırmaları, desenleri ve trendleri görmelerini kolaylaştırır.
Chart sınıfının toImage metodu, grafiği bir resim dosyasına dönüştürerek, diske veya akıma kaydedilebilecek bir resme dönüştürür.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

{{% alert color="primary" %}} 

Daha fazla ayrıntı için [Grafiği Resme Dönüştürme](/java/converting-chart-to-image) sayfasını ziyaret edin.

{{% /alert %}}
