---
title: 将视图到 SVG 格式的图表导出
type: docs
weight: 190
url: /zh/java/export-chart-to-svg-with-viewbox-attribute/
---

默认情况下，导出图表为SVG格式时，其XML中不包括**viewBox**属性。但是，当[**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort)设置为**true**时，Aspose.Cells提供了该属性，以将图表导出为带有viewBox属性的SVG。

如果您在记事本中打开图表的SVG文件，您会发现类似于这样的viewBox属性。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## 代码片段

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## 相关文章

- [图表渲染](/cells/zh/java/chart-rendering/)
- [使用所需宽度和高度将工作表或图表导出为图像](/cells/zh/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
