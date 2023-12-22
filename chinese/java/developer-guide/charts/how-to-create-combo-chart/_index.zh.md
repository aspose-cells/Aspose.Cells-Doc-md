---
title: 如何创建组合图
type: docs
weight: 73
url: /zh/java/create-combo-chart/
description: 如何创建组合图，如何添加股票图和折线图，如何生成组合图。
keywords: Add combo chart, Create stock chart with line chart, Generate combo chart, add stock chart with line chart.
---
##  **可能的使用场景**
Excel 中的组合图表让您可以利用此选项，因为您可以轻松组合两种或多种图表类型以使数据易于理解。当您的数据包含多种值（包括价格和数量）时，组合图非常有用。此外，当您的数据数量在系列之间变化很大时，组合图是可行的。
以下面的数据集为例，我们可以观察到这些数据与中提到的数据非常相似[**VHCL**](https://docs.aspose.com/cells/java/create-volume-high-low-close-stock-chart/)。如果我们想将对应于“总收入”的Series0可视化为折线图，我们应该如何进行？

![待办事项：图像_替代_文本](sample.png)
##  **组合图**
运行下面的代码后，您将看到如下所示的组合图。

![待办事项：图像_替代_文本](result.png)
##  **示例代码**
以下示例代码加载[Excel 文件示例](combo.xlsx)并生成[输出Excel文件](out.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-add-combo-chart.java" >}}
