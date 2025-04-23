---
title: 在饼图中自定义切片或扇区的颜色
description: 学习如何使用 Aspose.Cells for Python via .NET 自定义饼图中的扇区和切片颜色。我们的指南将展示如何为每个扇区、切片或区域设置独特的颜色，从而提升视觉吸引力和数据表现。
keywords: Aspose.Cells for Python via .NET，饼图，自定义切片颜色，自定义扇区颜色，视觉吸引力，数据表示。
type: docs
weight: 60
url: /zh/python-net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

本文解释了如何向饼图切片/扇区添加自定义颜色。默认情况下，饼图使用Microsoft Excel的默认模板。要使用其他颜色，需要重新定义图表中的颜色。

{{% /alert %}}

要为饼图的单独切片或扇区设置自定义颜色：

1. 访问 [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) 对象的 [**ChartPoint**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint)。
1. 使用[**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color)属性分配您选择的颜色。

本文还解释了如何：

- 图表的类别数据。
- 与单元格相关联的图表标题。
- 图表标题字体设置。
- 图例的位置。

{{% alert color="primary" %}}

[**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color) 不仅适用于饼图，还可用于所有类型的图表。

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CustomSliceSectorColorsPieChart-1.py" >}}
