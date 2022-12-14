---
title: Grafiği viewBox özniteliğiyle SVG'ye aktar
type: docs
weight: 190
url: /tr/java/export-chart-to-svg-with-viewbox-attribute/
---
 Varsayılan olarak, grafik SVG formatına dışa aktarıldığında,**görünüm kutusu** öznitelik, XML'ine dahil değildir. Ancak, Aspose.Cells sağlar[**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) ayarlandığında hangi özellik**doğru** grafiği, viewBox özniteliğiyle SVG'ye dışa aktarır.

 Grafiğin SVG'sini not defterinde açarsanız,**görünüm kutusu** buna benzer öznitelik.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## Kod Parçacığı

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## İlgili Makaleler

- [Grafik Oluşturma](/cells/tr/java/chart-rendering/)
- [Çalışma Sayfasını veya Grafiği İstenilen Genişlik ve Yükseklikte Görüntüye Aktarın](/cells/tr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
