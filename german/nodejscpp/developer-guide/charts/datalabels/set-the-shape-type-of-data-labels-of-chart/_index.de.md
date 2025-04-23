---
title: Festlegen des Formentyps der Datenetiketten des Diagramms mit Node.js über C++
linktitle: Legen Sie den Formtyp der Datenbeschriftungen des Diagramms fest
description: Erfahren Sie, wie Sie den Formtyp der Datenetiketten in Diagrammen mit Aspose.Cells for Node.js via C++ festlegen. Dieser Leitfaden erklärt die verschiedenen verfügbaren Formtypen und zeigt, wie Sie den geeigneten Formtyp für Ihre Datenetiketten wählen, um die Präsentation und Benutzerfreundlichkeit zu verbessern.
keywords: Aspose.Cells for Node.js via C++, Diagrammerstellung, Datenetiketten, Formtypen, Präsentation, Benutzerfreundlichkeit.
type: docs
weight: 110
url: /de/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Mögliche Verwendungsszenarien**
Sie können den Formtyp der Datenetiketten im Diagramm mit der Eigenschaft `DataLabels.shapeType` ändern. Es nimmt den Wert der Enumeration `DataLabelShapeType` an und ändert entsprechend den Formtyp der Datenetiketten. Einige seiner Werte sind

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Festlegen des Formtyps von Datenbeschriftungen des Diagramms**
Das folgende Beispiel ändert den Shape-Typ der Datenbeschriftungen im Diagramm auf `DataLabelShapeType.WedgeEllipseCallout`. Bitte beachten Sie die [Beispieldatei Excel](60489778.xlsx), die in diesem Beispiel verwendet wird, und die [Ausgabedatei Excel](60489779.xlsx), die daraus generiert wurde. Der Screenshot zeigt die Wirkung des Codes auf die Beispiel-Excel-Datei.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Beispielcode**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetShapeTypeOfDataLabelsOfChart.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Access first series
const series = chart.getNSeries().get(0);

// Set the shape type of data labels i.e. Speech Bubble Oval
series.getDataLabels().setShapeType(AsposeCells.DataLabelShapeType.WedgeEllipseCallout);

// Save the output Excel file
workbook.save(path.join(dataDir, "outputSetShapeTypeOfDataLabelsOfChart.xlsx"));
```
