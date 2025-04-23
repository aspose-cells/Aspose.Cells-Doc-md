---
title: Adresse, Zellenanzahl, Offset, gesamte Spalte und gesamte Zeile des Bereichs mit Node.js über C++ abrufen
linktitle: Adresse Zellenzahl Versatz Gesamte Spalte und Gesamte Zeile des Bereichs erhalten
type: docs
weight: 330
url: /de/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells for Node.js via C++ stellt das Range-Objekt bereit, das verschiedene Dienstmethoden hat, die die Arbeit mit Excel-Bereichen erleichtern. Dieser Artikel zeigt die Verwendung der folgenden Methoden oder Eigenschaften des Range-Objekts.

- **Adresse**

Holt die Adresse des Bereichs ab.

- **Zellanzahl**

Holt alle Zellenanzahlen im Bereich ab.

- **Versatz**

Holt den Bereich durch Versatz ab.

- **Gesamte Spalte**

Ruft ein Range-Objekt ab, das die gesamte Spalte (oder Spalten) enthält, die den angegebenen Bereich enthält.

- **Gesamte Zeile**

Ruft ein Range-Objekt ab, das die gesamte Zeile (oder Zeilen) enthält, die den angegebenen Bereich enthält.

## **Holt Adresse, Zellanzahl, Versatz, gesamte Spalte und gesamte Zeile des Bereichs ab.**
Der folgende Beispielcode erklärt die Verwendung der oben diskutierten Methoden und Eigenschaften. Bitte beachten Sie die Konsolenausgabe des unten angegebenen Codes als Referenz.

## **Beispielcode**
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

## **Konsolenausgabe**
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
