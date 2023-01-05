---
title: 查找数据点是否位于饼图饼图或饼图条形图的第二个饼图或条形图中
type: docs
weight: 180
url: /zh/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
## **可能的使用场景**
您可以找到系列的数据点是否在第二个饼图中*馅饼的馅饼*图表或在栏中*馅饼吧*使用 Aspose.Cells 的图表。请使用[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)属性来确定它。

请下载[示例 excel 文件](5115193.xlsx)在以下示例代码中使用并查看其控制台输出。如果你打开[示例 excel 文件](5115193.xlsx) ，你会发现，所有小于10的数据点都在*馅饼吧*图表也由控制台输出显示。
## **查找数据点是否位于饼图饼图或饼图条形图的第二个饼图或条形图中**
以下示例代码显示如何查找数据点是否在第二个饼图或条形图中*馅饼的馅饼*要么*馅饼吧*图表。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **控制台输出**
请查看执行上述示例代码后生成的以下控制台输出[示例 excel 文件](5115193.xlsx).如果[位于次要情节](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)是**错误的** 数据点在 Pie 内部或者如果它在**真的**那么数据点就在 Bar 里面。



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
