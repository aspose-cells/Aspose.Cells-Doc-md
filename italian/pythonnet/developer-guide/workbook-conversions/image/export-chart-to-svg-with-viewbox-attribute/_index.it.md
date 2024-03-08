---
title: Esporta grafico a SVG con attributo viewBox
type: docs
weight: 280
url: /it/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Esporta il grafico in SVG con l'attributo viewBox utilizzando Aspose.Cells for Python via .NET API.
keywords: Python Export Chart to SVG with viewBox attribute, Export Chart to SVG with viewBox attribute in Python via NET, Python Convert Chart to SVG with viewBox attribute.
---
{{% alert color="primary" %}}

 Per impostazione predefinita, quando il grafico viene esportato nel formato SVG, il file**viewBox** l'attributo non è incluso nel relativo XML. Tuttavia, Aspose.Cells for Python via .NET fornisce[**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) proprietà che, quando impostata su**VERO** esporta il grafico a SVG con l'attributo viewBox.

{{% /alert %}}

##  Esporta grafico a SVG con attributo viewBox

Il seguente codice di esempio esporta il grafico nel formato SVG con l'attributo viewBox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

 Se apri lo SVG del grafico nel blocco note, troverai il**viewBox** attributo simile a questo.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
