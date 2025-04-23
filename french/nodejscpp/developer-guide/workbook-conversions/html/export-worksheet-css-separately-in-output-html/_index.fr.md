---  
title: Exporter séparément le CSS de la feuille dans le HTML de sortie avec Node.js via C++  
linktitle: Exporter la feuille de calcul CSS séparément dans le HTML de sortie  
type: docs  
weight: 80  
url: /fr/nodejs-cpp/export-worksheet-css-separately-in-output/  
description: Apprenez comment exporter le CSS de la feuille séparément lors de la conversion d un fichier Excel en HTML en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**

Aspose.Cells for Node.js via C++ offre la fonctionnalité d'exporter le CSS de la feuille séparément lorsque vous convertissez votre fichier Excel en HTML. Veuillez utiliser la propriété [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--) à cette fin et la régler sur **true** lors de la sauvegarde du fichier Excel au format HTML.

## **Exporter la feuille de calcul CSS séparément dans le HTML de sortie**

Le code d'exemple suivant crée un fichier Excel, ajoute du texte dans la cellule **B5** en couleur **Rouge**, puis le sauvegarde au format HTML en utilisant la propriété [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--). Consultez le [HTML de sortie](60489766.zip) généré par le code pour référence. Vous y trouverez **stylesheet.css** comme résultat du code d'exemple.

## **Code d'exemple**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - export worksheet css separately
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportWorksheetCSSSeparately(true);

// Save the workbook in html 
wb.save("outputExportWorksheetCSSSeparately.html", opts);
```

## **Exporter un classeur à feuille unique en HTML**

Lorsqu'un classeur avec plusieurs feuilles est converti en HTML en utilisant Aspose.Cells for Node.js via C++, il crée un fichier HTML ainsi qu'un dossier contenant du CSS et plusieurs fichiers HTML. Lorsqu'on ouvre ce fichier HTML dans un navigateur, les onglets sont visibles. Le même comportement est nécessaire pour un classeur avec une seule feuille lors de sa conversion en HTML. Auparavant, aucun dossier séparé n'était créé pour les classeurs à une seule feuille, et seul un fichier HTML était créé. Ce fichier HTML ne montrait pas d'onglets lorsqu'il était ouvert dans le navigateur. MS Excel crée également un dossier et un HTML appropriés pour une seule feuille, c'est pourquoi ce comportement est également implémenté avec les APIs Aspose.Cells. Le fichier d'exemple peut être téléchargé via le lien suivant pour utilisation dans le code d'exemple ci-dessous :

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleSingleSheet.xlsx");
// Load the sample Excel file containing single sheet only
const wb = new AsposeCells.Workbook(sourceFilePath);

// Specify HTML save options
const options = new AsposeCells.HtmlSaveOptions();

// Set optional settings if required
options.setEncoding(AsposeCells.EncodingType.UTF8);
options.setExportImagesAsBase64(true);
options.setExportGridLines(true);
options.setExportSimilarBorderStyle(true);
options.setExportBogusRowData(true);
options.setExcludeUnusedStyles(true);
options.setExportHiddenWorksheet(true);

// Save the workbook in Html format with specified Html Save Options
wb.save(path.join(dataDir, "outputSampleSingleSheet.htm"), options);
```  

