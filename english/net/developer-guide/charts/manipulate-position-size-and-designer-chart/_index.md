---
title: Manipulate Position Size and Designer Chart
description: Learn how to use Aspose.Cells for .NET to effectively manipulate the position, size, and designer chart in Microsoft Excel. Our guide will demonstrate how to adjust these properties for improved layout and visualization.
keywords: Aspose.Cells for .NET, Position, Size, Designer Chart, Microsoft Excel, Layout, Visualization.
type: docs
weight: 45
url: /net/manipulate-position-size-and-designer-chart/
---

## **Chart Position and Size**
Sometimes, you want to change the position or size of the new or existing chart inside the worksheet. Aspose.Cells provides the [Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) property to achieve this. You can use its sub-properties to re-size the chart with new **height** and **width** or re-position it with new **X** and **Y** coordinates.
### **Controlling Chart Position and Size**
To change the chart's position (X, Y coordinates) or size (height, width), use these properties:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

The following example explains the usage of the above APIs, it loads the existing workbook which contains a chart in its first worksheet. Then it re-sizes and re-positions the chart using Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Manipulating Designer Charts**
There are times when you need to manipulate or modify charts in designer template files. Aspose.Cells fully supports manipulating designer chart contents and elements. The data, chart contents, background image, and formattings can be preserved with accuracy.
### **Manipulating Designer Charts in Template Files**
To manipulate designer charts in template files, use the chart related API. For example, you may use the Worksheet.Charts property to get the existing charts collection in the template file.
#### **Creating a Chart**
The following example shows how to create a pyramid chart. We will manipulate this chart later on.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Manipulating the Chart**
The following example shows how to manipulate the existing chart. In this example, we modify the chart created above. In the generated output, note that the date label of one data point has been set to 'United Kingdom, 30K'.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Manipulating a Line Chart in the Designer Template**
In this example, we will manipulate a line chart. We will add some data series to the existing chart and change their line colors.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}