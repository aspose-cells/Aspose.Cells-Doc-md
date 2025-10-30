---
title: Calcolo di formule array di tabelle dati con Node.js via C++
linktitle: Calcolo della Formula Array delle Tabelle Dati
description: Come usare la libreria Aspose.Cells per calcolare le formule array di una tabella dati in Microsoft Excel usando Node.js via C++. Carica o crea un file Excel, calcola la formula array, e salva il file modificato.
keywords: Aspose.Cells, Excel, tabelle dati, formule array, calcoli Node.js via C++
type: docs
weight: 70
url: /it/nodejs-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Puoi creare una tabella dati in Microsoft Excel usando Dati > Analisi What-If > Tabella dati.... Ora Aspose.Cells permette di calcolare la formula array di una tabella dati. Usa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) come normale per calcolare qualsiasi tipo di formula.

{{% /alert %}}

Nel seguente codice di esempio, abbiamo utilizzato il [file Excel di origine](5115535.xlsx). Se si cambia il valore della cella B1 a 100, i valori della tabella dati riempiti con il colore giallo diventeranno 120 come mostrato nelle immagini seguenti. Il codice di esempio genera il [PDF di output](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Ecco il codice di esempio utilizzato per generare il [PDF di output](5115538.pdf) dal [file Excel di origine](5115535.xlsx). Si prega di leggere i commenti per ulteriori informazioni.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataTable.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.getCells().get("B1").putValue(100);

// Calculate formula, now it also calculates Data Table array formula
workbook.calculateFormula();

// Save the workbook in pdf format
workbook.save(path.join(dataDir, "output_out.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
