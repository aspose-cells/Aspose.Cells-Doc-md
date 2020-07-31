---
title : "Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart" 
description : "" 
weight : 12558 
toc : false
type: docs
url: /java/developerguide/technicalarticles/find+if+data+points+are+in+the+second+pie+or+bar+on+a+pie+of+pie+or+bar+of+pie+chart/
---

# Aspose.Cells for Java : Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart](#find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart)
*   3 [Console Output](#console-output)
{{< /panel >}}
 

 


## Possible Usage Scenarios

You can find if data points of series are in the second pie on *Pie of Pie* chart or in the bar of *Bar of Pie* chart using Aspose.Cells. Please use the [ChartPoint.IsInSecondaryPlot](https://apireference.aspose.com/java/cells/com.aspose.cells/chartpoint#IsInSecondaryPlot) property to determine it.

Please download the [sample excel file](https://docs2.aspose.com/cells/java/attachments/5276184/5473373.xlsx) used in the following sample code and see its console output. If you open the [sample excel file](https://docs2.aspose.com/cells/java/attachments/5276184/5473373.xlsx), you will find, all the data points which are less than 10 are inside the bar of *Bar of Pie* chart as also shown by console output.

## Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart

The following sample code shows how to find if data points are in the second pie or bar on a *Pie of Pie* or *Bar of Pie* chart.

## Console Output

Please see the following console output generated after the execution of the above sample code with the [sample excel file](https://docs2.aspose.com/cells/java/attachments/5276184/5473373.xlsx). If [IsInSecondaryPlot](https://apireference.aspose.com/java/cells/com.aspose.cells/chartpoint#IsInSecondaryPlot) is **false**, the data point is inside the Pie or if it is **true**, then data point is inside the Bar.

{{< code lang="cs" >}}
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
{{< /code >}}

