---
title: Diagramm als SVG mit viewBox Attribut exportieren
type: docs
weight: 280
url: /de/net/export-chart-to-svg-with-viewbox-attribute/
---

{{% alert color="primary" %}}

Standardmäßig ist das **viewBox**-Attribut beim Export des Diagramms ins SVG-Format nicht in seinem XML enthalten. Allerdings bietet Aspose.Cells [**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) Eigenschaft, die beim Einstellen auf **true** das Diagramm ins SVG mit viewBox-Attribut exportiert.

{{% /alert %}}

## Diagramm als SVG mit viewBox-Attribut Exportieren

Der folgende Beispielcode exportiert das Diagramm im SVG-Format mit dem viewBox-Attribut.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

Wenn Sie das SVG des Diagramms in Notepad öffnen, finden Sie das **viewBox**-Attribut ähnlich wie dieses.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
