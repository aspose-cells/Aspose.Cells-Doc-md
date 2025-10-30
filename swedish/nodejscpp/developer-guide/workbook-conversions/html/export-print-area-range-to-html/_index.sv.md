---  
title: Exportera utskriftsområdesintervall till HTML med Node.js via C++  
linktitle: Exportera utskriftsområde till HTML  
type: docs  
weight: 60  
url: /sv/nodejs-cpp/export-print-area-range-to/  
---  

## **Möjliga användningsscenario**

Detta är ett vanligt scenario där vi bara vill exportera utskriftsområdet, det vill säga ett utvalt cellområde, till HTML. Denna funktion finns redan för PDF-rendering, men nu kan du utföra denna uppgift för HTML också. Först, ställ in utskriftsområdet i sidinställningsobjektet för kalkylbladet. Använder sedan [**HtmlSaveOptions.getExportPrintAreaOnly()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportPrintAreaOnly--)-flaggan för att exportera endast det valda området.

## Exempelkod

Följande exempelkod laddar en arbetsbok och exporterar sedan utskriftsområdet till HTML. Exempelfilen för att testa denna funktion kan laddas ned från följande länk:

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
