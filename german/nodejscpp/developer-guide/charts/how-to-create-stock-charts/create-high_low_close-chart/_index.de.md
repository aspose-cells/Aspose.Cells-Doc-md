---  
title: Erstellen Sie High Low Close(HLC) Aktienchart mit Node.js über C++  
linktitle: Erstellen eines Hoch Tief Schluss(HLC) Aktiendiagramms  
description: Erfahren Sie, wie Sie mithilfe von Aspose.Cells for Node.js via C++ einen High Low Close Aktienchart erstellen. Unser Schritt für Schritt Leitfaden zeigt, wie Sie Börsendaten, einschließlich der Hoch , Tief und Schlusskurse, in ein Diagramm einzeichnen, um eine bessere Analyse und Visualisierung zu erreichen.  
keywords: Aspose.Cells für Node.js, High Low Close Aktienchart, Börsendaten, Analyse, Visualisierung.  
type: docs  
weight: 181  
url: /de/nodejs-cpp/create-high-low-close-stock-chart/  
---  

## **Mögliche Verwendungsszenarien**  
Der High-Low-Close (HLC)-Aktienchart verwendet vier Datenkolonnen. Die erste Spalte ist eine Kategorie, normalerweise ein Datum, aber auch Aktiennamen können verwendet werden. Die nächsten drei Spalten sind für Hoch-, Tief- und Schlusskurse. Der Preisbereich für jede Kategorie wird durch eine vertikale Linie von Tief zu Hoch angezeigt, und der Schlusskurs wird durch ein Zeitsymbol rechts von dieser Linie dargestellt.  

![todo:image_alt_text](sample.png)  
## **Verbesserungen der Sichtbarkeit im Diagramm**  
Manchmal können wir das Aussehen des Markers (Schlusskurs) anpassen oder ihn auf der sekundären Achse anzeigen, um das Diagramm übersichtlicher zu gestalten.  

![todo:image_alt_text](sample2.png)  
## **Beispielcode**  
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](High-Low-Close.xlsx) und generiert die [Ausgabe-Excel-Datei](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:D9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set the marker with the built-in data 
chart.getNSeries().get(2).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(2).getMarker().setMarkerSize(20);
chart.getNSeries().get(2).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(2).getMarker().getArea().setForegroundColor(AsposeCells.Color.Maroon);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
