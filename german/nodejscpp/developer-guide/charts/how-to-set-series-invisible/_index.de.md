---
title: Wie man Serien mit Node.js über C++ unsichtbar macht
linktitle: Wie man Serien unsichtbar macht
description: Erfahren Sie, wie Sie Serien in Excel Diagrammen mit Aspose.Cells for Node.js via C++ unsichtbar machen. 
keywords: Excel Diagramm, Serie, Unsichtbar, IsFiltered Node.js über C++.
type: docs
weight: 74
url: /de/nodejs-cpp/how-to-set-series-invisible/
---

## Wie man Serien in Excel-Diagrammen unsichtbar macht

In Excel-Diagrammen können Sie mit einem Rechtsklick auf das Diagramm "Daten auswählen" wählen und im Popup-Fenster festlegen, ob eine Serie sichtbar sein soll, indem Sie sie an- oder abwählen. Sie können die folgende [Beispieldatei](SeriesFiltered.xlsx) herunterladen und in Excel öffnen, um diese Funktion wie in der Abbildung gezeigt zu erreichen. Anschließend erklären wir, wie man dies mit der Aspose.Cells-Bibliothek umsetzt.

![todo:image_alt_text](series-invisible.png)

## Wie man Serien mit Aspose.Cells unsichtbar macht 

Wir verwenden den folgenden Code, um Serien mit Aspose.Cells unsichtbar zu machen:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SeriesFiltered.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const charts = workbook.getWorksheets().get(0).getCharts();
const chart = charts.get("Chart 1");
const nSeriesFiltered = chart.getFilteredNSeries();
const nSeries = chart.getNSeries();
nSeries.get(1).setIsColorVaried(true);
nSeries.get(0).setIsColorVaried(true);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Sie können die folgende [Inputdatei](SeriesFiltered.xlsx) und [Ausgabedatei](output.xlsx) erhalten.

Wie in der Abbildung unten gezeigt, sind die ersten beiden Serien, die ursprünglich sichtbar waren, in der Ausgabedatei unsichtbar geworden.
![todo:image_alt_text](output.png)
