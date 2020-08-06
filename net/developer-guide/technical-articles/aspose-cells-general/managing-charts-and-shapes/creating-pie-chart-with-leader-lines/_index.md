---
title: Creating Pie Chart with Leader Lines
type: docs
weight: 180
url: /net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}} 

This article explains how to create a pie chart with leader lines from scratch while using Aspose.Cells for .NET API. In Excel, the 'Show leader lines' option is set by default so when you create a pie chart in Excel the leader lines are shown. However, while creating a similar chart with Aspose.Cells APIs, you have to explicitly set the [Series.HasLeaderLines](https://apireference.aspose.com/net/cells/aspose.cells.charts/series/properties/hasleaderlines) property.

{{% /alert %}} 

To demonstrate the usage of Aspose.Cells for .NET API to create a pie chart with leader lines, we will first create a new [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) and input some data that will serve as the series data source. Once the data is in place, we will add a [Chart](https://apireference.aspose.com/net/cells/aspose.cells.charts/chart) of type [ChartType.Pie](https://apireference.aspose.com/net/cells/aspose.cells.charts/charttype) to the collection of charts and set its different aspects to get the desired chart view.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}



So far we have created a pie chart and set its different aspects. Now we are going to turn on the leader lines for the chart. Please note, to show the leader lines, we have to move the data labels a little.

The following piece of code turns on the leader lines, refresh the chart, and then calculates the data labels' positions to move them accordingly.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}


Finally, the following code saves the chart in image format and the workbook in XLSX format.



{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Resultant Pie Chart**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

