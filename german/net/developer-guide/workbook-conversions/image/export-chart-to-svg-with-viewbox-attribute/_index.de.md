---
title: Diagramm mit viewBox-Attribut nach SVG exportieren
type: docs
weight: 280
url: /de/net/export-chart-to-svg-with-viewbox-attribute/
---
{{% alert color="primary" %}}

 Wenn das Diagramm in das SVG-Format exportiert wird, wird standardmäßig die**viewBox** -Attribut ist nicht in seinem XML enthalten. Allerdings bietet Aspose.Cells[**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) Eigenschaft, die, wenn festgelegt auf**Stimmt** Exportiert das Diagramm mit dem viewBox-Attribut nach SVG.

{{% /alert %}}

## Diagramm mit viewBox-Attribut nach SVG exportieren

Der folgende Beispielcode exportiert das Diagramm mit dem viewBox-Attribut in das SVG-Format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

 Wenn Sie die SVG-Datei des Diagramms im Editor öffnen, finden Sie die**viewBox** ähnliches Attribut.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
