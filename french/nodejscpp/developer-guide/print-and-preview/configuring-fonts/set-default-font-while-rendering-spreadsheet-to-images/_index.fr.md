---
title: Définir la police par défaut lors du rendu d une feuille de calcul en images avec Node.js via C++
linktitle: Définir la police par défaut lors du rendu de feuilles de calcul en images
type: docs
weight: 360
url: /fr/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Apprenez comment définir la police par défaut lors du rendu de feuilles de calcul en images en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Veuillez utiliser la propriété [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) pour définir la police par défaut lors du rendu des feuilles de calcul en images. Cette propriété ne sera efficace que lorsque la police par défaut du classeur ne pourra pas afficher vos caractères. La police par défaut spécifiée avec la propriété [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) est utilisée pour toutes les cellules qui ont des polices invalides ou inexistantes.

{{% /alert %}}

## Définir la police par défaut lors du rendu de feuilles de calcul en images

Le code d'exemple suivant crée un classeur, ajoute du texte dans la cellule A4 de la première feuille, et définit sa police avec une police invalide ou inexistante. Ensuite, il prend deux images de la feuille de calcul. La première image est prise en réglant la propriété [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) à *Courier New* et la seconde en réglant la propriété [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) à *Times New Roman*.

Voici l’image de sortie après avoir réglé la propriété [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) à *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Voici l’image de sortie après avoir réglé la propriété [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) à *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Code d'exemple

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Set default font of the workbook to none
let s = wb.getDefaultStyle();
s.getFont().setName("");
wb.setDefaultStyle(s);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access cell A4 and add some text inside it.
const cell = ws.getCells().get("A4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell A4 which is unknown.
let st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
st.setIsTextWrapped(true);
cell.setStyle(st);

// Set first column width and fourth column height
ws.getCells().setColumnWidth(0, 80);
ws.getCells().setRowHeight(3, 60);

// Create image or print options.
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);

// Render worksheet image with Courier New as default font.
opts.setDefaultFont("Courier New");
let sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "out_courier_new_out.png");

// Render worksheet image again with Times New Roman as default font.
opts.setDefaultFont("Times New Roman");
sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "times_new_roman_out.png");
```
