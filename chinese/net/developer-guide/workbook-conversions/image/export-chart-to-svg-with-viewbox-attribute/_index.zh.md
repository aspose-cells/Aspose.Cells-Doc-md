---
title: 将视图到 SVG 格式的图表导出
type: docs
weight: 280
url: /zh/net/export-chart-to-svg-with-viewbox-attribute/
---

{{% alert color="primary" %}}

默认情况下，当图表导出为 SVG 格式时，其 XML 中不包括 **viewBox** 属性。 然而，Aspose.Cells 提供了 [**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) 属性，当设置为 **true** 时导出带有 viewBox 属性的 SVG 图表。

{{% /alert %}}

## 将图表导出为带 viewBox 属性的 SVG 格式

以下示例代码将图表导出为带有viewBox属性的SVG格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

如果您在记事本中打开图表的SVG文件，您会发现类似于这样的viewBox属性。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
