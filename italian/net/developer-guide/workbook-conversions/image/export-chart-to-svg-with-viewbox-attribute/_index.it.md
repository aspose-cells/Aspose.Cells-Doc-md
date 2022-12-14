---
title: Esporta il grafico in SVG con l'attributo viewBox
type: docs
weight: 280
url: /it/net/export-chart-to-svg-with-viewbox-attribute/
---
{{% alert color="primary" %}}

 Per impostazione predefinita, quando il grafico viene esportato in formato SVG, il file**viewBox** l'attributo non è incluso nel suo XML. Tuttavia, Aspose.Cells fornisce[**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) proprietà che quando impostata su**VERO** esporta il grafico in SVG con l'attributo viewBox.

{{% /alert %}}

## Esporta il grafico in SVG con l'attributo viewBox

Il seguente codice di esempio esporta il grafico in formato SVG con l'attributo viewBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

 Se apri l'SVG del grafico nel blocco note, troverai il file**viewBox** attributo simile a questo.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
