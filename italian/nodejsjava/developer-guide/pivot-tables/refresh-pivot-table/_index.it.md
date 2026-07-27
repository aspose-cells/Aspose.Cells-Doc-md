---
title: Aggiornare tabelle pivot e cache pivot in Aspose.Cells per Java
linktitle: Aggiornare tabelle pivot
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells per Node.js via Java usando l'API di aggiornamento v26.7+. L'articolo tratta RefreshAll, RefreshPivotTables, PivotCache.refresh, calculateData e getPivotTables con esempi di codice pratici.
keywords: Aspose.Cells, Node.js via Java, tabella pivot, aggiornamento, PivotCache, calculateData, RefreshAll, RefreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /it/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---



{{% alert color="primary" %}}
...
{{% /alert %}}

const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Tutto il resto di questo articolo spiega quando scegliere un'API più ristretta.

## Importazioni richieste

Tutti gli esempi JavaScript in questo articolo richiedono il modulo Aspose.Cells for Node.js via Java. I tipi pivot risiedono nel namespace `Aspose.Cells.Pivot`, che fa parte dello stesso modulo:

- `const aspose = require('aspose.cells');`
- Oppure per importazioni specifiche: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Aggiornare tutte le tabelle pivot nella cartella di lavoro

Quando è necessario assicurarsi che ogni pivot cache e ogni tabella pivot nella cartella di lavoro rifletta i dati di origine più recenti, l'API più semplice e completa è `Workbook.RefreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro — aggiornando ogni `PivotCache` dalla sua origine e ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti generali dell'intero documento in cui le prestazioni non sono un problema.

L'esempio seguente crea una cartella di lavoro con un intervallo di origine Fruit/Year/Amount, crea una tabella pivot, modifica alcuni valori di origine e quindi utilizza `RefreshAll()` per aggiornare tutto in un'unica chiamata.

```javascript
const AsposeCells = require("aspose.cells");

// Crea una nuova cartella di lavoro
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Scrivi la riga di intestazione nelle celle A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Scrivi le righe di dati nelle celle A2:C9 (8 righe di dati sulla frutta nel 2020 e 2021)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);

// Aggiungi una tabella pivot: intervallo di origine "A1:C9", cella di destinazione "E3", nome "Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assegna i campi pivot: Frutta alle Righe, Anno alle Colonne, Importo ai Dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modifica diversi valori di Importo nei dati di origine per simulare le modifiche
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Aggiorna ogni tabella pivot / cache pivot nella cartella di lavoro
workbook.refreshAll();

// Salva la cartella di lavoro
workbook.save("output.xlsx");
```

## Aggiornare tutte le tabelle pivot su un singolo foglio di lavoro

A volte è necessario aggiornare solo le tabelle pivot che si trovano su un foglio di lavoro specifico — ad esempio, quando le tabelle pivot su altri fogli di lavoro sono note per essere non correlate e non dovrebbero essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.RefreshPivotTables()`, che è limitato a una singola istanza di `Worksheet`.

Questo è più selettivo rispetto a `Workbook.RefreshAll()`: vengono aggiornate solo le tabelle pivot sul foglio di lavoro target, lasciando intatte le tabelle pivot sugli altri fogli di lavoro.

L'esempio seguente popola gli stessi dati di origine Fruit/Year/Amount, aggiunge una tabella pivot sul primo foglio di lavoro, modifica alcuni valori di origine e quindi aggiorna solo le tabelle pivot su quel foglio di lavoro.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);

let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);

worksheet.refreshPivotTables();

workbook.save("output.xlsx");
```

## Aggiornare una singola tabella pivot

Quando si desidera un controllo dettagliato su una singola tabella pivot, l'API basata sulla cache offre due opzioni. La scelta tra di esse dipende da ciò che è effettivamente cambiato: i dati di origine sottostanti, o solo le impostazioni di vista/layout della tabella pivot stessa.

### Dati di origine modificati — Usa `PivotCache.Refresh()`

Se i dati di origine sottostanti sono cambiati, il punto di ingresso corretto è `pivotTable.PivotCache.Refresh()`. Questa chiamata rilegge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da quella cache.

{{% alert color="primary" %}}

Poiché le tabelle pivot condividono una singola istanza di `PivotCache`, la chiamata a `PivotCache.Refresh()` ricalcola **tutte** le tabelle pivot costruite su quella stessa cache — non solo quella a cui si fa riferimento. Se due tabelle pivot condividono lo stesso intervallo di origine, l'aggiornamento di una cache aggiorna entrambe.

{{% /alert %}}

L'esempio seguente crea due tabelle pivot sullo stesso intervallo di origine per dimostrare questo comportamento di cache condivisa, modifica alcuni valori di origine e quindi aggiorna tramite un riferimento di cache.

