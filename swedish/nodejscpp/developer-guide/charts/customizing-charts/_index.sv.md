---  
title: Anpassa diagram med Node.js via C++  
linktitle: Anpassa diagram  
description: Lär dig hur du anpassar diagram i Aspose.Cells for Node.js via C++. Vår guide visar hur du ändrar diagramlayouter, lägger till och formaterar dataserier, justerar axlar och använder olika formateringsalternativ för att förbättra utseendet och användbarheten av dina diagram.  
keywords: Aspose.Cells for Node.js via C++, diagram, anpassning, layouter, dataserier, axlar, formatering, utseende, användbarhet.  
type: docs  
weight: 40  
url: /sv/nodejs-cpp/customizing-charts/  
---  


## **Skapa Anpassade Diagram**  

Hittills, när vi diskuterat diagram, har vi tittat på standarddiagram med sina standardformatinställningar. Vi definierar bara datakällan, sätter ett par egenskaper, och diagrammet skapas med dess standardformatinställningar. Men Aspose.Cells API:er stödjer också att skapa anpassade diagram som låter utvecklare skapa diagram med egna formatinställningar.  

Utvecklare kan skapa anpassade diagram vid körning med Aspose.Cells.  

Ett diagram består av en dataserie. Varje dataserie i Aspose.Cells representeras av ett [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series)-objekt medan [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)-objekt fungerar som en samling av [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series)-objekt. När man skapar ett anpassat diagram har utvecklare friheten att använda olika typer av diagram för olika dataserier (samlade i [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)-objektet).  

Exempelkoden nedan visar hur man skapar anpassade diagram. I det här exemplet kommer vi att använda ett stapeldiagram för den första dataserien och ett linjediagram för den andra serien. Resultatet är att vi lägger till ett stapeldiagram, kombinerat med ett linjediagram, till arbetsbladet.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(110);
worksheet.getCells().get("B1").putValue(260);
worksheet.getCells().get("B2").putValue(12);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(100);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the chart type of 2nd NSeries to display as line chart
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  

För närvarande stöder Aspose.Cells endast anpassade diagram som kombinerar pip-, linje-, kolumn- och stapeldiagram, men fler diagram kommer att stödas i framtida versioner.  

{{% /alert %}}  

