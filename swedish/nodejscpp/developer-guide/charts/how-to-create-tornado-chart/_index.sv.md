---
title: Hur man skapar ett tornadadiagram med Node.js via C++
linktitle: Hur man skapar ett tornado diagram
type: docs
weight: 73
url: /sv/nodejs-cpp/create-tornado-chart/
description: Lär dig hur du skapar ett tornadadiagram med Aspose.Cells for Node.js via C++ API.
keywords: Node.js skapa ett tornado diagram, lägg till ett tornado diagram, infoga ett tornado diagram
---

## **Introduktion**
Ett tornado diagram, även känt som en tornado graf eller tornado diagram, är en typ av datavisualisering som ofta används för känslighetsanalys i Excel. Det hjälper dig att förstå effekten av förändrande variabler på ett visst resultat eller en viss effekt.

## **Hur man skapar ett tornado diagram i Excel**
Du kan skapa ett tornado diagram i Excel genom att följa dessa steg:
1. Välj datan och gå till Infoga --> Diagram --> Infoga kolumn- eller stapeldiagram --> Staplad stolpdiagram. Klicka på det.
<br>
<img src="1.png" width=70% />
2. Ändra Y-axeln: Högerklicka på y-axeln. Klicka på formatera axeln. I etiketter, klicka på etikettposition nedrullningsalternativ och välj Låg element.
<br>
<img src="2.png" width=70% />
3. Välj vilken som helst stapel och gå till formatering. Ange en lämplig luckbredd.
<br>
<img src="3.png" width=70% />
4. Låt oss ta bort minustecknet (-) från tornado diagrammet. Välj x-axeln. Gå till formatering. I axelalternativ, klicka på nummer. I kategori, välj anpassad. I formatkoden skriv ###0,###0. Klicka på lägg till.
<br>
<img src="4.png" width=70% />
5. Klicka på y-axeln och gå till axelalternativen. I axelalternativen, kryssa i kategorier i omvänd ordning.
<br>
<img src="5.png" width=70% />

## **Hur man lägger till ett tornado-diagram i Aspose.Cells for Node.js via C++**
Vänligen se följande kodexempel. Den laddar den [exempelfil i Excel](sample.xlsx) som innehåller viss provdata. Sedan skapas det staplade stolpdiagrammet baserat på den initiala datan och relevanta egenskaper anges. Slutligen sparas arbetsboken till [utmatning XLSX-format](out.xlsx). Följande skärmdump visar tornado diagrammet skapat av Aspose.Cells i den resulterande Excelfilen.
<br>
<img src="6.png" width=70% />

### **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);
const charts = sheet.getCharts();
// Add bar chart
const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
const chart = charts.get(index);

// Set data for bar chart
chart.setChartDataRange("A1:C7", true);

// Set properties for bar chart
chart.getTitle().setText("Tornado chart");
chart.setStyle(2);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getPlotArea().getBorder().setColor(AsposeCells.Color.White);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

chart.getCategoryAxis().setTickLabelPosition(AsposeCells.TickLabelPositionType.Low);
chart.getCategoryAxis().setIsPlotOrderReversed(true);

chart.setGapWidth(10);

const valueAxis = chart.getValueAxis();
valueAxis.getTickLabels().setNumberFormat("#,##0;#,##0");

workbook.save("out.xlsx");
```
