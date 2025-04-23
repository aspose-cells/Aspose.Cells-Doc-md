---
title: Daten in einem Bereich mit Node.js über C++ suchen und ersetzen
linktitle: Daten in einem Bereich suchen und ersetzen
type: docs
weight: 170
url: /de/nodejs-cpp/search-and-replace-data-in-a-range/
description: Dieser Artikel zeigt, wie man Daten in einem Bereich in Excel mit Node.js über C++ Code suchen und ersetzen kann.
keywords: node.js Daten in Excel suchen und ersetzen, node.js Daten in Excel suchen, node.js Daten in einem Bereich suchen und ersetzen, node.js Daten in einem Bereich suchen, node.js Daten in einem Bereich suchen, node.js Daten in einem Bereich suchen, node.js Daten in Excel suchen, node.js Daten im Bereich suchen, Daten in Excel mit Node.js suchen und ersetzen, Daten in einem Bereich mit Node.js suchen und ersetzen, Daten in einem Bereich mit Node.js suchen und ersetzen
---

{{% alert color="primary" %}}

Manchmal muss man bestimmte Daten in einem Bereich suchen und ersetzen, wobei alle Zellwerte außerhalb des gewünschten Bereichs ignoriert werden. Aspose.Cells for Node.js via C++ ermöglicht es, eine Suche auf einen bestimmten Bereich zu beschränken. Dieser Artikel erklärt wie.

{{% /alert %}}

Aspose.Cells for Node.js via C++ bietet die [**FindOptions.setRange(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setRange-cellarea-)-Methode zur Angabe eines Bereichs bei der Datensuche. Das nachstehende Codebeispiel zeigt, wie Daten in einem Bereich gesucht und ersetzt werden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

const area = AsposeCells.CellArea.createCellArea("E9", "H15");

const opts = new AsposeCells.FindOptions();
opts.setLookInType(AsposeCells.LookInType.Values);
opts.setLookAtType(AsposeCells.LookAtType.EntireContent);
opts.setRange(area);

let cell = null;

do {
cell = worksheet.getCells().find("search", cell, opts);
if (cell === null || cell.isNull()) {
break;
}
cell.putValue("replace");
} while (true);

workbook.save(path.join(dataDir, "output.out.xlsx"));
```
