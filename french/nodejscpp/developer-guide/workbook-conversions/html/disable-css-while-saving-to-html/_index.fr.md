---
title: Désactiver le CSS lors de l enregistrement en HTML avec Node.js via C++
linktitle: Désactiver le CSS lors de l enregistrement en HTML
type: docs
weight: 320
url: /fr/nodejs-cpp/disable-css-while-saving-to-html/
description: Apprenez comment désactiver le CSS lors de l enregistrement de fichiers Excel en HTML en utilisant Aspose.Cells for Node.js via C++. 
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML sur une seule page, en général les éléments CSS seront intégrés dans le fichier HTML et situés dans la section HEAD. Si vous attachez ce fichier comme contenu/corps d'un email, la majorité des clients de messagerie supprimeront les éléments CSS, ce qui entraînera un rendu incorrect. La version 24.12 d'Aspose.Cells introduit une option permettant de désactiver optionnellement le CSS, permettant aux styles d'être directement appliqués dans les éléments HTML eux-mêmes. Si vous souhaitez que le HTML soit le contenu/corps de l'email, veuillez utiliser la propriété [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) et la définir sur **true**.

## **Désactiver le CSS lors de l'enregistrement en HTML**

Le code d'exemple suivant montre l'utilisation de la propriété [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--). 

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableCss.xlsx"));

// Disable CSS
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableCss(true);

// Save the workbook in HTML
workbook.save(path.join(outputDir, "outputDisable.html"), opts);
```
