---
title: 确定在图表中存在的轴类型（使用Golang通过C++）
description: 了解如何确定使用Aspose.Cells for C++创建的图表中存在的轴。我们的指南将帮助您理解如何识别和访问图表中的不同轴，包括类别轴、数值轴和次轴。
keywords: Aspose.Cells for C++，图表，轴，存在性，类别轴，数值轴，次轴。
type: docs
weight: 140
url: /zh/go-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

有时，用户需要知道图表中是否存在特定的轴。例如，他想知道图表中是否存在次要值轴。有些图表，比如饼图，爆破饼图，饼-饼图，饼图-柱状图，3D饼图，3D爆破饼图，圆环图，爆破圆环图等，是没有轴的。

Aspose.Cells提供了[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/)方法来判断图表是否具有特定的轴。

{{% /alert %}}

以下示例代码演示了如何使用[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/)判断样本图表是否具有主类别和数值轴以及次类别和数值轴。

## 用C++判断图表中存在的轴的代码

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetermineWhichAxisExistsInTheChart.go" >}}
## 示例代码生成的控制台输出

代码的控制台输出如下所示，显示主类别和值轴为true，次要类别和值轴为false。

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
