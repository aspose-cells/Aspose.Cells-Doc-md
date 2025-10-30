---
title: Hur man skapar ett dynamiskt skrollande diagram med Node.js via C++
linktitle: Hur man skapar dynamiskt rullande diagram
description: Lär dig hur man skapar ett dynamiskt skrollande diagram med Aspose.Cells for Node.js via C++. Vår steg för steg guide visar hur man implementerar smidiga dataövergångar och automatisk scrollning i ditt diagram för en kontinuerlig och uppdaterad visning.
keywords: Aspose.Cells för Node.js, Dynamiskt skrollande diagram, Dataövergångar, Smoothing scrolling, Kontinuerlig visning, Uppdateringsvisualisering.
type: docs
weight: 75
url: /sv/nodejs-cpp/create-dynamic-scrolling-chart/
---

## **Möjliga användningsscenario**
Dynamiskt rullande diagram är en typ av grafisk representation som används för att visa data som förändras över tiden. Det är utformat för att ge en realtidsvy över data, vilket gör att användare kan följa kontinuerliga uppdateringar och trender. Diagrammet uppdaterar kontinuerligt sig självt när ny data läggs till, och det rullar automatiskt för att visa den senaste informationen.

Dynamiska rullande diagram används vanligtvis inom olika branscher, såsom finans, analys av aktiemarknaden, väderövervakning och analys av sociala medier. De möjliggör för användare att visualisera och analysera datapunkter och fatta informerade beslut baserat på realtidsinformation.

Dessa diagram är vanligtvis interaktiva, vilket låter användaren zooma in eller ut, bläddra genom historisk data och justera tidsintervall. De stödjer ofta flera dataserier, vilket ger en omfattande vy över olika mätvärden och deras korrelationer.

Övergripande sett är dynamiska rullande diagram värdefulla verktyg för övervakning och analys av tidsseriedata, vilket underlättar beslut i realtid och förbättrar datavisualiseringskapaciteten.

## **Använd Aspose.Cells för att skapa ett dynamiskt skrollande diagram**
 I följande avsnitt visar vi hur du skapar ett dynamiskt skrollande diagram med Aspose.Cells for Node.js via C++. Vi visar koden för exemplet, samt Excel-filen som skapats med denna kod.

## **Exempelkod**
Den följande provkoden kommer att generera [Dynamic Scrolling Chart File](DynamicScrollingChart.xlsx).

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
sheet.getCells().get("A1").putValue("Day");
sheet.getCells().get("B1").putValue("Sales");
// In this example, we will add 30 days of data
const allDays = 30;
const showDays = 10;
let currentDay = 1;

for (let i = 0; i < allDays; i++) {
const cellA = `A${i + 2}`;
const cellB = `B${i + 2}`;
sheet.getCells().get(cellA).putValue(i + 1);
sheet.getCells().get(cellB).putValue(50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3));
}

// This is the Dynamic Scrolling Control Data
sheet.getCells().get("G19").putValue("Start Day");
sheet.getCells().get("G20").putValue(currentDay);
sheet.getCells().get("H19").putValue("Show Days");
sheet.getCells().get("H20").putValue(showDays);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtScrollData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtScrollLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Add a ScrollBar for the Dynamic Scrolling Chart
const bar = sheet.getShapes().addScrollBar(2, 0, 3, 0, 200, 30);
bar.setMin(0);
bar.setMax(allDays - showDays);
bar.setCurrentValue(currentDay);
bar.setLinkedCell("$G$20");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 2, 4, 15, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtScrollData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtScrollLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicScrollingChart.xlsx"));
```

## **Anteckningar**
I den genererade filen kan du använda rullisten samtidigt som diagrammet dynamiskt räknar de senaste 10 datamängderna. Detta görs med "OFFSET"-formeln i provkoden:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

 Du kan prova att ändra numret "10" till "15" i cell "Sheet1!$H$20", och det dynamiska diagrammet kommer att räkna de senaste 15 dataset. Nu har vi framgångsrikt skapat ett dynamiskt skrollande diagram med Aspose.Cells for Node.js via C++.
{{< app/cells/assistant language="nodejs-cpp" >}}
