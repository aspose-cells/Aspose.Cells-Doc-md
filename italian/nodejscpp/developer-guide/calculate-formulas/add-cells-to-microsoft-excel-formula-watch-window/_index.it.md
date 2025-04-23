---
title: Aggiungi Celle alla finestra di Watch delle formule di Microsoft Excel con Node.js tramite C++
linktitle: Aggiungi celle alla finestra di monitoraggio delle formule di Microsoft Excel
description: Come usare la libreria Aspose.Cells per aggiungere celle alla finestra di watch delle formule in Excel utilizzando Node.js via C++. Caricando un file Excel esistente o creandone uno nuovo, possiamo manipolare le celle e impostare formule. Alla fine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, Finestra di watch delle formule, Celle, Aggiunta, Node.js via C++
type: docs
weight: 60
url: /it/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Possibili Scenari di Utilizzo**

La finestra di watch di Microsoft Excel è uno strumento utile per osservare i valori delle celle e le relative formule comodamente in una finestra. Puoi aprire la *Finestra di Watch* usando Microsoft Excel cliccando su *Formulas > Watch* *Window*. Ha il pulsante *Add Watch* che può essere usato per aggiungere le celle da ispezionare. In modo simile, puoi usare il metodo [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cellwatchcollection/#add-number-number-) per aggiungere celle alla *Watch Window* usando l'API di Aspose.Cells.

## **Aggiungere celle alla finestra di visualizzazione della formula di Microsoft Excel**

Il seguente esempio di codice imposta le formule delle celle C1 ed E1 e le aggiunge entrambe alla finestra di watch. Successivamente, salva il workbook come [file Excel di output](67338481.xlsx). Se apri il file Excel di output e visualizzi la *Finestra di Watch*, vedrai entrambe le celle come mostrato in questa schermata.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Codice di Esempio**

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

// Put some integer values in cell A1 and A2.
ws.getCells().get("A1").putValue(10);
ws.getCells().get("A2").putValue(30);

// Access cell C1 and set its formula.
const c1 = ws.getCells().get("C1");
c1.setFormula("=Sum(A1,A2)");

// Add cell C1 into cell watches by name.
ws.getCellWatches().add(c1.getName());

// Access cell E1 and set its formula.
const e1 = ws.getCells().get("E1");
e1.setFormula("=A2*A1");

// Add cell E1 into cell watches by its row and column indices.
ws.getCellWatches().add(e1.getRow(), e1.getColumn());

// Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", AsposeCells.SaveFormat.Xlsx);
```
