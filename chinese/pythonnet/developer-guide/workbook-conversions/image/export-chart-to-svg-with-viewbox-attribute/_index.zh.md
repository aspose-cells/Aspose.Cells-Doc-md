---
title: 使用 viewBox 属性将图表导出到 SVG
type: docs
weight: 280
url: /zh/python-net/export-chart-to-svg-with-viewbox-attribute/
description: 使用 Aspose.Cells for Python via .NET API 将图表导出到具有 viewBox 属性的 SVG。
keywords: Python Export Chart to SVG with viewBox attribute, Export Chart to SVG with viewBox attribute in Python via NET, Python Convert Chart to SVG with viewBox attribute.
---
{{% alert color="primary" %}}

默认情况下，当图表导出为 SVG 格式时，**视图框**属性不包含在其 XML 中。但是，Aspose.Cells for Python via .NET 提供[**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/)属性，当设置为**真的**使用 viewBox 属性将图表导出到 SVG。

{{% /alert %}}

## 使用 viewBox 属性将图表导出到 SVG

以下示例代码使用 viewBox 属性将图表导出为 SVG 格式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

如果你用记事本打开图表的SVG，你会发现**视图框**与此类似的属性。

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
