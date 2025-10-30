---
title: Diagramm mit Node.js über C++ erstellen und verwalten
linktitle: Diagramme
description: Erfahren Sie, wie Sie Aspose.Cells für Node.js verwenden, um Diagramme in Microsoft Excel zu erstellen. Unser Leitfaden zeigt verschiedene Diagrammtypen sowie die Anpassung ihres Erscheinungsbildes und Formats.
keywords: Aspose.Cells für Node.js, Diagrammerstellung, Microsoft Excel, Diagrammtypen, Anpassung, Erscheinungsbild, Formatierung.
type: docs
weight: 130
url: /de/nodejs-cpp/creating-charts/
---

{{% alert color="primary" %}}

Es ist möglich, verschiedene Diagramme zu Tabellenkalkulationen mit Aspose.Cells hinzuzufügen. Aspose.Cells bietet viele flexible Diagrammobjekte. In diesem Themenbereich werden die Diagrammobjekte von Aspose.Cells diskutiert.

{{% /alert %}}

## **Erstellen von Diagrammen**

### **Einfaches Erstellen eines Diagramms**
Das Erstellen eines Diagramms mit Aspose.Cells ist mit den folgenden Beispielcodes einfach:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding sample values to cells
worksheet.getCells().get("A2").putValue("Category1");
worksheet.getCells().get("A3").putValue("Category2");
worksheet.getCells().get("A4").putValue("Category3");

worksheet.getCells().get("B1").putValue("Column1");
worksheet.getCells().get("B2").putValue(4);
worksheet.getCells().get("B3").putValue(20);
worksheet.getCells().get("B4").putValue(50);
worksheet.getCells().get("C1").putValue("Column2");
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("C3").putValue(100);
worksheet.getCells().get("C4").putValue(150);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Setting chart data source as the range "A1:C4"
chart.setChartDataRange("A1:C4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Dinge, die beim Erstellen eines Diagramms zu beachten sind**

Bevor Sie Diagramme erstellen, ist es wichtig, einige grundlegende Konzepte zu verstehen, die beim Erstellen von Diagrammen mit Aspose.Cells hilfreich sind.

#### **Diagrammobjekte**

Die Diagrammobjekte sind unten aufgelistet:

- Serie, eine einzelne Datenreihe in einem Diagramm.
- Achse, die Achse eines Diagramms.
- Diagramm, ein einzelnes Excel-Diagramm.
- Diagrammbereich, der Diagrammbereich im Arbeitsblatt.
- Diagrammdaten Tabelle, eine Diagrammdatentabelle.
- Diagrammrahmen, das Rahmenobjekt in einem Diagramm.
- Diagrammpunkt, ein einzelner Punkt in einer Serie in einem Diagramm.
- Diagrammpunktsammlung, eine Sammlung, die alle Punkte in einer Serie enthält.
- Diagramme, eine Sammlung von Diagrammobjekten.
- Datenbeschriftungen, eine Sammlung aller Datenbeschriftungsobjekte für die angegebene Serie.
- Füllformat, Füllformat für eine Form.
- Boden, der Boden eines 3D-Diagramms.
- Legende, die Diagrammlegende.
- Linie, die Diagrammlinie.
- Seriensammlung, eine Sammlung von Serienobjekten.
- Achsenbeschriftungen, die Achsenbeschriftungen, die mit den Achsenmarkierungen auf einer Diagrammachse verbunden sind.
- Titel, der Titel eines Diagramms oder einer Achse.
- Trendlinie, eine Trendlinie in einem Diagramm.
- Trendliniensammlung, eine Sammlung aller Trendlinienobjekte für die angegebene Datenserie.
- Wände, die Wände eines 3D-Diagramms.

#### **Verwendung von Diagrammobjekten**

Wie oben erwähnt, sind alle Diagrammobjekte Instanzen ihrer jeweiligen Klassen und bieten spezifische Eigenschaften und Methoden zur Ausführung bestimmter Aufgaben. Verwenden Sie Diagrammobjekte, um Diagramme zu erstellen.

Fügen Sie jedem Arbeitsblatt mithilfe der [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--)-Sammlung beliebige Diagrammtypen hinzu. Jedes Element in der [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--)-Sammlung stellt ein [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)-Objekt dar. Ein [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)-Objekt kapselt alle anderen Diagrammobjekte ein, die erforderlich sind, um das Erscheinungsbild des Diagramms anzupassen. Der nächste Abschnitt zeigt, wie man einige grundlegende Diagrammobjekte verwendet, um ein einfaches Diagramm zu erstellen.

### **Diagramm mit Aspose.Cells erstellen**

**Schritte:**

1. Fügen Sie einige Daten zu den Zellen des Arbeitsblatts mit der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell/)-Methode des [**putValue(string)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-string-)-Objekts hinzu.
   Dies wird als Datenquelle für das Diagramm verwendet.
