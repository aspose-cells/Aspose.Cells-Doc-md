---
title: 在饼图中自定义切片或扇区的颜色
type: docs
weight: 30
url: /zh/java/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

本文介绍如何向饼图切片/扇区添加自定义颜色。默认情况下，饼图使用 Microsoft Excel 默认模板。要使用其他颜色，可以重新定义图表中的颜色。

{{% /alert %}}

设置饼图单独切片或扇区的自定义颜色：

1. 访问 [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) 对象的 [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)。
1. 使用 [**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) 方法分配所选颜色。

本文还解释了如何设置：

- 图表的类别数据。
- 与单元格相关联的图表标题。
- 图表标题字体设置。
- 图例的位置。

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) 不仅适用于饼图，还可用于所有类型的图表。

{{% /alert %}}

**饼图中的自定义切片颜色**

![todo:image_alt_text](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
{{< app/cells/assistant language="java" >}}
