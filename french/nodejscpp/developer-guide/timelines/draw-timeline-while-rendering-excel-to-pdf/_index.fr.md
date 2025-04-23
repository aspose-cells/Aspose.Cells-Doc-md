---  
title: Tracer Une Ligne de Temps lors du rendu d Excel en PDF avec Node.js via C++  
linktitle: Dessiner la chronologie lors du rendu d Excel en PDF  
type: docs  
weight: 60  
url: /fr/nodejs-cpp/draw-timeline-while-rendering-excel-to-pdf/  
description: Gérez les lignes de temps des fichiers Excel avec Aspose.Cells for Node.js via C++.  
keywords: Rendu de la timeline en PDF sans office 2013, 2016, 2019 et office 365 Node.js via C++  
---  

## **Dessiner une chronologie lors du rendu d'Excel en PDF**  
Si vous avez un fichier Excel avec une ligne de temps appliquée et que vous souhaitez exporter le fichier Excel en PDF avec les paramètres de la timeline, Aspose.Cells for Node.js via C++ prend désormais cela en charge par défaut. Il vous suffit d'exporter le fichier Excel avec ligne de temps en PDF, et le PDF généré affichera la timeline appliquée.  

Le code d'exemple suivant charge le [fichier Excel d'exemple](input.xlsx) qui contient une chronologie existante. Il enregistre ensuite le classeur sous la forme de [fichier PDF de sortie](out.pdf). La capture d'écran suivante compare le fichier Excel source et le fichier PDF généré.  

<img src="out.png" width="60%">  

## **Code d'exemple**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Save file to pdf
workbook.save("out.pdf", AsposeCells.SaveFormat.Pdf);
```  

