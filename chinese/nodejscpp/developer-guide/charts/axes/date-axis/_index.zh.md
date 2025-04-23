---
title: 使用Node.js通过C++管理日期轴
description: 学习如何在Aspose.Cells for Node.js via C++中管理日期轴。我们的指南将帮助你理解如何处理各种日期格式、时间刻度和刻度标签频率。
keywords: Aspose.Cells for Node.js，日期轴，管理，日期格式，时间刻度，刻度标签频率。
type: docs
weight: 200
url: /zh/nodejs-cpp/date-axis/
---

## **可能的使用场景**
 当你用日期数据创建图表，并将日期沿水平（类别）轴绘制时，Aspose.Cells for Node.js via C++会自动将类别轴更改为日期（时间刻度）轴。
日期轴以特定间隔或基本单位（例如天数、月份或年份）按年代顺序显示日期，即使工作表上的日期不是按顺序或基本单位相同。
 默认情况下，Aspose.Cells根据工作表数据中两个日期之间的最小差异确定日期轴的基本单位。例如，如果你的数据为股票价格，两个日期间的最小差异为七天，Excel会将基本单位设为天，但你可以将基本单位改为月或年，以观察股票在较长时间段内的表现。

## **处理日期轴就像处理Microsoft Excel一样**
请参阅以下示例代码，此代码创建一个新的Excel文件并将图表的值放在第一个工作表中。 
然后，我们添加一个图表并设置[**Axis**](https://reference.aspose.com/cells/nodejs-cpp/axis/)的类型 
到[**Axis.getCategoryType()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getCategoryType--)，然后将基本单位设置为天数。

![todo:image_alt_text](excel.png)

## **示例代码**
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
