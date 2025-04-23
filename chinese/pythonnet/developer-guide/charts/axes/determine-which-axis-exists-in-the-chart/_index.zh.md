---
title: 确定图表中存在哪个轴
description: 学习如何确定使用 Aspose.Cells for Python via .NET 创建的图表中存在哪个轴。我们的指南将帮助你理解如何识别和访问图表中的不同轴，包括类别轴、值轴和次轴。
keywords: Aspose.Cells for Python via .NET，图表，轴，存在，类别，值，次轴。
type: docs
weight: 140
url: /zh/python-net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

有时，用户需要知道图表中是否存在特定的轴。例如，他想知道图表中是否存在次要值轴。有些图表，比如饼图，爆破饼图，饼-饼图，饼图-柱状图，3D饼图，3D爆破饼图，圆环图，爆破圆环图等，是没有轴的。

Aspose.Cells for Python via .NET 提供 [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) 方法以判断图表是否具有特定的轴。

{{% /alert %}}

以下示例代码演示了如何使用[**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis)来确定示例图表是否具有主要和次要类别和值轴。

## 用于确定图表中存在哪些轴的C#代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DetermineAxisInChart.py" >}}

## 示例代码生成的控制台输出

代码的控制台输出如下所示，显示主类别和值轴为true，次要类别和值轴为false。

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
