---  
title: Exclure les styles inutilisés lors de la conversion Excel en HTML avec Node.js via C++  
linktitle: Exclure les styles inutilisés lors de la conversion d Excel en HTML  
type: docs  
weight: 30  
url: /fr/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/  
description: Apprenez comment exclure les styles inutilisés lors de la conversion d Excel en HTML en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Les fichiers Microsoft Excel peuvent contenir de nombreux styles inutilisés. Lors de l'exportation du fichier Excel en HTML, ces styles inutilisés sont également exportés. Cela peut augmenter la taille du HTML. Vous pouvez exclure ces styles inutilisés lors de la conversion d'Excel en HTML en utilisant la propriété [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--). Lorsqu'elle est définie sur **true**, tous les styles inutilisés sont exclus du HTML de sortie. La capture d'écran suivante affiche un style inutilisé dans le HTML de sortie.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Exclure les styles inutilisés lors de la conversion d'Excel en HTML**  

Le code d'exemple ci-dessous crée un classeur et y crée un style nommé inutilisé. Comme [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) est réglé sur **true**, ce style inutilisé ne sera pas exporté vers [HTML de sortie](61767778.zip). Mais si vous le réglez sur **false**, ce style inutilisé sera présent dans le HTML de sortie, comme montré dans la capture d'écran.  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const wb = new AsposeCells.Workbook();

// Create an unused named style
wb.createStyle().setName("UnusedStyle_XXXXXXXXXXXXXX");

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Put some value in cell C7
ws.getCells().get("C7").putValue("This is sample text.");

// Specify html save options, we want to exclude unused styles
const opts = new AsposeCells.HtmlSaveOptions();

// Comment this line to include unused styles
opts.setExcludeUnusedStyles(true);

// Save the workbook in html format
wb.save("outputExcludeUnusedStylesInExcelToHTML.html", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
