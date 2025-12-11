---
title: Find Type of X and Y Values of Points in Chart Series
description: Learn how to determine the type of X and Y values in chart series points using Aspose.Cells for .NET. Our guide will explain the different types of data values and show you how to access and work with them in your charts.
keywords: Aspose.Cells for .NET, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /net/find-type-of-x-and-y-values-of-points-in-chart-series/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Sometimes, you want to know the type of X and Y values of chart points in a series. Aspose.Cells provides the ChartPoint.XValueType and ChartPoint.YValueType properties that can be used for this purpose. Please note that you will have to call the Chart.Calculate() method before you can use these properties effectively.

## **Find Type of X and Y Values of Points in Chart Series**
The following sample code loads the [sample Excel file](64716905.xlsx) and accesses the first chart in the first worksheet. It then calls the Chart.Calculate() method, finds the type of X and Y values of the first chart point, and prints them to the console. Please see the console output shown below for reference.

## **Sample Code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}

## **Console Output**

{{< highlight java >}}
 X Value Type: IsString

Y Value Type: IsNumeric
{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
