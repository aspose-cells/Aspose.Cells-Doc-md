---
title: 查找数据点是否位于饼图或饼图条形图中的第二个饼图或条形图中
description: 了解如何使用 Aspose.Cells for .NET 查找数据点是否位于饼图或饼图条形图的第二个饼图或条形图中。我们的指南将演示如何识别和访问复合图表上的辅助饼图或条形图，使您能够有效地分析和操作数据。
keywords: Aspose.Cells for .NET, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.
type: docs
weight: 180
url: /zh/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
##  **可能的使用场景**
您可以找到系列的数据点是否在第二个饼图中*馅饼的馅饼*图表或栏中*馅饼吧*图表使用 Aspose.Cells。请使用[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)属性来确定它。

请下载[示例 Excel 文件](5115193.xlsx)在以下示例代码中使用并查看其控制台输出。如果您打开[示例 Excel 文件](5115193.xlsx)，你会发现，所有小于10的数据点都在*馅饼吧*控制台输出也显示了图表。
##  **查找数据点是否位于饼图或饼图条形图中的第二个饼图或条形图中**
以下示例代码演示了如何查找数据点是否位于第二个饼图或条形图中*馅饼的馅饼*或者*馅饼吧*图表。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
##  **控制台输出**
请参阅执行上述示例代码后生成的以下控制台输出：[示例 Excel 文件](5115193.xlsx) 。如果[是次要情节](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)为 *false**，则数据点位于 Pie 内部；如果为 *true**，则数据点位于 Bar 内部。



{{< highlight "java" >}}

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
