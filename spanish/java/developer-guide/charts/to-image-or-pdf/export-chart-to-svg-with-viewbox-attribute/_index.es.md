---
title: Exportar gráfico a SVG con el atributo viewBox
type: docs
weight: 190
url: /es/java/export-chart-to-svg-with-viewbox-attribute/
---

Por defecto, al exportar el gráfico a formato SVG, el atributo **viewBox** no se incluye en su XML. Sin embargo, Aspose.Cells proporciona la propiedad [**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) que, cuando se establece en **true**, exporta el gráfico a SVG con el atributo viewBox.

Si abres el SVG del gráfico en el bloc de notas, encontrarás el atributo **viewBox** similar a este:

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## Fragmento de código

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## Artículos relacionados

- [Representación de gráficos](/cells/es/java/chart-rendering/)
- [Exportar hoja de cálculo o gráfico a imagen con ancho y alto deseados](/cells/es/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
