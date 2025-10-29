---  
title: Exporter un style de bordure similaire lorsque le style de bordure n est pas supporté par les navigateurs Web avec Node.js via C++  
linktitle: Exporter un style de bordure similaire lorsque le style de bordure n est pas pris en charge par les navigateurs Web  
type: docs  
weight: 70  
url: /fr/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Apprenez comment exporter des bordures non supportées par les navigateurs Web lors de la conversion de fichiers Excel en HTML en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Microsoft Excel supporte certains types de bordures pointillées qui ne sont pas supportées par les navigateurs Web. Lors de la conversion d'un tel fichier Excel en HTML avec Aspose.Cells for Node.js via C++, ces bordures sont supprimées. Cependant, Aspose.Cells peut également supporter l'affichage de ces bordures avec la propriété [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--). Veuillez définir sa valeur à **true** et les bordures non supportées seront également exportées dans le fichier HTML.  

## **Exporter un style de bordure similaire lorsque le style de bordure n'est pas pris en charge par les navigateurs Web**  

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716806.xlsx) contenant certains bordures non prises en charge comme indiqué dans la capture d'écran suivante. La capture montre aussi l'effet de la propriété [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--) dans le [HTML de sortie](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportSimilarBorderStyle.xlsx");

// Load the sample Excel file
const wb = new AsposeCells.Workbook(filePath);

// Specify Html Save Options - Export Similar Border Style
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportSimilarBorderStyle(true);

// Save the workbook in Html format with specified Html Save Options
wb.save("outputExportSimilarBorderStyle.html", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
