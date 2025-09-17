##Creating Pie Chart with Leader Lines
Learn how to use Aspose.Cells for Python via .NET to create a pie chart with leader lines in Microsoft Excel. Our guide will demonstrate how to add leader lines that connect data points to the legend and enhance the overall clarity of your chart.
This article explains how to create a pie chart with leader lines from scratch while using Aspose.Cells for Python via .NET API. In Excel, the 'Show leader lines' option is set by default so when you create a pie chart in Excel the leader lines are shown. However, while creating a similar chart with Aspose.Cells for Python via .NET APIs, you have to explicitly set the [**Series.has_leader_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/has_leader_lines) property.
To demonstrate the usage of Aspose.Cells for Python via .NET API to create a pie chart with leader lines, we will first create a new [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) and input some data that will serve as the series data source. Once the data is in place, we will add a [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) of type [**ChartType.PIE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) to the collection of charts and set its different aspects to get the desired chart view.
So far we have created a pie chart and set its different aspects. Now we are going to turn on the leader lines for the chart. Please note, to show the leader lines, we have to move the data labels a little.
The following piece of code turns on the leader lines, refresh the chart, and then calculates the data labels' positions to move them accordingly.
Finally, the following code saves the chart in image format and the workbook in XLSX format.
|**Resultant Pie Chart**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|
## **Advance topics**
- [Custom Slice or Sector Colors in Pie Chart](https://docs.aspose.com/cells/python-net/custom-slice-or-sector-colors-in-pie-chart/)
- [Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart](https://docs.aspose.com/cells/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)
## Related Articles
- [Creating Charts](https://docs.aspose.com/cells/python-net/creating-charts/)
- [Cusomizing Charts](https://docs.aspose.com/cells/python-net/customizing-charts/)
- [Data Formatting in Charts](https://docs.aspose.com/cells/python-net/data-formatting-in-charts/)
- [Setting Chart Appearance](https://docs.aspose.com/cells/python-net/setting-chart-appearance/)
