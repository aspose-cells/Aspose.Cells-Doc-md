---
title: viewBox özniteliği ile SVG ye Grafik Dışa Aktarma
type: docs
weight: 280
url: /tr/net/export-chart-to-svg-with-viewbox-attribute/
---

{{% alert color="primary" %}}

Varsayılan olarak, grafik SVG biçimine dışa aktarıldığında, **viewBox** özniteliği içinde yer almaz. Ancak, Aspose.Cells, **true** olarak ayarlandığında grafiği viewBox özniteliği ile SVG'ye dışa aktarır.

{{% /alert %}}

## viewBox Özniteliği ile SVG'ye Grafik Dışa Aktarma

Aşağıdaki örnek kod, grafiği viewBox özniteliği ile SVG biçiminde dışa aktarır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

Grafiğin SVG'sini not defterinde açarsanız, benzer bir **viewBox** özniteliği bulacaksınız.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
