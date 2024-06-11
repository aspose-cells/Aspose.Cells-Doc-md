---
title: 创建高低收（HLC）股票图表
description: 使用 Aspose.Cells for .NET 学习如何创建高低收盘股票图表。我们的分步指南将演示如何将股票市场数据，包括最高、最低和收盘价格，绘制到图表上，以便进行更好的分析和可视化。
keywords: Aspose.Cells for .NET, 高低收盘股票图表, 股票市场数据, 分析, 可视化。
type: docs
weight: 181
url: /zh/net/create-high-low-close-stock-chart/
---

## **可能的使用场景**
高低收（HLC）股票图表使用四列数据。第一列通常是类别，通常是日期，但也可以使用股票名称。接下来的三列分别表示最高、最低和收盘价格。每个类别价格范围通过垂直线来表示，收盘价格则使用延伸至该线右侧的刻度线显示。

![todo:image_alt_text](sample.png)
## **图表的可见性改进**
有时，为了使图表看起来更直观，我们可以修改标记（收盘价）的外观，或者在辅助轴上显示它。

![todo:image_alt_text](sample2.png)
## **示例代码**
以下示例代码加载[示例Excel文件](High-Low-Close.xlsx)并生成[输出Excel文件](out.xlsx)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-high-low-close-stock-chart.cs" >}}
