---  
title: Datenquelle für das Diagramm mit Node.js über C++ festlegen  
description: Erfahren Sie mehr über die verschiedenen Datenquellen, die von Aspose.Cells for Node.js via C++ unterstützt werden. Unser Leitfaden führt Sie durch die unterschiedlichen Arten von Datenquellen, die verfügbar sind, und zeigt Ihnen, wie Sie sich verbinden und Daten abrufen, um Ihre Tabellen zu füllen.  
keywords: Aspose.Cells for Node.js via C++, Diagrammerstellung, Datenformatierung, Beschriftungen, Farben, Schriftarten, Erscheinungsbild, Benutzerfreundlichkeit.  
linktitle: Datenquelle  
type: docs  
weight: 10  
url: /de/nodejs-cpp/data-formatting-in-charts/  
---  

In unseren vorherigen Themen haben wir bereits viele Beispiele gezeigt, wie Sie eine Datenquelle für Ihr Diagramm festlegen können. In diesem Thema werden wir jedoch weitere Details zu den Arten von Daten bereitstellen, die für ein Diagramm eingestellt werden können.

## **Festlegen von Diagrammdaten**

Es gibt zwei Arten von Daten, mit denen Sie beim Arbeiten an Diagrammen mit Aspose.Cells umgehen können:

- Diagrammdaten.
- Kategoriedaten.

### **Diagrammdaten**

Diagrammdaten sind die Daten, die wir als Datenquelle verwenden, um unsere Diagramme zu erstellen. Wir können einen Zellbereich (mit Diagrammdaten) hinzufügen, indem wir die [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)-Eigenschaft des [**add(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#add-string-boolean-)-Objekts aufrufen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(300);
worksheet.getCells().get("B1").putValue(160);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Kategoriedaten**

Kategoriedaten werden zur Beschriftung der Diagrammdaten verwendet und können [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) mit seiner [**getCategoryData()**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#getCategoryData--)-Eigenschaft hinzugefügt werden. Ein vollständiges Beispiel wird unten gegeben, um die Verwendung von Diagramm- und Kategoriedaten zu demonstrieren. Nach Ausführung des oben genannten Beispielcodes wird ein Säulendiagramm wie unten gezeigt dem Arbeitsblatt hinzugefügt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(10);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(200);
worksheet.getCells().get("B1").putValue(120);
worksheet.getCells().get("B2").putValue(320);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the data source for the category data of SeriesCollection
chart.getNSeries().setCategoryData("C1:C4");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Erweiterte Themen**  
- [Ändern der Datenquelle des Diagramms zur Zieltabelle beim Kopieren von Zeilen oder Bereichen](/cells/de/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [Dynamische Diagramme erstellen](/cells/de/nodejs-cpp/create-dynamic-charts/)  
- [Einfacher Weg zur Diagrammeinrichtung mit der Methode Chart.SetChartDataRange](/cells/de/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden](/cells/de/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)  
{{< app/cells/assistant language="nodejs-cpp" >}}
