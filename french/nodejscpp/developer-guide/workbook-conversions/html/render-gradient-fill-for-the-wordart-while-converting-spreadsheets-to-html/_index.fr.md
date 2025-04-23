---  
title: Rendre un remplissage en dégradé pour WordArt lors de la conversion de feuilles de calcul en HTML avec Node.js via C++  
linktitle: Rendu de remplissage dégradé pour le WordArt lors de la conversion des feuilles de calcul en HTML  
type: docs  
weight: 90  
url: /fr/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: Apprenez comment rendre un remplissage en dégradé pour WordArt lors de la conversion de feuilles de calcul en HTML en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  
Avant Aspose.Cells 17.1, Aspose.Cells ne rendait pas le remplissage en dégradé du WordArt lors de la conversion du fichier Excel en format HTML. Depuis la version 17.1, le remplissage en dégradé WordArt est supporté. La capture d'écran suivante compare l'effet du remplissage en dégradé lors de la conversion du fichier Excel avec Aspose.Cells 17.1 et la version plus ancienne.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Rendu de remplissage dégradé pour le WordArt lors de la conversion des feuilles de calcul en HTML**  
Le code d'exemple suivant convertit le [fichier Excel source](22774111.xlsx) en [format HTML de sortie](22774109.zip). Le fichier Excel source contient un objet WordArt avec remplissage en dégradé comme montré dans la capture d'écran ci-dessus.  

## **Code d'exemple**  
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

