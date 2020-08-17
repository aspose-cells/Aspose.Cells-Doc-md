---
title: Read Axis Labels after Calculating the Chart
type: docs
weight: 130
url: /net/read-axis-labels-after-calculating-the-chart/
---

## **Possible Usage Scenarios**
You can read axis labels of your chart after calculating its values using the [Chart.Calculate()](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/calculate) method. Please use the [Axis.AxisLabels](https://apireference.aspose.com/cells/net/aspose.cells.charts/axis/properties/axislabels) property for this purpose that will return the list of axis labels.
## **Read Axis Labels after Calculating the Chart**
Please see the following sample code that loads the [sample Excel file](64716803.xlsx) and reads the category axis labels of the chart in the first worksheet. It then prints the values of the axis labels on the console. Please see the console output of the sample code given below for a reference.
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}
## **Console Output**
{{< highlight java >}}

 Category Axis Labels: 

---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
