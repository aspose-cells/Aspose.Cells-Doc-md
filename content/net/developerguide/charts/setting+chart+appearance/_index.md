---
title : "Setting Chart Appearance" 
description : "" 
weight : 12264 
toc : false
type: docs
url: /net/developerguide/charts/setting+chart+appearance/
---

# Aspose.Cells for .NET : Setting Chart Appearance


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Setting Chart Appearance](#setting-chart-appearance)
    *   1.1 [Setting Chart Area](#setting-chart-area)
    *   1.2 [Setting Chart Lines](#setting-chart-lines)
    *   1.3 [Applying Microsoft Excel 2007/2010 Themes to Charts](#applying-microsoft-excel-2007/2010-themes-to-charts)
    *   1.4 [Setting the Titles of Charts or Axes](#setting-the-titles-of-charts-or-axes)
    *   1.5 [Working with Major Gridlines](#working-with-major-gridlines)
        *   1.5.1 [Hiding Major Gridlines](#hiding-major-gridlines)
        *   1.5.2 [Changing Major Gridlines Settings](#changing-major-gridlines-settings)
{{< /panel >}}
 

## Setting Chart Appearance

In How to Create a Chart we gave a brief introduction to the types of charts and charting objects offered by Aspose.Cells, and described how to create one. This article discusses how to customize the appearance of charts by setting their properties:

*   Setting the chart area.
*   Setting chart lines.
*   Applying themes.
*   Setting titles to charts and axes.
*   Working with gridlines.

### Setting Chart Area

There are different kinds of areas in a chart and Aspose.Cells provides the flexibility to modify the appearance of each area. Developers can apply different formatting settings on an area by changing its foreground color, background color, and fill format etc.

In the example given below, we have applied different formatting settings on different kinds of areas of a chart. These areas include:

*   Plot area
*   Chart area
*   SeriesCollection area
*   Area of a single point in a SeriesCollection

The following code snippet demonstrates how to set the chart area.

### Setting Chart Lines

Developers can also apply different kinds of styles on the lines or data markers of the [SeriesCollection](https://apireference.aspose.com/cells/net/aspose.cells.charts/seriescollection). The following code snippet demonstrates how to set chart lines using Aspose.Cells API.

### Applying Microsoft Excel 2007/2010 Themes to Charts

Developers can apply different Microsoft Excel themes/colors to [SeriesCollection](https://apireference.aspose.com/cells/net/aspose.cells.charts/seriescollection) or other chart objects as shown below in the example.

### Setting the Titles of Charts or Axes

You can use Microsoft Excel to set the titles of a chart and its axes in a WYSIWYG environment. Aspose.Cells also allows developers to set the titles of a chart and its axes at runtime. All charts and their axes contain a [Title](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title) property that can be used to set their titles as shown below in an example.

The following code snippet demonstrates how to set titles to charts and axes.

### Working with Major Gridlines

It is possible to customize the look of major gridlines. Hide or show gridlines, or define their color and other settings. Below, we show how to hide gridlines and how to change their color.

#### Hiding Major Gridlines

Developers can control the visibility of major gridlines by setting the [IsVisible](https://apireference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) property of the [Line](https://apireference.aspose.com/cells/net/aspose.cells.drawing/line) object to **true** or **false**.

The following code snippet demonstrates how to hide major gridlines. After hiding the major gridlines, a column chart will be added to the worksheet will have not gridlines.

#### Changing Major Gridlines Settings

Developers cannot only control the visibility of major gridlines but also other properties including its color etc.

The following code snippet demonstrates how to change the major gridlines' color. After setting the color of the major gridlines, a column chart will be added to the worksheet with modified gridlines.

