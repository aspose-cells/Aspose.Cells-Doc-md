---
title: Exportar gráfico a SVG con el atributo viewBox
type: docs
weight: 280
url: /es/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Exporte el gráfico a SVG con el atributo viewBox utilizando Aspose.Cells for Python via .NET API.
keywords: Python Export Chart to SVG with viewBox attribute, Export Chart to SVG with viewBox attribute in Python via NET, Python Convert Chart to SVG with viewBox attribute.
---
{{% alert color="primary" %}}

 De forma predeterminada, cuando el gráfico se exporta al formato SVG, el**vercuadro** El atributo no está incluido en su XML. Sin embargo, Aspose.Cells for Python via .NET proporciona[**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) propiedad que cuando se establece en**verdadero** exporta el gráfico a SVG con el atributo viewBox.

{{% /alert %}}

##  Exportar gráfico a SVG con el atributo viewBox

El siguiente código de muestra exporta el gráfico al formato SVG con el atributo viewBox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

 Si abre el SVG del gráfico en el bloc de notas, encontrará el**vercuadro** atributo similar a este.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
