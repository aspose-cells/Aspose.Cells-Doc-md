---
title: Remove Existing PrinterSettings of Worksheets in Excel file with Node.js via C++
linktitle: Remove Existing PrinterSettings of Worksheets in Excel file
type: docs
weight: 60
url: /nodejs-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: In this article, you will learn how to remove existing PrinterSettings of Worksheet inside the Excel file programmatically using Aspose.Cells for Node.js via C++.
keywords: remove printer settings of worksheet Node.js via C++, remove printer settings of excel worksheet Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Sometimes developers want to prevent Excel from including *.bin* files of printer settings in the saved XLSX files. Printer settings files are located under *“[file "root"]\xl\printerSettings”.* This document explains how to remove existing printer settings using Aspose.Cells APIs.

## **Remove Existing PrinterSettings of Worksheets in Excel file**
Aspose.Cells allows you to remove existing printer settings specified for different sheets in the Excel file. The following sample code illustrates how to remove existing printer settings for all the worksheets in the workbook. Please see its [sample Excel file](45056020.xlsx), [output Excel file](45056021.xlsx), console output as well as the screenshot for a reference.

## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Sample Code**
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

## **Console Output**
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
