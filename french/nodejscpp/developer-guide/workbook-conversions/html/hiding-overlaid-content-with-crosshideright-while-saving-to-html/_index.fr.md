---
title: Cacher le contenu superposé avec CrossHideRight lors de la sauvegarde en HTML avec Node.js via C++
linktitle: Masquer le contenu superposé avec CrossHideRight lors de l enregistrement en HTML
type: docs
weight: 100
url: /fr/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---


## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, vous pouvez spécifier différents types de croisement pour les chaînes de cellules. Par défaut, Aspose.Cells génère le HTML selon Microsoft Excel, mais si vous changez le type de croisement en [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype), il cachera toutes les chaînes situées à droite de la cellule qui sont superposées ou chevauchantes avec la chaîne de la cellule.

## **Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement en HTML**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716894.xlsx) et le sauvegarde en [HTML de sortie](64716893.zip) après avoir défini le [**HtmlSaveOptions.getHtmlCrossStringType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getHtmlCrossStringType--) comme [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). La capture d'écran explique comment [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) influence le HTML de sortie par défaut.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.CrossHideRight);

// Save to HTML with HtmlSaveOptions
workbook.save(path.join(dataDir, "outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html"), opts);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
