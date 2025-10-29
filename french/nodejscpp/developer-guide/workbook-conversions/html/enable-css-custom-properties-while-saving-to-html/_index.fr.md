---
title: Activer les propriétés CSS personnalisées lors de l enregistrement en HTML avec Node.js via C++
linktitle: Activer les propriétés CSS personnalisées lors de l enregistrement en HTML
type: docs
weight: 320
url: /fr/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/
description: Apprenez à activer les propriétés personnalisées CSS lors de l enregistrement de fichiers Excel en HTML en utilisant Aspose.Cells for Node.js via C++. 
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, pour le scénario où il y a plusieurs occurrences d'une image en base64, avec une propriété personnalisée, les données de l'image n'ont besoin d'être enregistrées qu'une seule fois afin d'améliorer la performance du HTML résultant. Veuillez utiliser la propriété [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--) et la définir **true** lors de l'enregistrement en HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Activer les propriétés personnalisées CSS lors de l'enregistrement en HTML**

Le code d'exemple ci-dessous montre l'utilisation de la propriété [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--). La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas réglée sur **true**. Veuillez télécharger le [fichier Excel d'exemple](50528260.xlsx) utilisé dans ce code et le [HTML de sortie](50528261.zip) généré pour référence.



## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleEnableCssCustomProperties.xlsx"));

const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportImagesAsBase64(true);

// Enable EnableCssCustomProperties
opts.setEnableCssCustomProperties(true);

// Save the workbook in HTML
workbook.save(path.join(dataDir, "outputEnableCssCustomProperties.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
