---
title: Custom Slice or Sector Colors in Pie Chart
description: Learn how to use Aspose.Cells for .NET to customize slice and sector colors in a pie chart. Our guide will demonstrate how to assign unique colors to each slice, sector, or legion for improved visual appeal and data representation.
keywords: Aspose.Cells for .NET, Pie Chart, Custom Slice Colors, Custom Sector Colors, Visual Appeal, Data Representation.
type: docs
weight: 60
url: /net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

This article explains how to add custom colors to pie chart slices/sectors. By default, pie charts use the Microsoft Excel default template. To use other colors, redefine the colors in the chart.

{{% /alert %}}

To set a custom color for a pie chart's individual slices or sectors:

1. Access the [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) object's [**ChartPoint**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint).
1. Assign the color of your choice using the [**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) property.

This article also explains how to:

- A chart's category data.
- A chart title linked to a cell.
- The chart title font settings.
- The position of the legend.

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) is not specific to pie charts but it can be used for all types of charts.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
