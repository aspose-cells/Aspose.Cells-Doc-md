---
title: Exportar gráfico a SVG con el atributo viewBox
type: docs
weight: 190
url: /es/java/export-chart-to-svg-with-viewbox-attribute/
---
 De forma predeterminada, cuando el gráfico se exporta a formato SVG, el**viewBox** atributo no está incluido en su XML. Sin embargo, Aspose.Cells proporciona[**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) propiedad que cuando se establece en**verdadero** exporta el gráfico a SVG con el atributo viewBox.

 Si abre el SVG del gráfico en el bloc de notas, encontrará el**viewBox** atributo similar a este.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## Fragmento de código

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## Artículos relacionados

- [Representación de gráficos](/cells/es/java/chart-rendering/)
- [Exportar hoja de trabajo o gráfico a una imagen con el ancho y la altura deseados](/cells/es/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
