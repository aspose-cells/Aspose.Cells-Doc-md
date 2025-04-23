---  
title: Esporta i CSS del Foglio di Lavoro separatamente nell HTML di output con Node.js tramite C++  
linktitle: Esporta il foglio di lavoro CSS separatamente in HTML di output  
type: docs  
weight: 80  
url: /it/nodejs-cpp/export-worksheet-css-separately-in-output/  
description: Scopri come esportare i CSS del foglio di lavoro separatamente quando converti un file Excel in HTML usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**

Aspose.Cells for Node.js via C++ offre la funzione di esportare i CSS del foglio di lavoro separatamente quando converti il tuo file Excel in HTML. Utilizza la proprietà [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--) per questo scopo e imposta il valore su **true** durante il salvataggio del file Excel in formato HTML.

## **Esportare il Foglio di Stile CSS Separatamente nell'HTML di Output**

Il seguente esempio di codice crea un file Excel, aggiunge del testo nella cella **B5** di colore **Rosso** e successivamente lo salva in formato HTML usando la proprietà [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--). Si veda l'[HTML di output](60489766.zip) generato dal codice come riferimento. All'interno troverai **stylesheet.css** come risultato dell'esempio di codice.

## **Codice di Esempio**

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

## **Esporta un singolo foglio di lavoro in HTML**

Quando un workbook con più fogli viene convertito in HTML usando Aspose.Cells for Node.js via C++, crea un file HTML insieme a una cartella contenente CSS e più file HTML. Quando questo file HTML viene aperto nel browser, le schede sono visibili. Lo stesso comportamento è richiesto anche per un workbook con un singolo foglio quando viene convertito in HTML. In passato, non si creava una cartella separata per i workbook con un singolo foglio, e veniva creato solo un file HTML. Tale file HTML non mostra le schede quando aperto nel browser. MS Excel crea una cartella e un HTML corretti anche per un singolo foglio, e pertanto lo stesso comportamento è stato implementato utilizzando le API di Aspose.Cells. Il file di esempio può essere scaricato dal seguente link per l'uso nel codice di esempio sottostante:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Codice di Esempio**

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

