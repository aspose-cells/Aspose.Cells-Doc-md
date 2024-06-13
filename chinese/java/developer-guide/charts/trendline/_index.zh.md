---
title: 获取图表趋势线的方程文本
linktitle: 趋势线
type: docs
weight: 90
url: /zh/java/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells检索图表趋势线的方程文本。Aspose.Cells提供了[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)属性，该属性返回图表趋势线的方程文本。要使用此属性，您首先必须调用[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--)方法。

{{% /alert %}}

## **示例**

下图显示了有趋势线的图表，其方程文本以红色显示。我们将使用[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)属性来检索这个文本，在以下示例代码中。

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

### 获取图表趋势线的方程文本的Java代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### 由示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
