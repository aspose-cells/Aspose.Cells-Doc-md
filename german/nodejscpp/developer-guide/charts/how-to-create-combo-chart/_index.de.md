---
title: Wie man ein Kombidiagramm mit Node.js über C++ erstellt
linktitle: Wie man ein Kombinationsdiagramm erstellt
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ ein Kombidiagramm erstellen. Unser umfassender Leitfaden zeigt, wie Sie verschiedene Diagrammtypen zu einem einzigen Kombidiagramm kombinieren, um eine effektivere Datenpräsentation zu erreichen.
keywords: Aspose.Cells for Node.js via C++, Kombidiagramm, Diagrammtypen kombinieren, Datenvisualisierung, Effektive Präsentation.
type: docs
weight: 73
url: /de/nodejs-cpp/create-combo-chart/
---

## **Mögliche Verwendungsszenarien**
Kombinationsdiagramme in Excel ermöglichen es Ihnen, diese Option zu nutzen, da Sie problemlos zwei oder mehr Diagrammtypen kombinieren können, um Ihre Daten verständlich zu machen. Kombinationsdiagramme sind hilfreich, wenn Ihre Daten verschiedene Arten von Werten enthalten, einschließlich Preis und Volumen. Darüber hinaus sind Kombinationsdiagramme sinnvoll, wenn sich Ihre Datenwerte von Serie zu Serie stark ändern.
Anhand des folgenden Datensatzes können wir beobachten, dass diese Daten denen in [**VHCL**](https://docs.aspose.com/cells/nodejs-cpp/create-volume-high-low-close-stock-chart/) ähnlich sind. Wenn wir die Serie0, die "Gesamterlös" entspricht, als Liniendiagramm visualisieren möchten, wie sollten wir vorgehen?

![todo:image_alt_text](sample.png)
## **Kombinationsdiagramm**
Nach Ausführung des unten stehenden Codes sehen Sie das Kombinationsdiagramm wie unten gezeigt.

![todo:image_alt_text](result.png)
## **Beispielcode**
Der folgende Beispielscode lädt die [Beispieldatei](combo.xlsx) und erstellt die [Ausgabedatei](out.xlsx).

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
