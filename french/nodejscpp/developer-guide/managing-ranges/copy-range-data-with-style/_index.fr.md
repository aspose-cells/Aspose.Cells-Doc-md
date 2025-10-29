---  
title: Copier la plage de données avec style en utilisant Node.js via C++  
linktitle: Copier les données de la plage avec style  
type: docs  
weight: 610  
url: /fr/nodejs-cpp/copy-range-data-with-style/  
description: Apprenez comment copier une plage de cellules avec leur mise en forme en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

[Copier uniquement la plage de données](/cells/fr/nodejs-cpp/copy-range-data-only/) expliqué comment copier les données d'une plage à une autre. Plus précisément, il applique un nouvel ensemble de styles aux cellules copiées. Aspose.Cells peut également copier une plage complète avec la mise en forme. Cet article explique comment.  

{{% /alert %}}  

Aspose.Cells propose une gamme de classes et de méthodes pour travailler avec des plages, par exemple, [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-), [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/) et [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#applyStyle-style-styleflag-).  

Cet exemple :  

1. Crée un classeur.  
2. Remplit un certain nombre de cellules dans la première feuille avec des données.  
3. Crée un [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/).  
4. Crée un objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style/) avec des attributs de mise en forme spécifiés.  
5. Applique le style à la plage de données.  
6. Crée une deuxième plage de cellules.  
7. Copie les données avec la mise en forme de la première plage vers la deuxième.  

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
for (let i = 0; i < 50; i++)
{
for (let j = 0; j < 10; j++) 
{
cells.get(i, j).putValue(`${i},${j}`);
}
}

// Create a range (A1:D3).
const range = cells.createRange("A1", "D3");

// Create a style object.
let style = workbook.createStyle();
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

// Create the styleflag object.
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

// Copy the range data with formatting.
range2.copy(range);

const outputFilePath = path.join(dataDir, "CopyRange.out.xlsx");
// Save the excel file.
workbook.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
