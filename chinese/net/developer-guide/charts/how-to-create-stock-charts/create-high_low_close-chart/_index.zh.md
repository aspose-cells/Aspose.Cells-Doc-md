---
title: 创建高低收盘 (HLC) 股票图表
description: 了解如何使用 Aspose.Cells for .NET 创建股价高低收盘图表。我们的分步指南将演示如何将股票市场数据（包括最高价、最低价和收盘价）绘制到图表上，以便更好地分析和可视化。
keywords: Aspose.Cells for .NET, High-Low-Close Stock Chart, Stock Market Data, Analysis, Visualization.
type: docs
weight: 181
url: /zh/net/create-high-low-close-stock-chart/
---
##  **可能的使用场景**
高-低-收盘价 (HLC) 股票图表使用四列数据。第一列是类别，通常是日期，但也可以使用股票名称。接下来的三列按顺序分别是最高价、最低价和收盘价。每个类别的价格范围由从低到高的垂直线表示，收盘价使用延伸到该线右侧的刻度线显示。

![待办事项：图像_替代_文本](sample.png)
##  **图表中的可见性改进**
有时，为了使图表看起来更直观，我们可以修改标记的外观（关闭），或者使其显示在辅助轴上。

![待办事项：图像_替代_文本](sample2.png)
##  **示例代码**
以下示例代码加载[Excel 文件示例](High-Low-Close.xlsx)并生成[输出Excel文件](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-high-low-close-stock-chart.cs" >}}
