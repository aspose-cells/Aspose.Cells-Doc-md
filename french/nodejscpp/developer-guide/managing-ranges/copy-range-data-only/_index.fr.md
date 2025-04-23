---  
title: Copier uniquement la plage de données avec Node.js via C++  
linktitle: Copier uniquement les données de la plage  
type: docs  
weight: 600  
url: /fr/nodejs-cpp/copy-range-data-only/  
description: Apprenez comment copier des données d une plage de cellules à une autre à l aide de Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Parfois, vous devez copier des données d'une plage de cellules vers une autre, en copiant uniquement les données, pas la mise en forme. Aspose.Cells propose cette fonctionnalité.  

Cet article fournit un code d'exemple qui utilise Aspose.Cells pour copier une plage de données.  
{{% /alert %}}  

Cet exemple montre comment :  

1. Créer un classeur.  
1. Ajouter des données aux cellules dans la première feuille de calcul.  
1. Créer un [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
1. Créer un objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) avec des attributs de mise en forme spécifiés.  
1. Appliquer la mise en forme de style à la plage.  
1. Créer une autre plage de cellules.  
1. Copier les données de la première plage vers cette deuxième plage.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first Worksheet Cells.
const cells = workbook.getWorksheets().get(0).getCells();

// Fill some sample data into the cells.
for (let i = 0; i < 50; i++) {
for (let j = 0; j < 10; j++) {
cells.get(i, j).putValue(`${i},${j}`);
}
}

// Create a range (A1:D3).
const range = cells.createRange("A1", "D3");

// Create a style object.
const style = workbook.createStyle();
// Specify the font attribute.
style.getFont().setName("Calibri");
// Specify the shading color.
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
// Specify the border attributes.
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Blue);

// Create the style flag object.
const flag1 = new AsposeCells.StyleFlag();
// Implement font attribute
flag1.setFontName(true);
// Implement the shading / fill color.
flag1.setCellShading(true);
// Implement border attributes.
flag1.setBorders(true);
// Set the Range style.
range.applyStyle(style, flag1);

// Create a second range (C10:F12).
const range2 = cells.createRange("C10", "F12");

// Copy the range data only.
range2.copyData(range);

const outputFilePath = path.join(dataDir, "CopyRangeData.out.xlsx");
// Save the excel file.
workbook.save(outputFilePath);
```  

