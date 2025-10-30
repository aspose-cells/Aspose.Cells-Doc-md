---  
title: Verwalten Sie DataLabels von Excel Diagrammen mit Node.js über C++  
description: Erfahren Sie, wie Sie Data Labels in Excel Diagrammen mit Aspose.Cells for Node.js via C++ effektiv verwalten. Dieser umfassende Leitfaden behandelt verschiedene Verwaltungsaufgaben, einschließlich Hinzufügen, Entfernen und Ändern von Labels, um die Lesbarkeit und Benutzerfreundlichkeit des Diagramms zu verbessern.  
keywords: Aspose.Cells für Node.js, Excel Diagramme, Datenbeschriftungen, Verwaltung, Lesbarkeit, Benutzerfreundlichkeit, Hinzufügen, Entfernen, Ändern.  
linktitle: Datenbeschriftungen  
type: docs  
weight: 50  
url: /de/nodejs-cpp/insert-datalabels-to-chart/  
---  

{{% alert color="primary" %}}  

Datenbeschriftungen sind ein wichtiger Bestandteil eines Diagramms.  
Wir können leicht den Wert, den Prozentsatz usw. jeder Serie erfahren.  

{{% /alert %}}  

## **Datenbeschriftungen-Optionen**  
Aspose.Cells for Node.js via C++ ermöglicht auch die Verwaltung der Datenbeschriftungen des Diagramms zur Laufzeit mit dem [DataLabels]-Objekt. Es ist einfach, Datenbeschriftungen des Diagramms zu verschieben, zu aktualisieren und zu formatieren.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Verwalten der Datenbeschriftungen eines Diagramms**  
Die Verwaltung der Datenbeschriftungen des Diagramms mit Aspose.Cells [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/) ist einfach.  

Der folgende Codeausschnitt zeigt, wie DataLabels verwaltet werden können:  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

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

// Show value labels
chart.getNSeries().get(0).getDataLabels().setShowValue(true);
// Show series name labels
chart.getNSeries().get(1).getDataLabels().setShowSeriesName(true);
// Move labels to center
chart.getNSeries().get(1).getDataLabels().setPosition(AsposeCells.LabelPositionType.Center);

// Save the file
workbook.save("chart_datalabels.xlsx");
```  

## **Erweiterte Themen**  
- [Hinzufügen von benutzerdefinierten Beschriftungen zu Datenpunkten in der Serie des Diagramms](/cells/de/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Textumbruch für Datenbeschriftungen des Diagramms deaktivieren](/cells/de/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Ändern der Größe der Datenbeschriftungsform des Diagramms, um den Text anzupassen](/cells/de/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Benutzerdefinierte Datenauswahl im Diagrammpunkt](/cells/de/nodejs-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Festlegen des Formtyps von Datenbeschriftungen des Diagramms](/cells/de/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Anzeigen von Zellenbereichen als Datenbeschriftungen](/cells/de/nodejs-cpp/showing-cell-range-as-the-data-labels/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
