---  
title: Lägg till WordArt vattenmärke i diagrammet med Node.js via C++  
linktitle: Lägg till WordArt vattenstämpel till Diagram  
description: Lär dig hur du använder Aspose.Cells for Node.js via C++ för att lägga till ett WordArt vattenmärke i ett diagram i Microsoft Excel. Vår guide visar hur du skapar och positionerar ett WordArt vattenmärke för att förbättra diagrammets visuella tilltal och unikhet.  
keywords: Aspose.Cells för Node.js, WordArt vattenmärke, diagram vattenmärke, Microsoft Excel, visuell tilltal, diagramets unika egenskaper.  
type: docs  
weight: 50  
url: /sv/nodejs-cpp/add-wordart-watermark-to-chart/  
---  

{{% alert color="primary" %}}  

Du kan använda WordArt för att lägga till specialeffekter på text i kalkylblad. Till exempel: sträck en titel, dekorera text, få texten att passa en förinställd form eller tillämpa den på ett karts plottområde som en vattenstämpel. WordArt blir ett objekt som du kan flytta eller positionera i kalkylbladen för dekoration.  

Följande exempel visar hur man lägger till en WordArt-form som en vattenstämpel för diagrammets plottområde.  

{{% /alert %}}  

Följande exempel visar hur du lägger till en WordArt-form som en vattenstämpel för ett befintligt diagram.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Open the existing excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add a WordArt watermark (shape) to the chart's plot area.
const wordart = chart.getShapes().addTextEffectInChart(AsposeCells.MsoPresetTextEffect.TextEffect2,
"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

// Get the shape's fill format.
const wordArtFormat = wordart.getFill();

// Set the transparency.
wordArtFormat.setTransparency(0.9);

// Get the line format.
const lineFormat = wordart.getLine();

// Set Line format to invisible.
lineFormat.setWeight(0.0);

// Save the excel file.
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
