---
title: Wie man PivotChart mit PivotOptions für Node.js via C++ verwaltet
linktitle: Pivot Optionen
type: docs
weight: 10
url: /de/nodejs-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Wie man PivotChart mit PivotOptions in Node.js via C++ verwaltet.
keywords: PivotChart Node.js über C++
---
## Was ist ein PivotChart

Ein PivotChart in Excel ist eine grafische Darstellung von Daten, die aus einer PivotTable erstellt wird. Es ermöglicht Benutzern, Daten dynamisch zu visualisieren und zu analysieren, indem Informationen in Diagrammform zusammengefasst und angezeigt werden. PivotCharts sind interaktiv und können leicht modifiziert werden, um verschiedene Perspektiven der Daten zu zeigen, was es zu einem leistungsstarken Werkzeug für die Datenanalyse und Präsentation in Excel macht.

## Wie man PivotChart mit PivotOptions verwaltet

Durch die Verwendung von Aspose.Cells for Node.js via C++ können Sie [**PivotOptions**](https://reference.aspose.com/cells/nodejs-cpp/pivotoptions/) zur Verwaltung von PivotDiagrammen verwenden.

Beispiel-Datei und Code:
[Beispiel-Datei](Sample.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const chart = workbook.getWorksheets().get(0).getCharts().get(0);
const opt = chart.getPivotOptions();

// Hide ZoneFilter in PivotChart
opt.setDropZoneFilter(false); // HideZoneFilter

// You can set more properties, try them!
// opt.setDropZoneCategories(false); // HideZoneCategories
// opt.setDropZoneData(false); // HideZoneData
// opt.setDropZoneSeries(false); // HideZoneSeries
// opt.setDropZonesVisible(false); // Hide All

// Save the file and see the effect.
workbook.save(path.join(dataDir, "HideZoneFilter.xlsx"));
```

Mit dem obigen Beispielcode können Sie die Ergebnisdatei mit folgender Wirkung überprüfen, wie im Bild gezeigt:

**![Ergebnis](Output.png)**
{{< app/cells/assistant language="nodejs-cpp" >}}
