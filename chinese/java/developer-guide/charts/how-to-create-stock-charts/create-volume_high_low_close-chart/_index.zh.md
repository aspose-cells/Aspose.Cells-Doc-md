---
title: 创建成交量高低收（VHLC）股票图表
type: docs
weight: 183
url: /zh/java/create-volume-high-low-close-stock-chart/
description: 如何创建成交量高低收（VHLC）股票图表，如何添加成交量高低收（VHLC）股票图表， 如何生成成交量高低收（VHLC）股票图表。
keywords: 添加成交量高低收（VHLC）股票图表， 创建成交量高低收（VHLC）股票图表， 生成成交量高低收（VHLC）股票图表。
---

## **可能的使用场景**
我们将讨论的第三种股票图表是成交量高低收图。再次重申，必须确保数据顺序正确。如果需要重新排列数据表，应在设置图表之前进行。
此图表包括一个立即在第一个（类别）列之后的成交量列，并且图表在主轴上显示此成交量的柱形图，而价格则移至次要轴。

![todo:image_alt_text](data.png)
## **成交量高低收（VHLC）股票图表**

![todo:image_alt_text](sample.png)
## **示例代码**
以下示例代码加载了 [样本Excel文件](Volume-High-Low-Close.xlsx) 并生成了 [输出Excel文件](out.xlsx)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-create-volume-high-low-close-stock-chart.java" >}}
