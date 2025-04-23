---  
title: Achsen von Excel Diagrammen mit Node.js über C++ verwalten  
description: Lernen Sie, wie Sie Achsen in Diagrammen in Aspose.Cells for Node.js via C++ konfigurieren. Unser Leitfaden zeigt Ihnen, wie Sie die primären und sekundären Achsen anpassen, ihre Bereiche festlegen und ihre Eigenschaften ändern, um Ihre Diagramme zu verbessern.  
keywords: Aspose.Cells for Node.js via C++, Diagrammachsen, Konfiguration, primäre Achsen, sekundäre Achsen, Bereich, Eigenschaften.  
linktitle: Achsen  
type: docs  
weight: 50  
url: /de/nodejs-cpp/chart-axes/  
---  

{{% alert color="primary" %}}  

In Excel-Diagrammen gibt es 3 Arten von Achsen:  
1. Horizontale (Kategorie) Achse : X-Achse  
1. Vertikale(Wert) Achse: Y-Achse  
1. Tiefen(Serien) Achse: Z-Achse  

{{% /alert %}}  

## **Achsenoptionen**  
Aspose.Cells for Node.js via C++ ermöglicht es Ihnen auch, die Achsen eines Diagramms zur Laufzeit zu verwalten. Mit dem [Achse](https://reference.aspose.com/cells/nodejs-cpp/axis/) Objekt können Sie alle Optionen der Achse so ändern, wie es in Excel gemacht wird.  

|![todo:image_alt_text](chart_axes.png)|  

## **X- und Y-Achsen verwalten**  
In Excel-Diagrammen sind horizontale und vertikale Achsen die beiden beliebtesten Achsen.  

Das folgende Codebeispiel zeigt, wie man die Optionen der X- und Y-Achsen festlegt.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart_axes.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue("Series1");
worksheet.getCells().get("A2").putValue(50);
worksheet.getCells().get("A3").putValue(100);
worksheet.getCells().get("A4").putValue(150);
worksheet.getCells().get("B1").putValue("Series2");
worksheet.getCells().get("B2").putValue(60);
worksheet.getCells().get("B3").putValue(32);
worksheet.getCells().get("B4").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);

// Hiding X axis
chart.getCategoryAxis().setIsVisible(false);

// Setting max value of Y axis
chart.getValueAxis().setMaxValue(200);
// Setting major unit
chart.getValueAxis().setMajorUnit(50);

// Save the file
workbook.save(filePath);
```  

## **Erweiterte Themen**  
- [Ändern der Richtung der Markierungstexte](/cells/de/nodejs-cpp/change-tick-label-direction/)  
- [Bestimmen Sie, welche Achse im Diagramm existiert](/cells/de/nodejs-cpp/determine-which-axis-exists-in-the-chart/)  
- [Behandeln Sie automatische Einheiten der Diagrammachse wie Microsoft Excel](/cells/de/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Lesen Sie die Achsenbeschriftungen nach der Berechnung des Diagramms](/cells/de/nodejs-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Wie man die Kategorieachse im Excel-Diagramm einstellt](/cells/de/nodejs-cpp/how-to-set-category-axis/)  

