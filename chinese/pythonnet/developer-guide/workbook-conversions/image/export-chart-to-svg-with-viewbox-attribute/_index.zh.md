---
title: 导出带有viewBox属性的SVG图表
type: docs
weight: 280
url: /zh/python-net/export-chart-to-svg-with-viewbox-attribute/
description: 使用Aspose.Cells for Python via .NET API导出带有viewBox属性的SVG图表。
keywords: Python使用viewBox属性导出图表到SVG，Python中使用viewBox属性导出图表到SVG via NET，Python将图表转换为带有viewBox属性的SVG。
---

{{% alert color="primary" %}}

默认情况下，当图表导出为SVG格式时，其XML中不包含viewBox属性。但是，Aspose.Cells for Python via .NET提供了[**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/)属性，当设置为**true**时，将以包含viewBox属性的SVG格式导出图表。

{{% /alert %}}

## 导出带有viewBox属性的SVG图表

以下示例代码将图表导出为带有viewBox属性的SVG格式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

如果在记事本中打开图表的SVG文件，将会找到类似于这样的**viewBox**属性。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
