---  
title: Exporter les propriétés du document, du classeur et de la feuille de calcul dans la conversion Excel en HTML avec Node.js via C++  
linktitle: Exporter les propriétés du classeur et des feuilles de calcul du document en Excel vers la conversion HTML  
type: docs  
weight: 50  
url: /fr/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/  
description: Apprenez comment exporter les propriétés du document, du classeur et de la feuille de calcul dans Excel en HTML en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Lorsqu'un fichier Microsoft Excel est exporté en HTML à l'aide de Microsoft Excel ou Aspose.Cells for Node.js via C++, il exporte également divers types de propriétés du document, du classeur et de la feuille de calcul comme montré dans la capture d'écran suivante. Vous pouvez éviter d'exporter ces propriétés en réglant les propriétés [**HtmlSaveOptions.getExportDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportDocumentProperties--), [**HtmlSaveOptions.getExportWorkbookProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorkbookProperties--) et [**HtmlSaveOptions.getExportWorksheetProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetProperties--) sur **false**. La valeur par défaut de ces propriétés est **true**. La capture d'écran suivante montre à quoi ressemblent ces propriétés dans le HTML exporté.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Exporter les propriétés du Document, du Classeur et des Feuilles de calcul lors de la conversion d'Excel en HTML**  

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767776.xlsx) et le convertit en HTML sans exporter les propriétés du document, du classeur et de la feuille de calcul dans le [HTML de sortie](61767779.zip).  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// We do not want to export document, workbook and worksheet properties
options.setExportDocumentProperties(false);
options.setExportWorkbookProperties(false);
options.setExportWorksheetProperties(false);

// Export the Excel file to Html with Html Save Options
workbook.save("outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html", options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
