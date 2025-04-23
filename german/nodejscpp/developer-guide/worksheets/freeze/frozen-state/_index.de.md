---
title: Wie man den eingefrorenen Zustand ohne Excel mit Node.js via C++ überprüft
linktitle: Einfrierungsstatus
type: docs
weight: 190
url: /de/nodejs-cpp/how-to-check-frozen-state-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie den eingefrorenen Zustand eines Excel Arbeitsblatts programmatisch mit Node.js und C++ Bibliothek überprüfen.

---

## **Einführung**

In diesem Artikel lernen wir, wie man den eingefrorenen Zustand eines Excel-Arbeitsblatts programmatisch überprüft. Wir können einfach feststellen, ob das Arbeitsblatt eingefroren oder aufgeteilt ist in MS Excel. Aber gibt es eine Möglichkeit, festzustellen, ob es eingefroren oder aufgeteilt ist, mit Node.js? Das lässt sich einfach mit Aspose.Cells for Node.js via C++ machen.

## **Sind Fensterscheiben eingefroren?**
Mit Aspose.Cells for Node.js via C++ können wir überprüfen, ob das Fenster eingefroren ist, und wie viele Zeilen und Spalten gesperrt sind.

Bitte verwenden Sie die Eigenschaft [**Worksheet.getPaneState()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPaneState--), um den Zustand der Fensterbereiche zu überprüfen und die gesperrten Zeilen und Spalten mit der Methode [**Worksheet.getFreezedPanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFreezedPanes--) abzurufen.
1. Arbeitsmappe erstellen, um die Datei zu öffnen.
2. Überprüfen Sie, ob das Arbeitsblatt eingefroren ist.
3. Die gesperrten Zeilen und Spalten abrufen.

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Frozen.xlsx");

// Loads the workbook which contains frozen panes
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Check whether worksheet is frozen.
if (sheet.getPaneState() === AsposeCells.PaneStateType.Frozen || sheet.getPaneState() === AsposeCells.PaneStateType.FrozenSplit) {
let row, column, rows, columns;
// Gets locked rows and columns.
sheet.getFreezedPanes().forEach((value) => {
row = value[0];
column = value[1];
rows = value[2];
columns = value[3];
```  
