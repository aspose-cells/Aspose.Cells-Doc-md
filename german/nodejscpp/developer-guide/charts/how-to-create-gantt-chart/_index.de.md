---
title: So erstellen Sie ein Gantt Diagramm mit Node.js über C++
linktitle: So erstellen Sie ein Gantt Diagramm
type: docs
weight: 72
url: /de/nodejs-cpp/how-to-create-gantt-chart/
description: Lernen Sie, wie Sie mit der API Aspose.Cells for Node.js via C++ ein Gantt Diagramm erstellen.
keywords: Node.js erstellt ein Gantt Diagramm, fügt ein Gantt Diagramm hinzu, inseriert ein Gantt Diagramm
---

## **Was ist ein Gantt-Diagramm?**

Ein Gantt-Diagramm ist eine Art Balkendiagramm, das einen Projektzeitplan veranschaulicht. Es zeigt die Anfangs- und Enddaten der verschiedenen Elemente eines Projekts. Jede Aufgabe oder Aktivität wird durch einen Balken dargestellt, dessen Länge ihrer Dauer entspricht. Gantt-Diagrams zeigen auch Abhängigkeiten zwischen Aufgaben, sodass Projektmanager die Reihenfolge der Aufgaben visualisieren können. Sie werden häufig im Projektmanagement verwendet, um Projekte effektiv zu planen, zu planen und zu verfolgen.

## **So erstellen Sie ein Gantt-Diagramm in Excel**

Sie können in Excel ein Gantt-Diagramm erstellen, indem Sie diese Schritte befolgen:
1. Fügen Sie einige Daten für das Gantt-Diagramm hinzu. 
<br>
<img src="00.png" width=50% />
1. Wählen Sie die Daten aus und gehen Sie zu Einfügen --> Diagramme --> Säulen- oder Balkendiagramm einfügen --> Gestapeltes Balkendiagramm. In unserem Beispiel sind das B1:B7, dann fügen Sie ein **Gestapeltes Balken**-Diagramm ein.
<br>
<img src="1.png" width=50% />

1. Wählen Sie das Diagramm aus, **Daten auswählen** -> **Hinzufügen**, stellen Sie den **Seriennamen** und die **Serienwerte** wie folgt ein.
<br>
<img src="2.png" width=50% />

1. Wählen Sie das Diagramm aus, bearbeiten Sie die **Horizontalen (Kategorie) Achsenbeschriftungen**.
<br>
<img src="3.png" width=50% />

1. **Achse formatieren** des Y-Achse, wählen Sie **Kategorien umkehren**.
1. Wählen Sie die **Blaue Serie** und setzen Sie die **Füllung -> Keine Füllung**.
1. **Achse formatieren** der X-Achse, setzen Sie die **Minimale und Maximale Werte** (01.05.2019:43470, 30.01.2019:43494).
<br>
<img src="4.png" width=50% />

1. **Datenbeschriftungen hinzufügen** für das Diagramm, jetzt erhalten Sie ein Gantt-Diagramm.
<br>
<img src="0.png" width=50% />


## **So fügen Sie ein Gantt-Diagramm in Aspose.Cells hinzu**
Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die [Beispiel-Excel-Datei](sample.xlsx), die einige Beispieldaten enthält. Anschließend erstellt es das gestapelte Balkendiagramm basierend auf den Anfangsdaten und setzt die entsprechenden Eigenschaften. Schließlich speichert es die Arbeitsmappe im [Ausgabe XLSX-Format](result.xlsx). Der folgende Screenshot zeigt das von Aspose.Cells erstellte Gantt-Diagramm in der Ausgabedatei.
<br>
<img src="5.png" width=60% />

### **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Create BarStacked Chart
const i = worksheet.getCharts().add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(i);
// Set the chart title name 
chart.getTitle().setText("Gantt Chart");
// Set the chart title is Visible
chart.getTitle().setIsVisible(true);
// Set data range
chart.setChartDataRange("B1:B6", true);
// Add series data range
chart.getNSeries().add("C2:C6", true);
// No fill for one serie
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set the Horizontal(Category) Axis
chart.getNSeries().setCategoryData("A2:A6");
// Reverse the Horizontal(Category) Axis
chart.getCategoryAxis().setIsPlotOrderReversed(true);
// Set the value axis's MinValue and MaxValue
const minValue = parseFloat(worksheet.getCells().get("B2").getValue());
const maxValue = parseFloat(worksheet.getCells().get("D6").getValue());
chart.getValueAxis().setMinValue(isNaN(minValue) ? 0 : minValue);
chart.getValueAxis().setMaxValue(isNaN(maxValue) ? 0 : maxValue);
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Show the DataLabels
chart.getNSeries().get(1).getDataLabels().setShowValue(true);
// Disable the Legend
chart.setShowLegend(false);
// Save the result
workbook.save("result.xlsx");
```

