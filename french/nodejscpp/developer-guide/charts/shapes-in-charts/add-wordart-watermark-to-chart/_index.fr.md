---  
title: Ajouter un Filigrane WordArt au graphique avec Node.js via C++  
linktitle: Ajouter un filigrane WordArt au graphique  
description: Apprenez à utiliser Aspose.Cells for Node.js via C++ pour ajouter un filigrane WordArt à un graphique dans Microsoft Excel. Notre guide vous montrera comment créer et positionner un filigrane WordArt pour améliorer l attrait visuel et l unicité de votre graphique.  
keywords: Aspose.Cells pour Node.js, Filigrane WordArt, Filigrane du graphique, Microsoft Excel, attrait visuel, unicité du graphique.  
type: docs  
weight: 50  
url: /fr/nodejs-cpp/add-wordart-watermark-to-chart/  
---  

{{% alert color="primary" %}}  

Vous pouvez utiliser WordArt pour ajouter des effets spéciaux de texte aux feuilles de calcul. Par exemple, étirer un titre, décorer du texte, faire en sorte que le texte s'adapte à une forme prédéfinie, ou appliquer le texte affecté à la zone de traçage d'un graphique comme filigrane. Le WordArt devient un objet que vous pouvez déplacer ou positionner dans vos feuilles de calcul pour ajouter des décorations.  

L'exemple suivant montre comment ajouter une forme WordArt en filigrane pour la zone de traçage du graphique.  

{{% /alert %}}  

L'exemple suivant montre comment ajouter une forme WordArt en filigrane pour la zone de traçage d'un graphique existant.  

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

