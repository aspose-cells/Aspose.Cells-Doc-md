---
title: Datumaxel med Node.js via C++
description: Lär dig hur du hanterar datumaxeln i Aspose.Cells for Node.js via C++. Vår guide hjälper dig att förstå hur du arbetar med olika datumformat, tidsskalor och frekvenser för ticketiketter.
keywords: Aspose.Cells för Node.js, datumaxel, hantering, datumformat, tidsskalor, frekvens för ticketiketter.
type: docs
weight: 200
url: /sv/nodejs-cpp/date-axis/
---

## **Möjliga användningsscenario**
När du skapar ett diagram från worksheet-data som använder datum, och datumen plottas längs den horisontella (kategori) axeln i diagrammet, ändrar Aspose.Cells for Node.js via C++ automatiskt kategori-axeln till en datum (tids-skala) axel.
En datumsaxel visar datum i kronologisk ordning vid specifika intervall eller basenheter, såsom antalet dagar, månader eller år, även om datumen i arbetsboken inte är i sekventiell ordning eller i samma basenheter.
Som standard bestämmer Aspose.Cells basenheten för datumaxeln utifrån den minsta skillnaden mellan två datum i worksheet-data. Till exempel, om du har data för aktiekurser där den minsta skillnaden mellan datum är sju dagar, ställer Excel in basenheten till dagar, men du kan ändra basenheten till månader eller år om du vill se aktiens utveckling över en längre period.

## **Hantera datumaxeln som Microsoft Excel**
Se följande kodexempel som skapar en ny Excel-fil och placerar diagramvärden i det första arket. 
Sedan lägger vi till ett diagram och ställer in typen för [**Axis**](https://reference.aspose.com/cells/nodejs-cpp/axis/) 
till [**Axis.getCategoryType()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getCategoryType--) och ställer sedan in basenheterna till Dagar.

![todo:image_alt_text](excel.png)

## **Exempelkod**
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
