---
title: Grafiği viewBox özniteliğiyle SVG'e aktarın
type: docs
weight: 280
url: /tr/net/export-chart-to-svg-with-viewbox-attribute/
---
{{% alert color="primary" %}}

 Varsayılan olarak, grafik SVG biçiminde dışa aktarıldığında,**görünüm kutusu** öznitelik, XML'ine dahil değildir. Ancak, Aspose.Cells sağlar[**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) ayarlandığında hangi özellik**doğru** grafiği, viewBox özniteliğiyle SVG'e aktarır.

{{% /alert %}}

## Grafiği viewBox özniteliğiyle SVG'e aktarın

Aşağıdaki örnek kod, grafiği viewBox özniteliğiyle SVG biçiminde dışa aktarır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

 Grafiğin SVG'ini not defterinde açarsanız,**görünüm kutusu**buna benzer öznitelik.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