1. Fügen Sie dem Arbeitsblatt ein Diagramm hinzu, indem Sie die [**add**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection/#add-charttype-number-number-number-number-)-Methode der [**ChartCollection**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection)-Sammlung aufrufen, eingeschlossen im [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/)-Objekt.
1. Geben Sie den Diagrammtyp mit der [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/)-Aufzählung an.
   Das folgende Beispiel verwendet den [**ChartType.Pyramid**](https://reference.aspose.com/cells/nodejs-cpp/charttype)-Wert als Diagrammtyp.
1. Greifen Sie auf das neue [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)-Objekt aus der [**Charts**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection)-Sammlung zu, indem Sie dessen Index übergeben.
1. Nutzen Sie eines der im [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)-Objekt gekapselten Diagrammobjekte, um das Diagramm zu verwalten.
   Das folgende Beispiel verwendet das [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/)-Diagrammobjekt, um die Datenquelle des Diagramms anzugeben.

Beim Hinzufügen von Quelldaten zum Diagramm kann die Datenquelle ein Zellbereich sein (wie "A1:C3"), oder eine Sequenz von Nicht-Zusammenhängenden Zellen (wie "A1, A3, A5") oder eine Sequenz von Werten (wie "1,2,3").

Diese allgemeinen Schritte ermöglichen es Ihnen, beliebige Arten von Diagrammen zu erstellen. Verwenden Sie verschiedene Diagrammobjekte, um verschiedene Diagramme zu erstellen.

Es ist möglich, mit Aspose.Cells viele verschiedene Arten von Diagrammen zu erstellen. Alle von Aspose.Cells unterstützten Standarddiagramme sind in einer Aufzählung namens [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) vordefiniert.

Die vordefinierten Diagrammtypen sind:

|**Diagrammtypen**|**Beschreibung**|
| :- | :- |
|Column|Stellt gruppiertes Säulendiagramm dar|
|ColumnStacked|Stellt gestapeltes Säulendiagramm dar|
|Column100PercentStacked|Stellt zu 100 % gestapeltes Säulendiagramm dar|
|Column3DClustered|Stellt 3D-gruppiertes Säulendiagramm dar|
|Column3DStacked|Stellt 3D-gestapeltes Säulendiagramm dar|
|Column3D100PercentStacked|Stellt 3D-100%-gestapeltes Säulendiagramm dar|
|Column3D|Stellt 3D-Säulendiagramm dar|
|Bar|Stellt gestapeltes Balkendiagramm dar|
|BarStacked|Stellt gestapeltes Balkendiagramm dar|
|Bar100PercentStacked|Stellt 100%-gestapeltes Balkendiagramm dar|
|Bar3DClustered|Stellt 3D-gruppiertes Balkendiagramm dar|
|Bar3DStacked|Stellt 3D-gestapeltes Balkendiagramm dar|
|Bar3D100PercentStacked|Stellt 3D-100%-gestapeltes Balkendiagramm dar|
|Line|Stellt Liniendiagramm dar|
|LineStacked|Stellt gestapeltes Liniendiagramm dar|
|Line100PercentStacked|Stellt 100%-gestapeltes Liniendiagramm dar|
|LineWithDataMarkers|Stellt Liniendiagramm mit Datenmarkierungen dar|
|LineStackedWithDataMarkers|Stellt gestapeltes Liniendiagramm mit Datenmarkierungen dar|
|Line100PercentStackedWithDataMarkers|Stellt 100%-gestapeltes Liniendiagramm mit Datenmarkierungen dar|
|Line3D|Stellt 3D-Liniendiagramm dar|
|Pie|Stellt Tortendiagramm dar|
|Pie3D|Stellt 3D-Tortendiagramm dar|
|PiePie|Stellt Tortendiagramm von Tortendiagramm dar|
|PieExploded|Stellt explodiertes Tortendiagramm dar|
|Pie3DExploded|Stellt ein 3D-Sprengkuchendiagramm dar|
|PieBar|Stellt Balken eines Kuchendiagramms dar|
|Scatter|Stellt ein Scatter-Diagramm dar|
|ScatterConnectedByCurvesWithDataMarker|Stellt ein Scatter-Diagramm dar, das durch Kurven verbunden ist, mit Datenmarkierungen|
|ScatterConnectedByCurvesWithoutDataMarker|Stellt ein Scatter-Diagramm dar, das durch Kurven verbunden ist, ohne Datenmarkierungen|
|ScatterConnectedByLinesWithDataMarker|Stellt ein Scatter-Diagramm dar, das durch Linien verbunden ist, mit Datenmarkierungen|
|ScatterConnectedByLinesWithoutDataMarker|Stellt ein Scatter-Diagramm dar, das durch Linien verbunden ist, ohne Datenmarkierungen|
|Area|Stellt ein Flächendiagramm dar|
|AreaStacked|Stellt ein gestapeltes Flächendiagramm dar|
|Area100PercentStacked|Stellt ein 100 % gestapeltes Flächendiagramm dar|
|Area3D|Stellt ein 3D-Flächendiagramm dar|
|Area3DStacked|Stellt ein 3D-gestapeltes Flächendiagramm dar|
|Area3D100PercentStacked|Stellt ein 3D-100 %-gestapeltes Flächendiagramm dar|
|Doughnut|Stellt ein Doughnut-Diagramm dar|
|DoughnutExploded|Stellt ein explodiertes Doughnut-Diagramm dar|
|Radar|Stellt ein Radar-Diagramm dar|
|RadarWithDataMarkers|Stellt ein Radar-Diagramm mit Datenmarkierungen dar|
|RadarFilled|Stellt ein gefülltes Radar-Diagramm dar|
|Surface3D|Stellt ein 3D-Oberflächendiagramm dar|
|SurfaceWireframe3D|Stellt ein drahtgerahmtes 3D-Oberflächendiagramm dar|
|SurfaceContour|Stellt Konturdiagramm dar|
|SurfaceContourWireframe|Stellt Drahtgitter-Konturdiagramm dar|
|Bubble|Stellt Blasendiagramm dar|
|Bubble3D|Stellt 3D-Blasendiagramm dar|
|Cylinder|Stellt Zylinderdiagramm dar|
|CylinderStacked|Stellt gestapeltes Zylinderdiagramm dar|
|Cylinder100PercentStacked|Stellt 100 % gestapeltes Zylinderdiagramm dar|
|CylindericalBar|Stellt zylindrisches Balkendiagramm dar|
|CylindericalBarStacked|Stellt gestapeltes zylindrisches Balkendiagramm dar|
|CylindericalBar100PercentStacked|Stellt 100 % gestapeltes zylindrisches Balkendiagramm dar|
|CylindericalColumn3D|Stellt 3D-Säulendiagramm dar|
|Cone|Stellt Kegeldiagramm dar|
|ConeStacked|Stellt gestapeltes Kegeldiagramm dar|
|Cone100PercentStacked|Stellt 100 % gestapeltes Kegeldiagramm dar|
|ConicalBar|Stellt konisches Balkendiagramm dar|
|ConicalBarStacked|Stellt gestapeltes konisches Balkendiagramm dar|
|ConicalBar100PercentStacked|Stellt 100 % gestapeltes konisches Balkendiagramm dar|
|ConicalColumn3D|Stellt 3D-konisches Säulendiagramm dar|
|Pyramid|Stellt Pyramiden-Diagramm dar|
|PyramidStacked|Stellt gestapeltes Pyramiden-Diagramm dar|
|Pyramid100PercentStacked|Stellt 100% gestapeltes Pyramidendiagramm dar|
|PyramidBar|Stellt Pyramidensäulendiagramm dar|
|PyramidBarStacked|Stellt gestapeltes Pyramidensäulendiagramm dar|
|PyramidBar100PercentStacked|Stellt 100% gestapeltes Pyramidensäulendiagramm dar|
|PyramidColumn3D|Stellt 3D-Pyramiden-Säulendiagramm dar|
{{% alert color="primary" %}}

Wenn Sie einen Zellbereich als Datenquelle zuweisen, können Sie den Bereich nur von oben links nach unten rechts festlegen. Zum Beispiel ist "A1:C3" gültig, während "C3:A1" ungültig ist.

{{% /alert %}}

#### **Pyramiden-Diagramm**

Wenn der Beispielcode ausgeführt wird, wird ein Pyramiden-Diagramm dem Arbeitsblatt hinzugefügt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Linien-Diagramm**

Im obigen Beispiel erzeugt das Ändern von [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) zu *Line* ein Liniendiagramm. Der vollständige Quellcode ist unten. Wenn der Code ausgeführt wird, wird ein Liniendiagramm dem Arbeitsblatt hinzugefügt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Bubble-Diagramm**

Um ein Blasendiagramm zu erstellen, muss [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) auf [**ChartType.Bubble**](https://reference.aspose.com/cells/nodejs-cpp/charttype) gesetzt werden und einige zusätzliche Eigenschaften wie BubbleSizes, Values & XValues müssen entsprechend eingestellt werden. Nach Ausführung des folgenden Codes wird ein Blasendiagramm zum Arbeitsblatt hinzugefügt.

#### **Liniendiagramm mit Datenmarkierungen**

Um ein Linien-Diagramm mit Datenmarkern zu erstellen, muss [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) auf *ChartType.LineWithDataMarkers* gesetzt werden und einige zusätzliche Eigenschaften wie Hintergrundbereich, Serienmarkierungen, Werte & XValues müssen entsprechend eingestellt werden. Nach Ausführung des folgenden Codes wird ein Linien-Diagramm mit Datenmarkern zum Arbeitsblatt hinzugefügt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set columns title 
worksheet.getCells().get(0, 0).putValue("X");
worksheet.getCells().get(0, 1).putValue("Y");

// Random data shall be used for generating the chart
// Create random data and save in the cells
for (let i = 1; i < 21; i++) {
worksheet.getCells().get(i, 0).putValue(i);
worksheet.getCells().get(i, 1).putValue(0.8);
}

for (let i = 21; i < 41; i++) {
worksheet.getCells().get(i, 0).putValue(i - 20);
worksheet.getCells().get(i, 1).putValue(0.9);
}
// Add a chart to the worksheet
const idx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

// Access the newly created chart
const chart = worksheet.getCharts().get(idx);

// Set chart style
chart.setStyle(3);

// Set autoscaling value to true
chart.setAutoScaling(true);

// Set foreground color white
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Set Properties of chart title
chart.getTitle().setText("Sample Chart");

// Set chart type
chart.setType(AsposeCells.ChartType.LineWithDataMarkers);

// Set Properties of categoryaxis title
chart.getCategoryAxis().getTitle().setText("Units");

//Set Properties of nseries
const s2_idx = chart.getNSeries().add("A2:A2", true);
const s3_idx = chart.getNSeries().add("A22:A22", true);

// Set IsColorVaried to true for varied points color
chart.getNSeries().setIsColorVaried(true);

// Set properties of background area and series markers
chart.getNSeries().get(s2_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s2_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Yellow);
chart.getNSeries().get(s2_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s2_idx).setXValues("A2:A21");
chart.getNSeries().get(s2_idx).setValues("B2:B21");

// Set properties of background area and series markers
chart.getNSeries().get(s3_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s3_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(s3_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s3_idx).setXValues("A22:A41");
chart.getNSeries().get(s3_idx).setValues("B22:B41");

// Save the workbook
workbook.save(path.join(dataDir, "LineWithDataMarkerChart.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Erweiterte Themen**
- [Excel 2016 Diagramme lesen und bearbeiten](/cells/de/nodejs-cpp/read-and-manipulate-excel-2016-charts/)
- [Achsen von Excel-Diagrammen verwalten](/cells/de/nodejs-cpp/chart-axes/)
- [Diagrammaussehen festlegen](/cells/de/nodejs-cpp/setting-chart-appearance/)
- [Diagrammtypen](/cells/de/nodejs-cpp/chart-types/)
- [Diagramme anpassen](/cells/de/nodejs-cpp/customizing-charts/)
- [Datenquelle für das Diagramm festlegen](/cells/de/nodejs-cpp/data-formatting-in-charts/)
- [Datenbeschriftungen von Excel-Diagrammen verwalten](/cells/de/nodejs-cpp/insert-datalabels-to-chart/)
- [Arbeitsblatt des Diagramms erhalten](/cells/de/nodejs-cpp/get-worksheet-of-the-chart/)
- [Legende von Excel-Diagrammen verwalten](/cells/de/nodejs-cpp/chart-legend/)
- [Position Size und Gestaltung von Diagrammen bearbeiten](/cells/de/nodejs-cpp/manipulate-position-size-and-designer-chart/)
- [Erstellen eines Tortendiagramms mit Führungslinien](/cells/de/nodejs-cpp/creating-pie-chart-with-leader-lines/)
- [Formen in Diagrammen](/cells/de/nodejs-cpp/controls-in-charts/)
- [Titel von Excel-Diagrammen verwalten](/cells/de/nodejs-cpp/chart-and-axis-titles/)
- [Diagrammrendering](/cells/de/nodejs-cpp/chart-rendering/)
- [Gleichungstext der Trendlinie des Diagramms abrufen](/cells/de/nodejs-cpp/get-equation-text-of-chart-trendline/)
{{< app/cells/assistant language="nodejs-cpp" >}}
