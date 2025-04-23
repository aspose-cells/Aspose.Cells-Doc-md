---  
title: Gradientfüllung für WordArt beim Konvertieren von Tabellenkalkulationen nach HTML rendern mit Node.js via C++  
linktitle: Verlaufsfüllung für den WordArt beim Konvertieren von Tabellenkalkulationen in HTML rendern  
type: docs  
weight: 90  
url: /de/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: Lernen Sie, wie Sie eine Gradientfüllung für WordArt beim Konvertieren von Tabellenkalkulationen nach HTML mit Aspose.Cells for Node.js via C++ rendern.  
---  

## **Mögliche Verwendungsszenarien**  
Vor Aspose.Cells 17.1 rendert Aspose.Cells die Gradientfüllung von WordArt beim Konvertieren der Excel-Datei in HTML nicht. Seit der Version Aspose.Cells 17.1 wird die WordArt-Gradientfüllung unterstützt. Das folgende Screenshot vergleicht den Effekt der Gradientfüllung bei Umwandlung der Excel-Datei mit Aspose.Cells 17.1 und der älteren Version.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Verlaufsfüllung für den WordArt beim Konvertieren von Tabellenkalkulationen in HTML rendern**  
Der folgende Beispielcode konvertiert die [Quell-Excel](22774111.xlsx) in [Ausgabe-HTML](22774109.zip). Die Quelldatei enthält ein WordArt-Objekt mit Gradientfüllung, wie im oben stehenden Screenshot.  

## **Beispielcode**  
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

