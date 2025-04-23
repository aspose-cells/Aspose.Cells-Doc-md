---
title: Wie man mit Node.js über C++ ein dynamisches rollendes Diagramm erstellt
linktitle: Wie erstellt man ein dynamisches Rollbalkendiagramm
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ ein dynamisches rollendes Diagramm erstellen. Unser Leitfaden zeigt, wie Sie reibungslose Datenübergänge und rollende Durchschnitte in Ihrem Diagramm für eine kontinuierliche und aktualisierte Anzeige implementieren.
keywords: Aspose.Cells für Node.js, Dynamisches rollendes Diagramm, Datenübergänge, Reibungslose Durchschnitte, Kontinuierliche Anzeige, Aktualisierte Visualisierung.
type: docs
weight: 74
url: /de/nodejs-cpp/create-dynamic-rolling-chart/
---

## **Mögliche Verwendungsszenarien**
Ein dynamisches Rollbalkendiagramm bezieht sich auf eine grafische Darstellung, die Datenpunkte ständig verschiebt und aktualisiert. Es handelt sich um einen Diagrammtyp, der sich ständig selbst aktualisiert und dabei ein rollendes Fenster der neuesten Datenpunkte zeigt, während ältere Datenpunkte gelöscht werden, wenn neue hinzukommen.

Dynamische Rollbalkendiagramme werden häufig verwendet, um Trends und Muster in Echtzeit- oder Streaming-Daten zu visualisieren. Sie sind besonders nützlich in Szenarien, in denen zeitliche Aspekte und Veränderungen im Laufe der Zeit entscheidend sind, wie z.B. Börsenmarktanalysen, Wetterüberwachung oder Live-Performance-Verfolgung.

Diese Diagramme verwenden typischerweise Animationen oder automatisches Scrollen, um sicherzustellen, dass die aktuellsten Informationen stets präsentiert werden. Die Länge des rollenden Fensters kann angepasst werden, um einen bestimmten Zeitraum anzuzeigen, wie z.B. die letzten Stunde, den Tag oder die Woche.

Zusammenfassend ist ein dynamisches Rollbalkendiagramm eine kontinuierlich aktualisierte grafische Darstellung, die die neuesten Datenpunkte anzeigt und ältere löscht, so dass Benutzer Echtzeit-Trends und Muster beobachten können.

## **Verwenden Sie Aspose.Cells, um ein dynamisches Rollbalkendiagramm zu erstellen**
In den nächsten Absätzen zeigen wir Ihnen, wie Sie unter Verwendung von Aspose.Cells ein dynamisches Rollbalkendiagramm erstellen. Wir zeigen Ihnen den Code für das Beispiel, sowie die mit diesem Code erstellte Excel-Datei.

## **Beispielcode**
Der folgende Beispielcode wird die [Datei für das dynamische Rollbalkendiagramm](DynamicRollingChart.xlsx) generieren.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A1").putValue("Month");
sheet.getCells().get("A2").putValue(1);
sheet.getCells().get("A3").putValue(2);
sheet.getCells().get("A4").putValue(3);
sheet.getCells().get("A5").putValue(4);
sheet.getCells().get("A6").putValue(5);
sheet.getCells().get("A7").putValue(6);
sheet.getCells().get("A8").putValue(7);

sheet.getCells().get("B1").putValue("Sales");
sheet.getCells().get("B2").putValue(50);
sheet.getCells().get("B3").putValue(45);
sheet.getCells().get("B4").putValue(55);
sheet.getCells().get("B5").putValue(60);
sheet.getCells().get("B6").putValue(55);
sheet.getCells().get("B7").putValue(65);
sheet.getCells().get("B8").putValue(70);

// Set the dynamic range for the chart's data source.
let index = sheets.getNames().add("Sheet1!ChtData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

// Set the dynamic range for the chart's data labels.
index = sheets.getNames().add("Sheet1!ChtLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 10, 3, 25, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicRollingChart.xlsx"));
```

## **Anmerkungen**
In der generierten Datei können Sie weiterhin Daten in den Spalten A und B hinzufügen, während das Diagramm dynamisch die neuesten 5 Datensätze zählt. Dies wird im Beispielcode mit der "OFFSET"-Formel durchgeführt:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Sie können versuchen, die Zahl "-5" in der Formel zu "-10" zu ändern, und das dynamische Diagramm wird die neuesten 10 Datensätze zählen. Jetzt haben wir erfolgreich ein dynamisches Rollbalkendiagramm unter Verwendung von Aspose.Cells erstellt.
