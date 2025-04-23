---
title: 查找数据点是否在饼图的第二个饼图或柱状图的柱状图上
type: docs
weight: 910
url: /zh/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **可能的使用场景**
您可以使用 Aspose.Cells 来查看系列的数据点是否在 *饼图* 的第二个饼图中，或者在 *柱状图* 的柱状图中。请使用 [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) 属性来确定它。

请下载以下示例代码中使用的[示例 Excel 文件](5473373.xlsx)，并查看其控制台输出。如果打开[示例 Excel 文件](5473373.xlsx)，您将会发现，所有小于 10 的数据点都位于*柱状图*中，如控制台输出所示。
## **查找数据点是否在饼图的第二个饼图或柱状图的柱状图上**
以下示例代码显示了如何查看数据点是否在*饼图*的第二个饼图上，或者在*柱状图*的柱状图上。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **控制台输出**
请查看执行上述示例代码并使用[示例 Excel 文件](5473373.xlsx)后生成的以下控制台输出。如果 [IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) 为 false，则数据点位于饼图内；如果为 true，则数据点位于柱状图内。

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: false

Value: 9

IsInSecondaryPlot: true

Value: 2

IsInSecondaryPlot: true

Value: 40

IsInSecondaryPlot: false

Value: 5

IsInSecondaryPlot: true

Value: 4

IsInSecondaryPlot: true

Value: 25

IsInSecondaryPlot: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
