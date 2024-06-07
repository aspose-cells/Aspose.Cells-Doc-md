---
title: 查找数据点是否在饼状图的第二个饼图或条形图上。
description: 学习如何使用Aspose.Cells for .NET查找数据点是否在饼图的第二个饼图或条形图上。我们的指南将演示如何识别并访问复合图表上的次要饼图或条形图，从而使您能够有效分析和操作数据。
keywords: Aspose.Cells for .NET, 饼中饼图, 条中饼图, 次要饼图, 次要条形图, 数据分析, 数据操作。
type: docs
weight: 180
url: /zh/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **可能的使用场景**
您可以通过Aspose.Cells找出系列的数据点是否在 *饼中饼* 图表的第二个饼中或在 *条中饼* 图表中的条内。请使用 [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) 属性来确定。

请下载以下示例代码中使用的 [样本Excel文件](5115193.xlsx) 并查看其控制台输出。如果您打开 [样本Excel文件](5115193.xlsx)，您会发现所有小于10的数据点都在 *条中饼* 图的内部，如控制台输出所示。
## **查找在饼图或饼图的第二个饼或柱中的数据点**
以下示例代码展示如何查找数据点是否在 *饼中饼* 或 *条中饼* 图的第二个饼图或条图上。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **控制台输出**
请查看执行上述示例代码后生成的以下控制台输出及 [样本Excel文件](5115193.xlsx)。如果 [IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) 为 **false**，数据点在饼图内；如果为 **true**，数据点在条中。



{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
