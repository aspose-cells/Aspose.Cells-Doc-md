---
title: Find Type of X and Y Values of Points in Chart Series
description: Learn how to determine the type of X and Y values in chart series points using Aspose.Cells for .NET. Our guide will explain the different types of data values and show you how to access and work with them in your charts.
keywords: Aspose.Cells for .NET, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Possible Usage Scenarios**
Sometime, you want to know the type of X and Y values of chart points in a series. Aspose.Cells provides ChartPoint.XValueType and ChartPoint.YValueType properties that can be used for this purpose. Please note, you will have to call Chart.Calculate() method before you could use these properties effectively.
## **Find Type of X and Y Values of Points in Chart Series**
The following sample code loads the [sample Excel file](64716905.xlsx) and accesses the first chart inside the first worksheet. It then calls the Chart.Calculate() method and finds the type of X and Y values of first chart point and prints them on console. Please see the console output shown below for a reference.

## **Sample Code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}

## **Console Output**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
