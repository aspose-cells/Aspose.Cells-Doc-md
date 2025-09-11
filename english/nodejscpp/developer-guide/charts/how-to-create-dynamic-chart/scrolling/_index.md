---
title: How to create Dynamic Scrolling Chart with Node.js via C++
linktitle: How to create Dynamic Scrolling Chart
description: Learn how to create a dynamic scrolling chart using Aspose.Cells for Node.js via C++. Our step-by-step guide will demonstrate how to implement smooth data transitions and automatic scrolling in your chart for a continuous and updated display.
keywords: Aspose.Cells for Node.js, Dynamic Scrolling Chart, Data Transitions, Smooth Scrolling, Continuous Display, Updating Visualization.
type: docs
weight: 75
url: /nodejs-cpp/create-dynamic-scrolling-chart/
---

## **Possible Usage Scenarios**
Dynamic scrolling chart is a type of graphical representation used to display data that changes over time. It is designed to provide a real-time view of data, allowing users to track continuous updates and trends. The chart continuously updates itself as new data is added, and it automatically scrolls to show the most recent information.

Dynamic scrolling charts are commonly used in various industries, such as finance, stock market analysis, weather tracking, and social media analytics. They enable users to visualize and analyze data patterns and make informed decisions based on real-time information.

These charts are typically interactive, allowing the user to zoom in or out, scroll through historical data, and adjust time intervals. They often support multiple data series, providing a comprehensive view of different metrics and their correlations.

Overall, dynamic scrolling charts are valuable tools for monitoring and analyzing time-series data, facilitating real-time decision-making and enhancing data visualization capabilities.

## **Use Aspose.Cells to create Dynamic Scrolling Chart**
In the next paragraphs, we will show you how to create Dynamic Scrolling Chart using Aspose.Cells for Node.js via C++. We'll show you the code for the example, as well as the Excel file created with this code.

## **Sample Code**
The following sample code will generate the [Dynamic Scrolling Chart File](DynamicScrollingChart.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A1").putValue("Day");
sheet.getCells().get("B1").putValue("Sales");
// In this example, we will add 30 days of data
const allDays = 30;
const showDays = 10;
let currentDay = 1;

for (let i = 0; i < allDays; i++) {
const cellA = `A${i + 2}`;
const cellB = `B${i + 2}`;
sheet.getCells().get(cellA).putValue(i + 1);
sheet.getCells().get(cellB).putValue(50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3));
}

// This is the Dynamic Scrolling Control Data
sheet.getCells().get("G19").putValue("Start Day");
sheet.getCells().get("G20").putValue(currentDay);
sheet.getCells().get("H19").putValue("Show Days");
sheet.getCells().get("H20").putValue(showDays);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtScrollData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtScrollLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Add a ScrollBar for the Dynamic Scrolling Chart
const bar = sheet.getShapes().addScrollBar(2, 0, 3, 0, 200, 30);
bar.setMin(0);
bar.setMax(allDays - showDays);
bar.setCurrentValue(currentDay);
bar.setLinkedCell("$G$20");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 2, 4, 15, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtScrollData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtScrollLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicScrollingChart.xlsx"));
```

## **Notes**
In the generated file, you can operate on the scroll bar, while the chart dynamically counts the latest 10 sets of data. This is done using the "OFFSET" formula in the sample code:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

You can try changing the number "10" to "15" in cell "Sheet1!$H$20", and the dynamic chart will count the latest 15 sets of data. Now we have created a dynamic scrolling chart using Aspose.Cells for Node.js via C++ successfully.
{{< app/cells/assistant language="nodejs-cpp" >}}