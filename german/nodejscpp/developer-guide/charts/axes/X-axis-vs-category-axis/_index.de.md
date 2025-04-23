---
title: X Achse vs. Kategorieachse mit Node.js über C++
linktitle: X Achse Vs. Kategorieachse
description: Lernen Sie, wie Sie die Unterschiede zwischen der X Achse und der Kategorieachse in Aspose.Cells for Node.js via C++ erkennen. Unser Leitfaden hilft Ihnen, die Unterschiede in ihrer Verwendung und ihren Eigenschaften zu verstehen und sie entsprechend Ihren Anforderungen zu konfigurieren.
keywords: Aspose.Cells for Node.js via C++, X Achse, Kategorieachse, Unterschied, Verwendung, Eigenschaften, Konfiguration.
type: docs
weight: 180
url: /de/nodejs-cpp/X-axis-vs-category-axis/
---

## **Mögliche Verwendungsszenarien**
Es gibt verschiedene Arten von X-Achsen. Während die Y-Achse eine Werttyp-Achse ist, kann die X-Achse eine Kategorietyp-Achse oder eine Werttyp-Achse sein. Bei Verwendung einer Wertachse wird die Daten als fortlaufend variierende numerische Daten behandelt, und der Marker wird an einem Punkt entlang der Achse platziert, der entsprechend seinem numerischen Wert variiert. Bei Verwendung einer Kategorieachse wird die Daten als Sequenz von nicht-numerischen Textetiketten behandelt, und der Marker wird an einem Punkt entlang der Achse platziert, entsprechend seiner Position in der Sequenz. Das folgende Beispiel verdeutlicht den Unterschied zwischen Wert- und Kategorieachsen.
Unsere Beispieldaten werden in der [Beispiel-Tabellendatei](sample.png) unten dargestellt. Die erste Spalte enthält unsere X-Achsendaten, die als Kategorien oder als Werte behandelt werden können. Beachten Sie, dass die Zahlen nicht gleichmäßig verteilt sind und auch nicht numerisch geordnet erscheinen.

![todo:image_alt_text](sample.png)
## **Behandeln Sie X- und Kategorieachse wie in Microsoft Excel**
Wir werden diese Daten auf zwei Arten von Diagrammen anzeigen, das erste Diagramm ist XY (Streu) Diagramm X als Wertachse, das zweite Diagramm ist Linien-Diagramm X als Kategorieachse.

![todo:image_alt_text](compare.png)
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

// Put the sample values used in charts
worksheet.getCells().get("A2").putValue(1);
worksheet.getCells().get("A3").putValue(3);
worksheet.getCells().get("A4").putValue(2.5);
worksheet.getCells().get("A5").putValue(3.5);
worksheet.getCells().get("B1").putValue("Cats");
worksheet.getCells().get("C1").putValue("Dogs");
worksheet.getCells().get("D1").putValue("Fishes");
worksheet.getCells().get("B2").putValue(7);
worksheet.getCells().get("B3").putValue(6);
worksheet.getCells().get("B4").putValue(5);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("C2").putValue(7);
worksheet.getCells().get("C3").putValue(5);
worksheet.getCells().get("C4").putValue(4);
worksheet.getCells().get("C5").putValue(3);
worksheet.getCells().get("D2").putValue(8);
worksheet.getCells().get("D3").putValue(7);
worksheet.getCells().get("D4").putValue(3);
worksheet.getCells().get("D5").putValue(2);

// Create Line Chart: X as Category Axis
let pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 6, 15, 20, 21);
// Retrieve the Chart object
let chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$5");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);

// Create XY (Scatter) Chart: X as Value Axis
pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
// Retrieve the Chart object
chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set X values for series 
chart.getNSeries().get(0).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(1).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(2).setXValues("{1,3,2.5,3.5}");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("XAxis.xlsx");
```
