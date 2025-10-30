---
title: Datumsachse mit Node.js über C++
description: Erfahren Sie, wie Sie die Datumsachse in Aspose.Cells for Node.js via C++ verwalten. Unser Leitfaden hilft Ihnen, mit verschiedenen Datumsformaten, Zeitskalen und Frequenzen der Tick Beschriftungen zu arbeiten.
keywords: Aspose.Cells für Node.js, Datumsachse, verwalten, Datumsformate, Zeitskalen, Tick Beschriftungsfrequenzen.
type: docs
weight: 200
url: /de/nodejs-cpp/date-axis/
---

## **Mögliche Verwendungsszenarien**
Wenn Sie ein Diagramm aus Arbeitsblattdaten erstellen, das Daten mit Daten verwendet, und die Daten entlang der horizontalen (Kategorie-)Achse im Diagramm dargestellt werden, Aspose.Cells for Node.js via C++ ändert die Kategorieachse automatisch in eine Daten (Zeitskalen-)Achse.
Eine Datumsachse zeigt Daten in chronologischer Reihenfolge in bestimmten Intervallen oder Basiswerten an, wie die Anzahl der Tage, Monate oder Jahre, auch wenn die Datumsangaben auf dem Arbeitsblatt nicht in aufeinanderfolgender Reihenfolge oder in den gleichen Basiswerten vorliegen.
Standardmäßig bestimmt Aspose.Cells die Basiseinheiten für die Datumachse anhand des kleinsten Unterschieds zwischen zwei Daten in den Arbeitsblattdaten. Zum Beispiel, wenn Sie Aktienpreisdaten mit einem kleinsten Unterschied von sieben Tagen haben, setzt Excel die Basiseinheit auf Tage, aber Sie können die Basiseinheit auf Monate oder Jahre ändern, um die Entwicklung der Aktie über einen längeren Zeitraum zu sehen.

## **Behandeln Sie die Datumsachse wie Microsoft Excel**
Bitte sehen Sie sich den folgenden Beispielcode an, der eine neue Excel-Datei erstellt und die Werte des Diagramms im ersten Arbeitsblatt platziert. 
Dann fügen wir ein Diagramm hinzu und setzen den Typ des [**Axis**](https://reference.aspose.com/cells/nodejs-cpp/axis/) 
auf [**Axis.getCategoryType()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getCategoryType--) und setzen dann die Basiswerte auf Tage.

![todo:image_alt_text](excel.png)

## **Beispielcode**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add the sample values to cells
worksheet.getCells().get("A1").putValue("Date");
// 14 means datetime format
const style = worksheet.getCells().getStyle();
style.setNumber(14);
// Put values to cells for creating chart
worksheet.getCells().get("A2").setStyle(style);
worksheet.getCells().get("A2").putValue(new Date(Date.UTC(2022, 5, 26)));
worksheet.getCells().get("A3").setStyle(style);
worksheet.getCells().get("A3").putValue(new Date(Date.UTC(2022, 4, 22)));
worksheet.getCells().get("A4").setStyle(style);
worksheet.getCells().get("A4").putValue(new Date(Date.UTC(2022, 7, 3)));
worksheet.getCells().get("B1").putValue("Price");
worksheet.getCells().get("B2").putValue(40);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(60);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 9, 6, 21, 13);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);         
// Set the Axis type to Date time
chart.getCategoryAxis().setCategoryType(AsposeCells.CategoryType.TimeScale);
// Set the base unit for CategoryAxis to days
chart.getCategoryAxis().setBaseUnitScale(AsposeCells.TimeUnit.Days);
// Set the direction for the axis text to be vertical
chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Vertical);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set max value of Y axis.
chart.getValueAxis().setMaxValue(70);
// Set major unit.
chart.getValueAxis().setMajorUnit(10);
// Save the file
workbook.save("DateAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
