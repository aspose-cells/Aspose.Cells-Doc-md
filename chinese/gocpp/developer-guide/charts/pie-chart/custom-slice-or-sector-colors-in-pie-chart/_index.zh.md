---
title: 在饼图中自定义扇区或扇色，用Golang通过C++实现
linktitle: 在饼图中自定义切片或扇区的颜色
description: 了解如何使用 Aspose.Cells for C++ 自定义饼图中切片和扇区的颜色。我们的指南将演示如何为每个切片、扇区或图例分配独特的颜色，以增强视觉吸引力和数据表现。
keywords: Aspose.Cells for C++，饼图，自定义切片颜色，自定义扇区颜色，视觉吸引力，数据表现。
type: docs
weight: 60
url: /zh/go-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

本文解释了如何向饼图切片/扇区添加自定义颜色。默认情况下，饼图使用Microsoft Excel的默认模板。要使用其他颜色，需要重新定义图表中的颜色。

{{% /alert %}}

要为饼图的单独切片或扇区设置自定义颜色：

1. 访问 [**Series**](https://reference.aspose.com/cells/go-cpp/series/) 对象的 [**ChartPoint**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/)。
1. 使用[**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/go-cpp/area/getforegroundcolor/)属性分配您选择的颜色。

本文还解释了如何：

- 图表的类别数据。
- 与单元格相关联的图表标题。
- 图表标题字体设置。
- 图例的位置。

{{% alert color="primary" %}}

[**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/go-cpp/area/getforegroundcolor/) 不仅适用于饼图，还可用于所有类型的图表。

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomSliceOrSectorColorsInPieChart.go" >}}
