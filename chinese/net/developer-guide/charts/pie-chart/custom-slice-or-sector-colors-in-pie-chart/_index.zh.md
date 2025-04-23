---
title: 在饼图中自定义切片或扇区的颜色
description: 学习如何使用 Aspose.Cells for .NET 自定义饼图中的片区和扇区颜色。我们的指南将演示如何为每个片区、扇区或区域分配独特的颜色，以提高视觉吸引力和数据表现。
keywords: Aspose.Cells for .NET, 饼图, 自定义片区颜色, 自定义扇区颜色, 视觉吸引力, 数据表现。
type: docs
weight: 60
url: /zh/net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

本文解释了如何向饼图切片/扇区添加自定义颜色。默认情况下，饼图使用Microsoft Excel的默认模板。要使用其他颜色，需要重新定义图表中的颜色。

{{% /alert %}}

要为饼图的单独切片或扇区设置自定义颜色：

1. 访问 [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) 对象的 [**ChartPoint**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint)。
1. 使用[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)属性分配您选择的颜色。

本文还解释了如何：

- 图表的类别数据。
- 与单元格相关联的图表标题。
- 图表标题字体设置。
- 图例的位置。

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) 不仅适用于饼图，还可用于所有类型的图表。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
