---
title: Supprimer les paramètres d imprimante existants des feuilles de calcul dans un fichier Excel avec Node.js via C++
linktitle: Supprimer les paramètres d imprimante existants des feuilles de calcul dans le fichier Excel
type: docs
weight: 60
url: /fr/nodejs-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Dans cet article, vous apprendrez comment supprimer les paramètres d imprimante existants d une feuille de calcul dans le fichier Excel de manière programmatique en utilisant Aspose.Cells for Node.js via C++.
keywords: supprimer les paramètres d imprimante de la feuille de calcul avec Node.js via C++, supprimer les paramètres d imprimante d une feuille Excel avec Node.js via C++
---

## **Scénarios d'utilisation possibles**
Parfois, les développeurs souhaitent empêcher Excel d'inclure des fichiers *.bin* de paramètres d'imprimante dans les fichiers XLSX enregistrés. Les fichiers de paramètres d'imprimante se trouvent sous *« [fichier "root"]\xl\printerSettings ».* Ce document explique comment supprimer les paramètres d'imprimante existants à l'aide des API Aspose.Cells.

## **Supprimer les paramètres d'imprimante existants des feuilles de calcul dans le fichier Excel**
Aspose.Cells vous permet de supprimer les paramètres d'imprimante existants spécifiés pour différentes feuilles dans le fichier Excel. Le code d'exemple suivant illustre comment supprimer les paramètres d'imprimante existants pour toutes les feuilles de calcul dans le classeur. Veuillez consulter son [fichier Excel d'exemple](45056020.xlsx), [fichier Excel de sortie](45056021.xlsx), la sortie de la console ainsi que la capture d'écran à titre de référence.

## **Capture d'écran**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Code d'exemple**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Load source Excel file
const filePath = path.join(sourceDir, "sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");
const wb = new AsposeCells.Workbook(filePath);

// Get the sheet counts of the workbook
const sheetCount = wb.getWorksheets().getCount();

// Iterate all sheets
for (let i = 0; i < sheetCount; i++) {
// Access the i-th worksheet
const ws = wb.getWorksheets().get(i);

// Access worksheet page setup
const ps = ws.getPageSetup();

// Check if printer settings for this worksheet exist
if (ps.getPrinterSettings() != null) {
// Print the following message
console.log("PrinterSettings of this worksheet exist.");

// Print sheet name and its paper size
console.log("Sheet Name: " + ws.getName());
console.log("Paper Size: " + ps.getPaperSize());

// Remove the printer settings by setting them null
ps.setPrinterSettings(null);
console.log("Printer settings of this worksheet are now removed by setting it null.");
console.log("");
} // if
} // for

// Save the workbook
wb.save(path.join(outputDir, "outputRemoveExistingPrinterSettingsOfWorksheets.xlsx"));
```

## **Sortie console**
{{< highlight javascript >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
