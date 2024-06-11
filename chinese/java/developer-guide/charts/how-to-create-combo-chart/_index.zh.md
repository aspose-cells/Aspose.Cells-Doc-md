---
title: 如何创建组合图表
type: docs
weight: 73
url: /zh/java/create-combo-chart/
description: 如何创建组合图表，如何将股票图表与线图表合并，如何生成组合图表。
keywords: 添加组合图表，创建股票图表与线图表，生成组合图表，添加股票图表与线图表。
---

## **可能的使用场景**
Excel中的组合图表让您能够利用此选项，因为您可以轻松地组合两种或更多种图表类型，以使您的数据易于理解。当您的数据包含多种值（包括价格和交易量）时，组合图表是有用的。此外，当您的数据数字在系列之间有明显变化时，组合图表是可行的。
以以下数据集为例，我们可以观察到这些数据与[**VHCL**](https://docs.aspose.com/cells/java/create-volume-high-low-close-stock-chart/)中提到的数据相当相似。如果我们希望将与“总收入”对应的series0可视化为线图表，应该如何操作？

![todo:image_alt_text](sample.png)
## **组合图表**
运行以下代码后，您将看到下面展示的组合图表。

![todo:image_alt_text](result.png)
## **示例代码**
以下示例代码加载了[示例Excel文件](combo.xlsx)并生成了[输出Excel文件](out.xlsx)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-add-combo-chart.java" >}}
