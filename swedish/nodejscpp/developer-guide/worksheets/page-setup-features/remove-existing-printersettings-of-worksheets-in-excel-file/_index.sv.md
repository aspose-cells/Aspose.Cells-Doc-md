---
title: Ta bort befintliga PrinterSettings för arbetsblad i Excel filen med Node.js via C++
linktitle: Ta bort befintliga utskriftsinställningar för kalkylblad i Excel filen
type: docs
weight: 60
url: /sv/nodejs-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: I denna artikel lär du dig hur du programmässigt tar bort befintliga PrinterSettings för arbetsblad i Excel filen med hjälp av Aspose.Cells for Node.js via C++.
keywords: ta bort skrivareinställningar för arbetsblad Node.js via C++, ta bort skrivareinställningar för Excel arbetsblad Node.js via C++
---

## **Möjliga användningsscenario**
Ibland vill utvecklare förhindra Excel från att inkludera *.bin*-filer av skrivarinställningar i sparade XLSX-filer. Skrivarinställningsfiler finns under *“[fil "root"]\xl\printerSettings”.* I den här dokumentationen förklaras hur man tar bort befintliga skrivarinställningar med Aspose.Cells-API:er.

## **Ta bort befintliga skrivareinställningar för arbetsblad i Excel-fil**
Aspose.Cells möjliggör att ta bort befintliga skrivarinställningar som är specificerade för olika kalkylblad i Excel-filen. Följande exempelkod illustrerar hur man tar bort befintliga skrivarinställningar för alla kalkylblad i arbetsboken. Se dess [exempelfil för Excel](45056020.xlsx), [utdata för Excel-fil](45056021.xlsx), konsolresultat samt skärmdumpen som referens.

## **Skärmdump**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Exempelkod**
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

## **Konsoloutput**
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
