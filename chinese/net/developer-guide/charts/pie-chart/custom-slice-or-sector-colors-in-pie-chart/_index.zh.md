---
title: 饼图中的自定义切片或扇区颜色
type: docs
weight: 60
url: /zh/net/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

本文介绍如何向饼图切片/扇区添加自定义颜色。默认情况下，饼图使用 Microsoft Excel 默认模板。要使用其他颜色，请重新定义图表中的颜色。

{{% /alert %}}

要为饼图的各个切片或扇区设置自定义颜色：

1. 访问[**系列**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)对象的[**图表点**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint).
1. 使用分配您选择的颜色[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)财产。

本文还解释了如何：

- 图表的类别数据。
- 链接到单元格的图表标题。
- 图表标题字体设置。
- 图例的位置。

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)不特定于饼图，但它可用于所有类型的图表。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
