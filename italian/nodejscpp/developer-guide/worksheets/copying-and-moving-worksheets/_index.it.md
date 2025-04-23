---
title: Copiare e spostare fogli di lavoro con Node.js tramite C++
linktitle: Copiare e Spostare Fogli di Lavoro
type: docs
weight: 10
url: /it/nodejs-cpp/copying-and-moving-worksheets/
description: Questo articolo include codice di esempio e descrive come copiare e spostare fogli di lavoro programmaticamente sia all interno di un libro Excel che tra libri Excel usando l API Node.js con C++.
keywords: copia foglio di lavoro Node.js, sposta foglio di lavoro Node.js
---

{{% alert color="primary" %}}

A volte è necessario avere un numero di fogli di lavoro con formattazione e dati comuni. Ad esempio, se si lavora con budget trimestrali, potrebbe essere necessario creare un libro con fogli che contengono gli stessi titoli di colonna, titoli di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo.

Aspose.Cells for Node.js via C++ supporta la copia e lo spostamento di fogli di lavoro all’interno o tra i libri di lavoro. Il foglio di lavoro, completo di dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti, viene copiato con il massimo livello di precisione.

{{% /alert %}}

## **Spostare o Copiare Fogli Usando Microsoft Excel**

Di seguito sono riportati i passaggi coinvolti nella copia e nel trasferimento dei fogli di lavoro all'interno o tra i fogli di lavoro in Microsoft Excel.

1. Per spostare o copiare i fogli in un altro libro, aprire il libro che riceverà i fogli.
1. Passare al libro che contiene i fogli da spostare o copiare, e quindi selezionare i fogli.
1. Nel menu **Modifica**, fare clic su **Sposta o Copia Foglio**.
1. Nella finestra di dialogo **Al libro**, fare clic sul workbook per ricevere i fogli.
1. Per spostare o copiare i fogli selezionati in un nuovo workbook, fare clic su **Nuovo libro**.
1. Nella casella **Prima del foglio**, fare clic sul foglio prima del quale si desidera inserire i fogli spostati o copiati.
1. Per copiare i fogli anziché spostarli, selezionare la casella **Crea copia**.

### **Copiare fogli di lavoro all’interno di un libro di lavoro con Aspose.Cells for Node.js via C++**

Aspose.Cells fornisce un metodo sovraccaricato, [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#addCopy-number-), che viene utilizzato per aggiungere un foglio di lavoro alla raccolta e copiare i dati da un foglio di lavoro esistente. Una versione del metodo prende l'indice del foglio di lavoro di origine come parametro. L'altra versione prende il nome del foglio di lavoro di origine.

Nell'esempio seguente viene mostrato come copiare un foglio di lavoro esistente all'interno di un libro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Open an existing Excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to
// the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Copy data to a new sheet from an existing
// sheet within the Workbook.
sheets.addCopy("Sheet1");

// Save the Excel file.
wb.save(path.join(dataDir, "CopyWithinWorkbook_out.xls"));
```

### **Copiare i Fogli di Lavoro tra Cartelle di Lavoro**

Aspose.Cells fornisce un metodo, [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-), usato per copiare dati e formattazione da un foglio di lavoro di origine a un altro foglio di lavoro all’interno o tra i libri di lavoro. Il metodo prende come parametro l’oggetto del foglio di lavoro di origine.

L'esempio seguente mostra come copiare un foglio di lavoro da un libro di lavoro a un altro libro di lavoro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Create a Workbook.
// Open a file into the first book.
const excelWorkbook0 = new AsposeCells.Workbook(inputPath);

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Copy the first sheet of the first book into second book.
excelWorkbook1.getWorksheets().get(0).copy(excelWorkbook0.getWorksheets().get(0));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xls"));
```

L'esempio seguente mostra come copiare un foglio di lavoro da un libro di lavoro a un altro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook.
const excelWorkbook0 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws0 = excelWorkbook0.getWorksheets().get(0);

// Put some data into header rows (A1:A4)
for (let i = 0; i < 5; i++) {
ws0.getCells().get(i, 0).putValue(`Header Row ${i}`);
}

// Put some detail data (A5:A999)
for (let i = 5; i < 1000; i++) {
ws0.getCells().get(i, 0).putValue(`Detail Row ${i}`);
}

// Define a pagesetup object based on the first worksheet.
const pagesetup = ws0.getPageSetup();

// The first five rows are repeated in each page...
// It can be seen in print preview.
pagesetup.setPrintTitleRows("$1:$5");

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Name the worksheet.
ws1.setName("MySheet");

// Copy data from the first worksheet of the first workbook into the
// first worksheet of the second workbook.
ws1.copy(ws0);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetFromWorkbookToOther_out.xls"));
```

### **Sposta i fogli di lavoro all'interno del libro di lavoro**

Aspose.Cells fornisce un metodo [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#moveto-number-) che viene usato per spostare un foglio di lavoro in un’altra posizione nello stesso foglio di calcolo. Il metodo prende come parametro l’indice del foglio di lavoro di destinazione.

L'esempio seguente mostra come spostare un foglio di lavoro in un'altra posizione all'interno del libro di lavoro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "sample1.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get the first worksheet.
const worksheet = sheets.get(0);

// Move the first sheet to the third position in the workbook.
worksheet.moveTo(2);

// Save the excel file.
wb.save(path.join(dataDir, "MoveWorksheet_out.xls"));
```
