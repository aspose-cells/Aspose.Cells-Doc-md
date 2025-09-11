---
title: Read Axis Labels after Calculating the Chart
description: Learn how to read axis labels in Aspose.Cells for Python via .NET after calculating the chart. Our guide will show you how to access and retrieve axis labels, including their formatting and positioning.
keywords: Aspose.Cells for Python via .NET, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning.
type: docs
weight: 90
url: /python-net/read-axis-labels-after-calculating-the-chart/
---

## **Possible Usage Scenarios**

You can read axis labels of your chart after calculating its values using the [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/) method. Please use the [**Axis.get_axis_texts()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis/get_axis_texts) method for this purpose that will return the list of axis labels.

## **Read Axis Labels after Calculating the Chart**

Please see the following sample code that loads the [sample Excel file](ReadAxisLabels.xlsx) and reads the category axis labels of the chart in the first worksheet. It then prints the values of the axis labels on the console. Please see the console output of the sample code given below for a reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ReadAxisLabelsAfterCalculatingTheChart.py" >}}

## **Console Output**

{{< highlight csharp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}