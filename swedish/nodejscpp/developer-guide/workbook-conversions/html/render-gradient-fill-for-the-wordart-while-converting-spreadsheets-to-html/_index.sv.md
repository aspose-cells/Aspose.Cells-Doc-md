---  
title: Rendera gradientfyllning för WordArt vid konvertering av kalkylblad till HTML med Node.js via C++  
linktitle: Rendera Gradient Fill för WordArt vid konvertering av kalkylblad till HTML  
type: docs  
weight: 90  
url: /sv/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: Lär dig hur du renderar gradientfyllning för WordArt vid konvertering av kalkylblad till HTML med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  
 Före Aspose.Cells 17.1 renderades inte gradientfyllningen för WordArt när Excel-filen konverterades till HTML-format. Sedan Aspose.Cells 17.1 stöds WordArt-gradientfyllning. Följande skärmbild jämför effekten av gradientfyllning vid konvertering av Excel-filen med Aspose.Cells 17.1 och äldre version.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Rendera Gradient Fill för WordArt vid konvertering av kalkylblad till HTML**  
 Följande exempel kod konverterar den [käll Excel-filen](22774111.xlsx) till [utdata HTML-format](22774109.zip). Källxle-filen innehåller ett WordArt-objekt med gradientfyllning som visas i ovanstående skärmbild.  

## **Exempelkod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceGradientFill.xlsx");

// Read the source excel file having text with gradient fill
const workbook = new AsposeCells.Workbook(filePath);

// Save workbook to html format
workbook.save(path.join(dataDir, "out_sourceGradientFill.html"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
