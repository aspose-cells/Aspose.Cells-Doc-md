---  
title: Come impostare il punto come totale con Node.js tramite C++  
linktitle: Come impostare un punto come totale  
description: Impara a impostare i punti come totali nei grafici WaterFall usando Aspose.Cells for Node.js via C++.  
keywords: Grafico WaterFall, Punto, Impostare come totale, Node.js tramite C++  
type: docs  
weight: 72  
url: /it/nodejs-cpp/how-to-set-point-as-total/  
---  

## Cos'è "Impostare il punto come totale" in un grafico Excel

In alcuni grafici Excel, come ad esempio il grafico WaterFall, alcuni valori dei punti sono la somma dei punti precedenti, e potrebbe essere necessario "impostare il punto come totale". Mostreremo il codice di esempio e l'illustrazione di seguito.

## Un grafico WaterFall necessita di "Impostare il punto come totale" 

![todo:image_alt_text](set-as-total1.png)

Questa immagine mostra un grafico WaterFall in Excel. Possiamo vedere che ci sono quattro punti dati che iniziano con "Total", e sono usati per calcolare tutti i punti dati precedenti. In questa immagine, le impostazioni non sono esattamente corrette. Quando si seleziona un punto "Total 2024", si può vedere che l'opzione "Imposta come totale" non è selezionata in Excel. Allegato sotto c'è il [file Excel di esempio](SampleSheet.xlsx) che necessita di modifiche, e useremo Aspose.Cells for Node.js via C++ per configurarlo correttamente.

## Usare Aspose.Cells for Node.js via C++ per "Impostare il punto come totale" 

Usiamo il seguente codice per configurare correttamente il file:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const chart = worksheet.getCharts().get("Graphiq5");

// set some points as total column 
// In this example, we set points 0, 4, 8, 12 as total
chart.getNSeries().get(0).getLayoutProperties().setSubtotals([0, 4, 8, 12]);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Puoi ottenere il [file di output corretto](output.xlsx)

Come mostrato nell'immagine seguente, i quattro punti dati "Total" sono impostati correttamente, e puoi vedere la differenza rispetto al grafico precedente.

![todo:image_alt_text](set-as-total2.png)  
