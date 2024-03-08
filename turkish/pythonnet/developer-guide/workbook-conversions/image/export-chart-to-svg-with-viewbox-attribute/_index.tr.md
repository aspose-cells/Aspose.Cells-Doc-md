---
title: ViewBox özelliğiyle Grafiği SVG'e aktar
type: docs
weight: 280
url: /tr/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Aspose.Cells for Python via .NET API'i kullanarak Grafiği viewBox özniteliğiyle SVG'e aktarın.
keywords: Python Export Chart to SVG with viewBox attribute, Export Chart to SVG with viewBox attribute in Python via NET, Python Convert Chart to SVG with viewBox attribute.
---
{{% alert color="primary" %}}

 Varsayılan olarak, grafik SVG biçimine aktarıldığında,**görünüm kutusu** öznitelik XML'ine dahil edilmez. Ancak Aspose.Cells for Python via .NET şunu sağlar:[**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) ayarlandığında hangi özellik**doğru** grafiği viewBox özelliğiyle SVG'e aktarır.

{{% /alert %}}

##  ViewBox özelliğiyle Grafiği SVG'e aktar

Aşağıdaki örnek kod, grafiği viewBox özniteliğiyle SVG biçimine aktarır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

 Grafiğin SVG numarasını not defterinde açarsanız,**görünüm kutusu** buna benzer bir özellik.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
