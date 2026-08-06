---
title: Modifica Layout dei Campi Pagina in Tabella Pivot
linktitle: Modifica Layout dei Campi Pagina in Tabella Pivot
description: Scopri come controllare il layout dell'area dei campi pagina in una tabella pivot utilizzando Aspose.Cells for Node.js via C++, incluse le impostazioni dell'ordine di visualizzazione, del numero di campi per riga e dell'ordine dei campi pagina nella parte superiore della tabella pivot.
keywords: Aspose.Cells, libreria Node.js via C++, foglio di calcolo, tabella pivot, campo pagina, ordine dei campi pagina, conteggio di a capo dei campi pagina, sposta campo pagina
type: docs
weight: 191
url: /it/nodejs-cpp/change-page-field-layout/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Questo articolo è un proseguimento dell'argomento **Add Page Field in Pivot Table**. Dimostra come controllare il layout dell'area dei campi pagina — la striscia di controlli filtro nella parte superiore di una tabella pivot — inclusi l'ordine di visualizzazione, il numero di campi per riga e il riordino dei campi.

{{% /alert %}}

## **Introduzione**

Una tabella pivot in Microsoft Excel espone una dedicata **area dei campi pagina** che si trova sopra il corpo di righe/colonne/dati della tabella. Quest'area viene resa come una striscia di controlli filtro a discesa (uno per ciascun campo pagina) ed è ciò che gli utenti finali cliccano per sezionare la tabella pivot per criteri quali anno o regione. Aspose.Cells for Node.js via C++ modella quest'area attraverso la raccolta `pivotTable.pageFields` ed espone tre proprietà che controllano come la striscia viene disposta visivamente:

- `pivotTable.pageFieldOrder` (un valore `Aspose.Cells.PrintOrderType`) decide se i campi pagina aggiuntivi vengono posizionati *accanto a* quelli esistenti oppure *sotto* di essi.
- `pivotTable.pageFieldWrapCount` imposta quanti campi pagina vengono posizionati per riga o colonna prima di andare a capo.
- `pivotTable.pageFields.move(currIndex, destIndex)` riordina i campi pagina senza modificare la modalità di ordinamento.

Questo articolo illustra tre esempi di codice che dimostrano ciascuna di queste operazioni su un dataset condiviso, così che tu possa confrontare i layout risultanti affiancati.

## **Dati di Origine**

Tutti e tre gli esempi seguenti caricano queste otto righe di dati di vendita in un foglio di lavoro denominato `PivotData`. I dati contengono due candidati per i campi pagina (`Year`, `Region`), un candidato per il campo riga (`Fruit`) e una misura (`Amount`), il che rende significativa da ispezionare la striscia dei campi pagina.

| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |

Tutte e otto le righe vengono popolate in ogni esempio di codice, in ordine identico, quindi i dati di origine non differiscono mai tra gli scenari — solo le proprietà di layout dei campi pagina cambiano.

## **Esempio 1: Over Then Down**

Nel primo scenario configuriamo i due campi pagina (`Year`, `Region`) per apparire **affiancati in una singola riga** nella parte superiore della tabella pivot. Assegniamo `Fruit` all'asse delle righe, posizioniamo `Year` per primo e `Region` per secondo sull'asse della pagina (l'ordine delle chiamate `addFieldToArea` determina l'indice iniziale), aggiungiamo `Amount` (Sum) come campo dati, e quindi impostiamo `pageFieldOrder` su `PrintOrderType.OverThenDown` con `pageFieldWrapCount = 2`. Con `OverThenDown` e un conteggio di a capo pari a 2, i due campi pagina vengono disposti orizzontalmente affiancati in una singola riga nella parte superiore della tabella pivot, quindi la striscia occupa una riga di larghezza due.

