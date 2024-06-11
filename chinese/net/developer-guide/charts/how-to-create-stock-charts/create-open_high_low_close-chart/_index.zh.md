---
title: 创建开-高-低-收（OHLC）股票图表
description: 使用 Aspose.Cells for .NET 学习如何创建开盘高低收盘股票图表。我们的指南将演示如何将股票市场数据，包括开盘、最高、最低和收盘价格，绘制到图表上，以便进行更好的分析和可视化。
keywords: Aspose.Cells for .NET, 开盘高低收盘股票图表, 股票市场数据, 分析, 可视化。
type: docs
weight: 182
url: /zh/net/create-open-high-low-close-stock-chart/
---

## **可能的使用场景**
开-高-低-收（OHLC）图表使用五列数据，分别是类别、开盘、最高、最低和收盘。每个类别的价格范围再次通过垂直线表示，开盘价格和收盘价格之间的范围由一个更宽的浮动条表示；如果该类别的价格上升（收盘价高于开盘价），则该条将填充一种颜色，而如果价格下降，则用另一种颜色填充。这种图表通常被称为蜡烛图。

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **图表的可见性改进**
我们经常使用颜色而不是黑白来表示价格的涨跌。在下面的第一组蜡烛图中，红色显示上涨，绿色表示下跌。

![todo:image_alt_text](sample2.png)
## **示例代码**
以下示例代码加载了【示例Excel文件】(Open-High-Low-Close.xlsx)，并生成了【输出Excel文件】(out.xlsx)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}
