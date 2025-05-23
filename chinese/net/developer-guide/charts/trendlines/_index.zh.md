---
title: 获取图表趋势线的方程文本
description: 学习如何使用 Aspose.Cells for .NET 检索在 Microsoft Excel 创建的图表中趋势线的方程文本。我们的指南将演示如何访问和提取趋势线的方程以进行进一步分析或显示。
keywords: Aspose.Cells for .NET，图表趋势线，方程文本，Microsoft Excel，数据分析，显示。
linktitle: 趋势线
type: docs
weight: 110
url: /zh/net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells检索图表趋势线的方程文本。Aspose.Cells提供了[**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text)属性，该属性返回图表趋势线的方程文本。要使用此属性，您首先必须调用[**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/calculate)方法。

{{% /alert %}}

下图显示了有趋势线的图表，其方程文本以红色显示。我们将使用[**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text)属性来检索这个文本，在以下示例代码中。

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## 获取图表趋势线的方程文本的C#代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetEquationTextOfChartTrendLine-1.cs" >}}

## 示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
