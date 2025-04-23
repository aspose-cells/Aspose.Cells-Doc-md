---  
title: Ottieni intervallo massimo in un foglio di lavoro con Node.js tramite C++  
linktitle: Ottieni Max Range In Un Foglio di Lavoro  
type: docs  
weight: 360  
url: /it/nodejs-cpp/get-max-range-in-a-worksheet/  
description: Questo articolo descrive come ottenere l intervallo massimo, l intervallo massimo di dati e l intervallo massimo di visualizzazione dei file Excel usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Quando si leggono i dati dal foglio di lavoro, è necessario conoscere l'area massima.  

Quando si copiano tutti i dati da un foglio di lavoro, è necessario conoscere l'area massima.  

Quando esportiamo un'area specificata in HTML e PDF, dobbiamo conoscere l'area massima.  

Aspose.Cells for Node.js via C++ offre diversi metodi per trovare l'intervallo massimo in un foglio di lavoro.  

{{% /alert %}}  

## **Ottenere l'intervallo massimo**  
In Aspose.Cells, se gli oggetti [**row**](https://reference.aspose.com/cells/nodejs-cpp/row/) e [**column**](https://reference.aspose.com/cells/nodejs-cpp/column/) sono inizializzati, queste righe e colonne verranno conteggiate per l'area massima, anche se non ci sono dati nelle righe o colonne vuote.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxRow();
let maxColumn = sheet.getCells().getMaxColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxRow();
maxColumn = sheet.getCells().getMaxColumn();
// The range is updated to A1:B10.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **Ottieni il massimo intervallo di dati**  
Nella maggior parte dei casi, abbiamo solo bisogno di ottenere tutti i range contenenti tutti i dati, anche se le celle vuote al di fuori del range sono formattate.  
E le impostazioni su forme, tabelle e tabelle pivot verranno ignorate.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxDataRow();
let maxColumn = sheet.getCells().getMaxDataColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxDataRow();
maxColumn = sheet.getCells().getMaxDataColumn();
// The range is still A1:B3.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **Ottieni l'intervallo massimo di visualizzazione**  
Quando esportiamo tutti i dati dal foglio di lavoro in HTML, PDF o immagini, dobbiamo ottenere un'area che contenga tutti gli oggetti visibili, inclusi dati, stili, grafici, tabelle e tabelle pivot.  
I seguenti codici mostrano come rendere l'intervallo di visualizzazione massimo in HTML:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Gets the max display range.
const range = worksheets.get(0).getCells().getMaxDisplayRange();

// Save the range to html
const saveOptions = new AsposeCells.HtmlSaveOptions();
saveOptions.setExportActiveWorksheetOnly(true);
saveOptions.setExportArea(AsposeCells.CellArea.createCellArea(range.getFirstRow(), range.getFirstColumn(), range.getFirstRow() + range.getRowCount() - 1, range.getFirstColumn() + range.getColumnCount() - 1));

// Save the range.
workbook.save("html.html", saveOptions);
```  

Ecco il [file excel di origine](Book1.xlsx).  

