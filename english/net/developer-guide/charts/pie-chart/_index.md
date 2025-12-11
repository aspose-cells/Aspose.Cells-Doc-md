---
title: Creating Pie Chart with Leader Lines
description: Learn how to use Aspose.Cells for .NET to create a pie chart with leader lines in Microsoft Excel. Our guide will demonstrate how to add leader lines that connect data points to the legend and enhance the overall clarity of your chart.
keywords: Aspose.Cells for .NET, Pie Chart, Leader Lines, Microsoft Excel, Data Visualization, Chart Customization.
linktitle: Pie Chart
type: docs
weight: 45
url: /net/creating-pie-chart-with-leader-lines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This article explains how to create a pie chart with leader lines from scratch while using the Aspose.Cells for .NET API. In Excel, the **'Show leader lines'** option is set by default, so when you create a pie chart in Excel the leader lines are shown. However, while creating a similar chart with Aspose.Cells APIs, you have to explicitly set the [**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) property.

{{% /alert %}}

To demonstrate the usage of Aspose.Cells for .NET API to create a pie chart with leader lines, we will first create a new [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) and input some data that will serve as the series data source. Once the data is in place, we will add a [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) of type [**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) to the collection of charts and set its different aspects to get the desired chart view.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

So far we have created a pie chart and set its different aspects. Now we are going to turn on the leader lines for the chart. Please note that to show the leader lines, we have to move the data labels a little.

The following piece of code turns on the leader lines, **refreshes** the chart, and then calculates the data labels' positions to move them accordingly.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Finally, the following code saves the chart in image format and the workbook in XLSX format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Resultant Pie Chart**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Advanced topics**
- [Custom Slice or Sector Colors in Pie Chart](/cells/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart](/cells/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Related Articles

- [Creating Charts](/cells/net/creating-charts/)
- [Customizing Charts](/cells/net/customizing-charts/)
- [Data Formatting in Charts](/cells/net/data-formatting-in-charts/)
- [Setting Chart Appearance](/cells/net/setting-chart-appearance/)

{{< app/cells/assistant language="csharp" >}}
