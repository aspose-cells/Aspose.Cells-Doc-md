---  
title: Conversion de graphique en image au format SVG avec Node.js via C++  
linktitle: Conversion de graphique en image au format SVG  
type: docs  
weight: 240  
url: /fr/nodejs-cpp/converting-chart-to-image-in-svg-format/  
description: Apprenez comment convertir un graphique en une image au format SVG en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Scalable Vector Graphics (SVG) est un format d'image vectorielle basé sur XML pour les graphiques en deux dimensions qui prend également en charge l'interactivité et l'animation. La spécification SVG est une norme ouverte développée par le World Wide Web Consortium (W3C) depuis 1999.  

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'elles peuvent être recherchées, indexées, scriptées et compressées. En tant que fichiers XML, les images SVG peuvent être créées et modifiées avec n'importe quel éditeur de texte, mais sont plus souvent créées avec un logiciel de dessin.  

Aspose.Cells peut sauvegarder un graphique en images dans divers formats comme BMP, JPEG, PNG, GIF, SVG, etc. Cet article explique comment sauvegarder un graphique au format SVG.  

{{% /alert %}}  

Le code d'exemple suivant explique comment utiliser Aspose.Cells pour convertir un graphique en une image au format SVG. Le code charge le fichier source Microsoft Excel, puis enregistre le premier graphique trouvé sur la première feuille de calcul en SVG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from source file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleChartBook.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Set image or print options
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Svg);

// Save the chart to svg format
chart.toImage(path.join(dataDir, "Image_out.svg"), opts);
```  

