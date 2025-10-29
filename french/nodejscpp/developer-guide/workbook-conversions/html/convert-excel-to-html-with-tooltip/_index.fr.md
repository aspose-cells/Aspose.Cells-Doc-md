---  
title: Convertir Excel en HTML avec infobulle en utilisant Node.js via C++  
linktitle: Convertir Excel en HTML avec info bulle  
type: docs  
weight: 200  
url: /fr/nodejs-cpp/convert-excel-to-html-with-tooltip/  
description: Apprenez comment convertir des fichiers Excel en format HTML avec des infobulles pour un affichage complet du texte en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Convertir Excel en HTML avec info-bulle**

Il peut arriver que le texte soit coupé dans le HTML généré et que vous souhaitiez afficher le texte complet comme infobulle lors du survol. Aspose.Cells for Node.js via C++ prend en charge cette fonctionnalité en fournissant la propriété [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--). La définition de la propriété [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--) à **true** ajoutera le texte complet en tant qu'infobulle dans le HTML généré.

L'image suivante montre l'info-bulle dans le fichier HTML généré.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Le code d'exemple suivant charge le [fichier Excel source](98107416.xlsx) et génère le [fichier HTML de sortie](98107417.zip) avec l'infobulle.

Code d'exemple

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "AddTooltipToHtmlSample.xlsx"));

const options = new AsposeCells.HtmlSaveOptions();
options.setAddTooltipText(true);

// Save as Markdown
workbook.save(path.join(outputDir, "AddTooltipToHtmlSample_out.html"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
