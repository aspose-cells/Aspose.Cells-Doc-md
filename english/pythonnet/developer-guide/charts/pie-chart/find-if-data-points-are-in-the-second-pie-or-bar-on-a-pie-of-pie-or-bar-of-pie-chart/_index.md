---
title: Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart
description: Learn how to use Aspose.Cells for Python via .NET to find if data points are in the second pie or bar on a pie of pie or bar of pie chart. Our guide will demonstrate how to identify and access the secondary pie or bar on a composite chart, allowing you to analyze and manipulate the data effectively.
keywords: Aspose.Cells for Python via .NET, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.
type: docs
weight: 180
url: /python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
You can determine whether data points of a series are in the second pie of a *Pie of Pie* chart or in the bar of a *Bar of Pie* chart using Aspose.Cells for Python via .NET. Please use the [ChartPoint.is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot) property to determine this.

Please download the [sample Excel file](5115193.xlsx) used in the following sample code and see its console output. If you open the [sample Excel file](5115193.xlsx), you will find that all data points less than 10 are inside the bar of a *Bar of Pie* chart, as also shown by the console output.

## **Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart**
The following sample code shows how to find if data points are in the second pie or bar on a *Pie of Pie* or *Bar of Pie* chart.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindDataPointsInPieBar.py" >}}
## **Console Output**
Please see the following console output generated after the execution of the above sample code with the [sample Excel file](5115193.xlsx). If [is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot/) is **false**, the data point is inside the pie; if it is **true**, then the data point is inside the bar.

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
