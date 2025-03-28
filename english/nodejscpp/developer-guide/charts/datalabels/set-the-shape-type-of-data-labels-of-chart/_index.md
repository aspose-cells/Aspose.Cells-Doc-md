---
title: Set the Shape Type of Data Labels of Chart with Node.js via C++
linktitle: Set the Shape Type of Data Labels of Chart
description: Learn how to set the shape type of data labels in charts using Aspose.Cells for Node.js via C++. This guide will explain the different shape types available and show you how to choose the appropriate shape for your data labels to enhance presentation and usability.
keywords: Aspose.Cells for Node.js via C++, charting, data labels, shape types, presentation, usability.
type: docs
weight: 110
url: /nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Possible Usage Scenarios**
You can change the shape type of data labels of the chart using the `DataLabels.shapeType` property. It takes the value of `DataLabelShapeType` enumeration and changes the shape type of data labels accordingly. Some of its values are

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Set the Shape Type of Data Labels of Chart**
The following sample code changes the shape type of data labels of the chart to `DataLabelShapeType.WedgeEllipseCallout`. Please see the [sample Excel file](60489778.xlsx) used in this code and the [output Excel file](60489779.xlsx) generated by it. The screenshot shows the effect of the code on the sample Excel file.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetShapeTypeOfDataLabelsOfChart.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Access first series
const series = chart.getNSeries().get(0);

// Set the shape type of data labels i.e. Speech Bubble Oval
series.getDataLabels().setShapeType(AsposeCells.DataLabelShapeType.WedgeEllipseCallout);

// Save the output Excel file
workbook.save(path.join(dataDir, "outputSetShapeTypeOfDataLabelsOfChart.xlsx"));
```
