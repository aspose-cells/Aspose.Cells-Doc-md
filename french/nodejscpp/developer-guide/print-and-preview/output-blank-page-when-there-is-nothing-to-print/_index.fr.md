---
title: Sortie de page blanche lorsqu il n y a rien à imprimer avec Node.js via C++
linktitle: Afficher une page blanche lorsqu il n y a rien à imprimer
type: docs
weight: 90
url: /fr/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **Scénarios d'utilisation possibles**

 Si la feuille est vide, Aspose.Cells n'imprimera rien lorsque vous exportez la feuille en image. Vous pouvez changer ce comportement en utilisant la propriété [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--). Lorsque vous la mettez sur **true**, elle imprimera la page blanche.

## **Afficher une page vierge lorsqu'il n'y a rien à imprimer**

 Le code d'exemple ci-dessous crée un classeur vide contenant une feuille vide et rend cette feuille vide en une image après avoir défini la propriété [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--) sur **true**. Par conséquent, la page blanche est générée car il n'y a rien à imprimer, comme vous pouvez le voir dans l'image ci-dessous.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet - it is empty sheet
const ws = wb.getWorksheets().get(0);

// Specify image or print options
// Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
// So that empty page gets printed
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Png);
opts.setOutputBlankPageWhenNothingToPrint(true);

// Render empty sheet to png image
const sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, path.join(outputDir, "OutputBlankPageWhenNothingToPrint.png"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
