---
title: Impostare le opzioni di stampa con Node.js tramite C++
linktitle: Impostazione delle opzioni di stampa
type: docs
weight: 40
url: /it/nodejs-cpp/setting-print-options/
description: Questo articolo dimostra come impostare programmaticamente le opzioni di stampa della funzione Page Setup del foglio di lavoro Excel utilizzando l API Node.js e la libreria C++. Puoi impostare l area di stampa, i titoli di stampa e l ordine delle pagine.
keywords: impostare area di stampa excel con Node.js tramite C++, impostare titoli di stampa excel con Node.js tramite C++, impostare l ordine delle pagine excel con Node.js tramite C++
---

{{% alert color="primary" %}}

Le impostazioni di pagina di Microsoft Excel forniscono diverse opzioni di stampa (anche chiamate opzioni di foglio) che consentono agli utenti di controllare come vengono stampate le pagine del foglio di lavoro.

{{% /alert %}}

## **Opzioni di stampa**

Queste opzioni di stampa consentono agli utenti di:

- Selezionare un'area di stampa specifica su un foglio di lavoro.
- Stampare i titoli.
- Stampare le linee di griglia.
- Stampare gli intitoli di riga/colonna.
- Ottenere una qualità di bozza.
- Stampare commenti.
- Stampare errori di cella.
Definire l'ordinamento delle pagine.

Aspose.Cells for Node.js via C++ supporta tutte le opzioni di stampa offerte da Microsoft Excel e gli sviluppatori possono facilmente configurare queste opzioni per i fogli di lavoro utilizzando le proprietà offerte dalla classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). Di seguito si discuterà più dettagliatamente di come vengono utilizzate queste proprietà.

### **Impostare l'area di stampa**

Per impostazione predefinita, l'area di stampa incorpora tutte le aree del foglio di lavoro che contengono dati. Gli sviluppatori possono stabilire un'area di stampa specifica del foglio di lavoro.

Per selezionare una specifica area di stampa, utilizzare la proprietà [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) della classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). Assegnare a questa proprietà un intervallo di celle che definisce l'area di stampa.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Specifying the cells range (from A1 cell to T35 cell) of the print area
pageSetup.setPrintArea("A1:T35");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintArea_out.xls"));
```

### **Impostare i titoli di stampa**

Aspose.Cells consente di designare l'intestazione delle righe e delle colonne da ripetere su tutte le pagine di un foglio di lavoro stampato. Per farlo, utilizzare le proprietà [**PageSetup.getPrintTitleColumns()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleColumns--) e [**PageSetup.getPrintTitleRows()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleRows--) della classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup).

Le righe o le colonne che verranno ripetute sono definite passando il loro numero di riga o colonna. Ad esempio, le righe sono definite come $1:$2 e le colonne sono definite come $A:$B.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Defining column numbers A & B as title columns
pageSetup.setPrintTitleColumns("$A:$B");

// Defining row numbers 1 & 2 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintTitle_out.xls"));
```

### **Impostare altre opzioni di stampa**

La classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) fornisce anche diverse altre proprietà per impostare le opzioni di stampa generali come segue:

- [**PageSetup.getPrintGridlines()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintGridlines--): una proprietà booleana che definisce se stampare o meno le linee della griglia.
- [**PageSetup.getPrintHeadings()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintHeadings--): una proprietà booleana che definisce se stampare o meno le intestazioni di riga e colonna.
- [**PageSetup.getBlackAndWhite()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBlackAndWhite--): una proprietà booleana che definisce se stampare o meno il foglio in modalità bianco e nero.
- [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--): determina se visualizzare i commenti di stampa sul foglio o alla fine del foglio.
- [**PageSetup.getPrintDraft()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintDraft--): una proprietà booleana che definisce se stampare il foglio senza grafica.
- [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--): definisce se stampare gli errori delle celle come visualizzati, vuoto, trattino o N/D.

Per impostare le proprietà [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) e [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--), Aspose.Cells for Node.js via C++ fornisce anche due enumerazioni, [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) e [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype), che contengono valori predefiniti da assegnare alle proprietà [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) e [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) rispettivamente.

 I valori predefiniti dell'enumerazione [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) sono elencati di seguito con le loro descrizioni.

|**Tipi di Commenti di Stampa**|**Descrizione**|
| :- | :- |
|PrintInPlace|Specifica di stampare i commenti come visualizzati sul foglio di lavoro.|
|PrintNoComments|Specifica di non stampare i commenti.|
|PrintSheetEnd| Specifica di stampare i commenti alla fine del foglio di lavoro.

 I valori predefiniti dell'enumerazione [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) sono elencati di seguito con le loro descrizioni.

|**Tipi di Errori di Stampa**|**Descrizione**|
| :- | :- |
|PrintErrorsBlank| Specifica di non stampare gli errori.
|PrintErrorsDash| Specifica di stampare gli errori come "--".
|PrintErrorsDisplayed| Specifica di stampare gli errori come visualizzato.
|PrintErrorsNA| Specifica di stampare gli errori come "#N/A".

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Save the workbook.
workbook.save(path.join(dataDir, "OtherPrintOptions_out.xls"));
```

### **Imposta l'Ordine delle Pagine**

 La classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) fornisce la proprietà [**PageSetup.getOrder()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrder--) che viene utilizzata per ordinare le pagine multiple del tuo foglio di lavoro da stampare. Ci sono due possibilità per ordinare le pagine come segue.

- **In basso poi a destra:** stampa tutte le pagine in basso prima di stampare eventuali pagine a destra.
- **A destra poi in basso:** stampa le pagine da sinistra a destra prima di stampare le pagine sottostanti.

Aspose.Cells fornisce un'enumerazione, [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) che contiene tutti i tipi di ordinamento predefiniti.

 I valori predefiniti dell'enumerazione [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) sono elencati di seguito.

|**Tipi di Ordine di Stampa**|**Descrizione**|
| :- | :- |
|DownThenOver|Rappresenta l'ordine di stampa come in basso e poi sopra.|
|OverThenDown|Rappresenta l'ordine di stampa come sopra e poi in basso.|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook.
workbook.save(path.join(dataDir, "SetPageOrder_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
