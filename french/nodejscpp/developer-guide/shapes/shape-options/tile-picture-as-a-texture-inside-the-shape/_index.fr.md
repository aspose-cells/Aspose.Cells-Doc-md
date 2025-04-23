---  
title: Tuiler l’image en tant que texture à l’intérieur de la forme avec Node.js via C++  
linktitle: Image tuilée comme une texture à l intérieur de la forme  
type: docs  
weight: 1700  
url: /fr/nodejs-cpp/tile-picture-as-a-texture-inside-the-shape/  
description: Apprenez comment tuiler une petite image en tant que texture à l’intérieur d’une forme en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Lorsque l'image est petite et ne couvre pas toute la surface de la forme sans perdre en qualité, alors vous avez la possibilité de la tuiler. Le tuilage remplit la surface de la forme avec une petite image en les répétant comme s'ils étaient des carreaux.  

## **Image tuilée comme une texture à l'intérieur de la forme**  

Vous pouvez remplir la surface de la forme avec une image et la tuiler en utilisant la propriété [**Shape.isTiling()**](https://reference.aspose.com/cells/nodejs-cpp/texturefill/#isTiling--) et en la configurant sur **true**. Veuillez consulter le code d’exemple ci-dessous, son [fichier Excel d’exemple](46465050.xlsx) ainsi que la capture d’écran pour référence.  

## **Capture d'écran**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleTextureFill_IsTiling.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Tile Picture as a Texture inside the Shape 
shape.getFill().getTextureFill().setIsTiling(true);

// Save the output Excel file
workbook.save(path.join(outputDir, "outputTextureFill_IsTiling.xlsx"));
```  

