---  
title: Renderizza una pagina PDF per ogni foglio di lavoro Excel  Conversione da Excel a PDF con Node.js tramite C++  
linktitle: Rendere una pagina PDF per foglio di lavoro di Excel  Conversione di Excel in PDF  
type: docs  
weight: 100  
url: /it/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/  
---  

{{% alert color="primary" %}}  

Quando lavori con grandi file Microsoft Excel (ad esempio un libro di lavoro con molti fogli, ognuno con 50 colonne e 300 o più righe di dati), potresti voler che l'output PDF mostri una pagina per foglio di lavoro, indipendentemente dalle dimensioni del foglio. Ciò significa che ogni pagina avrà dimensioni drasticamente diverse. Questo può essere ottenuto usando Aspose.Cells for Node.js via C++.  

{{% /alert %}}  

Si prega di vedere il seguente codice di esempio che converte un file di Excel con più fogli di lavoro in PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Implement one page per worksheet option
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setOnePagePerSheet(true);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile.out.pdf"), pdfSaveOptions);
```  

{{% alert color="primary" %}}  

Se l'opzione [PdfSaveOptions.getOnePagePerSheet()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) è impostata su **true**, tutto il contenuto del foglio verrà renderizzato in una singola pagina PDF.  

{{% /alert %}} {{% alert color="primary" %}}  

Se il foglio di calcolo contiene formule, è meglio chiamare [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) subito prima di renderizzare il foglio in PDF. Questo garantisce che i valori dipendenti dalle formule vengano ricalcolati e siano corretti nel PDF.  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
