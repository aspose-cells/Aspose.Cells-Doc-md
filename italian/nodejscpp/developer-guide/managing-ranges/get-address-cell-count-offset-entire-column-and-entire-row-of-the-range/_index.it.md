---
title: Ottieni indirizzo, numero di celle, offset, intera colonna e intera riga dell intervallo con Node.js tramite C++
linktitle: Ottenere Conteggio Cellule Indirizzo Spostamento Intera Colonna e Intera Riga della Gamma
type: docs
weight: 330
url: /it/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells for Node.js via C++ fornisce l'oggetto Range che ha vari metodi utili per facilitare l'utente nel lavorare con gli intervalli di Excel. Questo articolo illustra l'uso dei seguenti metodi o proprietà dell'oggetto Range.

- **Indirizzo**

Ottiene l'indirizzo della gamma.

- **Conteggio celle**

Ottiene il conteggio di tutte le celle nella gamma.

- **Spostamento**

Ottiene la gamma per spostamento.

- **Intera Colonna**

Restituisce un oggetto Range che rappresenta l'intera colonna (o colonne) che contiene il range specificato.

- **Intera Riga**

Restituisce un oggetto Range che rappresenta l'intera riga (o righe) che contiene il range specificato.

## **Ottieni Indirizzo, Conteggio Celle, Spostamento, Intera Colonna e Intera Riga del Range**
Il seguente codice di esempio spiega l'uso dei metodi e delle proprietà come discusso in precedenza. Si prega di consultare l'output della console del codice fornito di seguito per un riferimento.

## **Codice di Esempio**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Create range A1:B3.
console.log("Creating Range A1:B3\n");
let rng = ws.getCells().createRange("A1:B3");

// Print range address and cell count.
console.log("Range Address: " + rng.getAddress());
console.log("Range row Count: " + rng.getRowCount());
console.log("Range column Count: " + rng.getColumnCount());

// Formatting console output.
console.log("----------------------");
console.log("");

// Create range A1.
console.log("Creating Range A1\n");
rng = ws.getCells().createRange("A1");

// Print range offset, entire column and entire row.
console.log("Offset: " + rng.getOffset(2, 2).getAddress());
console.log("Entire Column: " + rng.getEntireColumn().getAddress());
console.log("Entire Row: " + rng.getEntireRow().getAddress());

// Formatting console output.
console.log("----------------------");
console.log("");
```

## **Output della console**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
