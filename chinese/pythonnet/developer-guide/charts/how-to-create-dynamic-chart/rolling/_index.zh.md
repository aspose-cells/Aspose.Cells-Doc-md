---
title: 如何创建动态滚动图表
description: 学习如何使用 Aspose.Cells for Python via .NET 创建动态滚动图表。我们的指南将演示如何在图表中实现平滑的数据过渡和滚动平均，以实现持续更新的显示效果。
keywords: Aspose.Cells for Python via .NET，动态滚动图表，数据过渡，平滑平均，连续显示，更新可视化。
type: docs
weight: 74
url: /zh/python-net/create-dynamic-rolling-chart/
---

## **可能的使用场景**
动态滚动图表是指显示数据点不断变化和更新的图形表示。这是一种图表类型，会不断更新自己，展示最近数据点的滚动窗口，同时丢弃旧的数据点，因为新的数据点出现。

动态滚动图表通常用于可视化实时或流数据中的趋势和模式。在临时方面和随时间的变化至关重要的场景中特别有用，如股票市场分析、天气监测或实时性能跟踪。

这些图表通常采用动画或自动滚动机制，以确保始终呈现最新的信息。滚动窗口的长度可以自定义，以显示特定的时间段，如最近一小时、一天或一周。

总之，动态滚动图表是不断更新的图形表示，显示最新数据点，丢弃旧数据点，使用户能够观察实时趋势和模式。

## **使用 Aspose.Cells for Python via .NET 创建动态滚动图表**
在接下来的段落中，我们将向您展示如何使用 Aspose.Cells for Python via .NET 创建动态滚动图表。我们会提供示例代码以及用此代码生成的 Excel 文件。

## **示例代码**
以下示例代码将生成[动态滚动图表文件](DynamicRollingChart.xlsx)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-dynamic-rolling-chart.py" >}}

## **备注**
在生成的文件中，您可以继续在A列和B列中添加数据，同时图表动态计算最新的 5 组数据。这是通过示例代码中的“OFFSET”公式完成的：

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

您可以尝试将公式中的数字 "-5" 改为 "-10"，动态图表会显示最新的 10 组数据。现在我们已经成功使用 Aspose.Cells for Python via .NET 创建了动态滚动图表。
{{< app/cells/assistant language="python-net" >}}
