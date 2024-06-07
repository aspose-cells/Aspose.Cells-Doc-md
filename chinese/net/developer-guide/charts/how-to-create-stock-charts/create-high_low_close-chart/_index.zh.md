---
title: 创建高低收(HLC)股票图表
description: 学习如何使用Aspose.Cells for .NET创建高低收股票图表。我们的逐步指南将演示如何绘制股市数据，包括高、低和收盘价格，到图表中以进行更好的分析和可视化。
keywords: Aspose.Cells for .NET，高低收股票图表，股票市场数据，分析，可视化。
type: docs
weight: 181
url: /zh/net/create-high-low-close-stock-chart/
---

## **可能的使用场景**
高低收（HLC）股票图表使用四列数据。第一列是一个类别，通常是日期，但也可以使用股票名称。接下来的三列依次是高、低和收盘价格。每个类别的价格范围由从低到高的垂直线表示，收盘价格使用延伸到这条线右侧的刻度线显示。

![todo:image_alt_text](sample.png)
## **图表中的可见性改进**
有时，为了使图表看起来更直观，我们可以修改标记（收盘价）的外观，或者使其显示在次要轴上。

![todo:image_alt_text](sample2.png)
## **示例代码**
以下示例代码加载[示例Excel文件](High-Low-Close.xlsx)，并生成[输出Excel文件](out.xlsx)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-high-low-close-stock-chart.cs" >}}
