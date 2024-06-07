---
title: 查找数据点是否在饼状图的第二个饼图或条形图上。
type: docs
weight: 910
url: /zh/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **可能的使用场景**
您可以使用Aspose.Cells查找系列的数据点是否在第二个饼图中的*饼图*或在*饼状柱*图中。请使用[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot)属性来确定。

请下载以下示例代码中使用的[sample excel file](5473373.xlsx)并查看其控制台输出。如果您打开[sample excel file](5473373.xlsx)，您将发现所有小于10的数据点都在*饼状柱*图的内部，正如控制台输出所示。
## **查找在饼图或饼图的第二个饼或柱中的数据点**
以下示例代码展示如何查找数据点是否在 *饼中饼* 或 *条中饼* 图的第二个饼图或条图上。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **控制台输出**
请在执行上述示例代码后查看生成的[console output](5473373.xlsx)。如果[IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot)为**false**，则数据点在饼图内部，如果为**true**，则数据点在柱状图内。

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
