---
title: Get Worksheet of the Chart
type: docs
weight: 90
url: /net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Sometimes, you want to access a worksheet from a chart's reference. Aspose.Cells provides the [**Chart.Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet) property which returns the reference of the worksheet that contains the chart.

{{% /alert %}}

The following example shows how to use the [**Chart.Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet) property. The code first prints the name of the worksheet, then accesses the first chart on the worksheet. It then prints the worksheet name again, using the [**Chart.Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetWorksheetOfTheChart-GetWorksheetOfTheChart.cs" >}}

Below is the console output that the sample code results in. As you can see, it prints the same worksheet name both times.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
