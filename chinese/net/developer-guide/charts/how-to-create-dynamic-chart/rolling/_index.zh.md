---
title: 如何创建动态滚动图表
description: 学习如何使用Aspose.Cells for .NET创建动态滚动图表。我们的指南将演示如何在图表中实现平滑的数据过渡和滚动平均值，以实现连续和更新的显示。
keywords: Aspose.Cells for .NET, Dynamic Rolling Chart, Data Transitions, Smooth Averages, Continuous Display, Updating Visualization。
type: docs
weight: 74
url: /zh/net/create-dynamic-rolling-chart/
---

## **可能的使用场景**
动态滚动图表是指一种图形表示方法，不断变化和更新数据点。它是一种不断更新自身的图表类型，展示最新数据点的滚动窗口，随着新数据点的到来而丢弃较旧的数据点。

动态滚动图表通常用于可视化实时或流式数据中的趋势和模式。在时间方面和随时间变化至关重要的情况下，例如股票市场分析、天气监测或实时表现跟踪中，它们特别有用。

这些图表通常采用动画或自动滚动机制，以确保始终呈现最新的信息。滚动窗口的长度可以定制以显示特定的时间段，例如过去一小时、一天或一周。

总而言之，动态滚动图是一种不断更新的图形表示，显示最新数据点，丢弃较旧的数据点，使用户能够观察实时趋势和模式。

## **使用Aspose Cells创建动态滚动图**
在接下来的段落中，我们将向您展示如何使用Aspose.Cells创建动态滚动图。我们将展示示例代码，以及使用该代码创建的Excel文件。

## **示例代码**
以下示例代码将生成[动态滚动图文件](DynamicRollingChart.xlsx)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

## **笔记**
在生成的文件中，您可以在A列和B列中继续添加数据，而图表会动态计算最新的5组数据。这是使用样例代码中的“OFFSET”公式来实现的:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

您可以尝试将公式中的数字“-5”更改为“-10”，动态图表将计算最新的10组数据。现在我们已成功使用Aspose.Cells创建了一个动态滚动图。
