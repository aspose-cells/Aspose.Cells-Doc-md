---
title: Rimuovere le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel con Node.js tramite C++
linktitle: Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel
type: docs
weight: 60
url: /it/nodejs-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: In questo articolo imparerai come rimuovere le impostazioni della stampante esistenti del foglio di lavoro all’interno del file Excel programmaticamente usando Aspose.Cells for Node.js via C++.
keywords: rimuovi impostazioni della stampante del foglio di lavoro Node.js tramite C++, rimuovi impostazioni della stampante del foglio Excel Node.js tramite C++
---

## **Possibili Scenari di Utilizzo**
A volte gli sviluppatori vogliono impedire ad Excel di includere i file *.bin* delle impostazioni della stampante nei file XLSX salvati. I file delle impostazioni della stampante si trovano in *"[file "root"]\xl\printerSettings".* Questo documento spiega come rimuovere le impostazioni della stampante esistenti utilizzando le API di Aspose.Cells.

## **Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel**
Aspose.Cells consente di rimuovere le impostazioni della stampante esistenti specificate per fogli diversi nel file Excel. Il seguente codice di esempio illustra come rimuovere le impostazioni della stampante esistenti per tutti i fogli di lavoro nella cartella di lavoro. Si prega di consultare il [file Excel di esempio](45056020.xlsx), [file Excel di output](45056021.xlsx), output della console e la schermata per un riferimento.

## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Codice di Esempio**
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

## **Output della console**
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
