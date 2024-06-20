---
title: Exportar gráfico a SVG con el atributo viewBox
type: docs
weight: 280
url: /es/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Exportar gráfico a SVG con atributo viewBox utilizando Aspose.Cells para Python via .NET API.
keywords: Python Exportar gráfico a SVG con el atributo viewBox, Exportar gráfico a SVG con el atributo viewBox en Python via NET, Python Convertir gráfico a SVG con el atributo viewBox.
---

{{% alert color="primary" %}}

Por defecto, cuando el gráfico se exporta al formato SVG, el atributo **viewBox** no se incluye en su XML. Sin embargo, Aspose.Cells para Python via .NET proporciona la propiedad [**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) que, cuando se establece en **true**, exporta el gráfico a SVG con el atributo viewBox.

{{% /alert %}}

## Exportar gráfico a SVG con el atributo viewBox

El siguiente código de ejemplo exporta el gráfico al formato SVG con el atributo viewBox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

Si abres el SVG del gráfico en el bloc de notas, encontrarás el atributo **viewBox** similar a este:

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