```javascript
const AsposeCells = require("aspose.cells");

// Crea una nuova cartella di lavoro e accedi al primo foglio di lavoro
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Scrivi la riga di intestazione: Frutto / Anno / Importo
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Scrivi circa 9 righe di dati (uva / mirtillo / kiwi / ciliegia tra 2020-2021)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// Aggiungi la prima tabella pivot "Pivot1" ancorata alla cella E3, intervallo di origine A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Assegna i campi per Pivot1
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Aggiungi una SECONDA tabella pivot "Pivot2" ancorata a E15 utilizzando lo STESSO intervallo di origine A1:C9
// Sia Pivot1 che Pivot2 condividono un unico PivotCache perché l'intervallo di origine è identico.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Assegna gli stessi campi per Pivot2
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modifica diversi valori delle celle Importo nei dati di origine per simulare un cambio di dati
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Aggiorna il PivotCache condiviso.
// Poiché Pivot1 e Pivot2 condividono lo stesso PivotCache, questa singola chiamata
// aggiorna ENTRAMBE le tabelle pivot (dati + stile) dall'origine aggiornata.
pivotTable1.getPivotCache().refresh();

// Salva la cartella di lavoro
workbook.save("output.xlsx");
```

### Solo vista/layout modificati — Usa `CalculateData()`

