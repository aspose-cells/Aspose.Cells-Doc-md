---
title: 将视图到 SVG 格式的图表导出
type: docs
weight: 280
url: /zh/python-net/export-chart-to-svg-with-viewbox-attribute/
description: 通过使用Aspose.Cells for Python通过.NET API导出带有viewBox属性的SVG图表。
keywords: Python使用viewBox属性导出图表为SVG，通过NET导出带有viewBox属性的图表为SVG，在Python中将图表转换为具有viewBox属性的SVG。
---

{{% alert color="primary" %}}

默认情况下，在将图表导出为SVG格式时，其XML中不包括**viewBox**属性。但是，Aspose.Cells for Python通过.NET提供了[**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/)属性，在将其设置为**true**时，将带有viewBox属性的图表导出为SVG。

{{% /alert %}}

## 将图表导出为带 viewBox 属性的 SVG 格式

以下示例代码将图表导出为带有viewBox属性的SVG格式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

如果您在记事本中打开图表的SVG文件，您会发现类似于这样的viewBox属性。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
