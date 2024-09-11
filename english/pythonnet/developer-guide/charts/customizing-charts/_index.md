---
title: Customizing Charts
description: Learn how to customize charts in Aspose.Cells for .NET. Our guide will show you how to modify chart layouts, add and format data series, adjust axes, and apply various formatting options to enhance the appearance and usability of your charts.
keywords: Aspose.Cells for .NET, charting, customization, layouts, data series, axes, formatting, appearance, usability.
type: docs
weight: 40
url: /python-net/customizing-charts/
---

{{% alert color="primary" %}}

## **Creating Custom Charts**

So far, when we've discussed charts, we've looked at standard charts that have their standard formatting settings. We only define the data source, set a few properties, and the chart is created with its default format settings. But Aspose.Cells APIs also supports creating custom charts that allows developers to create charts with their own format settings.

Developers can create custom charts at run-time using Aspose.Cells.

A chart is composed of a data series. Each data series in Aspose.Cells is represented by a [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) object whereas [**series_collection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series_collection) object serves as a collection of [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) objects. When creating a custom chart, developers have the freedom to use different types of charts for different data series (collected in the [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series_collection) object).

The example code below demonstrates how to create custom charts. In this example, we are going to use a column chart for the first data series and a line chart for the second series. The result is that we add a column chart, combined with a line chart, to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Currently Aspose.Cells only supports custom charts that combine pie, line, column, and column stack charts but more charts will be supported in future releases.

{{% /alert %}}
