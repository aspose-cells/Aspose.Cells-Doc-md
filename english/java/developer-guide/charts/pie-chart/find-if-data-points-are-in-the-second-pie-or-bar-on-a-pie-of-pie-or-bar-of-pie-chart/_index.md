---
title: Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart
type: docs
weight: 910
url: /java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
You can find if data points of series are in the second pie on *Pie of Pie* chart or in the bar of *Bar of Pie* chart using Aspose.Cells. Please use the [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#isInSecondaryPlot--) property to determine it.

Please download the [sample excel file](5473373.xlsx) used in the following sample code and see its console output. If you open the [sample excel file](5473373.xlsx), you will find, all the data points which are less than 10 are inside the bar of *Bar of Pie* chart as also shown by console output.
## **Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart**
The following sample code shows how to find if data points are in the second pie or bar on a *Pie of Pie* or *Bar of Pie* chart.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **Console Output**
Please see the following console output generated after the execution of the above sample code with the [sample excel file](5473373.xlsx). If [IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#isInSecondaryPlot--) is **false**, the data point is inside the Pie or if it is **true**, then data point is inside the Bar.

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
