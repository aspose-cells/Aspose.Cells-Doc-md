---
title: 通过 Golang 和 C++ 获取图表趋势线的方程文本
linktitle: 趋势线
description: 学习如何使用 Aspose.Cells for C++ 获取 Microsoft Excel 中创建的图表趋势线的方程文本。我们的指南将演示如何访问和提取趋势线的方程以进行后续分析或显示。
keywords: Aspose.Cells for C++，图表趋势线，方程文本，Microsoft Excel，数据分析，显示。
type: docs
weight: 110
url: /zh/go-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells检索图表趋势线的方程文本。Aspose.Cells提供了[**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/)属性，该属性返回图表趋势线的方程文本。要使用此属性，您首先必须调用[**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/)方法。

{{% /alert %}}

以下截图显示带有趋势线的图表及其方程文本（红色显示）。我们将在下面的示例代码中使用 [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) 属性检索这段文本。

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## 获取图表趋势线方程文本的 C++ 代码

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Trendlines.go" >}}
## 示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
