---
title: Rendre une feuille de calcul en contexte graphique avec Node.js via C++
linktitle: Rendre la feuille de calcul dans le contexte graphique
type: docs
weight: 300
url: /fr/nodejs-cpp/render-worksheet-to-graphic-context/
description: Apprenez comment rendre une feuille de calcul en contexte graphique en utilisant Aspose.Cells for Node.js via C++. Cela inclut le rendu en fichiers image, sur écran et via imprimantes.
---

{{% alert color="primary" %}}

Aspose.Cells peut maintenant rendre des feuilles de calcul en contexte graphique. Le contexte graphique peut être une image, un écran, une imprimante, etc. Veuillez utiliser l'une des deux méthodes suivantes pour rendre une feuille de calcul en contexte graphique.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

 Le code suivant illustre comment utiliser Aspose.Cells pour rendre une feuille de calcul en contexte graphique. Une fois le code exécuté, il imprimera toute la feuille, puis remplira l'espace vide restant en bleu dans le contexte graphique et enregistrera l'image sous le nom **OutputImage_out_.png**. Vous pouvez utiliser n'importe quel fichier Excel source pour essayer ce code. Veuillez également lire les commentaires à l'intérieur du code pour une meilleure compréhension.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook object from source file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create empty image buffer
const bmpOptions = new AsposeCells.ImageOrPrintOptions();
bmpOptions.setOnePagePerSheet(true);

// Render worksheet to image
const sheetRender = new AsposeCells.SheetRender(worksheet, bmpOptions);
sheetRender.toImage(0, dataDir + "/OutputImage_out.png");

// Save the image in Png format
```
