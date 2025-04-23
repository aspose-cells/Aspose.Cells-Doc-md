---
title: Erstellen Sie ein Volumen High Low Close (VHLC) Aktienchart mit Node.js via C++
linktitle: Erstellen Sie ein Volumen High Low Close(VHLC) Aktiendiagramm
description: Lernen Sie, wie man ein Volumen High Low Close Aktienchart mit Aspose.Cells for Node.js via C++ erstellt. Unser Leitfaden zeigt, wie Sie Börsendaten, einschließlich Volumen, Hoch, Tief und Schlusskurse, auf einen Chart plotten, um eine bessere Analyse und Visualisierung zu ermöglichen.
keywords: Aspose.Cells for Node.js via C++, Volumen High Low Close Aktienchart, Börsendaten, Analyse, Visualisierung.
type: docs
weight: 183
url: /de/nodejs-cpp/create-volume-high-low-close-stock-chart/
---

## **Mögliche Verwendungsszenarien**
Das dritte Aktienchart, das wir betrachten werden, ist das Volumen-High-Low-Close-Chart. Hierbei ist es erneut wichtig zu wiederholen, dass die Daten in der richtigen Reihenfolge vorliegen müssen. Wenn Sie Ihre Datentabelle neu anordnen müssen, sollten Sie dies vor dem Erstellen des Charts tun.
Dieses Chart enthält eine Spalte für Volumen unmittelbar nach der ersten (Kategorie-)Spalte. Die Charts zeigen auf der primären Achse ein SäulenDiagramm für das Volumen, während die Kurse auf die sekundäre Achse verschoben werden.

![todo:image_alt_text](data.png)
## **Volume-High-Low-Close (VHLC) Aktiendiagramm**

![todo:image_alt_text](sample.png)
## **Beispielcode**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](Volume-High-Low-Close.xlsx) und generiert die [Ausgabedatei Excel](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Volume-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series(Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
