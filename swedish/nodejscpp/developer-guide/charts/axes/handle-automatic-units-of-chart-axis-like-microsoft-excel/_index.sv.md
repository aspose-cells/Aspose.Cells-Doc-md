---  
title: Hantera automatiska enheter för diagramaxlar som Microsoft Excel med Node.js via C++  
linktitle: Hantera automatiska enheter för diagramaxeln som Microsoft Excel  
description: Lär dig hur du hanterar automatiska enheter på diagramaxlar i Aspose.Cells for Node.js via C++. Vår guide visar hur du konfigurerar och anpassar automatiska enheter på en diagramaxel, inklusive visning av vetenskaplig notation och justering av skalan.  
keywords: Aspose.Cells for Node.js via C++, diagramaxlar, automatiska enheter, Microsoft Excel, konfiguration, anpassning, vetenskaplig notation, skala.  
type: docs  
weight: 120  
url: /sv/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/  
---  

## **Möjliga användningsscenario**  
Tidigare versioner av Aspose.Cells for Node.js via C++ kunde inte hantera automatiska enheter för diagramaxlar korrekt när diagrammet renderades till bild eller PDF. Nu stöder Aspose.Cells for Node.js via C++ hantering av automatiska enheter för diagramaxlar. Det finns ingen kodändring. Konvertera bara ditt diagram till en bild eller PDF och det kommer att rendera diagramaxeln precis som Microsoft Excel gör.  

## **Hantera automatiska enheter för diagramaxeln som Microsoft Excel**  
Följande kodexempel laddar [exempel-Excelfilen](61767755.xlsx) och genererar [utdata PDF-diagram](61767752.pdf). Skärmbilden visar de automatiska enheterna för diagramaxeln i röda rektanglar och jämför också exempel-Excelfilen med utdata PDF-diagrammet. Båda är exakt likadana.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Exempelkod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Render chart to pdf
chart.toPdf("outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf");
```  
