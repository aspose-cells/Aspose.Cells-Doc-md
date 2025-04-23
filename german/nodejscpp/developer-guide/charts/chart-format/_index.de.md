---
title: Diagrammoptik mit Node.js über C++ einstellen
description: Erfahren Sie, wie Sie das Erscheinungsbild von Diagrammen in Aspose.Cells for Node.js via C++ konfigurieren. Unser Leitfaden zeigt Ihnen, wie Sie Diagrammlayouts, Farben, Schriftarten und Effekte ändern, um den gewünschten visuellen Stil zu erreichen und Ihre Arbeitsblätter zu verbessern.
keywords: Aspose.Cells for Node.js via C++, Diagrammerstellung, Diagrammoptik, Layouts, Farben, Schriftarten, Effekte, Arbeitsblätter.
linktitle: Diagrammformat
type: docs
weight: 20
url: /de/nodejs-cpp/setting-chart-appearance/
---

## **Diagrammaussehen festlegen**
In How to Create a Chart haben wir eine kurze Einführung in die Arten von Diagrammen und Diagrammobjekten gegeben, die von Aspose.Cells angeboten werden, und beschrieben, wie man eines erstellt. In diesem Artikel wird erläutert, wie das Erscheinungsbild von Diagrammen durch Festlegen ihrer Eigenschaften angepasst werden kann:

- Festlegen des Diagrammbereichs.
- Festlegen von Diagrammlinien.
- Anwenden von Designs.
- Titel für Diagramme und Achsen festlegen.
- Arbeiten mit Gitterlinien.

### **Diagrammbereich einstellen**
Es gibt verschiedene Arten von Bereichen in einem Diagramm und Aspose.Cells bietet die Flexibilität, das Erscheinungsbild jedes Bereichs zu ändern. Entwickler können verschiedene Formatierungseinstellungen auf einen Bereich anwenden, indem sie seine Vordergrundfarbe, Hintergrundfarbe und Füllformat usw. ändern.

Im untenstehenden Beispiel haben wir verschiedene Formatierungseinstellungen auf verschiedene Arten von Bereichen eines Diagramms angewendet. Diese Bereiche umfassen:

- Plot-Bereich
- Diagrammbereich
- SeriesCollection Bereich
- Fläche eines einzelnen Punktes in einer SeriesCollection

Der folgende Codeschnipsel zeigt, wie der Diagrammbereich festgelegt wird.

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
chart.getPlotArea().getArea().setForegroundColor(new AsposeCells.Color(0, 0, 255));

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(new AsposeCells.Color(255, 255, 0));

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(255, 0, 0));

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(new AsposeCells.Color(0, 255, 255));

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(new AsposeCells.Color(0, 255, 0), 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Einstellen von Diagramm Linien**
Entwickler können auch verschiedene Arten von Stilen auf die Linien oder Datenmarker der [SerienSammlung](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) anwenden. Das folgende Codebeispiel zeigt, wie man Diagrammlinien mit der Aspose.Cells API festlegt.

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

// Applying a dotted line style on the lines of a SeriesCollection
chart.getNSeries().get(0).getBorder().setStyle(AsposeCells.LineType.Dot);

// Applying a triangular marker style on the data markers of a SeriesCollection
chart.getNSeries().get(0).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Triangle);

// Setting the weight of all lines in a SeriesCollection to medium
chart.getNSeries().get(1).getBorder().setWeight(AsposeCells.WeightType.MediumLine);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Anwendung von Microsoft Excel 2007/2010-Themen auf Diagramme**
Entwickler können verschiedene Microsoft Excel-Themen/Farben auf die [SerienSammlung](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) oder andere Diagrammobjekte anwenden, wie im Beispiel unten gezeigt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_chart.xlsx");

// Loads the workbook containing the chart
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first chart in the sheet
const chart = worksheet.getCharts().get(0);

// Specify the FillFormat's type to Solid Fill of the first series
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.Solid);

// Get the CellsColor of SolidFill
const cc = chart.getNSeries().get(0).getArea().getFillFormat().getSolidFill().getCellsColor();

// Create a theme in Accent style
cc.setThemeColor(new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent6, 0.6));

// Apply the theme to the series
chart.getNSeries().get(0).getArea().getFillFormat().getSolidFill().setCellsColor(cc);

// Save the Excel file
workbook.save(path.join(dataDir, "output.out.xlsx"));
```

### **Einstellen der Titel von Diagrammen oder Achsen**
Sie können Microsoft Excel verwenden, um die Titel eines Diagramms und seiner Achsen in einer WYSIWYG-Umgebung festzulegen. Aspose.Cells ermöglicht es Entwicklern auch, die Titel eines Diagramms und seiner Achsen zur Laufzeit festzulegen. Alle Diagramme und ihre Achsen enthalten eine [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) Eigenschaft, mit der ihre Titel festgelegt werden können, wie im Beispiel unten gezeigt.

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

### **Arbeiten mit Haupt-Gitterlinien**
Es ist möglich, das Aussehen der Haupt-Gitterlinien anzupassen. Gitterlinien ausblenden oder anzeigen, oder ihre Farbe und andere Einstellungen definieren. Nachfolgend zeigen wir, wie die Gitterlinien ausgeblendet und wie ihre Farbe geändert wird.

#### **Ausblenden von Haupt-Gitterlinien**
Entwickler können die Sichtbarkeit der Hauptgitterlinien steuern, indem sie die [isVisible()](https://reference.aspose.com/cells/nodejs-cpp/line/#isVisible--) Eigenschaft des [Linie](https://reference.aspose.com/cells/nodejs-cpp/line/) Objekts auf **true** oder **false** setzen.

Das folgende Codebeispiel zeigt, wie Hauptgitterlinien ausgeblendet werden. Nach dem Ausblenden der Hauptgitterlinien wird ein Säulendiagramm zur Arbeitsblatt hinzugefügt, bei dem keine Gitterlinien vorhanden sind.

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

// Hiding the major gridlines of Category Axis
chart.getCategoryAxis().getMajorGridLines().setIsVisible(false);

// Hiding the major gridlines of Value Axis
chart.getValueAxis().getMajorGridLines().setIsVisible(false);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

#### **Ändern der Einstellungen für Haupt-Gitterlinien**
Entwickler können nicht nur die Sichtbarkeit der Haupt-Gitterlinien, sondern auch andere Eigenschaften wie deren Farbe usw. steuern.

Das folgende Codebeispiel zeigt, wie man die Farbe der Hauptgitterlinien ändert. Nach dem Festlegen der Farbe der Hauptgitterlinien wird ein Säulendiagramm mit modifizierten Gitterlinien zum Arbeitsblatt hinzugefügt.

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

// Setting the color of Category Axis' major gridlines to silver
chart.getCategoryAxis().getMajorGridLines().setColor(AsposeCells.Color.Silver);

// Setting the color of Value Axis' major gridlines to red
chart.getValueAxis().getMajorGridLines().setColor(AsposeCells.Color.Red);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Erweiterte Themen**
- [Setzen des Werteformatcodes der Diagrammserie](/cells/de/nodejs-cpp/set-the-values-format-code-of-chart-series/)
- [Bild als Hintergrundfüllung im Diagramm festlegen](/cells/de/nodejs-cpp/set-picture-as-background-fill-in-the-chart/)


