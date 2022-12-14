---
title: Grafiği viewBox özniteliğiyle SVG'ye aktar
type: docs
weight: 280
url: /tr/net/export-chart-to-svg-with-viewbox-attribute/
---
{{% alert color="primary" %}}

 Varsayılan olarak, grafik SVG biçiminde dışa aktarıldığında,**görünüm kutusu** öznitelik, XML'ine dahil değildir. Ancak, Aspose.Cells sağlar[**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) ayarlandığında hangi özellik**doğru** grafiği, viewBox özniteliğiyle SVG'ye dışa aktarır.

{{% /alert %}}

## Grafiği viewBox özniteliğiyle SVG'ye aktar

Aşağıdaki örnek kod, grafiği viewBox özniteliğiyle SVG biçimine aktarır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

 Grafiğin SVG'sini not defterinde açarsanız,**görünüm kutusu** buna benzer öznitelik.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
