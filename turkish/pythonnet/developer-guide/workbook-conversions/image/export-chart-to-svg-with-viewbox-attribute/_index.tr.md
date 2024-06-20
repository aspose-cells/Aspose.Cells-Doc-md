---
title: viewBox özniteliği ile SVG ye Grafik Dışa Aktarma
type: docs
weight: 280
url: /tr/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Aspose.Cells for Python via .NET API sını kullanarak viewBox özelliği ile SVG ye Grafik Dışa Aktarma.
keywords: Python da viewBox özniteliği ile Grafikleri SVG ye dışa aktarma, Python da viewBox özniteliği ile Grafikleri SVG ye dışa aktarma via NET, Python da Grafikleri SVG ye dönüştürme işlemi ve viewBox özniteliği.
---

{{% alert color="primary" %}}

Varsayılan olarak, grafiği SVG biçimine dışa aktardığınızda, XML'deki **viewBox** özelliği içermemektedir. Ancak, Aspose.Cells for Python via .NET, **True** olarak ayarlandığında grafiği viewBox özelliğiyle SVG biçimine dışa aktarır.

{{% /alert %}}

## viewBox Özniteliği ile SVG'ye Grafik Dışa Aktarma

Aşağıdaki örnek kod, grafiği viewBox özniteliği ile SVG biçiminde dışa aktarır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

Grafiğin SVG'sini not defterinde açarsanız, benzer bir **viewBox** özniteliği bulacaksınız.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
