---
title: Verwendung von Sparklines und Einstellungen im 3D Format mit Node.js über C++
linktitle: Verwenden von Sparklines und Einstellungen 3D Format
type: docs
weight: 40
url: /de/nodejs-cpp/using-sparklines-and-settings-3d-format/
description: Erfahren Sie, wie Sie Sparklines verwenden und 3D Formatierungen in Excel Dateien mit Aspose.Cells for Node.js via C++ anwenden. 
---

## **Verwendung von Sparklines**
Microsoft Excel 2010 kann Informationen auf vielfältige Weise analysieren. Es ermöglicht Benutzern, wichtige Datentrends mit neuen Datenanalyse- und Visualisierungstools nachzuverfolgen und hervorzuheben. Sparklines sind Mini-Diagramme, die Sie innerhalb von Zellen platzieren können, um Daten und Diagramme in derselben Tabelle anzuzeigen. Wenn Sparklines richtig verwendet werden, ist die Datenanalyse schneller und präziser. Sie bieten auch einen einfachen Überblick über Informationen, vermeiden überfüllte Arbeitsblätter mit vielen belebten Diagrammen.

Aspose.Cells for Node.js via C++ bietet eine API für die Manipulation von Sparklines in Tabellenkalkulationen.
### **Sparklines in Microsoft Excel**
Um Sparklines in Microsoft Excel 2010 einzufügen:

1. Wählen Sie die Zellen aus, in denen die Sparklines erscheinen sollen. Um sie leicht zu sehen, wählen Sie Zellen neben den Daten aus.
1. Klicken Sie auf **Einfügen** im Menüband und wählen Sie dann **Spalte** in der Gruppe **Sparklines** aus.
1. Wählen Sie den Bereich der Zellen im Arbeitsblatt aus oder geben Sie ihn ein, der die Quelldaten enthält. Die Diagramme werden angezeigt.

Sparklines helfen Ihnen, Trends zu erkennen, beispielsweise die Gewinn- oder Verlustbilanz für eine Softball-Liga. Sparklines können sogar die gesamte Saison jedes Teams in der Liga zusammenfassen.
### **Sparklines mit Aspose.Cells for Node.js via C++**
Entwickler können Sparklines (im Template) mit der API von Aspose.Cells for Node.js via C++ erstellen, löschen oder lesen. Die Klassen, die Sparklines verwalten, sind im [SparklineGroupCollection](https://reference.aspose.com/cells/nodejs-cpp/sparklinegroupcollection/) Modul enthalten, daher müssen Sie dieses Modul vor der Verwendung dieser Funktionen importieren.

Durch das ​​Hinzufügen benutzerdefinierter Grafiken für einen bestimmten Datenbereich haben Entwickler die Freiheit, verschiedene Arten von Mini-Diagrammen in ausgewählten Zellbereichen hinzuzufügen.

Das folgende Beispiel zeigt die Sparklines-Funktion. Das Beispiel zeigt, wie man:

1. Eine einfache Vorlagendatei öffnen.
1. Sparklines-Informationen für ein Arbeitsblatt lesen.
1. Neue Sparklines für einen bestimmten Datenbereich zu einem Zellbereich hinzufügen.
1. Speichern Sie die Excel-Datei auf der Festplatte.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Use the following lines if you need to read the Sparklines
// Read the Sparklines from the template file (if it has)
const sparklinesCount = sheet.getSparklineGroups().getCount();

for (let i = 0; i < sparklinesCount; i++)
{
const group = sheet.getSparklineGroups().get(i);
// Display the Sparklines group information e.g type, number of sparklines items
console.log(`sparkline group: type:${group.getType()}, sparkline items count:${group.getSparklines().getCount()}`);
const sparklineCount = sparklineGroup.getSparklines().getCount();
for (let j = 0; j < sparklineCount; j++) 
{
const sparkline = sparklineGroup.getSparklines().get(j);
// Display the individual Sparkines and the data ranges
console.log(`sparkline: row:${sparkline.getRow()}, col:${sparkline.getColumn()}, dataRange:${sparkline.getDataRange()}`);
}
}


// Add Sparklines
// Define the CellArea D2:D10
const ca = AsposeCells.CellArea.createCellArea(1, 4, 7, 4);
// Add new Sparklines for a data range to a cell area
const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "Sheet1!B2:D8", false, ca);
const group = sheet.getSparklineGroups().get(idx);
// Create CellsColor
const clr = workbook.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Save the excel file
workbook.save(path.join(dataDir, "Book1.out.xlsx"));
```
## **Einstellung des 3D-Formats**
Sie benötigen möglicherweise 3D-Diagramm-Styles, um nur die Ergebnisse für Ihr Szenario zu erhalten. Aspose.Cells for Node.js via C++ bietet die entsprechende API, um Microsoft Excel 2007 3D-Formatierungen anzuwenden.

Ein vollständiges Beispiel finden Sie unten, um zu demonstrieren, wie man ein Diagramm erstellt und Microsoft Excel 2007 3D-Formatierung anwendet. Nach Ausführung des Beispielcodes wird ein Spaltendiagramm (mit 3D-Effekten) zum Arbeitsblatt hinzugefügt.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "3d_format.out.xlsx");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Add a Data Worksheet
const dataSheet = book.getWorksheets().add("DataSheet");

// Add Chart Worksheet
const sheet = book.getWorksheets().add("MyChart");

// Put some values into the cells in the data worksheet
dataSheet.getCells().get("B1").putValue(1);
dataSheet.getCells().get("B2").putValue(2);
dataSheet.getCells().get("B3").putValue(3);
dataSheet.getCells().get("A1").putValue("A");
dataSheet.getCells().get("A2").putValue("B");
dataSheet.getCells().get("A3").putValue("C");

// Define the Chart Collection
const charts = sheet.getCharts();
// Add a Column chart to the Chart Worksheet
const chartSheetIdx = charts.add(AsposeCells.ChartType.Column, 5, 0, 25, 15);

// Get the newly added Chart
const chart = book.getWorksheets().get(2).getCharts().get(0);

// Set the background/foreground color for PlotArea/ChartArea
chart.getPlotArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Hide the Legend
chart.setShowLegend(false);

// Add Data Series for the Chart
chart.getNSeries().add("DataSheet!B1:B3", true);
// Specify the Category Data
chart.getNSeries().setCategoryData("DataSheet!A1:A3");

// Get the Data Series
const ser = chart.getNSeries().get(0);

// Apply the 3-D formatting
const spPr = ser.getShapeProperties();
const fmt3d = spPr.getFormat3D();

// Specify Bevel with its height/width
const bevel = fmt3d.getTopBevel();
bevel.setType(AsposeCells.BevelPresetType.Circle);
bevel.setHeight(2);
bevel.setWidth(5);

// Specify Surface material type
fmt3d.setSurfaceMaterialType(AsposeCells.PresetMaterialType.WarmMatte);

// Specify surface lighting type
fmt3d.setSurfaceLightingType(AsposeCells.LightRigType.ThreePoint);

// Specify lighting angle
fmt3d.setLightingAngle(20);

// Specify Series background/foreground and line color
ser.getArea().setBackgroundColor(AsposeCells.Color.Maroon);
ser.getArea().setForegroundColor(AsposeCells.Color.Maroon);
ser.getBorder().setColor(AsposeCells.Color.Maroon);

// Save the Excel file
book.save(filePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
