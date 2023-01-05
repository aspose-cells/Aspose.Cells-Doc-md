---
title: 使用 viewBox 属性将图表导出到 SVG
type: docs
weight: 280
url: /zh/net/export-chart-to-svg-with-viewbox-attribute/
---
{{% alert color="primary" %}}

默认情况下，当图表导出为 SVG 格式时，**视图框**属性不包含在其 XML 中。但是，Aspose.Cells 提供[**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport)设置为的属性**真的**使用 viewBox 属性将图表导出到 SVG。

{{% /alert %}}

## 使用 viewBox 属性将图表导出到 SVG

以下示例代码使用 viewBox 属性将图表导出为 SVG 格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

如果你用记事本打开图表的SVG，你会发现**视图框**属性类似于此。

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
