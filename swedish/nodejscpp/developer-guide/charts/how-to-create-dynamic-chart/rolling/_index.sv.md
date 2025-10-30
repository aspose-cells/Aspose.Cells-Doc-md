---
title: Hur man skapar ett dynamiskt rullande diagram med Node.js via C++
linktitle: Hur man skapar dynamiskt rullande diagram
description: Lär dig hur man skapar ett dynamiskt rullande diagram med Aspose.Cells for Node.js via C++. Vår guide visar hur man implementerar smidiga dataövergångar och rullande medelvärden i ditt diagram för en kontinuerlig och uppdaterad visning.
keywords: Aspose.Cells för Node.js, Dynamiskt rullande diagram, Dataövergångar, Smoothing averages, Kontinuerlig visning, Uppdateringsvisualisering.
type: docs
weight: 74
url: /sv/nodejs-cpp/create-dynamic-rolling-chart/
---

## **Möjliga användningsscenario**
Ett dynamiskt rullande diagram syftar till en grafisk representation som visar data punkter som konstant förskjuts och uppdateras över tiden. Det är en typ av diagram som kontinuerligt uppdaterar sig själv och visar ett rullande fönster av de senaste datapunkterna samtidigt som äldre datapunkter kastas bort när nya kommer in.

Dynamiska rullande diagram används vanligen för att visualisera trender och mönster i realtid eller strömningsdata. De är särskilt användbara i scenarier där tidsmässiga aspekter och förändringar över tid är avgörande, såsom analys av aktiemarknaden, väderövervakning eller spårning av liveprestanda.

Dessa diagram använder vanligtvis animation eller automatisk rullning för att säkerställa att den mest aktuella informationen alltid presenteras. Längden på det rullande fönstret kan anpassas för att visa en specifik tidsperiod, såsom den senaste timmen, dagen eller veckan.

Sammanfattningsvis är ett dynamiskt rullande diagram en kontinuerligt uppdaterad grafisk representation som visar de senaste datapunkterna samtidigt som äldre kastas bort, vilket gör att användarna kan observera trender och mönster i realtid.

## **Använd Aspose Cells för att skapa dynamiskt rullande diagram**
I de följande styckena kommer vi att visa dig hur du skapar ett dynamiskt rullande diagram med hjälp av Aspose.Cells. Vi kommer att visa koden för exemplet, liksom Excel-filen skapad med denna kod.

## **Exempelkod**
Följande provkod kommer att generera [Dynamic Rolling Chart File](DynamicRollingChart.xlsx).

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

## **Anteckningar**
I den genererade filen kan du fortsätta att lägga till data i kolumnerna A och B, samtidigt som diagrammet dynamiskt räknar de senaste 5 datamängderna. Detta görs med hjälp av "OFFSET"-formeln i provkoden:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Du kan prova att ändra numret "-5" till "-10" i formeln, och det dynamiska diagrammet kommer att räkna de senaste 10 datamängderna. Nu har vi skapat ett dynamiskt rullande diagram med hjälp av Aspose.Cells framgångsrikt.
{{< app/cells/assistant language="nodejs-cpp" >}}
