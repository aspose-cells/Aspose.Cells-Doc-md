---  
title: Exporter la plage de zone d impression en HTML avec Node.js via C++  
linktitle: Exporter la plage de zone d impression au format HTML  
type: docs  
weight: 60  
url: /fr/nodejs-cpp/export-print-area-range-to/  
---  

## **Scénarios d'utilisation possibles**

Il s'agit d'un scénario courant où nous devons exporter uniquement la zone d'impression, c'est-à-dire une plage sélectionnée de cellules au lieu de toute la feuille en HTML. Cette fonctionnalité est déjà disponible pour le rendu PDF ; cependant, vous pouvez maintenant effectuer cette tâche pour HTML également. Tout d'abord, définissez la zone d'impression dans l'objet de configuration de la page de la feuille de calcul. Ensuite, utilisez le drapeau [**HtmlSaveOptions.getExportPrintAreaOnly()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportPrintAreaOnly--) pour n'exporter que la plage sélectionnée.

## Code d'exemple

Le code d'exemple suivant charge un classeur puis exporte la zone d'impression au format HTML. Le fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleInlineCharts.xlsx](79527946.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleInlineCharts.xlsx");

// Load the Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access the sheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area.
worksheet.getPageSetup().setPrintArea("D2:M20");

// Initialize HtmlSaveOptions
const options = new AsposeCells.HtmlSaveOptions();

// Set flag to export print area only
options.setExportPrintAreaOnly(true);

// Save to HTML format
const outputFilePath = path.join(dataDir, "outputInlineCharts.html");
workbook.save(outputFilePath, options);
```  

