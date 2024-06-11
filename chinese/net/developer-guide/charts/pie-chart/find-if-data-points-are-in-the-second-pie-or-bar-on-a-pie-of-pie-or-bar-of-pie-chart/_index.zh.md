---
title: 查找数据点是否在饼图的第二个饼图或柱状图的柱状图上
description: 学习如何使用 Aspose.Cells for .NET 查找属于饼图或条形图上第二个饼图或条形图的数据点。我们的指南将演示如何识别和访问复合图表上的第二个饼图或条形图，从而能够有效分析和操作数据。
keywords: Aspose.Cells for .NET, 饼图的饼图, 条形图的饼图, 第二个饼图, 第二个条形图, 数据分析, 数据操作。
type: docs
weight: 180
url: /zh/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **可能的使用场景**
您可以使用Aspose.Cells来查找系列的数据点是否位于*饼图的饼图*或者*条状饼图*的第二个饼图中。请使用[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)属性来确定。

请下载以下示例代码中使用的[样本excel文件](5115193.xlsx)，并查看其控制台输出。如果您打开[样本excel文件](5115193.xlsx)，您会发现所有小于10的数据点都在*饼图的柱状图*中，正如控制台输出所示。
## **查找数据点是否在饼图的第二个饼图或柱状图的柱状图上**
以下示例代码显示了如何查看数据点是否在*饼图*的第二个饼图上，或者在*柱状图*的柱状图上。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **控制台输出**
请查看执行上述示例代码后生成的以下控制台输出，配合[样本excel文件](5115193.xlsx)。如果[IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)为**false**，则数据点在饼图内，如果为**true**，则数据点在柱状图内。



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
