---
title: 导出带有viewBox属性的SVG图表
type: docs
weight: 190
url: /zh/java/export-chart-to-svg-with-viewbox-attribute/
---

默认情况下，将图表导出为SVG格式时，其XML中不包括**viewBox**属性。但是，Aspose.Cells提供了一个属性，当设置为**true**时，将图表导出为带有viewBox属性的SVG。

如果在记事本中打开图表的SVG文件，将会找到类似于这样的**viewBox**属性。

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
- [使用所需的宽度和高度将工作表或图表导出为图像](/cells/zh/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
