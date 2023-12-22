---
title: 如何创建动态滚动图表
description: 了解如何使用 Aspose.Cells for .NET 创建动态滚动图表。我们的指南将演示如何在图表中实现平滑的数据转换和滚动平均值，以实现连续和更新的显示。
keywords: Aspose.Cells for .NET, Dynamic Rolling Chart, Data Transitions, Smooth Averages, Continuous Display, Updating Visualization.
type: docs
weight: 74
url: /zh/net/create-dynamic-rolling-chart/
---
##  **可能的使用场景**
动态滚动图表是指显示数据点随时间不断变化和更新的图形表示形式。它是一种不断自我更新的图表，显示最新数据点的滚动窗口，同时在新数据点出现时丢弃旧数据点。

动态滚动图表通常用于可视化实时或流数据中的趋势和模式。它们在时间方面和随时间变化至关重要的场景中特别有用，例如股票市场分析、天气监控或实时绩效跟踪。

这些图表通常采用动画或自动滚动机制来确保始终呈现最新信息。可以自定义滚动窗口的长度以显示特定时间段，例如最后一小时、一天或一周。

总之，动态滚动图表是一种不断更新的图形表示，它显示最新的数据点，同时丢弃旧的数据点，允许用户观察实时趋势和模式。

##  **使用 Aspose Cells 创建动态滚动图表**
在接下来的段落中，我们将向您展示如何使用 Aspose.Cells 创建动态滚动图表。我们将向您展示该示例的代码，以及使用此代码创建的 Excel 文件。

##  **示例代码**
以下示例代码将生成[动态滚动图表文件](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

##  **笔记**
在生成的文件中，可以继续添加A列和B列的数据，同时图表动态统计最新的5组数据。这是使用示例代码中的“OFFSET”公式完成的：

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

您可以尝试将公式中的数字“-5”改为“-10”，动态图表将统计最新10组数据。现在我们已经成功使用Aspose.Cells创建了一个动态滚动图表。
