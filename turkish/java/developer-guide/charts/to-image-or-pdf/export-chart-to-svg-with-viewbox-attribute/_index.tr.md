---
title: viewBox özniteliği ile SVG ye Grafik Dışa Aktarma
type: docs
weight: 190
url: /tr/java/export-chart-to-svg-with-viewbox-attribute/
---

Varsayılan olarak, bir grafik SVG biçimine dönüştürüldüğünde XML'sinde **viewBox** özelliği bulunmaz. Bununla birlikte, Aspose.Cells, [**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) özelliğini sağlar, bu özellik **true** olarak ayarlandığında grafik SVG'yi **viewBox** özelliğiyle birlikte ihraç eder.

Grafiğin SVG'sini not defterinde açarsanız, benzer bir **viewBox** özniteliği bulacaksınız.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## Kod Örneği

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## İlgili Makaleler

- [Grafik Rendeleme](/cells/tr/java/chart-rendering/)
- [Belirtilen Genişlik ve Yükseklikte Çalışsayısı veya Tabloyu Resme Dışa Aktarma](/cells/tr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
{{< app/cells/assistant language="java" >}}
