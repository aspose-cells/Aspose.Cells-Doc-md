---
title: Date Axis with Node.js via C++
description: Learn how to manage the date axis in Aspose.Cells for Node.js via C++. Our guide will help you understand how to work with various date formats, time scales, and tick label frequencies.
keywords: Aspose.Cells for Node.js, date axis, manage, date formats, time scales, tick label frequencies.
type: docs
weight: 200
url: /nodejs-cpp/date-axis/
---

## **Possible Usage Scenarios**
When you create a chart from worksheet data that uses dates, and the dates are plotted along the horizontal (category) axis in the chart, Aspose.Cells for Node.js via C++ automatically changes the category axis to a date (time-scale) axis.
A date axis displays dates in chronological order at specific intervals or base units, such as the number of days, months, or years, even if the dates on the worksheet are not in sequential order or in the same base units.
By default, Aspose.Cells determines the base units for the date axis based on the smallest difference between any two dates in the worksheet data. For example, if you have data for stock prices where the smallest difference between dates is seven days, Excel sets the base unit to days, but you can change the base unit to months or years if you want to see the performance of the stock over a longer period of time.

## **Handle Date Axis like Microsoft Excel**
Please see the following sample code that creates a new Excel file and puts values of the chart in the first worksheet. 
Then we add a chart and set the type of the [**Axis**](https://reference.aspose.com/cells/nodejs-cpp/axis/) 
to [**Axis.getCategoryType()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getCategoryType--) and then set the base units to Days.

![todo:image_alt_text](excel.png)

## **Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add the sample values to cells
worksheet.getCells().get("A1").putValue("Date");
// 14 means datetime format
const style = worksheet.getCells().getStyle();
style.setNumber(14);
// Put values to cells for creating chart
worksheet.getCells().get("A2").setStyle(style);
worksheet.getCells().get("A2").putValue(new Date(Date.UTC(2022, 5, 26)));
worksheet.getCells().get("A3").setStyle(style);
worksheet.getCells().get("A3").putValue(new Date(Date.UTC(2022, 4, 22)));
worksheet.getCells().get("A4").setStyle(style);
worksheet.getCells().get("A4").putValue(new Date(Date.UTC(2022, 7, 3)));
worksheet.getCells().get("B1").putValue("Price");
worksheet.getCells().get("B2").putValue(40);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(60);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 9, 6, 21, 13);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);         
// Set the Axis type to Date time
chart.getCategoryAxis().setCategoryType(AsposeCells.CategoryType.TimeScale);
// Set the base unit for CategoryAxis to days
chart.getCategoryAxis().setBaseUnitScale(AsposeCells.TimeUnit.Days);
// Set the direction for the axis text to be vertical
chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Vertical);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set max value of Y axis.
chart.getValueAxis().setMaxValue(70);
// Set major unit.
chart.getValueAxis().setMajorUnit(10);
// Save the file
workbook.save("DateAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}