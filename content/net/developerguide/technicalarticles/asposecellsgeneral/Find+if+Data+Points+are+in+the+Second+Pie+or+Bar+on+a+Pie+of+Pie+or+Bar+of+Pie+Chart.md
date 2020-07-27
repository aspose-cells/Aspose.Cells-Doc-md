+++
title = "Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart" 
description = "" 
weight = 16574 
+++

Aspose.Cells for .NET : Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart  

# Aspose.Cells for .NET : Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#FindifDataPointsareintheSecondPieorBaronaPieofPieorBarofPieChart-PossibleUsageScenarios)
*   2 [Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart](#FindifDataPointsareintheSecondPieorBaronaPieofPieorBarofPieChart-FindifDataPointsareintheSecondPieorBaronaPieofPieorBarofPieChart)
*   3 [Console Output](#FindifDataPointsareintheSecondPieorBaronaPieofPieorBarofPieChart-ConsoleOutput)
{{< /panel >}}
 

 

## Possible Usage Scenarios

You can find if data points of series are in the second pie on *Pie of Pie* chart or in the bar of *Bar of Pie* chart using Aspose.Cells. Please use the [ChartPoint.IsInSecondaryPlot](https://apireference.aspose.com/net/cells/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) property to determine it.

Please download the [sample excel file](https://docs2.aspose.com/cells/net/attachments/5024989/5115193.xlsx) used in the following sample code and see its console output. If you open the [sample excel file](https://docs2.aspose.com/cells/net/attachments/5024989/5115193.xlsx), you will find, all the data points which are less than 10 are inside the bar of *Bar of Pie* chart as also shown by console output.

## Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart

The following sample code shows how to find if data points are in the second pie or bar on a *Pie of Pie* or *Bar of Pie* chart.

## Console Output

Please see the following console output generated after the execution of the above sample code with the [sample excel file](https://docs2.aspose.com/cells/net/attachments/5024989/5115193.xlsx). If [IsInSecondaryPlot](https://apireference.aspose.com/net/cells/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) is **false**, the data point is inside the Pie or if it is **true**, then the data point is inside the Bar.

{{< code lang="cs" >}}
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
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [PieBars.xlsx](https://docs2.aspose.com/cells/net/attachments/5024989/5115193.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

