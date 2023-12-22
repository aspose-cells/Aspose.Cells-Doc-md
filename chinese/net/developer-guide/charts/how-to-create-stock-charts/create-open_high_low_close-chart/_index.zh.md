---
title: 创建开盘-最高-最低-收盘 (OHLC) 股票图表
description: 了解如何使用 Aspose.Cells for .NET 创建开盘-最高-最低-收盘股票图表。我们的指南将演示如何将股票市场数据（包括开盘价、最高价、最低价和收盘价）绘制到图表上，以便更好地分析和可视化。
keywords: Aspose.Cells for .NET, Open-High-Low-Close Stock Chart, Stock Market Data, Analysis, Visualization.
type: docs
weight: 182
url: /zh/net/create-open-high-low-close-stock-chart/
---
##  **可能的使用场景**
开盘价-最高价-最低价-收盘价 (OHLC) 图表使用五列数据，按顺序排列：类别、开盘价、最高价、最低价和收盘价。每个类别的价格范围再次由垂直线表示，而开盘价和收盘价之间的范围由更宽的浮动条给出；如果类别中的价格上涨（收盘价高于开盘价），则条形会填充一种颜色，而如果价格下降，则条形会填充另一种颜色。这种类型的图表通常称为烛台图。

![待办事项：图像_替代_文本](data.png)

![待办事项：图像_替代_文本](sample.png)
##  **图表中的可见性改进**
我们经常使用颜色而不是黑白来表示价格的上涨和下跌。在下面的第一组烛台中，红色表示价格上涨，绿色表示价格下降。

![待办事项：图像_替代_文本](sample2.png)
##  **示例代码**
以下示例代码加载[Excel 文件示例](Open-High-Low-Close.xlsx)并生成[输出Excel文件](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}
