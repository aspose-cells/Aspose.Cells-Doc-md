---
title: Adatta tutte le colonne del foglio di lavoro su una singola pagina PDF con Node.js tramite C++
linktitle: Adatta Tutte le Colonne del Foglio di Lavoro su una Singola Pagina PDF
type: docs
weight: 160
url: /it/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

A volte si desidera generare un file PDF che adatti tutte le colonne di un foglio di lavoro in una sola pagina. La proprietà [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) fornisce questa funzionalità in modo molto semplice da utilizzare. Calcoli complessi come l'altezza e la larghezza dell'output PDF sono gestiti internamente e si basano sui dati presenti nel foglio di lavoro.

{{% /alert %}}

## **Adatta le Colonne del Foglio di Lavoro su una Singola Pagina PDF**

[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) assicura che tutte le colonne di un foglio di lavoro siano rappresentate su una singola pagina PDF, anche se le righe possono espandersi su più pagine a seconda dei dati nel foglio.

Il codice di esempio qui sotto mostra come utilizzare la proprietà [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) per rendere un ampio foglio di lavoro con 100 colonne.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create and initialize an instance of Workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Create and initialize an instance of PdfSaveOptions
const saveOptions = new AsposeCells.PdfSaveOptions();
// Set AllColumnsInOnePagePerSheet to true
saveOptions.setAllColumnsInOnePagePerSheet(true);
// Save Workbook to PDF format by passing the object of PdfSaveOptions
const outputFilePath = path.join(dataDir, "output.out.pdf");
workbook.save(outputFilePath, saveOptions);
```

{{% alert color="primary" %}}

Quando un dato foglio di lavoro ha molte colonne, il file PDF generato potrebbe mostrare il contenuto in dimensioni molto ridotte. È comunque leggibile se ingrandito in un'applicazione di visualizzazione come Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}
