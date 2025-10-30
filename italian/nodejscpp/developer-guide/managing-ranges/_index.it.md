---
title: Gestione degli Intervalli con Node.js tramite C++
linktitle: Intervalli
type: docs
weight: 105
url: /it/nodejs-cpp/managing-ranges/
description: Impara come gestire gli intervalli in Excel usando Aspose.Cells for Node.js via C++. Crea intervalli, imposta valori, stili e svolgi varie operazioni.
---

## **Introduzione**

In Excel, puoi selezionare più celle con una selezione tramite il mouse; il insieme di celle selezionate è chiamato "Intervallo".

Ad esempio, puoi cliccare con il pulsante sinistro del mouse nella cella "A1" di Excel e quindi trascinare fino alla cella "C4". L'area rettangolare selezionata può essere facilmente creata anche come un oggetto utilizzando Aspose.Cells for Node.js via C++.

Ecco come creare un intervallo, inserire un valore, impostare uno stile e svolgere altre operazioni sull'oggetto "Intervallo".

## **Gestione degli Intervalli con Aspose.Cells for Node.js via C++**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una raccolta [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).

### **Crea Intervallo**

Quando si desidera creare un'area rettangolare che si estende da A1 a C4, è possibile utilizzare il seguente codice:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
```

### **Inserire un valore nelle celle dell'Intervallo**

Supponiamo di avere un intervallo di celle che si estende da A1 a C4. La matrice crea 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte in sequenza: Intervallo[0,0], Intervallo[0,1], Intervallo[0,2], Intervallo[1,0], Intervallo[1,1], Intervallo[1,2], Intervallo[2,0], Intervallo[2,1], Intervallo[2,2], Intervallo[3,0], Intervallo[3,1], Intervallo[3,2].

Nell'esempio seguente viene mostrato come inserire alcuni valori nelle celle dell'Intervallo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "RangeValueTest.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook();
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
// Put value
range.get(0, 0).setValue("A1");
range.get(0, 1).setValue("B1");
range.get(0, 2).setValue("C1");
range.get(3, 0).setValue("A4");
range.get(3, 1).setValue("B4");
range.get(3, 2).setValue("C4");
// Save the Workbook
workbook.save(filePath);
```

### **Impostare lo stile delle celle dell'Intervallo**

Il seguente esempio mostra come impostare lo stile delle celle dell'Intervallo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Creates a Workbook
const workbook = new AsposeCells.Workbook();
// Gets Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Creates Range
const range = cells.createRange("A1:C4");
// Puts value
range.get(0, 0).setValue("A1");
range.get(3, 2).setValue("C4");
// Sets Style
let style00 = workbook.createStyle();
style00.setPattern(AsposeCells.BackgroundType.Solid);
style00.setForegroundColor(new AsposeCells.Color(255, 0, 0)); // Red
range.get(0, 0).setStyle(style00);
let style32 = workbook.createStyle();
style32.setPattern(AsposeCells.BackgroundType.HorizontalStripe);
style32.setForegroundColor(new AsposeCells.Color(0, 255, 0)); // Green
range.get(3, 2).setStyle(style32);
// Saves the Workbook
workbook.save("RangeStyleTest.xlsx");
```

### **Ottieni la CurrentRegion del Range**

CurrentRegion è una proprietà che restituisce un oggetto Range che rappresenta la regione corrente. 

La regione corrente è una gamma delimitata da qualsiasi combinazione di righe o colonne vuote. Solo lettura.

In Excel, puoi ottenere l'area CurrentRegion tramite:
1. Seleziona un'area (range1) con il box del mouse.
2. Clicca su "Home - Editing - Trova e Seleziona - Vai a Speciale - Regione Corrente", o usa "Ctrl+Shift+*", vedrai che Excel ti aiuta automaticamente a selezionare un'area (range2). Ora l'hai fatto, range2 è la Regione Corrente di range1.

Scarica il file di test seguente, aprilo in Excel, usa il box del mouse per selezionare un'area "A1:D7", quindi clicca su "Ctrl+Shift+*", vedrai l'area "A1:C3" selezionata.

[current_region.xlsx](current_region.xlsx)

Ora esegui il seguente esempio per vedere come funziona in Aspose.Cells:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "current_region.xlsx");
// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("A1:D7");
// Get CurrentRegion
const A1C3 = src.getCurrentRegion();
```


## **Argomenti avanzati**
- [Riempimento automatico dell'area del file Excel](/cells/it/nodejs-cpp/autofill-ranges/)
- [Copia dei range di Excel](/cells/it/nodejs-cpp/copy-ranges-of-Excel/)
- [Copia solo i dati dell'intervallo.](/cells/it/nodejs-cpp/copy-range-data-only/)
- [Copia intervallo dati con stile.](/cells/it/nodejs-cpp/copy-range-data-with-style/)
- [Copia solo lo stile dell'intervallo](/cells/it/nodejs-cpp/copy-range-style-only/)
- [Crea un intervallo di unione](/cells/it/nodejs-cpp/create-union-range/)
- [Taglia e incolla il range](/cells/it/nodejs-cpp/cut-and-paste-cells/)
- [Elimina ranges](/cells/it/nodejs-cpp/delete-ranges-from-Excel/)
- [Ottieni l'indirizzo, il conteggio delle celle, lo spostamento, l'intera colonna e la riga intera del range](/cells/it/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Inserisci ranges](/cells/it/nodejs-cpp/insert-ranges-to-Excel/)
- [Unisci o Separa Intervallo di Celle](/cells/it/nodejs-cpp/merge-or-unmerge-range-of-cells/)
- [Sposta Intervallo di Celle in un Foglio di Lavoro](/cells/it/nodejs-cpp/move-range-of-cells-in-a-worksheet/)
- [Crea Riferimenti con Nome a Livello di Cartella e Foglio di Lavoro](/cells/it/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Cerca e Sostituisci Dati in un Intervallo](/cells/it/nodejs-cpp/search-and-replace-data-in-a-range/)
{{< app/cells/assistant language="nodejs-cpp" >}}
