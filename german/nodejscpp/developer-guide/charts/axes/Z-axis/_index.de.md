---
title: Z Achse mit Node.js über C++
description: Lernen Sie, wie Sie mit der Z Achse in Aspose.Cells for Node.js via C++ arbeiten. Unser Leitfaden hilft Ihnen zu verstehen, wie Sie die Z Achse konfigurieren und anpassen, einschließlich ihrer Skalierung und Beschriftungen, um Ihre Diagramme zu verbessern.
keywords: Aspose.Cells for Node.js via C++, Z Achse, Diagrammerstellung, Konfiguration, Anpassung, Skala, Beschriftungen.
type: docs
weight: 210
url: /de/nodejs-cpp/z-axis/
---

## **Mögliche Verwendungsszenarien**
 Für einige 3-D-Diagramme wie 3D-Spalten, 3D-Kegel oder 3D-Pyramide, die eine Tiefen- (Serien-) Achse, auch bekannt als Z-Achse, haben, die Sie ändern können. Sie können den Intervall zwischen den Markierungen, Achsenbeschriftungen und andere Operationen festlegen.

## ** Primäre und Sekundäre Achse wie Microsoft Excel behandeln**
 Bitte sehen Sie sich den folgenden Beispielcode an, der eine neue Excel-Datei erstellt und die Werte des Diagramms im ersten Arbeitsblatt platziert. Dann fügen wir ein Diagramm hinzu und setzen den Diagrammtyp auf Column3D, wobei Sie die Z-Achse, auch Tiefenachse genannt, sehen können. 

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
// Put values to cells for creating chart
worksheet.getCells().get("A1").putValue("A");
worksheet.getCells().get("B1").putValue("B");
worksheet.getCells().get("C1").putValue("C");
worksheet.getCells().get("A2").putValue(2);
worksheet.getCells().get("A3").putValue(1);
worksheet.getCells().get("B2").putValue(2);
worksheet.getCells().get("B3").putValue(3);
worksheet.getCells().get("C2").putValue(2);
worksheet.getCells().get("C3").putValue(3);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column3D, 9, 6, 25, 16);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Calculate the chart
chart.calculate();
// Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
chart.setChartDataRange("A2:C3", true);
// Hide the CategoryAxis axis
chart.getCategoryAxis().setIsVisible(false);
// Hide the ValueAxis axis
chart.getValueAxis().setIsVisible(false);
// Save the file
workbook.save("ZAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
