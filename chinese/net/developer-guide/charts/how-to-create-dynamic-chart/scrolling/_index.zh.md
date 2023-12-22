---
title: 如何创建动态滚动图表
description: 了解如何使用 Aspose.Cells for .NET 创建动态滚动图表。我们的分步指南将演示如何在图表中实现平滑的数据转换和自动滚动，以实现连续和更新的显示。
keywords: Aspose.Cells for .NET, Dynamic Scrolling Chart, Data Transitions, Smooth Scrolling, Continuous Display, Updating Visualization.
type: docs
weight: 75
url: /zh/net/create-dynamic-scrolling-chart/
---
##  **可能的使用场景**
动态滚动图表是一种图形表示形式，用于显示随时间变化的数据。它旨在提供实时数据视图，允许用户跟踪持续更新和趋势。随着新数据的添加，图表不断更新，并自动滚动以显示最新信息。

动态滚动图表通常用于各个行业，例如金融、股市分析、天气跟踪和社交媒体分析。它们使用户能够可视化和分析数据模式，并根据实时信息做出明智的决策。

这些图表通常是交互式的，允许用户放大或缩小、滚动历史数据以及调整时间间隔。它们通常支持多个数据系列，提供不同指标及其相关性的全面视图。

总体而言，动态滚动图表是监测和分析时序数据、促进实时决策、增强数据可视化能力的宝贵工具。

##  **使用 Aspose Cells 创建动态滚动图表**
在接下来的段落中，我们将向您展示如何使用 Aspose.Cells 创建动态滚动图表。我们将向您展示该示例的代码，以及使用此代码创建的 Excel 文件。

##  **示例代码**
以下示例代码将生成[动态滚动图表文件](DynamicScrollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-scrolling-chart.cs" >}}

##  **笔记**
在生成的文件中，可以对滚动条进行操作，同时图表动态统计最新10组数据。这是使用示例代码中的“OFFSET”公式完成的：

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

您可以尝试将“Sheet1!$H$20”单元格中的数字“10”更改为“15”，动态图表将统计最新的15组数据。现在我们已经成功使用Aspose.Cells创建了一个动态滚动图表。
