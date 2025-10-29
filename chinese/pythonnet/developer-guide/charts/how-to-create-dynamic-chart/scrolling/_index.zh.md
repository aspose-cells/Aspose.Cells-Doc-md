---
title: 如何创建动态滚动图表
description: 学习如何使用 Aspose.Cells for Python via .NET 创建动态滚动图表。我们的逐步指南将演示如何在图表中实现平滑数据过渡和自动滚动，从而实现连续且更新的显示。
keywords: Aspose.Cells for Python via .NET，动态滚动图表，数据过渡，平滑滚动，连续显示，更新可视化。
type: docs
weight: 75
url: /zh/python-net/create-dynamic-scrolling-chart/
---

## **可能的使用场景**
动态滚动图表是一种用于显示随时间变化的数据的图形表示类型。它旨在实时显示数据，使用户能够追踪连续的更新和趋势。随着新增数据的加入，图表将持续更新并自动滚动，以显示最新的信息。

动态滚动图表通常在各个行业中被广泛使用，如金融、股市分析、天气跟踪和社交媒体分析。它们使用户能够可视化和分析数据模式，并基于实时信息做出明智的决策。

这些图表通常是交互式的，允许用户放大或缩小、滚动历史数据和调整时间间隔。它们通常支持多个数据系列，提供不同指标及其相关性的综合视图。

总的来说，动态滚动图表是用于监控和分析时间序列数据的有价值的工具，有助于实时决策和增强数据可视化能力。

## **使用 Aspose.Cells for Python via .NET 创建动态滚动图表**
在接下来的段落中，我们将向您展示如何使用 Aspose.Cells for Python via .NET 创建动态滚动图表。我们会提供示例代码以及用此代码生成的 Excel 文件。

## **示例代码**
以下示例代码将生成[动态滚动图表文件](DynamicScrollingChart.xlsx)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-dynamic-scrolling-chart.py" >}}

## **备注**
在生成的文件中，您可以操作滚动条，而图表会动态计算最新的10组数据。这是在示例代码中使用“OFFSET”公式完成的：

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

您可以尝试将单元格 "Sheet1!$H$20" 中的数字 "10" 改为 "15"，动态图表会显示最新的 15 组数据。现在我们已经成功使用 Aspose.Cells for Python via .NET 创建了动态滚动图表。
{{< app/cells/assistant language="python-net" >}}
