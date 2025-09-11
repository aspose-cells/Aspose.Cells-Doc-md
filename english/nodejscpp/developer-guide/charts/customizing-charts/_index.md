---  
title: Customizing Charts with Node.js via C++  
linktitle: Customizing Charts  
description: Learn how to customize charts in Aspose.Cells for Node.js via C++. Our guide will show you how to modify chart layouts, add and format data series, adjust axes, and apply various formatting options to enhance the appearance and usability of your charts.  
keywords: Aspose.Cells for Node.js via C++, charting, customization, layouts, data series, axes, formatting, appearance, usability.  
type: docs  
weight: 40  
url: /nodejs-cpp/customizing-charts/  
---  
  
  
## **Creating Custom Charts**  

So far, when we've discussed charts, we've looked at standard charts that have their standard formatting settings. We only define the data source, set a few properties, and the chart is created with its default format settings. But Aspose.Cells APIs also supports creating custom charts that allow developers to create charts with their own format settings.  

Developers can create custom charts at run-time using Aspose.Cells.  

A chart is composed of a data series. Each data series in Aspose.Cells is represented by a [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) object whereas [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) object serves as a collection of [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) objects. When creating a custom chart, developers have the freedom to use different types of charts for different data series (collected in the [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) object).  

The example code below demonstrates how to create custom charts. In this example, we are going to use a column chart for the first data series and a line chart for the second series. The result is that we add a column chart, combined with a line chart, to the worksheet.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(110);
worksheet.getCells().get("B1").putValue(260);
worksheet.getCells().get("B2").putValue(12);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(100);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the chart type of 2nd NSeries to display as line chart
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  

Currently, Aspose.Cells only supports custom charts that combine pie, line, column, and column stack charts but more charts will be supported in future releases.  

{{% /alert %}}  
  
{{< app/cells/assistant language="nodejs-cpp" >}}