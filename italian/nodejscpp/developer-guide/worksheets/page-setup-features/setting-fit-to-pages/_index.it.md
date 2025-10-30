---
title: Come stampare Excel come pagine adattate in larghezza e altezza con Node.js tramite C++
linktitle: Come stampare Excel in pagine larghe e alte adattate
type: docs
weight: 200
url: /it/nodejs-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Questo articolo mostra codice che spiega come impostare FitToPagesWide e FitToPagesTall usando Aspose.Cells for Node.js via C++.
keywords: Node.js tramite C++ Come impostare FitToPagesWide e FitToPagesTall, Come aggiungere FitToPagesWide e FitToPagesTall in Node.js, Come impostare FitToPagesWide e FitToPagesTall in Excel, Come cancellare FitToPagesWide e FitToPagesTall in Excel, Come stampare Excel come pagine adattate in larghezza e altezza, Come stampare il foglio come pagina unica, Come stampare tutte le colonne del foglio in una pagina.
---

## **Introduzione**

Le impostazioni FitToPagesWide e FitToPagesTall sono usate nelle applicazioni di fogli di calcolo (come Microsoft Excel) per controllare come viene scalato un foglio di calcolo durante la stampa. Queste impostazioni aiutano a garantire che il risultato stampato si adatti a un numero specificato di pagine, sia orizzontalmente che verticalmente. Ecco una spiegazione di ogni impostazione:

1. FitToPagesWide: questa impostazione specifica il numero di pagine di larghezza in cui il risultato stampato deve adattarsi. Ad esempio, impostando FitToPagesWide su 1 significa che il contenuto sarà ridimensionato per adattarsi a una singola pagina di larghezza, indipendentemente dalla larghezza del foglio di calcolo.
2. FitToPagesTall: Questa impostazione specifica il numero di pagine in altezza in cui il output stampato dovrebbe adattarsi. Ad esempio, impostando FitToPagesTall a 1, il contenuto verrà ridimensionato per adattarsi a un'unica altezza di pagina, indipendentemente dal numero di righe.

## **Perché usare FitToPagesWide e FitToPagesTall**
Ecco alcuni motivi per impostare FitToPagesWide e FitToPagesTall:
1. Controllo del Layout di Stampa: specificando il numero di pagine di larghezza e altezza, puoi garantire che il tuo documento stampato sia facile da leggere e ben organizzato, senza che colonne o righe siano divise in modo inappropriato tra le pagine.
2. Coerenza: Se stai stampando più fogli o report, usare queste impostazioni aiuta a mantenere un formato coerente, rendendo più facile confrontare e analizzare i documenti stampati.
3. Presentazione professionale: Ridimensionando e adattando correttamente i contenuti a un numero specificato di pagine si può ottenere una presentazione dei dati più professionale e curata.

## **Come stampare il file come pagine adattate in larghezza e altezza in Excel**

Per impostare le impostazioni FitToPagesWide e FitToPagesTall in Microsoft Excel, segui questi passaggi:

1. Apri il tuo file Excel e vai sul foglio che desideri stampare.
2. Vai alla scheda Layout di pagina sulla barra multifunzione.
3. Nella sezione Imposta pagina, clicca sulla piccola freccia in basso a destra per aprire la finestra di dialogo Imposta pagina.
4. Nella finestra di dialogo Imposta pagina, vai alla scheda Pagina.
5. Sotto Scala, seleziona l'opzione "Adatta a" e poi specifica il numero di pagine in larghezza e altezza desiderate: inserisci il numero di pagine in larghezza nel primo riquadro (Adatta a x pagine in larghezza). inserisci il numero di pagine in altezza nel secondo riquadro (Adatta a y pagine in altezza).
<br>
<img src="2.png" width=60% />

6. Clicca su OK per applicare le impostazioni.

## **Come stampare Excel come pagine adattate in larghezza e altezza usando Aspose.Cells for Node.js via C++**

Per impostare FitToPagesWide e FitToPagesTall in un foglio specifico: prima carica il [file di esempio](input.xlsx), quindi modifica le proprietà [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) e [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--) dell’oggetto [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) per il foglio desiderato. Ecco un esempio in Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Save the workbook
workbook.save("out_net.pdf");
```

Il risultato dell'output:
<br>
<img src="1.png" width=60% />

## **Come stampare il foglio come pagina unica usando Aspose.Cells for Node.js via C++**

Per stampare il foglio come pagina unica: prima carica il [file di esempio](sample.xlsx), poi imposta la proprietà [**PdfSaveOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) dell’oggetto [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/). Ecco un esempio in Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);

// Save the workbook.
workbook.save("OnePagePerSheet.pdf", options);
```

Il risultato dell'output:
<br>
<img src="3.png" width=60% />

## **Come stampare tutte le colonne del foglio in una pagina usando Aspose.Cells for Node.js via C++**

Per stampare tutte le colonne del foglio in una pagina: prima carica il [file di esempio](sample.xlsx), poi imposta la proprietà [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) dell’oggetto [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/). Ecco un esempio in Node.js:

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setAllColumnsInOnePagePerSheet(true);

// Save the workbook.
workbook.save("AllColumnsInOnePagePerSheet.pdf", options);
```

Il risultato dell'output:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="nodejs-cpp" >}}
