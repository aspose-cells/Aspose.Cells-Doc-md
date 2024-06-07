---
title: 创建成交量-开-高-低-收盘（VHLC）股票图表
type: docs
weight: 183
url: /zh/java/create-volume-high-low-close-stock-chart/
description: 如何创建一个成交量-最高-最低-收盘(VHLC)股票图表，如何添加一个成交量-最高-最低-收盘(VHLC)股票图表，如何生成一个成交量-最高-最低-收盘(VHLC)股票图表。
keywords: 添加成交量-最高-最低-收盘（VHLC）股票图表，创建成交量-最高-最低-收盘（VHLC）股票图表，生成成交量-最高-最低-收盘（VHLC）股票图表。
---

## **可能的使用场景**
我们将看一下第三种股票图表，即成交量高低收盘图。再次重申必须按正确顺序拥有数据。如果需要重新排列数据表，则应在设置图表之前完成。
该图表在第一列（类别）后立即包括一列成交量，并且图表在主轴上显示该成交量的柱形图，而价格移至次要轴。

![todo:image_alt_text](data.png)
## **成交量-开-高-低-收盘（VHLC）股票图表**

![todo:image_alt_text](sample.png)
## **示例代码**
以下示例代码加载了[sample Excel文件](Volume-High-Low-Close.xlsx)并生成了[output Excel文件](out.xlsx)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-create-volume-high-low-close-stock-chart.java" >}}
