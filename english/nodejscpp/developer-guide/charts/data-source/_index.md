---  
title: Set Data source for the chart with Node.js via C++  
description: Learn about the various data sources supported by Aspose.Cells for Node.js via C++. Our guide will walk you through the different types of data sources available and show you how to connect and retrieve data from them to populate your worksheets.  
keywords: Aspose.Cells for Node.js via C++, charting, data formatting, labels, colors, fonts, appearance, usability.  
linktitle: Data source  
type: docs  
weight: 10  
url: /nodejs-cpp/data-formatting-in-charts/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

In our previous topics, we have already provided many examples to demonstrate how you can set a data source for your chart but in this topic, we are going to provide more details about the types of data that can be set for a chart.

## **Setting Chart Data**

There are two types of data to deal with while working on charts using Aspose.Cells as follows:

- Chart data.
- Category data.

### **Chart Data**

Chart data is the data that we use as a data source to build our charts. We can add a range of the cells (containing chart data) by calling the [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) object's [**add(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#add-string-boolean-) method.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(300);
worksheet.getCells().get("B1").putValue(160);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Category Data**

Category data is used for the labeling of chart data and can be added to [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) by using its [**getCategoryData()**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#getCategoryData--) property. A complete example is given below to demonstrate the use of chart and category data. After executing the above example code, a column chart will be added to the worksheet as shown below.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(10);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(200);
worksheet.getCells().get("B1").putValue(120);
worksheet.getCells().get("B2").putValue(320);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the data source for the category data of SeriesCollection
chart.getNSeries().setCategoryData("C1:C4");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Advance topics**  
- [Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range](/cells/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [Create Dynamic Charts](/cells/nodejs-cpp/create-dynamic-charts/)  
- [Easy way for Chart Setup using Chart.SetChartDataRange method](/cells/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [Find Type of X and Y Values of Points in Chart Series](/cells/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)  
{{< app/cells/assistant language="nodejs-cpp" >}}
