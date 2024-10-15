---
title: Export Chart to SVG with viewBox attribute
type: docs
weight: 280
url: /net/export-chart-to-svg-with-viewbox-attribute/
---

{{% alert color="primary" %}}

By default, when the chart is exported to SVG format, the **viewBox** attribute is not included in its XML. However, Aspose.Cells provides [**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) property which when set to **true** exports the chart to SVG with viewBox attribute.

{{% /alert %}}

## Export Chart to SVG with viewBox attribute

The following sample code exports the chart to SVG format with the viewBox attribute.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

If you open the chart's SVG in notepad, you will find the **viewBox** attribute similar to this.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}