---  
title: Esporta l intervallo dell area di stampa in HTML con Node.js tramite C++  
linktitle: Esportare l area di stampa in HTML  
type: docs  
weight: 60  
url: /it/nodejs-cpp/export-print-area-range-to/  
---  

## **Possibili Scenari di Utilizzo**

Questo è uno scenario comune in cui è necessario esportare solo l'area di stampa ovvero un intervallo selezionato di celle invece dell'intero foglio in HTML. Questa funzione è già disponibile per la renderizzazione PDF, tuttavia ora puoi farlo anche per HTML. Prima imposta l'area di stampa nell'oggetto di configurazione della pagina del foglio. Successivamente, utilizza il flag [**HtmlSaveOptions.getExportPrintAreaOnly()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportPrintAreaOnly--) per esportare solo l'intervallo selezionato.

## Codice di esempio

Il codice di esempio seguente carica un libro di lavoro e quindi esporta l'area di stampa in HTML. Il file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

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

