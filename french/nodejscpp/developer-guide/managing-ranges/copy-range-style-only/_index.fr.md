---
title: Copier uniquement le style de la plage avec Node.js via C++
linktitle: Copier uniquement le style de la plage
type: docs
weight: 620
url: /fr/nodejs-cpp/copy-range-style-only/
description: Apprenez comment copier uniquement le style d une plage tout en manipulant les données dans Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

[Copier uniquement la plage de données](/cells/fr/nodejs-cpp/copy-range-data-only/) et [Copier la plage de données avec style](/cells/fr/nodejs-cpp/copy-range-data-with-style/) expliquent comment copier les données d'une plage vers une autre seule ou avec la mise en forme. Il est également possible de copier uniquement la mise en forme. Cet article montre comment.

{{% /alert %}} 

Cet exemple crée un classeur, le remplit de données et copie uniquement le style d'une plage.

1. Créer une plage.
1. Créez un objet `Style` avec des attributs de mise en forme spécifiés.
1. Appliquer la mise en forme de style à la plage.
1. Créer une deuxième plage de cellules.
1. Copier la mise en forme de la première plage vers la deuxième plage.

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
cells.get(i, j).putValue(i.toString() + "," + j.toString());
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
const top = style.getBorders().get(AsposeCells.BorderType.TopBorder);
top.setLineStyle(AsposeCells.CellBorderType.Thin);
top.setColor(AsposeCells.Color.Blue);

const bottom = style.getBorders().get(AsposeCells.BorderType.BottomBorder);
bottom.setLineStyle(AsposeCells.CellBorderType.Thin);
bottom.setColor(AsposeCells.Color.Blue);

const left = style.getBorders().get(AsposeCells.BorderType.LeftBorder);
left.setLineStyle(AsposeCells.CellBorderType.Thin);
left.setColor(AsposeCells.Color.Blue);

const right = style.getBorders().get(AsposeCells.BorderType.RightBorder);
right.setLineStyle(AsposeCells.CellBorderType.Thin);
right.setColor(AsposeCells.Color.Blue);


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

// Create a second range (C10:E13).
const range2 = cells.createRange("C10", "E13");

// Copy the range style only.
range2.copyStyle(range);

const outputFilePath = path.join(dataDir, "copyrangestyle.out.xls");
// Save the excel file.
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
