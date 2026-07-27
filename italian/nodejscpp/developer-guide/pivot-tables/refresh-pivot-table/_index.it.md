---
title: Aggiornamento delle tabelle pivot in Aspose.Cells for Node.js via C++
linktitle: Aggiornamento delle tabelle pivot
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells for Node.js via C++ utilizzando l'API di aggiornamento delle pivot v26.7+, questo articolo illustra RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData e GetPivotTables con esempi pratici di codice.
keywords: Aspose.Cells, Node.js via C++, tabella pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells fornisce un'API di aggiornamento a più livelli che consente di ricaricare i dati pivot in quattro ambiti diversi — dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for Node.js via C++ v26.7**, il metodo legacy `PivotTable.RefreshData()` è contrassegnato come obsoleto e dovrebbe essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.

{{% /alert %}}

## Introduzione

L'aggiornamento di una tabella pivot raramente è una singola operazione. Dietro le quinte, Aspose.Cells mantiene una catena di dati a più livelli che collega i dati di origine originali ai valori visualizzati nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento giusta per ogni situazione.

La catena di dati a quattro livelli è:

1. **Origine dati** — gli intervalli originali del foglio di lavoro, le query di database o gli intervalli di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati di origine. Ogni tabella pivot è costruita sopra un `PivotCache`; è qui che tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto vista che definisce i campi riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dal proprio `PivotCache`, mai direttamente dall'origine dati.
4. **Cells** — le `Cells` del foglio di lavoro in cui la `PivotTable` rende i valori calcolati e gli stili.

Un concetto particolarmente importante è la **cache condivisa**. Quando più tabelle pivot in una cartella di lavoro fanno riferimento allo stesso intervallo di origine, condividono *una* singola istanza di `PivotCache`. Un singolo `PivotCache` può essere referenziato da molte tabelle pivot, e l'aggiornamento di quella cache aggiorna immediatamente ogni `PivotTable` dipendente.

{{% alert color="primary" %}}

`PivotCache.SourceType` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire da v26.7, `PivotCache.Refresh()` supporta solo i tipi di origine **`Sheet`** e **`Consolidation`** — ovvero dati che risiedono negli intervalli del foglio di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.

{{% /alert %}}

A causa di questa catena, esistono due percorsi di aggiornamento fondamentali in Aspose.Cells:

- **`PivotCache.Refresh()`** — ricarica l'origine nella cache E ricalcola tutte le `PivotTable` dipendenti in un'unica operazione.
- **`PivotTable.CalculateData()`** — ricalcola la visualizzazione di una `PivotTable` dai dati già memorizzati nella cache, senza tornare all'origine dati.

Tutti gli scenari in questo articolo utilizzano dati di origine provenienti da celle del foglio di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.

## Importazioni richieste

Tutti gli esempi JavaScript in questo articolo presuppongono che il modulo Aspose.Cells for Node.js via C++ sia stato caricato e che i tipi pivot risiedano nel namespace `Aspose.Cells.Pivot`. Una configurazione tipica è:

- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (oppure accedere tramite `AsposeCells.Pivot.PivotFieldType`)

## Aggiornare tutte le tabelle pivot nella cartella di lavoro

Quando è necessario garantire che ogni cache pivot e ogni tabella pivot nella cartella di lavoro rifletta i dati di origine più recenti, l'API più semplice e completa è `Workbook.RefreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro — aggiornando ogni `PivotCache` dalla propria origine e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti generali e completi del documento in cui le prestazioni non sono un problema.

L'esempio seguente crea una cartella di lavoro con un intervallo di origine Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori di origine e quindi utilizza `RefreshAll()` per portare tutto aggiornato in un'unica chiamata.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Scrivi la riga di intestazione nelle celle A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Scrivi le righe di dati nelle celle A2:C9 (8 righe di dati sulla frutta per il 2020 e il 2021)
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
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assegna i campi pivot: Fruit a Righe, Year a Colonne, Amount a Dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modifica diversi valori di Amount nei dati di origine per simulare le modifiche
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Aggiorna ogni tabella pivot / cache pivot nella cartella di lavoro
workbook.refreshAll();

// Salva la cartella di lavoro
workbook.save("output.xlsx");
```

## Aggiornare tutte le tabelle pivot su un singolo foglio di lavoro

A volte è necessario aggiornare solo le tabelle pivot che si trovano su un foglio di lavoro specifico — ad esempio, quando le tabelle pivot su altri fogli di lavoro non sono correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.RefreshPivotTables()`, che è limitato a una singola istanza di `Worksheet`.

Questo è più selettivo rispetto a `Workbook.RefreshAll()`: vengono aggiornate solo le tabelle pivot nel foglio di lavoro di destinazione, lasciando intatte le tabelle pivot negli altri fogli di lavoro.

L'esempio seguente popola gli stessi dati di origine Frutto/Anno/Importo, aggiunge una tabella pivot sul primo foglio di lavoro, modifica alcuni valori di origine e quindi aggiorna solo le tabelle pivot su quel foglio di lavoro.

