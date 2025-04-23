---  
title: Salva ogni foglio di lavoro in un file PDF diverso con Node.js tramite C++  
linktitle: Salva ciascun foglio di calcolo in un file PDF separato  
type: docs  
weight: 130  
url: /it/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/  
---  

{{% alert color="primary" %}}  
Aspose.Cells supporta la conversione di file XLS (che contengono immagini, grafici, ecc.) in documenti PDF. Aspose.Cells for Node.js via C++ può funzionare indipendentemente per convertire un foglio di calcolo in PDF, e non è necessario usare Aspose.PDF per Node.js tramite C++ per la conversione. La conversione non richiede che il software crei o utilizzi file temporanei, poiché l'intero processo può essere eseguito in memoria.  
{{% /alert %}}  

## **Salva ciascun foglio di calcolo in un file PDF separato**  
Se hai bisogno di salvare ogni foglio del tuo file Excel modello per generare diversi file PDF, puoi farlo facilmente. Puoi provare a impostare un indice di foglio a [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/nodejs-cpp/pdfs saveoptions/#sheetSet) alla volta per renderlo in PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Get the Excel file path
const filePath = path.join(dataDir, "input.xlsx");

// Instantiate a new workbook and open the Excel file from its location
const workbook = new AsposeCells.Workbook(filePath);

// Get the count of the worksheets in the workbook
const sheetCount = workbook.getWorksheets().getCount();

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Take PDFs of each sheet
for (let j = 0; j < sheetCount; j++) {
const ws = workbook.getWorksheets().get(j);

// set worksheet to output
const sheetSet = new AsposeCells.SheetSet([ws.getIndex()]);
pdfSaveOptions.setSheetSet(sheetSet);

workbook.save(path.join(dataDir, `worksheet-${ws.getName()}.out.pdf`), pdfSaveOptions);
}
```  

{{% alert color="primary" %}}  
Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.  
{{% /alert %}}  

