---
title: Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart with Golang via C++
linktitle: Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart
description: Learn how to use Aspose.Cells for C++ to find if data points are in the second pie or bar on a pie of pie or bar of pie chart. Our guide will demonstrate how to identify and access the secondary pie or bar on a composite chart, allowing you to analyze and manipulate the data effectively.
keywords: Aspose.Cells for C++, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.
type: docs
weight: 180
url: /go-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Possible Usage Scenarios**
You can find if data points of a series are in the second pie on a *Pie of Pie* chart or in the bar of a *Bar of Pie* chart using Aspose.Cells. Please use the [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/go-cpp/chartpoint/isinsecondaryplot/) property to determine this.

Please download the [sample excel file](5115193.xlsx) used in the following sample code and see its console output. If you open the sample Excel file, you will find that all data points less than 10 are inside the bar of the *Bar of Pie* chart, as also shown by the console output.

## **Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart**
The following sample code shows how to find if data points are in the second pie or bar on a *Pie of Pie* or *Bar of Pie* chart.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfDataPointsAreInTheSecondPieOrBarOnAPieOfPieOrBarOfPieChart.go" >}}
## **Console Output**
Please see the following console output generated after executing the above sample code with the sample Excel file. If [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) is **false**, the data point is inside the pie; if it is **true**, the data point is inside the bar.

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