```javascript
= new AsposeCells.Workbook();
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

Quando si desidera un controllo granulare su una singola tabella pivot, l'API basata sulla cache offre due opzioni. La scelta tra esse dipende da cosa è effettivamente cambiato: i dati di origine sottostanti, o solo le impostazioni di vista/layout della tabella pivot stessa.

### Dati di origine modificati — Usare `PivotCache.Refresh()`

Se i dati di origine sottostanti sono cambiati, il giusto punto di ingresso è `pivotTable.PivotCache.Refresh()`. Questa chiamata rilegge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da quella cache.

{{% alert color="primary" %}}

Poiché le tabelle pivot condividono una singola istanza di `PivotCache`, chiamare `PivotCache.Refresh()` ricalcola **tutte** le tabelle pivot costruite su quella stessa cache — non solo quella a cui fai riferimento. Se due tabelle pivot condividono lo stesso intervallo di origine, l'aggiornamento di una cache aggiorna entrambe.

{{% /alert %}}

L'esempio seguente crea due tabelle pivot sullo stesso intervallo di origine per dimostrare questo comportamento di cache condivisa, modifica alcuni valori di origine e quindi aggiorna tramite un riferimento di cache.

```javascript
const AsposeCells = require("aspose.cells");

// Crea una nuova cartella di lavoro e accedi al primo foglio di lavoro
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Scrivi la riga di intestazione: Frutto / Anno / Quantità
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Scrivi circa 9 righe di dati (uva / mirtillo / kiwi / ciliegia per 2020-2021)
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

// Aggiungi una SECONDA tabella pivot "Pivot2" ancorata a E15 usando lo STESSO intervallo di origine A1:C9
// Sia Pivot1 che Pivot2 condividono un singolo PivotCache perché l'intervallo di origine è identico.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Assegna gli stessi campi per Pivot2
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modifica diversi valori delle celle Quantità nei dati di origine per simulare una modifica dei dati
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

### Solo vista/layout modificati — Usare `CalculateData()`

