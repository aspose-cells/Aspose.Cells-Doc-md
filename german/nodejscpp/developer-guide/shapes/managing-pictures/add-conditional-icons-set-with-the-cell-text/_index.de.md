---
title: Bedingte Symbolsets mit Zelltext mit Node.js über C++ hinzufügen
linktitle: Bedingte Symbolsätze mit dem Zellentext hinzufügen
type: docs
weight: 160
url: /de/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/
description: Lernen Sie, wie Sie bedingte Symbole neben dem Zelltext mit Aspose.Cells for Node.js via C++ hinzufügen. Verbesserung der Bedeutung der Daten durch Symbole.
---

{{% alert color="primary" %}} 

Manchmal möchten Sie bedingte Symbole neben dem Text in einer Zelle hinzufügen, um Daten für die Leser aussagekräftiger zu machen. Sie möchten einige der bedingten Formatierungssymboltypen verwenden, ohne die bedingte Formatierung auf Zellen anzuwenden. Aspose.Cells for Node.js via C++ unterstützt diese Funktion.

{{% /alert %}} 

Das folgende Codebeispiel zeigt, wie man bedingte Symbolsätze mit dem Zellentext hinzufügt.



```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet (default worksheet) in the workbook
const worksheet = workbook.getWorksheets().get(0);
// Get the cells
const cells = worksheet.getCells();
// Set the columns widths (A, B and C)
worksheet.getCells().setColumnWidth(0, 24);
worksheet.getCells().setColumnWidth(1, 24);
worksheet.getCells().setColumnWidth(2, 24);

// Input date into the cells
cells.get("A1").putValue("KPIs");
cells.get("A2").putValue(19551794);
cells.get("A3").putValue(11.8070745566204);
cells.get("A4").putValue(11.858589818569);
cells.get("B1").putValue("UA Contract Size Group 4");
cells.get("B2").putValue(19551794);
cells.get("B3").putValue(11.8070745566204);
cells.get("B4").putValue(11.858589818569);
cells.get("C1").putValue("UA Contract Size Group 3");
cells.get("C2").putValue(8150131.66666667);
cells.get("C3").putValue(10.3168384396244);
cells.get("C4").putValue(11.3326931937091);

// Get the conditional icon's image data and add pictures
const iconTypes = [
{ type: AsposeCells.IconSetType.TrafficLights31, row: 1, column: 1 },
{ type: AsposeCells.IconSetType.Arrows3, row: 1, column: 2 },
{ type: AsposeCells.IconSetType.Symbols3, row: 2, column: 1 },
{ type: AsposeCells.IconSetType.Stars3, row: 2, column: 2 },
{ type: AsposeCells.IconSetType.Boxes5, row: 3, column: 1 },
{ type: AsposeCells.IconSetType.Flags3, row: 3, column: 2 }
];

iconTypes.forEach(icon => {
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(icon.type, icon.type === AsposeCells.IconSetType.Flags3 ? 1 : 0);
const stream = new Uint8Array(imagedata);
worksheet.getPictures().add(icon.row, icon.column, stream);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
