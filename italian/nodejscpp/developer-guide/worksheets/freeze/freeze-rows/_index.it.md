---
title: Congela la riga superiore del foglio Excel con Node.js tramite C++
linktitle: Congelare righe
type: docs
weight: 190
url: /it/nodejs-cpp/how-to-freeze-rows-of-excel-worksheet
description: In questo articolo, imparerai come congelare le righe superiori dei fogli Excel programmaticamente utilizzando la libreria Node.js con API C++.
keywords: Congela le righe superiori, Congela la prima riga con Node.js tramite C++.
---

## **Introduzione**

In questo articolo, impareremo come congelare la/riga/rice superiore(i). Quando hai una grande quantità di dati sotto una intestazione comune, non puoi vedere l'intestazione quando scorri verso il basso il foglio di lavoro. Puoi congelare le righe superiori in modo da poter vedere quella parte congelata anche quando il resto dei dati viene sceso. Puoi facilmente vedere le intestazioni nelle righe superiori.

## **Congelare le righe in Excel**

**![Congelare la/e riga/e superiore/i in Excel](Freeze-Rows.png)**

1. Se vuoi bloccare le righe superiori, seleziona prima la riga sotto la riga che deve essere bloccata.
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Congela riga superiore.
4. Se scorri verso il basso, la prima riga rimane sempre visibile in alto.

**![Riga congelata](Frozen-Row.png)**

Come puoi vedere, la prima riga è congelata; la prima riga rimane sempre in cima alla visualizzazione quando scorri verso il basso.

Congelare le righe ti permette di visualizzare i tuoi grandi dati senza tenere traccia dell'etichetta della riga.

## **Congela le righe con Aspose.Cells for Node.js via C++**
 È semplice congelare riga(i) con Aspose.Cells for Node.js via C++. 
Si prega di usare il metodo [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) per congelare riga/righe alla riga selezionata.
1. Costruire un libro di lavoro per aprire il file o creare un file vuoto.
2. Congela la prima riga con il metodo Worksheet.freezePanes().
3. Salvare il file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("A2", 1, 0);

// Saving the file
workbook.save("frozen.xlsx");
```

File Excel di esempio allegato(../Freeze.xlsx).
{{< app/cells/assistant language="nodejs-cpp" >}}
