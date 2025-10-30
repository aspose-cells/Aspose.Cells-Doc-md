---  
title: Der Druckbereich wird mit Node.js via C++ nach HTML exportiert  
linktitle: Bereich des Druckbereichs in HTML exportieren  
type: docs  
weight: 60  
url: /de/nodejs-cpp/export-print-area-range-to/  
---  

## **Mögliche Verwendungsszenarien**

Dies ist ein häufiges Szenario, bei dem nur der Druckbereich, also ein ausgewählter Zellbereich, anstatt des gesamten Blatts nach HTML exportiert werden soll. Dieses Feature ist bereits für PDF-Renderings verfügbar; jetzt können Sie diese Aufgabe auch für HTML ausführen. Zuerst setzen Sie den Druckbereich im Seiteneinrichtungsobjekt des Arbeitsblatts. Später verwenden Sie das [**HtmlSaveOptions.getExportPrintAreaOnly()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportPrintAreaOnly--)-Flag, um nur den ausgewählten Bereich zu exportieren.

## Beispielcode

Der folgende Beispielscode lädt eine Arbeitsmappe und exportiert dann den Druckbereich in das HTML. Die Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

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

{{< app/cells/assistant language="nodejs-cpp" >}}
