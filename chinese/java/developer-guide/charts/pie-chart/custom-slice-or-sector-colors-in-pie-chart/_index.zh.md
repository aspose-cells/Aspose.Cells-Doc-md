---
title: 饼图中的自定义切片或扇区颜色
type: docs
weight: 30
url: /zh/java/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

本文介绍如何向饼图切片/扇区添加自定义颜色。默认情况下，饼图使用 Microsoft Excel 默认模板。要使用其他颜色，可以重新定义图表中的颜色。

{{% /alert %}}

要为饼图的各个切片或扇区设置自定义颜色：

1. 访问[**系列**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)对象的[**图表点**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1. 使用分配您选择的颜色[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)方法。

本文还介绍了如何设置：

- 图表的类别数据。
- 链接到单元格的图表标题。
- 图表标题字体设置。
- 图例的位置。

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)不特定于饼图，但可用于所有类型的图表。

{{% /alert %}}

**饼图中的自定义切片颜色**

![待办事项：图片_替代_文本](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
