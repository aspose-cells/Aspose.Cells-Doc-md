---
title: 确定图表中存在哪个轴
type: docs
weight: 140
url: /zh/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

有时，用户需要知道图表中是否存在特定轴。例如，他想知道图表中是否存在次要值轴。一些图表，如 Pie、PieExploded、PiePie、PieBar、Pie3D、Pie3DExploded、Doughnut、DoughnutExploded 等没有轴。

Aspose.Cells提供[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)确定图表是否具有特定轴的方法。

{{% /alert %}}

下面的示例代码演示了使用[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)以确定示例图表是否具有主要和次要类别以及值轴。

## C# 判断图表中存在哪个轴的代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## 示例代码生成的控制台输出

代码的控制台输出如下所示，其中对主要类别和价值轴显示 true，对次要类别和价值轴显示 false。

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
