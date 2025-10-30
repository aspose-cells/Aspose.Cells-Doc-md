---
title: Cerca e Sostituisci Dati in un Intervallo con Node.js tramite C++
linktitle: Cerca e Sostituisci Dati in un Intervallo
type: docs
weight: 170
url: /it/nodejs-cpp/search-and-replace-data-in-a-range/
description: Questo articolo mostra come cercare e sostituire dati in un intervallo in Excel usando Node.js tramite codice C++.
keywords: node.js cerca e sostituisce dati in excel, node.js cerca dati in excel, node.js cerca e sostituisce dati in un intervallo, node.js cerca dati in un intervallo, node.js ricerca dati in un intervallo, node.js ricerca dati in intervallo, node.js ricerca dati in excel, node.js cerca dati in intervallo, cerca e sostituisci dati in excel con node.js, cerca e sostituisci dati in un intervallo con node.js, cerca e sostituisci dati in intervallo con node.js
---

{{% alert color="primary" %}}

A volte è necessario cercare e sostituire specifici dati in un intervallo ignorando eventuali valori delle celle al di fuori dell'intervallo desiderato. Aspose.Cells for Node.js via C++ ti permette di limitare una ricerca a un intervallo specifico. Questo articolo spiega come.

{{% /alert %}}

Aspose.Cells for Node.js via C++ fornisce il metodo [**FindOptions.setRange(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setRange-cellarea-) per specificare un intervallo durante la ricerca di dati. Di seguito un esempio di codice che cerca e sostituisce dati in un intervallo.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
