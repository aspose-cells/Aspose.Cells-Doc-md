---  
title: WortArt Wasserzeichen zum Diagramm mit Node.js über C++ hinzufügen  
linktitle: Fügen Sie WordArt Wasserzeichen zum Diagramm hinzu  
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ ein WortArt Wasserzeichen zu einem Diagramm in Microsoft Excel hinzufügen. Unser Leitfaden zeigt, wie man ein WortArt Wasserzeichen erstellt und positioniert, um die visuelle Attraktivität und Einzigartigkeit Ihres Diagramms zu verbessern.  
keywords: Aspose.Cells für Node.js, WortArt Wasserzeichen, Diagrammwasserzeichen, Microsoft Excel, Visuelle Attraktivität, Diagrammunique  
type: docs  
weight: 50  
url: /de/nodejs-cpp/add-wordart-watermark-to-chart/  
---  

{{% alert color="primary" %}}  

Sie können WordArt verwenden, um spezielle Texteffekte für Tabellenkalkulationen hinzuzufügen. Zum Beispiel einen Titel strecken, Text dekorieren, den Text in eine voreingestellte Form passen lassen oder den betroffenen Text auf den Diagrammbereich eines Diagramms als Wasserzeichen anwenden. Das WordArt wird zu einem Objekt, das Sie in Ihren Tabellenkalkulationen bewegen oder positionieren können, um Dekorationen hinzuzufügen.  

Das folgende Beispiel zeigt, wie Sie eine WordArt-Form als Wasserzeichen für den Diagrammbereich hinzufügen.  

{{% /alert %}}  

Das folgende Beispiel zeigt, wie Sie eine WordArt-Form als Wasserzeichen für den Plotbereich eines vorhandenen Diagramms hinzufügen.  

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
