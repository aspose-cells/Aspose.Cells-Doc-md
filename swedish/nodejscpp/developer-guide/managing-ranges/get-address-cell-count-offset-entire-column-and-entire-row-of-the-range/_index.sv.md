---
title: Hämta adress cellantal offset hela kolumnen och hela raden av området med Node.js via C++
linktitle: Få adress Cellräkning Offset Hela kolumnen och hela raden av intervallet
type: docs
weight: 330
url: /sv/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Möjliga användningsscenario**
Aspose.Cells for Node.js via C++ tillhandahåller Range-objektet som har olika hjälpfunktioner som gör det enklare att arbeta med Excel-områden. Denna artikel visar bruket av följande metoder eller egenskaper för Range-objektet.

- **Adress**

Får adressen för intervallet.

- **Cellräkning**

Får all cellräkning i intervallet.

- **Offset**

Får intervall genom offset.

- **Hela kolumnen**

Får ett Rangeobjekt som representerar hela kolumnen (eller kolumner) som innehåller det angivna intervallet.

- **Hela raden**

Får ett Rangeobjekt som representerar hela raden (eller rader) som innehåller det angivna intervallet.

## **Få adress, Cellräkning, Offset, Hela kolumnen och Hela raden av intervallet**
Följande provkod förklarar användningen av metoderna och egenskaperna som diskuterats ovan. Se konsolresultatet för den angivna koden nedan som referens.

## **Exempelkod**
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

## **Konsoloutput**
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
{{< app/cells/assistant language="nodejs-cpp" >}}
