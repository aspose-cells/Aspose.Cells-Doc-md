---
title: Erstellen Sie Open High Low Close(OHLC) Aktienchart mit Node.js über C++
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ einen Open High Low Close Aktienchart erstellen. Unser Leitfaden zeigt, wie Sie Börsendaten, einschließlich der Eröffnungs , Hoch , Tief und Schlusskurse, in ein Diagramm zeichnen, um eine bessere Analyse und Visualisierung zu ermöglichen.
keywords: Aspose.Cells for Node.js via C++, Open High Low Close Aktienchart, Börsendaten, Analyse, Visualisierung.
type: docs
weight: 182
url: /de/nodejs-cpp/create-open-high-low-close-stock-chart/
---

## **Mögliche Verwendungsszenarien**
Das Open-High-Low-Close (OHLC) Diagramm verwendet fünf Datenkategorien in dieser Reihenfolge: Kategorie, Öffnen, Hoch, Tief und Schlusskurs. Die Preisspanne in jeder Kategorie wird erneut durch eine vertikale Linie angezeigt, während die Spanne zwischen Öffnen und Schließen durch eine breitere, freischwebende Leiste angegeben wird. Wenn der Preis in der Kategorie steigt (Schlusskurs höher als Öffnungspreis), wird die Leiste mit einer Farbe gefüllt, während sie bei sinkenden Preisen mit einer anderen Farbe gefüllt wird. Dieser Diagrammtyp wird oft als Candlestick-Diagramm bezeichnet.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Verbesserungen der Sichtbarkeit im Diagramm**
Wir verwenden oft Farben anstelle von Schwarz-Weiß, um steigende und fallende Kurse anzuzeigen. Im ersten Satz von Kerzencharts unten zeigt Rot steigende und Grün fallende Kurse.

![todo:image_alt_text](sample2.png)
## **Beispielcode**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](Open-High-Low-Close.xlsx) und generiert die [Ausgabedatei Excel](out.xlsx).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E9", true);
// Set category data 
chart.getNSeries().getCategoryData("A2:A9");
// Set the DownBars and UpBars with different color
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Red);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