Se i dati di origine *non* sono cambiati ma solo le impostazioni di vista o layout della tabella pivot sono state modificate (ad esempio, un campo è stato spostato in un'area diversa, o un'impostazione di aggiornamento all'apertura è stata attivata/disattivata), non è necessario tornare all'origine dati. La cache contiene già i dati corretti; solo la `PivotTable` renderizzata deve essere ricalcolata. In questo caso, `pivotTable.CalculateData()` è la scelta giusta.

Questo evita l'inutile recupero dall'origine ed è significativamente più veloce quando molte tabelle pivot condividono la stessa cache.

L'esempio seguente modifica una proprietà non di origine della tabella pivot e quindi chiama `CalculateData()` per renderizzarla di nuovo dalla cache esistente.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Scrivi la riga di intestazione Frutto / Anno / Importo
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Scrivi 8 righe di dati (righe 2-9, corrispondenti all'intervallo sorgente A1:C9)
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

// Assegna i campi: Fruit a Riga, Year a Colonna, Amount a Dati
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

// Modifica una proprietà di visualizzazione/layout — si tratta di una modifica solo di presentazione,
// quindi NON richiede la rilettura dei dati sorgente tramite PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() ridisegna la visualizzazione di QUESTA tabella pivot (dati + stile) dai
// dati già presenti nella PivotCache. Poiché i dati sorgente non sono cambiati,
// non viene eseguito alcun round-trip verso la sorgente — vengono ricalcolati solo i valori memorizzati nella cache
// nelle celle del foglio di lavoro.
pivotTable.calculateData();

// Salva la cartella di lavoro su disco
workbook.save("output.xlsx");
```

## Ottenere tutte le tabelle pivot che condividono lo stesso PivotCache

Una cartella di lavoro spesso contiene molte tabelle pivot che si trovano tutte sopra una cache condivisa. Per enumerarle — ad esempio, prima di eseguire un aggiornamento in batch, o per diagnosticare l'impatto della cache condivisa — utilizzare `PivotCache.GetPivotTables()`. Questo metodo restituisce la raccolta di tutte le `PivotTable` che dipendono dalla cache data.

Questo è anche il modo più diretto per confermare che due tabelle pivot condividono effettivamente la stessa istanza di `PivotCache`: è possibile confrontare i riferimenti della cache, o semplicemente iterare la raccolta restituita da `GetPivotTables()` e osservare quali tabelle pivot appaiono in essa.

L'esempio seguente crea due tabelle pivot sullo stesso intervallo di origine, verifica che condividono la stessa istanza di cache e quindi enumera le tabelle pivot della cache.

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
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## Migrazione dall'obsoleto `PivotTable.RefreshData()`

Prima di Aspose.Cells for Node.js via C++ v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.RefreshData()` su ciascuna tabella pivot individualmente. A partire da v26.7, quel metodo è contrassegnato come **obsoleto** e dovrebbe essere sostituito con le API consapevoli della cache descritte sopra.

Ci sono due motivi per cui l'approccio per-tabella `RefreshData()` è problematico nelle cartelle di lavoro reali:

- Recupera i dati dall'origine *ogni* volta che viene chiamato, anche quando l'origine non è cambiata.
- Ogni chiamata aggiorna l'intera cache condivisa. Quando molte tabelle pivot condividono una cache, chiamare ripetutamente `RefreshData()` per ogni tabella pivot fa sì che la stessa cache venga recuperata più e più volte, il che è molto lento.

Le sostituzioni consigliate sono:

- **Aggiornare TUTTE le tabelle pivot nella cartella di lavoro** → utilizzare `workbook.refreshAll();`
- **Aggiornare ALCUNE di esse** → utilizzare `pivotTable.PivotCache.Refresh();` per una cache. Poiché la cache è condivisa, questa singola chiamata aggiorna ogni tabella pivot costruita sopra quella cache. Altre tabelle pivot che si trovano su una cache già aggiornata possono essere tranquillamente saltate.
- **Solo la vista/layout della pivot è cambiata** → utilizzare `pivotTable.CalculateData();` per renderizzare di nuovo dalla cache esistente senza alcun round-trip all'origine.

L'esempio seguente dimostra il nuovo modello efficiente per cartelle di lavoro con più tabelle pivot che condividono una singola cache.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- Costruisce i dati sorgente: Frutta / Anno / Importo (intestazione + 9 righe) ---
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

// --- Aggiunge la prima tabella pivot (Pivot1) nella cella di destinazione E3 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Aggiunge la SECONDA tabella pivot (Pivot2) sullo STESSO intervallo sorgente ---
// Sia Pivot1 che Pivot2 condividono UN unico PivotCache sottostante.
// Questo è esattamente lo scenario in cui l'approccio legacy RefreshData()
// per singola tabella diventa inefficiente: aggiornare una tabella recupera
// nuovamente l'intera cache condivisa, quindi aggiornare N tabelle comporta
// lo stesso recupero dispendioso N volte.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Modifica diversi valori di Importo nei dati sorgente ---
sheet.getCells().get("C2").putValue(5000);   // Grape  2020
sheet.getCells().get("C5").putValue(7500);   // Cherry 2020
sheet.getCells().get("C9").putValue(9500);   // Cherry 2021

// --- Pattern OBSOLETO (pre-26.7) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // recupera dalla sorgente, aggiorna l'intera cache
// pivotTable2.RefreshData();  // recupera DI NUOVO — la cache è già aggiornata!
// Ogni chiamata ricostruisce la cache condivisa, quindi N tabelle = N recuperi ridondanti.

// --- NUOVO pattern v26.7+: aggiorna la cache UNA VOLTA, poi rirenderizza se necessario ---
// Una singola chiamata a PivotCache.Refresh() recupera i valori modificati nella
// cache condivisa E ricalcola la visualizzazione di OGNI tabella pivot che vi fa riferimento.
// Poiché Pivot1 e Pivot2 condividono un unico PivotCache, questa singola chiamata
// aggiorna entrambe le tabelle — non è richiesto un secondo round-trip alla sorgente.
pivotTable1.getPivotCache().refresh();

// CalculateData() rirenderizza solo la visualizzazione di una tabella pivot
// (dati + stile) dai dati già presenti nella cache — NON tocca la sorgente.
// Lo chiamiamo su Pivot2 qui solo per dimostrare l'API: dopo che la cache
// è stata aggiornata una volta, qualsiasi tabella dipendente può essere
// rirenderizzata senza tornare alla sorgente. Usa CalculateData() da sola
// quando sono cambiate solo le impostazioni di vista/layout della tabella
// pivot e la cache è aggiornata.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Quale API di aggiornamento dovrei usare?

La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna.

| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.RefreshAll()` | Una chiamata; copre tutte le cache e le tabelle. |
| Aggiornare solo le tabelle pivot su un singolo foglio | `Worksheet.RefreshPivotTables()` | Limitato a un foglio di lavoro. |
| Dati di origine modificati per una cache | `pivotTable.PivotCache.Refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Solo le impostazioni di vista/layout sono cambiate | `pivotTable.CalculateData()` | Evita l'inutile round-trip all'origine. |
| Elencare tutte le tabelle pivot su una cache condivisa | `pivotCache.GetPivotTables()` | Utilizzare per enumerare prima dell'aggiornamento in blocco. |

In pratica, preferire le API basate sulla cache rispetto all'obsoleto `RefreshData()` per tabella. Sono consapevoli delle cache condivise, evitano recuperi ridondanti dall'origine e consentono di scegliere l'ambito più piccolo che soddisfa il requisito di aggiornamento.

## Articoli correlati

- [Inserimento di un'immagine in una cella](/cells/it/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Lettura e scrittura di file DBF](/cells/it/nodejs-cpp/dbf/)
- [Divisione di file Excel in più file](/cells/it/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Sparkline in Aspose.Cells for Node.js via C++](/cells/it/nodejs-cpp/sparkline/)

{{< app/cells/assistant language="javascript" >}}