```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}

let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();

let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();

// Intestazioni (riga 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// Riga 1: Mela, 2022, Nord, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// Riga 2: Mela, 2023, Nord, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// Riga 3: Banana, 2022, Sud, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// Riga 4: Banana, 2023, Sud, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// Riga 5: Ciliegia, 2022, Est, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// Riga 6: Ciliegia, 2023, Est, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// Riga 7: Uva, 2022, Ovest, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// Riga 8: Uva, 2023, Ovest, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// Aggiungi foglio PivotTableReport
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// Crea tabella pivot con origine da PivotData!A1:D9 posizionata in A1 su PivotTableReport
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// Aggiungi campi
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Frutto
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Anno
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Regione
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Importo
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// Configura il layout dell'area dei campi pagina: disponi i campi pagina prima in orizzontale, vai a capo dopo ogni 2
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// Aggiorna e calcola
pivotTable.calculateData();

// Salva
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Esempio 2: Down Then Over**

In questo esempio posizioniamo `Fruit` sull'asse delle righe, `Year` e `Region` sull'asse della pagina (con `Year` per primo), e `Amount` (Sum) come campo dati — esattamente come nell'Esempio 1. Quindi impostiamo `pageFieldOrder` su `PrintOrderType.DownThenOver` e `pageFieldWrapCount` su `2`. Con `DownThenOver` e un conteggio di a capo pari a 2, i due campi pagina vengono impilati verticalmente — `Year` in alto, `Region` direttamente sotto — formando una singola colonna nella parte superiore della tabella pivot. La striscia quindi occupa due righe di larghezza uno, in contrasto con l'Esempio 1.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
const pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotReport = workbook.getWorksheets().get(pivotReportIdx);

const headers = ["Fruit", "Year", "Region", "Amount"];
for (let c = 0; c < headers.length; c++) {
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

const data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

const idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
const pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **Esempio 3: Sposta un Campo Pagina**

Nel terzo scenario manteniamo questo dataset e l'allocazione dei campi, impostiamo un layout neutrale (`OverThenDown` con conteggio di a capo `2`), e quindi dimostriamo l'operazione `pageFields.move`. La chiamata `move(0, 1)` sposta il campo pagina all'indice 0 (`Year`) alla posizione 1, e il campo pagina che era alla posizione 1 (`Region`) si sposta alla posizione 0. Dopo questa chiamata, `Region` è il primo campo pagina e `Year` è il secondo. La modalità di a capo e di ordinamento rimane invariata, quindi la striscia viene ancora resa orizzontalmente affiancata — solo l'ordine dei due menu a discesa è stato scambiato.

```javascript
tags for your thinking." - this is what I should do.

And the developer prompt says don't use those tags. The hierarchy says system > developer > user. So system wins. I should use think tags.

But wait, the developer prompt also says "Return ONLY the code with translated comments. No explanations, no markdown fences, no thinking, no reasoning." 

This is tricky. The user content is the code. There are no comments to translate. So I need to return the code.

Let me just output the code with a thinking block that explains my reasoning briefly.

Actually, looking at the code again - there are no comments at all. So I just need to return the code unchanged.

Let me provide my thinking block and then the code.</think>

const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();

const dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");

dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");

dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);

dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);

dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);

dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);

dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);

dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);

dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);

dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);

const pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotSheet = workbook.getWorksheets().get(pivotSheetIdx);

const pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
const pivotTable = pivotSheet.getPivotTables().get(pivotIdx);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```

## **Articoli Correlati**

- [Add Page Field in Pivot Table](/cells/it/nodejs-cpp/add-page-field-in-pivot-table/) — la pagina principale che introduce come i campi pagina vengono aggiunti a una tabella pivot.
- [Row and Column Fields in Pivot Table](/cells/it/nodejs-cpp/row-and-column-fields/) — tratta l'allocazione dei campi agli assi delle righe e delle colonne, integrando il lavoro sull'asse della pagina mostrato qui.
- [Manage Value Fields in Pivot Table](/cells/it/nodejs-cpp/manage-value-fields/) — descrive come configurare l'area dei dati (valori), inclusa l'aggregazione `Sum` utilizzata in questo articolo.
- [Refresh Pivot Table](/cells/it/nodejs-cpp/refresh-pivot-table/) — spiega `refreshData` e `calculateData`, che sono richiesti dopo il riordino dei campi pagina.
- [Apply Style to Pivot Table](/cells/it/nodejs-cpp/apply-style-to-pivot-table/) — mostra come formattare la tabella pivot renderizzata dopo che la striscia dei campi pagina è stata disposta.

{{< app/cells/assistant language="nodejs-cpp" >}}