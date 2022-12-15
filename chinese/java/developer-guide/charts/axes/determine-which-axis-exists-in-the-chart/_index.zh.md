---
title: 确定图表中存在哪个轴
type: docs
weight: 130
url: /zh/java/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

有时，用户需要知道图表中是否存在特定轴。例如，他想知道图表中是否存在次要值轴。一些图表，如 Pie、PieExploded、PiePie、PieBar、Pie3D、Pie3DExploded、Doughnut、DoughnutExploded 等没有轴。

Aspose.Cells提供[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) 方法来确定图表是否具有特定轴。

{{% /alert %}}

## 确定图表中存在哪个轴

以下屏幕截图显示了一个只有主类别和值轴的图表。它没有任何次要类别和价值轴。

![待办事项：图像_替代_文本](determine-which-axis-exists-in-the-chart_1.png)

下面的示例代码演示了使用[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)以确定示例图表是否具有主要和次要类别以及值轴。代码的控制台输出如下所示，其中对主要类别和价值轴显示 true，对次要类别和价值轴显示 false。

### Java 确定图表中存在哪个轴的代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### 示例代码生成的控制台输出

这是上述示例代码的控制台输出。

{{< highlight "java" >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
