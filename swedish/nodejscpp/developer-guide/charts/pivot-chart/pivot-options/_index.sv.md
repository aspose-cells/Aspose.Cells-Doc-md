---
title: Hur man hanterar PivotChart med PivotOptions för Node.js via C++
linktitle: Pivotalternativ
type: docs
weight: 10
url: /sv/nodejs-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Hur man hanterar PivotChart med PivotOptions i Node.js via C++.
keywords: PivotDiagram Node.js via C++
---
## Vad är PivotChart

En PivotChart i Excel är en grafisk representation av data skapad från en PivotTable. Den låter användare visualisera och analysera data dynamiskt genom att sammanfatta och visa information i diagramform. PivotCharts är interaktiva och kan lätt modifieras för att visa olika perspektiv av data, vilket gör det till ett kraftfullt verktyg för dataanalys och presentation i Excel.

## Hur man hanterar PivotChart med PivotOptions

Genom att använda Aspose.Cells for Node.js via C++ kan du använda [**PivotOptions**](https://reference.aspose.com/cells/nodejs-cpp/pivotoptions/) för att hantera PivotDiagram.

Exempelfil och kod:
[Exempelfil](Sample.xlsx)

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

Med den tidigare nämnda exempelkoden kan du kontrollera resultatfilen med följande effekt, som visas i figuren:

**![Output](Output.png)**
{{< app/cells/assistant language="nodejs-cpp" >}}
