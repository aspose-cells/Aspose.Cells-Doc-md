---
title: 创建成交量-高-低-收盘价(VHLC) 股票图表
type: docs
weight: 183
url: /zh/java/create-volume-high-low-close-stock-chart/
description: 如何创建成交量高低收盘 (VHLC) 股票图表、如何添加成交量高低收盘 (VHLC) 股票图表、如何生成成交量高低收盘 (VHLC) 股票图表。
keywords: Add Volume-High-Low-Close(VHLC) Stock Chart, Create Volume-High-Low-Close(VHLC) Stock Chart, Generate Volume-High-Low-Close(VHLC) Stock Chart.
---
##  **可能的使用场景**
我们要查看的第三个股票图表是成交量高低收盘图。再次强调，数据必须按正确的顺序排列，这一点很重要。如果您需要重新排列数据表，您应该在设置图表之前执行此操作。
该图表在第一个（类别）列之后立即包含一个交易量列，并且该图表在主轴上包含一个显示该交易量的柱形图，而价格则移至次轴。

![待办事项：图像_替代_文本](data.png)
##  **成交量-高-低-收盘价 (VHLC) 股票图表**

![待办事项：图像_替代_文本](sample.png)
##  **示例代码**
以下示例代码加载[Excel 文件示例](Volume-High-Low-Close.xlsx)并生成[输出Excel文件](out.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-create-volume-high-low-close-stock-chart.java" >}}
