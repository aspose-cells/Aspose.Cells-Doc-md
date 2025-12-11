---
title: Find Type of X and Y Values of Points in Chart Series with Golang via C++
linktitle: Find Type of X and Y Values of Points in Chart Series
description: Learn how to determine the type of X and Y values in chart series points using Aspose.Cells for C++. Our guide will explain the different types of data values and show you how to access and work with them in your charts.
keywords: Aspose.Cells for C++, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /go-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Possible Usage Scenarios**
Sometimes, you want to know the type of X and Y values of chart points in a series. Aspose.Cells provides `ChartPoint::get_XValueType` and `ChartPoint::get_YValueType` methods that can be used for this purpose. Please note, you will have to call the `Chart::Calculate()` method before you can use these properties effectively.

## **Find Type of X and Y Values of Points in Chart Series**
The following sample code loads the [sample Excel file](64716905.xlsx) and accesses the first chart inside the first worksheet. It then calls the `Chart::Calculate()` method, finds the type of X and Y values of the first chart point, and prints them to the console. Please see the console output shown below as a reference.

## **Sample Code**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindTypeOfXAndYValuesOfPointsInChartSeries.go" >}}

## **Console Output**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}