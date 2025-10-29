---
title: 获取图表趋势线的方程文本
description: 了解如何使用Aspose.Cells for Python via .NET检索Microsoft Excel中创建的图表中趋势线的方程文本。我们的指南将演示如何访问和提取趋势线的方程以供进一步分析或显示。
keywords: Aspose.Cells for Python via .NET，图表趋势线，方程文本，Microsoft Excel，数据分析，显示。
linktitle: 趋势线
type: docs
weight: 110
url: /zh/python-net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

你可以使用Aspose.Cells for Python via .NET检索图表趋势线的方程文本。Aspose.Cells for Python via .NET提供了返回图表趋势线方程文本的属性。要使用此属性，您首先需要调用[**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate)方法。

{{% /alert %}}

下图显示了有趋势线的图表，其方程文本以红色显示。我们将使用[**Trendline.data_labels.text**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/datalabels/text)属性来检索这个文本，在以下示例代码中。

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## 获取图表趋势线的方程文本的C#代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetEquationTextOfChartTrendLine-1.py" >}}

## 示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
