---
title: Export Chart to SVG with viewBox attribute
type: docs
weight: 280
url: /python-net/export-chart-to-svg-with-viewbox-attribute/
description: Export Chart to SVG with viewBox attribute by using Aspose.Cells for Python via .NET API.
keywords: Python Export Chart to SVG with viewBox attribute, Export Chart to SVG with viewBox attribute in Python via NET, Python Convert Chart to SVG with viewBox attribute.
---

{{% alert color="primary" %}}

By default, when the chart is exported to SVG format, the **viewBox** attribute is not included in its XML. However, Aspose.Cells for Python via .NET provides [**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) property which when set to **true** exports the chart to SVG with viewBox attribute.

{{% /alert %}}

## Export Chart to SVG with viewBox attribute

The following sample code exports the chart to SVG format with the viewBox attribute.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

If you open the chart's SVG in notepad, you will find the **viewBox** attribute similar to this.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