Se i dati di origine *non* sono cambiati ma sono state modificate solo le impostazioni di vista o layout della tabella pivot (ad esempio, un campo è stato spostato in un'area diversa, o un'impostazione di aggiornamento all'apertura è stata attivata/disattivata), non è necessario effettuare un round-trip verso l'origine dati. La cache contiene già i dati corretti; solo la `PivotTable` resa necessita di ricalcolo. In questo caso, `pivotTable.CalculateData()` è la scelta giusta.

Ciò evita l'inutile recupero dell'origine ed è significativamente più veloce quando molte tabelle pivot condividono la stessa cache.

L'esempio seguente modifica una proprietà non di origine della tabella pivot e quindi chiama `CalculateData()` per ri-renderizzarla dalla cache esistente.

```javascript
new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Scrivi la riga di intestazione Frutto / Anno / Importo
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Scrivi 8 righe di dati (righe 2-9, adattandosi all'intervallo di origine A1:C9)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);

// Aggiungi una tabella pivot denominata "Pivot1" posizionata nella cella di destinazione E3, con origine da A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assegna i campi: Frutto a Riga, Anno a Colonna, Importo a Dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modifica una proprietà di visualizzazione/layout — questo è un cambiamento solo di presentazione,
// quindi NON richiede di ricaricare i dati di origine tramite PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() ridisegna la visualizzazione di QUESTA tabella pivot (dati + stile) dai
// dati già presenti nella PivotCache. Poiché i dati di origine non sono cambiati,
// non viene eseguito alcun ritorno all'origine — vengono ricalcolati solo i valori memorizzati nella cache
// nelle celle del foglio di lavoro.
pivotTable.calculateData();

// Salva la cartella di lavoro su disco
workbook.save("output.xlsx");
```

## Ottenere tutte le tabelle pivot che condividono lo stesso PivotCache

Una cartella di lavoro spesso contiene molte tabelle pivot che poggiano tutte su una cache condivisa. Per enumerarle — ad esempio, prima di eseguire un aggiornamento in batch, o per diagnosticare l'impatto della cache condivisa — utilizzare `PivotCache.GetPivotTables()`. Questo metodo restituisce la raccolta di ogni `PivotTable` che dipende dalla cache specificata.

Questo è anche il modo più diretto per confermare che due tabelle pivot condividono effettivamente la stessa istanza di `PivotCache`: è possibile confrontare i riferimenti di cache, o semplicemente iterare la raccolta restituita da `GetPivotTables()` e osservare quali tabelle pivot vi compaiono.

L'esempio seguente crea due tabelle pivot sullo stesso intervallo di origine, verifica che condividano la stessa istanza di cache e quindi enumera le tabelle pivot della cache.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

let pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## Migrazione dall'obsoleto `PivotTable.RefreshData()`

Prima di Aspose.Cells for Node.js via Java v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.RefreshData()` su ciascuna tabella pivot individualmente. A partire dalla v26.7, quel metodo è contrassegnato come **obsoleto** e dovrebbe essere sostituito con le API consapevoli della cache descritte sopra.

Ci sono due motivi per cui l'approccio `RefreshData()` per tabella è problematico nelle cartelle di lavoro reali:

- Recupera i dati dall'origine *ogni* volta che viene chiamato, anche quando l'origine non è cambiata.
- Ogni chiamata aggiorna l'intera cache condivisa. Quando molte tabelle pivot condividono una cache, chiamare ripetutamente `RefreshData()` per tabella pivot fa sì che la stessa cache venga recuperata più e più volte, il che è molto lento.

Le sostituzioni consigliate sono:

- **Aggiornare TUTTE le tabelle pivot nella cartella di lavoro** → usare `workbook.refreshAll();`
- **Aggiornarne ALCUNE** → usare `pivotTable.getPivotCache().refresh();` per una cache. Poiché la cache è condivisa, questa singola chiamata aggiorna ogni tabella pivot costruita sopra quella cache. Altre tabelle pivot che poggiano su una cache già aggiornata possono essere tranquillamente saltate.
- **Solo la vista/layout della pivot è cambiata** → usare `pivotTable.calculateData();` per ri-renderizzare dalla cache esistente senza alcun round-trip dell'origine.

L'esempio seguente dimostra il nuovo pattern efficiente per cartelle di lavoro con più tabelle pivot che condividono una singola cache.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- Costruisci i dati di origine: Frutto / Anno / Importo (intestazione + 9 righe) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- Aggiungi la prima tabella pivot (Pivot1) alla cella di destinazione E3 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Aggiungi la SECONDA tabella pivot (Pivot2) sullo STESSO intervallo di origine ---
// Sia Pivot1 che Pivot2 condividono UN unico PivotCache sottostante.
// Questo è esattamente lo scenario in cui l'approccio legacy RefreshData() per tabella
// diventa inefficiente: aggiornando una tabella si recupera di nuovo l'intero
// cache condiviso, quindi aggiornando N tabelle si esegue la stessa operazione costosa N volte.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Modifica diversi valori di Importo nei dati di origine ---
sheet.getCells().get("C2").putValue(5000);   // Uva 2020
sheet.getCells().get("C5").putValue(7500);   // Ciliegia 2020
sheet.getCells().get("C9").putValue(9500);   // Ciliegia 2021

// --- Schema OBSOLETO (pre-26.7) — PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // recupera di nuovo dall'origine, aggiorna l'intera cache
// pivotTable2.refreshData();  // recupera DI NUOVO — la cache è già aggiornata!
// Ogni chiamata ricostruisce la cache condivisa, quindi N tabelle = N recuperi ridondanti.

// --- NUOVO schema v26.7+: aggiorna la cache UNA VOLTA, quindi rirendirizza secondo necessità ---
// Una sola chiamata a PivotCache.Refresh() recupera i valori modificati nella cache condivisa
// E ricalcola la visualizzazione di OGNI tabella pivot che vi fa riferimento.
// Poiché Pivot1 e Pivot2 condividono un unico PivotCache, questa singola chiamata aggiorna
// entrambe le tabelle — non è necessario un secondo viaggio di andata e ritorno dall'origine.
pivotTable1.getPivotCache().refresh();

// CalculateData() rirendizza solo la visualizzazione di una tabella pivot (dati + stile)
// dai dati già presenti nella cache — NON tocca l'origine.
// Lo chiamiamo qui su Pivot2 puramente per dimostrare l'API: dopo che la cache
// è stata aggiornata una volta, qualsiasi tabella dipendente può essere rirenderizzata senza
// tornare all'origine. Usa CalculateData() da solo quando solo le impostazioni
// di visualizzazione/layout della tabella pivot sono cambiate e la cache è aggiornata.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Quale API di aggiornamento dovrei usare?

La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna.

| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.RefreshAll()` | Una chiamata; copre tutte le cache e tabelle. |
| Aggiornare solo le tabelle pivot su un singolo foglio | `Worksheet.RefreshPivotTables()` | Limitato a un foglio di lavoro. |
| Dati di origine cambiati per una cache | `pivotTable.PivotCache.Refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Solo impostazioni di vista/layout cambiate | `pivotTable.CalculateData()` | Salta l'inutile round-trip dell'origine. |
| Elencare tutte le tabelle pivot su una cache condivisa | `pivotCache.GetPivotTables()` | Usare per enumerare prima dell'aggiornamento in blocco. |

In pratica, preferire le API basate sulla cache rispetto all'obsoleto `RefreshData()` per tabella. Sono consapevoli delle cache condivise, evitano recuperi ridondanti dall'origine e consentono di scegliere l'ambito più piccolo che soddisfa il requisito di aggiornamento.


## Problemi comuni

- **Forgetting to refresh before saving.** A pivot table only writes its rendered values into the worksheet when its data chain is refreshed. If you modify source cells, call `PivotCache.refresh()` (or `Workbook.refreshAll()`) before `save()`, otherwise the saved file still contains the old aggregated values.
- **Calling the obsolete `refreshData()` per table.** In v26.7, `PivotTable.refreshData()` is marked obsolete and re-fetches the source for every call. With multiple pivot tables sharing a cache this means N redundant source fetches. Replace with a single `PivotCache.refresh()` followed by `calculateData()` per table.
- **Refreshing when only the layout changed.** If you only changed a pivot table's view (column order, `ConsolidationFunction`, etc.) without touching source data, `PivotCache.refresh()` is unnecessary and slow. Call `calculateData()` to re-render from the existing cache.
- **External source not supported by `PivotCache.refresh()`.** If the pivot table's source comes from an external connection (database, OLAP cube, etc.), `PivotCache.refresh()` cannot refresh it in v26.7 — it currently only supports `Sheet` and `Consolidation` source types. For external sources, re-open the workbook or rebuild the cache from the source.


- [Inserimento di un'immagine in una cella](/cells/it/nodejs-java/inserting-an-image-into-a-cell/)
- [Lettura e scrittura di file DBF](/cells/it/nodejs-java/dbf/)
- [Divisione di file Excel in più file](/cells/it/nodejs-java/splitting-excel-files-into-multiple-files/)
- [Sparkline in Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/sparkline/)
{{< app/cells/assistant language="javascript" >}}
