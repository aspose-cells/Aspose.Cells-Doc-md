---
title: 确定图表中存在哪些轴
type: docs
weight: 130
url: /zh/java/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

有时，用户需要知道图表中是否存在特定的轴。例如，他想知道图表中是否存在次要值轴。一些图表，如饼图、饼图（扩展）、饼图（饼）、饼图（条形）、3D饼图、3D饼图（扩展）、圆环图、圆环图（扩展）等等没有轴。

Aspose.Cells提供了 [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean) 方法来确定图表是否具有特定轴。

{{% /alert %}}

## 确定图表中存在哪些轴

以下屏幕截图显示了一个图表，它只有主要类别和值轴。它没有任何次要类别和值轴。

![todo:image_alt_text](determine-which-axis-exists-in-the-chart_1.png)

以下示例代码演示了使用[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)）来确定样本图表是否具有主要和次要类别和值轴。代码的控制台输出如下所示，显示了主要类别和值轴为true，次要类别和值轴为false。

### Java代码确定图表中存在哪个轴

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### 由示例代码生成的控制台输出

以下是上述示例代码的控制台输出。

{{< highlight java >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
