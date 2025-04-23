---
title: Exportera diagram till SVG med viewBox attribut
type: docs
weight: 280
url: /sv/net/export-chart-to-svg-with-viewbox-attribute/
---

{{% alert color="primary" %}}

Som standard, när diagrammet exporteras till SVG-format, ingår inte attributet **viewBox** i dess XML. Men Aspose.Cells tillhandahåller [**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport)-egenskapen som när den är inställd på **true** exporterar diagrammet till SVG med viewBox-attributen.

{{% /alert %}}

## Exportera diagram till SVG med viewBox-attribut

Följande kodexempel exporterar diagrammet till SVG-format med viewBox-attributet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

Om du öppnar diagrammets SVG i anteckningar kommer du att hitta **viewBox** -attributet som liknar detta.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
