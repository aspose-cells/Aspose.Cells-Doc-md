---
title: Sblocca righe o colonne con Node.js tramite C++
linktitle: Scongelare riquadri
type: docs
weight: 190
url: /it/nodejs-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: In questo articolo imparerai come sbloccare righe, colonne o pannelli di fogli Excel programmaticamente utilizzando l API Node.js con C++.
keywords: Sblocca pannelli, sblocca righe, sblocca colonne, sblocca finestra Node.js tramite C++.
---

## **Introduzione**

In questo articolo impareremo come sbloccare righe, colonne e pannelli. Se i fogli di lavoro nei file Excel sono bloccati, a volte vogliamo sbloccare il foglio di lavoro o regolare righe, colonne o pannelli bloccati.


## **In Excel**

1. Fare clic sulla scheda Visualizzazione > Riquadri bloccati > Scongela riquadri.

**![scongelare riquadri in Excel](Scongela-Riquadri.png)**




## **Sblocca righe, colonne o pannelli con Aspose.Cells for Node.js via C++**
È semplice sbloccare pannelli con Aspose.Cells for Node.js via C++. Usa il metodo [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unFreezePanes--) per sbloccare i pannelli.

1. Costruisci il workbook per aprire il file bloccato.
2. Sblocca pannelli con il metodo Worksheet.unfreezePanes().
3. Salvare il file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const frozenFilePath = path.join(dataDir, "Frozen.xlsx");

const workbook = new AsposeCells.Workbook(frozenFilePath); 
workbook.getWorksheets().get(0).unFreezePanes();
workbook.save("Unfrozen.xlsx");
```

Allegato il [file Excel di origine di esempio](Frozen.xlsx).
