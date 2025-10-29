---
title: 查找数据点是否在饼图的第二个饼图或柱状图的柱状图上
description: 了解如何使用Aspose.Cells for Python via .NET查找数据点是否位于派的第二个饼或条形图中。我们的指南将演示如何识别和访问复合图表中的次级饼或条，帮助您有效分析和操作数据。
keywords: Aspose.Cells for Python via .NET，Pie of Pie图表，Bar of Pie图表，次级饼，次级条，数据分析，数据操作。
type: docs
weight: 180
url: /zh/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **可能的使用场景**
您可以使用Aspose.Cells for Python via .NET判断系列的数据点是否位于*Pie of Pie*图表的第二个饼或*Bar of Pie*图表的条中。请使用[ChartPoint.is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot)属性进行判断。

请下载以下示例代码中使用的[样本excel文件](5115193.xlsx)，并查看其控制台输出。如果您打开[样本excel文件](5115193.xlsx)，您会发现所有小于10的数据点都在*饼图的柱状图*中，正如控制台输出所示。

## **查找数据点是否在饼图的第二个饼图或柱状图的柱状图上**
以下示例代码显示了如何查看数据点是否在*饼图*的第二个饼图上，或者在*柱状图*的柱状图上。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindDataPointsInPieBar.py" >}}
## **控制台输出**
请查看运行上述示例代码后生成的控制台输出（使用[示例Excel文件](5115193.xlsx)）。如果[is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot/)为**false**，则数据点在饼中；如果为**true**，则在条中。



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
{{< app/cells/assistant language="python-net" >}}
