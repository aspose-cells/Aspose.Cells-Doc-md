---
title: Verwalten Sie Legenden in Excel Diagrammen mit Node.js über C++
description: Erfahren Sie, wie Sie Aspose.Cells for Node.js via C++ nutzen können, um Diagrammlegenden in Microsoft Excel effektiv zu nutzen und anzupassen. Unser umfassender Leitfaden erklärt die Funktionalität der Legende, wie man sie zugreift und ändert sowie wie man die Visualisierung und das Datenverständnis mit Legenden verbessert.
keywords: Aspose.Cells for Node.js via C++, Diagrammlegenden, Microsoft Excel, Visualisierung, Datenverständnis.
linktitle: Legende
type: docs
weight: 50
url: /de/nodejs-cpp/chart-legend/
---

## **Legendenoptionen**
Aspose.Cells for Node.js via C++ erlaubt auch die Verwaltung der Legende eines Diagramms zur Laufzeit. Das [Legende](https://reference.aspose.com/cells/nodejs-cpp/legend/) Objekt kann bewegt, aktualisiert und formatiert werden.

|![todo:image_alt_text](chart_legend.png)|

## **Festlegen der Legende des Diagramms**
Es ist einfach, die Legende des Diagramms mit Aspose.Cells [Legende](https://reference.aspose.com/cells/nodejs-cpp/legend/) zu verwalten.

Das folgende Code-Snippet zeigt, wie die Legende verwaltet wird:


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Move the legend to left
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Left);

// Set font color of the legend
chart.getLegend().getFont().setColor(AsposeCells.Color.Blue);

// Save the file
workbook.save("chart_legend.xlsx");
```

## **Erweiterte Themen**
- [Setzen Sie den Text des Fülls des Diagrammlegendeneintrags auf keinen mithilfe von Aspose.Cells](/cells/de/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
{{< app/cells/assistant language="nodejs-cpp" >}}
