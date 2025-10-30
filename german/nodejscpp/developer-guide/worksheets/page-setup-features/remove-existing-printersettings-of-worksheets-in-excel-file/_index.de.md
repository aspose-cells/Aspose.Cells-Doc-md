---
title: Bestehende PrinterSettings von Arbeitsblättern in Excel Dateien mit Node.js über C++ entfernen
linktitle: Entfernen Sie vorhandene Dokumenteinstellungen der Arbeitsblätter in der Excel Datei
type: docs
weight: 60
url: /de/nodejs-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: In diesem Artikel erfahren Sie, wie Sie die vorhandenen PrinterSettings eines Arbeitsblatts in der Excel Datei programmgesteuert mit Aspose.Cells for Node.js via C++ entfernen.
keywords: Printer Einstellungen des Arbeitsblatts entfernen Node.js über C++, Printer Einstellungen des Excel Arbeitsblatts entfernen Node.js über C++
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Entwickler verhindern, dass Excel * .bin * -Dateien der Druckereinstellungen in den gespeicherten XLSX-Dateien einführt. Druckereinstellungsdateien befinden sich unter * "[Datei \"Root \ "] \ xl \ printerSettings ".* Dieses Dokument erläutert, wie vorhandene Druckereinstellungen mithilfe von Aspose.Cells-APIs entfernt werden.

## **Entfernen Sie die vorhandenen Druckereinstellungen von Arbeitsblättern in der Excel-Datei**
Aspose.Cells ermöglicht es Ihnen, vorhandene Druckereinstellungen für verschiedene Arbeitsblätter in der Excel-Datei zu entfernen. Der folgende Beispielcode veranschaulicht, wie vorhandene Druckereinstellungen für alle Arbeitsblätter in der Arbeitsmappe entfernt werden. Bitte beachten Sie die [Beispiel-Excel-Datei](45056020.xlsx), [Ausgabedatei](45056021.xlsx), Konsolenausgabe sowie den Screenshot zur Referenz.

## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Beispielcode**
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

## **Konsolenausgabe**
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
