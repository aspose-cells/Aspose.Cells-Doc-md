---
title: Erstellen Sie ein Volumen Open High Low Close (VOHLC) Aktienchart mit Node.js via C++
description: Lernen Sie, wie man ein Volumen Open High Low Close Aktienchart mit Aspose.Cells for Node.js via C++ erstellt. Unser Leitfaden zeigt, wie man Börsendaten einschließlich Volumen, Eröffnung, Hoch, Tief und Schlusskurse auf einen Chart plotten kann, um eine bessere Analyse und Visualisierung zu ermöglichen.
keywords: Aspose.Cells for Node.js via C++, Volumen Open High Low Close Aktienchart, Börsendaten, Analyse, Visualisierung.
type: docs
weight: 184
url: /de/nodejs-cpp/create-volume-open-high-low-close-stock-chart/
---

## **Mögliche Verwendungsszenarien**
Das vierte Aktienchart, das wir uns ansehen werden, ist das Volume Open High Low Close-Chart. Hier ist es erneut wichtig zu wiederholen, dass die Daten in der richtigen Reihenfolge vorliegen müssen. Wenn Sie Ihre Datentabelle neu anordnen müssen, tun Sie dies vor dem Erstellen des Charts. Das Chart enthält eine Spalte für Volumen unmittelbar nach der ersten (Kategorie-)Spalte. Die Charts zeigen auf der primären Achse ein SäulenDiagramm für das Volumen, während die Preise auf die sekundäre Achse verschoben werden.

![todo:image_alt_text](data.png)
## **Volume-Open-High-Low-Close (VOHLC) Aktiendiagramm**

![todo:image_alt_text](sample.png)
## **Beispielcode**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](Volume-Open-High-Low-Close.xlsx) und generiert die [Ausgabedatei Excel](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Volume-Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:F9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series (Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
