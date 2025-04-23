---
title: Verwalten von Titeln in Excel Diagrammen mit Node.js über C++
description: Lernen Sie, wie Sie mit Aspose.Cells for Node.js via C++ Diagramm und Achsentitel in Microsoft Excel hinzufügen und formatieren. Unser Leitfaden zeigt, wie man verschiedene Titeltypen setzt, deren Erscheinungsbild anpasst und Achsentitel für eine bessere Datenpräsentation und Klarheit modifiziert.
keywords: Aspose.Cells for Node.js via C++, Diagrammtitel, Achsentitel, Microsoft Excel, Datenpräsentation, Erscheinungsbild.
linktitle: Titel
type: docs
weight: 50
url: /de/nodejs-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

In Excel-Diagrammen gibt es 2 Arten von Titeln:
1. Diagrammtitel 
1. Achsentitel

{{% /alert %}}

## **Titeloptionen**
Aspose.Cells for Node.js via C++ ermöglicht auch die Verwaltung von Diagrammtiteln zur Laufzeit. Mit dem [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) Objekt können Sie Text, Schriftart und Füllformat für Titel ändern.

|![todo:image_alt_text](chart_title.png)|

## **Einstellen der Titel von Diagrammen oder Achsen**
Sie können Microsoft Excel verwenden, um in einer WYSIWYG-Umgebung die Titel eines Diagramms und seiner Achsen festzulegen. Aspose.Cells for Node.js via C++ ermöglicht es Entwicklern außerdem, die Titel eines Diagramms und seiner Achsen zur Laufzeit festzulegen. Alle Diagramme und ihre Achsen besitzen eine [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) Eigenschaft, mit der sie ihre Titel setzen können, wie im untenstehenden Beispiel gezeigt.

Das folgende Codebeispiel zeigt, wie man Titel für Diagramme und Achsen setzt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Setting the title of category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Erweiterte Themen**
- [Diagramm-Untertitel aus ODS-Datei lesen](/cells/de/nodejs-cpp/read-chart-subtitle-from-ods-file/)
