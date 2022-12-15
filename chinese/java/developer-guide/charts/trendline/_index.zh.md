---
title: 获取图表趋势线的公式文本
linktitle: 趋势线
type: docs
weight: 90
url: /zh/java/get-equation-text-of-chart-trendline/
---
{{% alert color="primary" %}}

您可以使用 Aspose.Cells 检索图表趋势线的公式文本。Aspose.Cells 提供[**趋势线.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)返回图表趋势线的公式文本的属性。要使用此属性，您首先必须调用[**图表.计算()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()） 方法。

{{% /alert %}}

## **例子**

以下屏幕截图显示了带有趋势线的图表，其公式文本显示为红色。我们将使用[**趋势线.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)以下示例代码中的属性。

![待办事项：图像_替代_文本](get-equation-text-of-chart-trendline_1.png)

### Java 获取图表趋势线等式文本的代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### 示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight "java" >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
