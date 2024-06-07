---
title: 创建开盘高低收(OHLC)股票图表
description: 学习如何使用Aspose.Cells for .NET创建开高低收盘股票图表。我们的指南将演示如何将股市数据，包括开盘价、最高价、最低价和收盘价，绘制到图表上，以进行更好的分析和可视化。
keywords: Aspose.Cells for .NET，开高低收盘股票图表，股市数据，分析，可视化。
type: docs
weight: 182
url: /zh/net/create-open-high-low-close-stock-chart/
---

## **可能的使用场景**
开高低收盘（OHLC）图表使用五列数据，顺序为：类别、开盘价、最高价、最低价和收盘价。每个类别的价格范围再次由竖直线表示，而开盘价和收盘价之间的范围由更宽的浮动条表示；如果某个类别的价格上涨（收盘价高于开盘价），则条形图填充一种颜色，而如果价格下降，则条形图填充另一种颜色。这种类型的图表通常被称为蜡烛图。

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **图表中的可见性改进**
我们通常使用颜色而不是黑白来表示价格的涨跌。在下面的第一组蜡烛图中，红色表示价格上涨，绿色表示价格下跌。

![todo:image_alt_text](sample2.png)
## **示例代码**
以下示例代码加载了[sample Excel文件](Open-High-Low-Close.xlsx)并生成了[output Excel文件](out.xlsx)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}
