---
title: How to create Dynamic Rolling Chart with Node.js via C++
linktitle: How to create Dynamic Rolling Chart
description: Learn how to create a dynamic rolling chart using Aspose.Cells for Node.js via C++. Our guide will demonstrate how to implement smooth data transitions and rolling averages in your chart for a continuous and updated display.
keywords: Aspose.Cells for Node.js, Dynamic Rolling Chart, Data Transitions, Smooth Averages, Continuous Display, Updating Visualization.
type: docs
weight: 74
url: /nodejs-cpp/create-dynamic-rolling-chart/
---

## **Possible Usage Scenarios**
A dynamic rolling chart refers to a graphical representation that displays data points constantly shifting and updating over time. It is a type of chart that continually updates itself, showcasing a rolling window of the most recent data points while discarding older data points as new ones come in.

Dynamic rolling charts are commonly used to visualize trends and patterns in real-time or streaming data. They are particularly useful in scenarios where temporal aspects and changes over time are critical, such as stock market analysis, weather monitoring, or live performance tracking.

These charts typically employ animation or auto-scrolling mechanisms to ensure the most up-to-date information is always presented. The length of the rolling window can be customized to show a specific time period, such as the last hour, day, or week.

In summary, a dynamic rolling chart is a continuously updated graphical representation that displays the latest data points while discarding older ones, allowing users to observe real-time trends and patterns.

## **Use Aspose Cells to create Dynamic Rolling Chart**
In the next paragraphs, we will show you how to create Dynamic Rolling Chart using Aspose.Cells. We'll show you the code for the example, as well as the Excel file created with this code.

## **Sample Code**
The following sample code will generate the [Dynamic Rolling Chart File](DynamicRollingChart.xlsx).

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
sheet.getCells().get("A1").putValue("Month");
sheet.getCells().get("A2").putValue(1);
sheet.getCells().get("A3").putValue(2);
sheet.getCells().get("A4").putValue(3);
sheet.getCells().get("A5").putValue(4);
sheet.getCells().get("A6").putValue(5);
sheet.getCells().get("A7").putValue(6);
sheet.getCells().get("A8").putValue(7);

sheet.getCells().get("B1").putValue("Sales");
sheet.getCells().get("B2").putValue(50);
sheet.getCells().get("B3").putValue(45);
sheet.getCells().get("B4").putValue(55);
sheet.getCells().get("B5").putValue(60);
sheet.getCells().get("B6").putValue(55);
sheet.getCells().get("B7").putValue(65);
sheet.getCells().get("B8").putValue(70);

// Set the dynamic range for the chart's data source.
let index = sheets.getNames().add("Sheet1!ChtData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

// Set the dynamic range for the chart's data labels.
index = sheets.getNames().add("Sheet1!ChtLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 10, 3, 25, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicRollingChart.xlsx"));
```

## **Notes**
In the generated file, you can continue to add data in columns A and B, while the chart dynamically counts the latest 5 sets of data. This is done using the "OFFSET" formula in the sample code:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

You can try changing the number "-5" to "-10" in the formula, and the dynamic chart will count the latest 10 sets of data. Now we have created a dynamic rolling chart using Aspose.Cells successfully.
