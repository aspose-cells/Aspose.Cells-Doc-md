---
title: Converti file XLS con immagini o grafici in PDF con Node.js tramite C++
linktitle: Converti il file XLS con immagini o grafici nel formato PDF
type: docs
weight: 50
url: /it/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells supporta la conversione di file XLS che contengono immagini e grafici in documenti PDF. Aspose.Cells for Node.js via C++ può funzionare indipendentemente per convertire un foglio di calcolo in PDF: Aspose.PDF per Node.js tramite C++ non è richiesto per la conversione. Il processo può essere eseguito in memoria in quanto non dipende da file XML temporanei o intermedi. Ciò significa che grandi file Excel, ad esempio contenenti immagini, grafici e altri oggetti di disegno, possono essere convertiti rapidamente ed efficientemente.

{{% /alert %}} 
## **Codice di Esempio**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
try {
// Get the template excel file path.
const designerFile = path.join(dataDir, "SampleInput.xls");

// Specify the pdf file path.
const pdfFile = path.join(dataDir, "Output.out.pdf");

// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}} 

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) giusto prima di esportare in PDF. In questo modo si garantisce che i valori dipendenti dalle formule siano ricalcolati e i valori corretti vengano rappresentati nel PDF.

{{% /alert %}}
