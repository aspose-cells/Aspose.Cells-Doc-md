---
title: Exportar gráfico a SVG con el atributo viewBox
type: docs
weight: 280
url: /es/net/export-chart-to-svg-with-viewbox-attribute/
---
{{% alert color="primary" %}}

 De forma predeterminada, cuando el gráfico se exporta a formato SVG, el**viewBox** atributo no está incluido en su XML. Sin embargo, Aspose.Cells proporciona[**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) propiedad que cuando se establece en**verdadero** exporta el gráfico a SVG con el atributo viewBox.

{{% /alert %}}

## Exportar gráfico a SVG con el atributo viewBox

El siguiente código de ejemplo exporta el gráfico a formato SVG con el atributo viewBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

 Si abre el SVG del gráfico en el bloc de notas, encontrará el**viewBox** atributo similar a este.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
