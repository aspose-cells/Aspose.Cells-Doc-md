---
title: Setting Chart Appearance with Golang via C++
linktitle: Chart Format
description: Learn how to configure the appearance of charts in Aspose.Cells for C++. Our guide will show you how to modify chart layouts, colors, fonts, and effects to achieve the desired visual style and enhance your worksheets.
keywords: Aspose.Cells for C++, charting, chart appearance, layouts, colors, fonts, effects, worksheets.
type: docs
weight: 20
url: /go-cpp/setting-chart-appearance/
---

## **Setting Chart Appearance**
In How to Create a Chart we gave a brief introduction to the types of charts and charting objects offered by Aspose.Cells, and described how to create one. This article discusses how to customize the appearance of charts by setting their properties:

- Setting the chart area.
- Setting chart lines.
- Applying themes.
- Setting titles to charts and axes.
- Working with gridlines.

### **Setting Chart Area**
There are different kinds of areas in a chart and Aspose.Cells provides the flexibility to modify the appearance of each area. Developers can apply different formatting settings on an area by changing its foreground color, background color, and fill format etc.

In the example given below, we have applied different formatting settings on different kinds of areas of a chart. These areas include:

- Plot area
- Chart area
- SeriesCollection area
- Area of a single point in a SeriesCollection

The following code snippet demonstrates how to set the chart area.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-ChartFormat.go" >}}
### **Setting Chart Lines**
Developers can also apply different kinds of styles on the lines or data markers of the [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/). The following code snippet demonstrates how to set chart lines using Aspose.Cells API.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-ChartFormat-1.go" >}}
### **Applying Microsoft Excel 2007/2010 Themes to Charts**
Developers can apply different Microsoft Excel themes/colors to [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/) or other chart objects as shown below in the example.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-ChartFormat-2.go" >}}
### **Setting the Titles of Charts or Axes**
You can use Microsoft Excel to set the titles of a chart and its axes in a WYSIWYG environment. Aspose.Cells also allows developers to set the titles of a chart and its axes at runtime. All charts and their axes contain a [Title](https://reference.aspose.com/cells/go-cpp/title/) property that can be used to set their titles as shown below in an example.

The following code snippet demonstrates how to set titles to charts and axes.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-ChartFormat-3.go" >}}
### **Working with Major Gridlines**
It is possible to customize the look of major gridlines. Hide or show gridlines, or define their color and other settings. Below, we show how to hide gridlines and how to change their color.

#### **Hiding Major Gridlines**
Developers can control the visibility of major gridlines by setting the [IsVisible](https://reference.aspose.com/cells/go-cpp/line/isvisible/) property of the [Line](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/) object to **true** or **false**.

The following code snippet demonstrates how to hide major gridlines. After hiding the major gridlines, a column chart will be added to the worksheet will have not gridlines.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-ChartFormat-4.go" >}}
#### **Changing Major Gridlines Settings**
Developers cannot only control the visibility of major gridlines but also other properties including its color etc.

The following code snippet demonstrates how to change the major gridlines' color. After setting the color of the major gridlines, a column chart will be added to the worksheet with modified gridlines.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-ChartFormat-5.go" >}}
## **Advance topics**
- [Set the Values Format Code of Chart Series](/cells/cpp/set-the-values-format-code-of-chart-series/)
- [Set Picture as Background Fill in the Chart](/cells/cpp/set-picture-as-background-fill-in-the-chart/)