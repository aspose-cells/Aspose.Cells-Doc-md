---
title: Export Chart to SVG with viewBox attribute
type: docs
weight: 190
url: /java/export-chart-to-svg-with-viewbox-attribute/
---

{{% alert color="primary" %}} 

By default, when the chart is export to SVG format, the **viewBox** attribute is not included in its XML. However, Aspose.Cells provides [ImageOrPrintOptions.setSVGFitToViewPort()](https://apireference.aspose.com/java/cells/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) property which when set to **true** exports the chart to SVG with viewBox attribute.

If you open the chart's SVG in notepad, you will find the **viewBox** attribute similar to this.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}} 
#### **Export Chart to SVG with viewBox attribute**
{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}
