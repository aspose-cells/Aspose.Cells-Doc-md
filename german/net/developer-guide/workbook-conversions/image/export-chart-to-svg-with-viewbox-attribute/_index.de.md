---
title: Diagramm nach SVG mit viewBox-Attribut exportieren
type: docs
weight: 280
url: /de/net/export-chart-to-svg-with-viewbox-attribute/
---
{{% alert color="primary" %}}

 Wenn das Diagramm in das Format SVG exportiert wird, wird standardmäßig die**viewBox** -Attribut ist nicht in seinem XML enthalten. Allerdings bietet Aspose.Cells[**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) Eigenschaft, die, wenn festgelegt auf**wahr** Exportiert das Diagramm nach SVG mit dem viewBox-Attribut.

{{% /alert %}}

## Diagramm nach SVG mit viewBox-Attribut exportieren

Der folgende Beispielcode exportiert das Diagramm mit dem viewBox-Attribut in das Format SVG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

 Wenn Sie die SVG des Diagramms im Notizblock öffnen, finden Sie die**viewBox**ähnliches Attribut.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
