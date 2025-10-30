---
title: So erstellen Sie ein Tornado Diagramm mit Node.js via C++
linktitle: Wie man ein Tornado Diagramm erstellt
type: docs
weight: 73
url: /de/nodejs-cpp/create-tornado-chart/
description: Lernen Sie, wie Sie mit der API Aspose.Cells for Node.js via C++ ein Tornado Diagramm erstellen.
keywords: Node.js ein Tornado Diagramm erstellen, ein Tornado Diagramm hinzufügen, ein Tornado Diagramm einfügen
---

## **Einführung**
Ein Tornado-Diagramm, auch als Tornado-Diagramm oder Tornado-Grafik bekannt, ist eine Art der Datendarstellung, die oft für die Sensitivitätsanalyse in Excel verwendet wird. Es hilft Ihnen, den Einfluss von sich ändernden Variablen auf ein bestimmtes Ergebnis oder Resultat zu verstehen.

## **Wie man ein Tornado-Diagramm in Excel erstellt**
Sie können ein Tornado-Diagramm in Excel erstellen, indem Sie diesen Schritten folgen:
1. Wählen Sie die Daten aus und gehen Sie zu Einfügen --> Diagramme --> Säulen- oder Balkendiagramm einfügen --> Gestapeltes Balkendiagramm. Klicken Sie darauf.
<br>
<img src="1.png" width=70% />
2. Ändern Sie die Y-Achse: Klicken Sie mit der rechten Maustaste auf die y-Achse. Klicken Sie auf Achsenformat. Klicken Sie in Beschriftungen auf das Dropdown-Menü für die Position der Beschriftung und wählen Sie Niedrigstes Element aus.
<br>
<img src="2.png" width=70% />
3. Wählen Sie eine beliebige Leiste aus und gehen Sie zur Formatierung. Legen Sie einen geeigneten Abstand fest.
<br>
<img src="3.png" width=70% />
4. Entfernen wir das Minuszeichen (-) aus dem Tornado-Diagramm. Wählen Sie die x-Achse aus. Gehen Sie zur Formatierung. Klicken Sie in den Achsenoptionen auf die Nummer. Wählen Sie in der Kategorie Benutzerdefiniert aus. Im Formatcode schreiben Sie ###0,###0. Klicken Sie auf Hinzufügen.
<br>
<img src="4.png" width=70% />
5. Klicken Sie auf die y-Achse und gehen Sie zu den Achsenoptionen. Überprüfen Sie in den Achsenoptionen Kategorien in umgekehrter Reihenfolge.
<br>
<img src="5.png" width=70% />

## **So fügen Sie ein Tornado-Diagramm in Aspose.Cells for Node.js via C++ hinzu**
Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die [Beispieldatei Excel](sample.xlsx), die einige Beispieldaten enthält. Danach erstellt es das gestapelte Balkendiagramm basierend auf den Anfangsdaten und setzt relevante Eigenschaften. Schließlich speichert es die Arbeitsmappe im [Ausgabe-XLSX-Format](out.xlsx). Der folgende Screenshot zeigt das von Aspose.Cells erstellte Tornado-Diagramm in der Ausgabe-Excel-Datei.
<br>
<img src="6.png" width=70% />

### **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);
const charts = sheet.getCharts();
// Add bar chart
const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
const chart = charts.get(index);

// Set data for bar chart
chart.setChartDataRange("A1:C7", true);

// Set properties for bar chart
chart.getTitle().setText("Tornado chart");
chart.setStyle(2);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getPlotArea().getBorder().setColor(AsposeCells.Color.White);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

chart.getCategoryAxis().setTickLabelPosition(AsposeCells.TickLabelPositionType.Low);
chart.getCategoryAxis().setIsPlotOrderReversed(true);

chart.setGapWidth(10);

const valueAxis = chart.getValueAxis();
valueAxis.getTickLabels().setNumberFormat("#,##0;#,##0");

workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
