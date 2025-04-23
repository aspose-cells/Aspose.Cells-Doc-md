---
title: Redimensionner automatiquement les colonnes et lignes lors du chargement HTML dans un classeur avec Node.js via C++
linktitle: Ajuster automatiquement les colonnes et les lignes lors du chargement du HTML dans le classeur
type: docs
weight: 120
url: /fr/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Apprenez à ajuster automatiquement les colonnes et les lignes lors du chargement de fichiers HTML dans un classeur utilisant Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez ajuster automatiquement les colonnes et les lignes lors du chargement de votre fichier HTML dans l'objet Classeur. Veuillez définir la propriété [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) à **true** à cette fin.

## **Ajuster automatiquement les colonnes et les lignes lors du chargement du HTML dans le classeur**

Le code d'exemple suivant charge d'abord le HTML d'exemple dans le classeur sans options de chargement et l'enregistre au format XLSX. Il charge ensuite à nouveau le HTML d'exemple dans le classeur mais cette fois, il charge le HTML après avoir défini la propriété [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) à **true** et l'enregistre au format XLSX. Téléchargez les deux fichiers Excel de sortie, c'est-à-dire [Fichier Excel de sortie sans AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) et [Fichier Excel de sortie avec AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). La capture d'écran suivante montre l'effet de la propriété [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) sur les deux fichiers Excel de sortie.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Sample HTML.
const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

// Load HTML string into memory stream.
const ms = Uint8Array.from(sampleHtml, c => c.charCodeAt(0));

// Load memory stream into workbook.
let wb = new AsposeCells.Workbook(ms);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWithout_AutoFitColsAndRows.xlsx"));

// Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
const opts = new AsposeCells.HtmlLoadOptions();
opts.setAutoFitColsAndRows(true);

// Load memory stream into workbook with the above HTMLLoadOptions.
wb = new AsposeCells.Workbook(ms, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWith_AutoFitColsAndRows.xlsx"));
```

