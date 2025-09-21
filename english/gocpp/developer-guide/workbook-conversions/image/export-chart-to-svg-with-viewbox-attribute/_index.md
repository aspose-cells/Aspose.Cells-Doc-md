---
title: Export Chart to SVG with viewBox attribute using C++
linktitle: Export Chart to SVG with viewBox attribute
type: docs
weight: 280
url: /go-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Export a chart to SVG format with viewBox attribute using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

By default, when the chart is exported to SVG format, the **viewBox** attribute is not included in its XML. However, Aspose.Cells provides [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getsvgfittoviewport/) property which when set to **true** exports the chart to SVG with viewBox attribute.

{{% /alert %}}

## Export Chart to SVG with viewBox attribute

The following sample code exports the chart to SVG format with the viewBox attribute.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportChartToSvgWithViewboxAttribute.go" >}}
{{% alert color="primary" %}}

If you open the chart's SVG in notepad, you will find the **viewBox** attribute similar to this.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}