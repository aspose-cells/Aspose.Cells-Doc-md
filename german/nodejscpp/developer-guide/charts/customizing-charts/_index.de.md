---  
title: Diagramme in Node.js über C++ anpassen  
linktitle: Diagramme anpassen  
description: Lernen Sie, wie Sie Diagramme in Aspose.Cells for Node.js via C++ anpassen. Unser Leitfaden zeigt Ihnen, wie Sie Diagrammlayouts ändern, Datenserien hinzufügen und formatieren, Achsen anpassen und verschiedene Formatierungsoptionen anwenden, um das Erscheinungsbild und die Benutzerfreundlichkeit Ihrer Diagramme zu verbessern.  
keywords: Aspose.Cells for Node.js via C++, Diagrammerstellung, Anpassung, Layouts, Datenserien, Achsen, Formatierung, Erscheinungsbild, Benutzerfreundlichkeit.  
type: docs  
weight: 40  
url: /de/nodejs-cpp/customizing-charts/  
---  

{{% alert color="primary" %}}  

## **Erstellen von benutzerdefinierten Diagrammen**  

Bisher haben wir beim Diskutieren von Diagrammen die Standarddiagramme mit ihren Standard-Formatierungseinstellungen betrachtet. Wir definieren nur die Datenquelle, setzen einige Eigenschaften, und das Diagramm wird mit den Standard-Formatierungen erstellt. Aber Aspose.Cells APIs unterstützen auch die Erstellung benutzerdefinierter Diagramme, mit denen Entwickler eigene Formatierungen vornehmen können.  

Entwickler können benutzerdefinierte Diagramme zur Laufzeit mithilfe von Aspose.Cells erstellen.  

Ein Diagramm besteht aus einer Datensammlung. Jede Datenreihe in Aspose.Cells wird durch ein [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) Objekt dargestellt, während [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) Objekt als Sammlung von [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) Objekten dient. Bei der Erstellung eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Diagrammtypen für verschiedene Datenreihen (gesammelt im [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) Objekt) zu verwenden.  

Der nachstehende Beispielcode zeigt, wie benutzerdefinierte Diagramme erstellt werden können. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir ein Säulendiagramm, kombiniert mit einem Liniendiagramm, dem Arbeitsblatt hinzufügen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(110);
worksheet.getCells().get("B1").putValue(260);
worksheet.getCells().get("B2").putValue(12);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(100);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the chart type of 2nd NSeries to display as line chart
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  

Derzeit unterstützt Aspose.Cells nur benutzerdefinierte Diagramme, die Kreis-, Linien-, Säulen- und Säulenstapel-Diagramme kombinieren, aber in zukünftigen Versionen werden weitere Diagrammtypen unterstützt.  

{{% /alert %}}  

