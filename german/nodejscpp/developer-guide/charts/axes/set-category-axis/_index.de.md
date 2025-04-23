---
title: So setzen Sie die Kategorieachse mit Node.js über C++
linktitle: Wie man die Kategorieachse einstellt
description: Lernen Sie, wie Sie die Kategorieachse in Aspose.Cells for Node.js via C++ setzen. Unser Leitfaden hilft Ihnen zu verstehen, wie Sie den Bereich der Kategorieachse definieren, ihre Eigenschaften anpassen und ihre Beschriftungen formatieren.
keywords: Aspose.Cells for Node.js via C++, Kategorieachse, Einstellung, Bereich, Eigenschaften, Formatierung.
type: docs
weight: 205
url: /de/nodejs-cpp/how-to-set-category-axis/
---

## **Mögliche Verwendungsszenarien**
Nachdem Sie ein Diagramm in einem Arbeitsblatt erstellt haben, können Sie die Kategorieachse dafür festlegen. In diesem Artikel zeigen wir Ihnen, wie Sie die Kategorieachse für ein Excel-Diagramm mit Aspose.Cells und Beispielcode einstellen.

## **Die Schritte im Beispielcode**

1. Erstellen Sie eine neue Arbeitsmappe.

2. Erstellen Sie ein neues Diagramm im ersten Arbeitsblatt.

3. Fügen Sie einige Werte in Zellen im ersten Arbeitsblatt ein.

4. Jetzt können Sie die Kategorieachse einstellen; es gibt zwei Möglichkeiten: Verwendung der Zellendaten oder direkter Einsatz von Strings, beide werden im Beispielcode gezeigt.

5. Setzen Sie die Werteachse und speichern Sie die Arbeitsmappe, um das Ergebnis anzuzeigen.

## **Beispielcode**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const dataDir = ""; // Update with your path

// Create a new workbook
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CHART");

// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 8, 0, 20, 10);
const chart = worksheet.getCharts().get(chartIndex);

// Add some values to cells
worksheet.getCells().get("A1").putValue("Sales");
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(130);
worksheet.getCells().get("A5").putValue(160);
worksheet.getCells().get("A6").putValue(150);
worksheet.getCells().get("B1").putValue("Days");
worksheet.getCells().get("B2").putValue(1);
worksheet.getCells().get("B3").putValue(2);
worksheet.getCells().get("B4").putValue(3);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("B6").putValue(5);

// Some values in string
const Sales = "100,150,130,160,150";
const Days = "1,2,3,4,5";

// Set Category Axis Data with string
chart.getNSeries().setCategoryData(`{${Days}}`);
// Or you can set Category Axis Data with data in cells
// chart.getNSeries().setCategoryData("B2:B6");

// Add Series to the chart
chart.getNSeries().add("Demand1", true);
// Set value axis with string 
chart.getNSeries().get(0).setValues(`{${Sales}}`);
chart.getNSeries().add("Demand2", true);
// Set value axis with data in cells
chart.getNSeries().get(1).setValues("A2:A6");

// Set some Category Axis properties
chart.getCategoryAxis().getTickLabels().setRotationAngle(45);
chart.getCategoryAxis().getTickLabels().getFont().setSize(8);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

// Save the workbook to view the result file
workbook.save(path + "Output.xlsx");
```
