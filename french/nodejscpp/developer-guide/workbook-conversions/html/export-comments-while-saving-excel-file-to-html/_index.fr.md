---
title: Exporter les commentaires lors de l enregistrement d un fichier Excel en HTML avec Node.js via C++
linktitle: Exporter les commentaires lors de l enregistrement d un fichier Excel en HTML
type: docs
weight: 40
url: /fr/nodejs-cpp/export-comments-while-saving-excel-file-to/
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, les commentaires ne sont pas exportés. Cependant, Aspose.Cells for Node.js via C++ offre cette fonctionnalité en utilisant la propriété [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/). Si vous la réglez sur **true**, alors le HTML affichera également les commentaires présents dans votre fichier Excel.

## **Exporter les commentaires lors de l'enregistrement d'un fichier Excel en HTML**

Le code d'exemple suivant explique l'utilisation de la propriété [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/). La capture d'écran montre l'effet du code sur le HTML lorsqu'il est défini sur **true**. Veuillez télécharger le [fichier Excel d'exemple](50528260.xlsx) et le [HTML généré](5052826.txt) pour référence.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const sourceDir = path.join(__dirname, "data");
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportCommentsHTML.xlsx"));

// Export comments - set IsExportComments property to true
const opts = new AsposeCells.HtmlSaveOptions();
opts.setIsExportComments(true);

// Save the Excel file to HTML
const outputDir = path.join(__dirname, "output");
wb.save(path.join(outputDir, "outputExportCommentsHTML.html"), opts);
```
