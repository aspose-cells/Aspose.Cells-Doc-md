---
title: Hur skapa kombinationsdiagram med Node.js via C++
linktitle: Hur du skapar kombinationsdiagram
description: Lär dig hur man skapar ett kombinationsdiagram med Aspose.Cells for Node.js via C++. Vår omfattande guide visar hur man kombinerar olika diagramtyper till ett effektivt kombinationsdiagram för en mer tydlig dataskildring.
keywords: Aspose.Cells for Node.js via C++, Kombinationsdiagram, Kombinera diagramtyper, Datavisualisering, Effektiv presentation.
type: docs
weight: 73
url: /sv/nodejs-cpp/create-combo-chart/
---

## **Möjliga användningsscenario**
Kombinationsdiagram i Excel låter dig dra nytta av detta alternativ eftersom du enkelt kan kombinera två eller flera diagramtyper för att göra din data förståelig. Kombinationsdiagram är användbara när din data innehåller flera olika typer av värden, inklusive pris och volym. Dessutom är kombinationsdiagram genomförbara när dina datanummer skiljer sig markant från serie till serie.
Med det följande datasättet som exempel kan vi konstatera att dessa data är ganska lika de data som nämns i [**VHCL**](https://docs.aspose.com/cells/nodejs-cpp/create-volume-high-low-close-stock-chart/). Om vi vill visualisera serie0, som motsvarar "Total Revenue," som ett Linjediagram, hur ska vi gå tillväga?

![todo:image_alt_text](sample.png)
## **Kombinationsdiagram**
Efter att ha kört koden nedan kommer du att se kombinationsdiagrammet som visas nedan.

![todo:image_alt_text](result.png)
## **Exempelkod**
Följande provkod laddar den [provfilen i Excel](combo.xlsx) och genererar den [resulterande Excelfilen](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "combo.xlsx");

// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a stock volume (VHLC)
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeHighLowClose, 15, 0, 34, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Combo Chart");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E12", true);
// Set category data 
chart.getNSeries().get(0).setXValues("A2:A12");  // Corrected method

// Set the Series[1] Series[2] and Series[3] to different Marker Style
for (let j = 0; j < chart.getNSeries().getCount(); j++) {
switch (j) {
case 1:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Circle);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Pink);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 2:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Orange);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 3:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Square);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.LightBlue);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
}
}
// Set the chart type for Series[0] 
chart.getNSeries().get(0).setType(AsposeCells.ChartType.Line);
// Set style for the border of first series
chart.getNSeries().get(0).getBorder().setStyle(AsposeCells.LineType.Solid);
// Set Color for the first series
chart.getNSeries().get(0).getBorder().setColor(AsposeCells.Color.DarkBlue);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
