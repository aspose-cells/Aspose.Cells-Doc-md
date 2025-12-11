---
title: Custom Slice or Sector Colors in Pie Chart with Golang via C++
linktitle: Custom Slice or Sector Colors in Pie Chart
description: Learn how to use Aspose.Cells for C++ to customize slice and sector colors in a pie chart. Our guide will demonstrate how to assign unique colors to each slice, sector, or legend for improved visual appeal and data representation.
keywords: Aspose.Cells for C++, Pie Chart, Custom Slice Colors, Custom Sector Colors, Visual Appeal, Data Representation.
type: docs
weight: 60
url: /go-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

This article explains how to add custom colors to pie chart slices/sectors. By default, pie charts use the Microsoft Excel default template. To use other colors, redefine the colors in the chart.

{{% /alert %}}

To set a custom color for a pie chart's individual slices or sectors:

1. Access the [**Series**](https://reference.aspose.com/cells/go-cpp/series/) object's [**ChartPoint**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/).
1. Assign the color of your choice using the [**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/go-cpp/area/getforegroundcolor/) property.

This article also explains how to:

- Set a chart's category data.
- Set a chart title linked to a cell.
- Adjust the chart title font settings.
- Position the legend.

{{% alert color="primary" %}}

[**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/go-cpp/area/getforegroundcolor/) is not specific to pie charts but it can be used for all types of charts.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomSliceOrSectorColorsInPieChart.go" >}}