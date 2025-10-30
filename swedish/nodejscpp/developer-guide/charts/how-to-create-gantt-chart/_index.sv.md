---
title: Hur man skapar ett Gantt diagram med Node.js via C++
linktitle: Hur man skapar ett Gantt diagram
type: docs
weight: 72
url: /sv/nodejs-cpp/how-to-create-gantt-chart/
description: Lär dig hur du skapar ett Gantt diagram med Aspose.Cells for Node.js via C++ API.
keywords: Node.js skapar ett Gantt diagram, lägger till ett Gantt diagram, infogar ett Gantt diagram
---

## **Vad är Gantt-diagram**

Ett Gantt-diagram är en sorts stapeldiagram som illustrerar ett projektschema. Det visar start- och sluttider för olika delar av ett projekt. Varje uppgift eller aktivitet representeras av en stapel, vars längd motsvarar dess varaktighet. Gantt-diagram visar också beroenden mellan uppgifter, vilket gör det möjligt för projektledare att visualisera i vilken ordning uppgifter ska utföras. Det används ofta inom projektledning för att planera, schemalägga och följa upp projekt effektivt.

## **Hur man skapar ett Gantt-diagram i Excel**

Du kan skapa ett Gantt-diagram i Excel genom att följa dessa steg:
1. Lägg till några data för Gantt-diagrammet. 
<br>
<img src="00.png" width=50% />
1. Markera datan och gå till Infoga --> Diagram --> Infoga kolumn- eller stapeldiagram --> Staplat stapeldiagram. I vårt exempel är det B1:B7, och sedan infoga **Staplat stapeldiagram**.
<br>
<img src="1.png" width=50% />

1. Markera diagrammet, **Välj data** -> **Lägg till**, ställ in **Serienamn** och **Serievärden** enligt följande.
<br>
<img src="2.png" width=50% />

1. Välj diagrammet, redigera **Horisontell (Kategor) -axelrubriker**.
<br>
<img src="3.png" width=50% />

1. **Formatera axeln** på Y-axeln, välj **Kategorier i omvänd ordning**.
1. Markera **Blå Serien** och sätt **Fyllning -> Ingen Fyllning**.
1. **Formatere axeln** för X-axeln, ställ in **Minimum och Maximum** (1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. Lägg till **Datamärkningar** för diagrammet, nu får du ett Gantt-diagram.
<br>
<img src="0.png" width=50% />


## **Hur man lägger till ett ganttdiagram i Aspose.Cells**
Se följande exempel på kod. Den laddar [exempelfilen Excel](sample.xlsx) som innehåller några exempeldata. Sedan skapar den ett staplat stapeldiagram baserat på de initiala data och ställer in relevanta egenskaper. Slutligen sparar den arbetsboken till [utdata XLSX-format](result.xlsx). Skärmbilderna nedan visar ganttdiagrammet som skapats av Aspose.Cells i den utgående Excel-filen.
<br>
<img src="5.png" width=60% />

### **Exempelkod**

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

{{< app/cells/assistant language="nodejs-cpp" >}}
