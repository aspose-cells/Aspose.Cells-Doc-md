---
title: Primär und Sekundärachse mit Node.js über C++
description: Erfahren Sie, wie Sie Primär und Sekundärachsen in Aspose.Cells for Node.js via C++ verstehen und mit ihnen arbeiten. Unser Leitfaden hilft Ihnen, die Unterschiede zwischen Primär und Sekundärachsen zu verstehen und sie effektiv in Ihren Diagrammen zu konfigurieren und zu verwenden.
keywords: Aspose.Cells for Node.js via C++, Primärachsen, Sekundärachsen, Verständnis, Unterschiede, Konfiguration, Verwendung.
type: docs
weight: 190
url: /de/nodejs-cpp/primary-and-second-axis/
---

## **Mögliche Verwendungsszenarien**
Wenn die Zahlen in einem Diagramm von Datenreihen zu Datenreihen stark variieren oder wenn verschiedene Arten von Daten (Preis und Volumen) vorliegen, platzieren Sie eine oder mehrere Datenreihen auf einer sekundären vertikalen (Wert-) Achse. Die Skala der sekundären vertikalen Achse zeigt die Werte für die zugehörigen Datenreihen an. Eine sekundäre Achse funktioniert gut in einem Diagramm, das eine Kombination aus Säulen- und Liniendiagrammen zeigt.

## **Behandeln Sie die primäre und sekundäre Achse wie in Microsoft Excel**
Bitte sehen Sie sich den folgenden Beispielcode an, der eine neue Excel-Datei erstellt und die Werte des Diagramms im ersten Arbeitsblatt platziert. 
Dann fügen wir ein Diagramm hinzu und zeigen die zweite Achse.

![todo:image_alt_text](excel.png)

## **Beispielcode**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in a chart
worksheet.getCells().get("A1").putValue("Region");
worksheet.getCells().get("A2").putValue("Peking");
worksheet.getCells().get("A3").putValue("New York");
worksheet.getCells().get("A4").putValue("Paris");
worksheet.getCells().get("B1").putValue("Sales Volume");
worksheet.getCells().get("C1").putValue("Growth Rate");
worksheet.getCells().get("B2").putValue(100);
worksheet.getCells().get("B3").putValue(80);
worksheet.getCells().get("B4").putValue(140);
worksheet.getCells().get("C2").putValue(0.7);
worksheet.getCells().get("C3").putValue(0.8);
worksheet.getCells().get("C4").putValue(1.0);

// Create a Scatter chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Scatter, 6, 6, 15, 11);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:C4", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$4");
// Set the Second-Axis
chart.getNSeries().get(1).setPlotOnSecondAxis(true);
// Show the Second-Axis
chart.getSecondValueAxis().setIsVisible(true);
// Set the second series ChartType to line
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);
// Set the series name
chart.getNSeries().get(0).setName("Sales Volume");
chart.getNSeries().get(1).setName("Growth Rate");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the file
workbook.save("PrimaryandSecondaryAxis.xlsx");
```
