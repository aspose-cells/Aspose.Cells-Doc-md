---
title: 使用 viewBox 属性将图表导出到 SVG
type: docs
weight: 190
url: /zh/java/export-chart-to-svg-with-viewbox-attribute/
---
默认情况下，当图表导出为 SVG 格式时，**视图框**属性不包含在其 XML 中。但是，Aspose.Cells 提供[**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort)设置为的属性**真的**使用 viewBox 属性将图表导出到 SVG。

如果你用记事本打开图表的SVG，你会发现**视图框**属性类似于此。

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## 代码片段

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## 相关文章

- [图表渲染](/cells/zh/java/chart-rendering/)
- [将工作表或图表导出为具有所需宽度和高度的图像](/cells/zh/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
