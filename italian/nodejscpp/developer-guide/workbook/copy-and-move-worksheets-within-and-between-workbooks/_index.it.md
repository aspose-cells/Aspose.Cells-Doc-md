---
title: Copia e sposta fogli di lavoro all’interno e tra i file con Node.js tramite C++
linktitle: Copiare e Spostare Fogli di Lavoro All interno e Tra Workbooks
type: docs
weight: 80
url: /it/nodejs-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Impara come copiare e spostare fogli di lavoro all’interno e tra i file usando Aspose.Cells for Node.js via C++. Gestisci efficacemente le strutture del tuo workbook.
---

{{% alert color="primary" %}}

A volte è necessario un numero di fogli di lavoro con formattazione comune e inserimento dati. Ad esempio, se lavori con i bilanci trimestrali, potresti voler creare un foglio con fogli che contengono gli stessi titoli di colonna, titoli di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo tre volte.

Aspose.Cells for Node.js via C++ supporta la copia o lo spostamento di fogli di lavoro all’interno o tra i file. I fogli di lavoro con dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti vengono copiati con il massimo livello di precisione.

{{% /alert %}}

## **Copia e Sposta Fogli di Lavoro**

### **Copiare un foglio di lavoro all'interno di un libro di lavoro**

I passaggi iniziali sono gli stessi per tutti gli esempi.

1. Creare due libri di lavoro con alcuni dati in Microsoft Excel. A fini di questo esempio, abbiamo creato due nuovi libri di lavoro in Microsoft Excel e inserito alcuni dati nei fogli di lavoro.

- FirstWorkbook.xlsx (3 fogli di lavoro).
- SecondWorkbook.xlsx (1 foglio di lavoro).

1. Scarica e installa Aspose.Cells:
   1. [Scarica Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).
   1. Installalo sul tuo computer di sviluppo.
      Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. Crea un progetto:
   1. Avvia il tuo ambiente di sviluppo.
   1. Crea una nuova applicazione console.
1. Aggiungi riferimenti:
   1. Aggiungere un riferimento a Aspose.Cells al progetto.
      Ad esempio, aggiungi un riferimento a ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll
1. Copia il foglio di lavoro all'interno di un workbook
   Il primo esempio copia il primo foglio di lavoro (Copia) all'interno di FirstWorkbook.xlsx.

Quando si esegue il codice, il foglio di lavoro chiamato Copia viene copiato all'interno di FirstWorkbook.xlsx con il nome Ultimo foglio.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open a file into the first book.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "FirstWorkbook.xlsx"));

// Copy the first sheet of the first book within the workbook
excelWorkbook1.getWorksheets().get(2).copy(excelWorkbook1.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "FirstWorkbookCopied_out.xlsx"));
```

### **Spostamento di un foglio di lavoro all'interno di un workbook**

Il codice sottostante mostra come spostare un foglio di lavoro da una posizione all'interno di un workbook a un'altra. Eseguendo il codice sposta il foglio di lavoro chiamato Spostare dall'indice 1 all'indice 2 in FirstWorkbook.xlsx.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "FirstWorkbook.xlsx");
// Open a file into the first book.
const excelWorkbook2 = new AsposeCells.Workbook(filePath);

// Move the sheet
const worksheets = excelWorkbook2.getWorksheets();
const worksheet = worksheets.get(0);
worksheet.moveTo(1);

// Save the file.
excelWorkbook2.save(path.join(dataDir, "FirstWorkbookMoved_out.xlsx"));
```

### **Copia un Foglio di Lavoro tra i Workbooks**

Eseguendo il codice si copia il foglio di lavoro chiamato Copy nel file SecondWorkbook.xlsx con il nome Sheet2.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const excelWorkbook3 = new AsposeCells.Workbook();
const excelWorkbook4 = new AsposeCells.Workbook();

// Create source worksheet
excelWorkbook3.getWorksheets().add("Copy");

// Add new worksheet into second Workbook
excelWorkbook4.getWorksheets().add();

// Copy the first sheet of the first book into second book.
excelWorkbook4.getWorksheets().get(1).copy(excelWorkbook3.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook4.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xlsx"));
```

### **Spostare un foglio di lavoro tra i Workbooks**

Eseguendo il codice sposta il foglio di lavoro chiamato Spostare da FirstWorkbook.xlsx a SecondWorkbook.xlsx con il nome Foglio3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbooks instead of opening existing files
const excelWorkbook5 = new AsposeCells.Workbook();
const excelWorkbook6 = new AsposeCells.Workbook();

// Add New Worksheet
excelWorkbook6.getWorksheets().add();

// Copy the sheet from first book into second book.
excelWorkbook6.getWorksheets().get(0).copy(excelWorkbook5.getWorksheets().get(0));

// Remove the copied worksheet from first workbook
excelWorkbook5.getWorksheets().removeAt(0);

// Save the file.
excelWorkbook5.save(path.join(dataDir, "FirstWorkbookWithMove_out.xlsx"));

// Save the file.
excelWorkbook6.save(path.join(dataDir, "SecondWorkbookWithMove_out.xlsx"));
```
