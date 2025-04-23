---  
title: Ignora gli errori durante il rendering di Excel in PDF con Node.js via C++  
linktitle: Ignora gli errori durante la conversione di Excel in PDF  
type: docs  
weight: 80  
url: /it/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/  
description: Impara a ignorare gli errori durante la conversione di file Excel in PDF usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

A volte, quando converti il file Excel in PDF, si verificano errori o eccezioni e il processo di conversione termina. Puoi ignorare tutti questi errori durante il processo di conversione usando la proprietà [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--). In questo modo, il processo di conversione si completerà senza generare errori o eccezioni, ma potrebbe verificarsi perdita di dati. Quindi, utilizza questa proprietà solo se la perdita di dati non è critica per te.  

## **Ignora gli errori durante la conversione di Excel in PDF**  

Il seguente codice carica il [file Excel di esempio](55541778.xlsx) ma il file Excel di esempio è errato e genera un errore durante [conversione in PDF](55541779.pdf) in 17.11, ma poiché utilizziamo la proprietà [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--), non viene generato alcun errore. Tuttavia, una *forma a freccia rossa arrotondata* come mostrato in questa schermata viene persa.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleErrorExcel2Pdf.xlsx");
// Load the Sample Workbook that throws Error on Excel2Pdf conversion
const wb = new AsposeCells.Workbook(filePath);

// Specify Pdf Save Options - Ignore Error
const opts = new AsposeCells.PdfSaveOptions();
opts.IgnoreError = true;

// Save the Workbook in Pdf with Pdf Save Options
wb.save("outputErrorExcel2Pdf.pdf", opts);
```  

