---
title: Exporter le graphique vers SVG avec l'attribut viewBox
type: docs
weight: 280
url: /fr/net/export-chart-to-svg-with-viewbox-attribute/
---
{{% alert color="primary" %}}

 Par défaut, lorsque le graphique est exporté au format SVG, le**viewBox** L'attribut n'est pas inclus dans son XML. Cependant, Aspose.Cells fournit[**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) propriété qui, lorsqu'elle est définie sur**vrai** exporte le graphique en SVG avec l'attribut viewBox.

{{% /alert %}}

## Exporter le graphique vers SVG avec l'attribut viewBox

L'exemple de code suivant exporte le graphique au format SVG avec l'attribut viewBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

 Si vous ouvrez le SVG du graphique dans le bloc-notes, vous trouverez le**viewBox** attribut similaire à celui-ci.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
