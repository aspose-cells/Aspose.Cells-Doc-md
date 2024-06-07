---
title: 确定图表中存在哪些轴
description: 学习如何确定使用Aspose.Cells for .NET创建的图表中存在哪些轴。我们的指南将帮助您了解如何识别和访问图表中的不同轴，包括类别、值和辅助轴。
keywords: Aspose.Cells for .NET, 图表, 轴, 存在, 类别, 值，辅助。
type: docs
weight: 140
url: /zh/net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

有时，用户需要知道图表中是否存在特定的轴。例如，他想知道图表中是否存在次要数值轴。像饼图、饼图(分裂)、饼图饼图、饼图条形图、3D饼图、3D饼图(分裂)、环图、环图(分裂)等图表没有轴。

Aspose.Cells提供[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)方法来确定图表是否具有特定轴。

{{% /alert %}}

以下示例代码演示了如何使用[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)来确定样本图表是否有主类别轴和次要类别和值轴。

## 用于确定图表中存在哪些轴的C#代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## 示例代码生成的控制台输出

代码的控制台输出如下：显示主要类别和值轴为true，次要类别和值轴为false。

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
