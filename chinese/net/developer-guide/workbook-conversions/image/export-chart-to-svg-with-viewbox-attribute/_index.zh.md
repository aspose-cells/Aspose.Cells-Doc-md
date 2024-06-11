---
title: 导出带有viewBox属性的SVG图表
type: docs
weight: 280
url: /zh/net/export-chart-to-svg-with-viewbox-attribute/
---

{{% alert color="primary" %}}

默认情况下，将图表导出为SVG格式时，其XML中不包括**viewBox**属性。但是，Aspose.Cells提供了[**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport)属性，将其设置为**true**时会导出具有viewBox属性的SVG图表。

{{% /alert %}}

## 导出带有viewBox属性的SVG图表

以下示例代码将图表导出为带有viewBox属性的SVG格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

如果在记事本中打开图表的SVG文件，将会找到类似于这样的**viewBox**属性。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
