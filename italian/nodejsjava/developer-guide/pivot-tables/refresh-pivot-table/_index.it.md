---
title: Refresh Pivot Tables and Pivot Caches in Aspose.Cells for Node.js via Java
linktitle: Refresh Pivot Tables and Pivot Caches
description: Learn how to refresh pivot tables in Aspose.Cells for Node.js via Java using the v26.7+ pivot-refresh API. This article covers RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData, and GetPivotTables with practical code examples.
keywords: Aspose.Cells, Node.js, Java, tabella pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce un'API di aggiornamento a più livelli che consente di ricaricare i dati delle tabelle pivot in quattro ambiti diversi, dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for Node.js via Java v26.7**, il metodo legacy `PivotTable.RefreshData()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.
{{% /alert %}}

## Introduction
Aggiornare una tabella pivot raramente è un'operazione singola. Dietro le quinte, Aspose.Cells mantiene una catena dati a più livelli che collega i dati sorgente originali ai valori renderizzati che si vedono nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento giusta per ogni situazione.
La catena dati a quattro livelli è:
1. **Data Source** — gli intervalli originali del foglio di lavoro, la query del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati sorgente. Ogni tabella pivot è costruita sopra una `PivotCache`; è qui che tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto vista che definisce i campi riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dalla sua `PivotCache`, mai direttamente dalla fonte dati.
4. **Cells** — le `Cells` del foglio di lavoro in cui la `PivotTable` rende i valori calcolati e gli stili.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire dalla v26.7, `PivotCache.refresh()` supporta solo i tipi di sorgente **`Sheet`** e **`Consolidation`**, ovvero dati che risiedono negli intervalli del foglio di lavoro. Le sorgenti esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.
A causa di questa catena, ci sono due percorsi di aggiornamento fondamentali in Aspose.Cells:
- **`PivotTable.calculateData()`** — ricalcola la visualizzazione di una `PivotTable` dai dati già in cache, senza tornare alla fonte dati.
Tutti gli scenari in questo articolo utilizzano dati sorgente da celle del foglio di lavoro, quindi il tipo di sorgente è `Sheet` e le operazioni di aggiornamento si comportano come descritto.
{{% /alert %}}

## Quick Start
Se hai bisogno solo del codice più breve possibile che aggiorni ogni pivot nella cartella di lavoro, una singola chiamata è sufficiente:

```javascript
const aspose = require('aspose.cells');
const workbook = new aspose.cells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Tutto il resto in questo articolo spiega quando scegliere invece un'API più ristretta.

## Required Imports
- `const aspose = require('aspose.cells');`
- Oppure per importazioni specifiche: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Refresh All Pivot Tables in the Workbook
Quando è necessario garantire che ogni pivot cache e ogni tabella pivot nella cartella di lavoro riflettano i dati sorgente più recenti, l'API più semplice e completa è `Workbook.refreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla sua sorgente e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti generali e completi del documento in cui le prestazioni non sono un problema.
L'esempio seguente crea una cartella di lavoro con un intervallo sorgente Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori sorgente e quindi utilizza `refreshAll()` per portare tutto aggiornato in una singola chiamata.

```javascript
const AsposeCells = require("aspose.cells");
// Create a new workbook
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
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
// Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

## Refresh All Pivot Tables on a Single Worksheet
A volte è necessario aggiornare solo le tabelle pivot che si trovano su un foglio di lavoro specifico, ad esempio quando le tabelle pivot su altri fogli di lavoro sono note per non essere correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.refreshPivotTables()`, che è limitato a una singola istanza di `Worksheet`.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
Quando si desidera un controllo granulare su una singola tabella pivot, l'API basata sulla cache offre due opzioni. La scelta tra esse dipende da ciò che è effettivamente cambiato: i dati sorgente sottostanti, o solo le impostazioni di vista/layout della tabella pivot stessa.

### Source Data Changed — Use `PivotCache.refresh()`
Se i dati sorgente sottostanti sono cambiati, il punto di ingresso corretto è `pivotTable.PivotCache.refresh()`. Questa chiamata rilegge i dati sorgente nella cache e quindi ricalcola ogni `PivotTable` che dipende da quella cache.

### Only View/Layout Changed — Use `calculateData()`
Se i dati sorgente *non* sono cambiati ma sono state modificate solo le impostazioni di vista o layout della tabella pivot (ad esempio, un campo è stato spostato in un'area diversa, o un'impostazione di aggiornamento all'apertura è stata attivata), non è necessario tornare alla fonte dati. La cache contiene già i dati corretti; solo la `PivotTable` renderizzata deve essere ricalcolata. In questo caso, `pivotTable.calculateData()` è la scelta giusta.
L'esempio seguente modifica una proprietà non sorgente della tabella pivot e quindi chiama `calculateData()` per renderizzarla nuovamente dalla cache esistente.

```javascript
const AsposeCells = require("aspose.cells");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write 8 data rows (rows 2-9, fitting the source range A1:C9)
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
// Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Modify a view/layout property — this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed — only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

Una cartella di lavoro spesso contiene molte tabelle pivot che si trovano tutte sopra una cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento in batch, o per diagnosticare l'impatto della cache condivisa, utilizzare `PivotCache.getPivotTables()`. Questo metodo restituisce la raccolta di ogni `PivotTable` che dipende dalla cache data.

## Migrating from the Obsolete `PivotTable.RefreshData()`
Prima di Aspose.Cells for Node.js via Java v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.RefreshData()` su ogni tabella pivot individualmente. Dalla v26.7, quel metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API consapevoli della cache descritte sopra.
Ci sono due motivi per cui l'approccio `RefreshData()` per tabella è problematico nelle cartelle di lavoro reali:
- Recupera nuovamente i dati dalla sorgente *ogni* volta che viene chiamato, anche quando la sorgente non è cambiata.
Le sostituzioni consigliate sono:
L'esempio seguente dimostra il nuovo schema efficiente per cartelle di lavoro con più tabelle pivot che condividono una singola cache.

## Which Refresh API Should I Use?
La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.refreshAll()` | Una chiamata; copre tutte le cache e le tabelle. |
| Aggiornare solo le tabelle pivot su un singolo foglio | `Worksheet.refreshPivotTables()` | Limitato a un foglio di lavoro. |
| Dati sorgente cambiati per una cache | `pivotTable.PivotCache.refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Solo impostazioni di vista/layout cambiate | `pivotTable.calculateData()` | Evita il round-trip non necessario alla sorgente. |
| Elencare tutte le tabelle pivot su una cache condivisa | `pivotCache.getPivotTables()` | Da usare per enumerare prima dell'aggiornamento in blocco. |
In pratica, preferisci le API basate sulla cache rispetto all'obsoleto `RefreshData()` per tabella. Sono consapevoli delle cache condivise, evitano recuperi sorgente ridondanti e ti consentono di scegliere il più piccolo ambito che soddisfa il tuo requisito di aggiornamento.

## Common Pitfalls
- **Dimenticare di aggiornare prima di salvare.** Una tabella pivot scrive i suoi valori renderizzati nel foglio di lavoro solo quando la sua catena dati viene aggiornata. Se modifichi le celle sorgente, chiama `PivotCache.refresh()` (o `Workbook.refreshAll()`) prima di `Workbook.save()`, altrimenti il file salvato contiene ancora i vecchi valori aggregati.
- **Chiamare l'obsoleto `RefreshData()` per tabella.** Nella v26.7, `PivotTable.RefreshData()` è contrassegnato come obsoleto e recupera la sorgente per ogni chiamata. Con più tabelle pivot che condividono una cache, questo significa N recuperi sorgente ridondanti. Sostituisci con una singola `PivotCache.refresh()` seguita da `calculateData()` per tabella.
- **Aggiornare quando è cambiato solo il layout.** Se hai cambiato solo la vista di una tabella pivot (ordine delle colonne, `ConsolidationFunction`, ecc.) senza toccare i dati sorgente, `PivotCache.refresh()` è inutile e lento. Chiama `pivotTable.calculateData()` per renderizzare nuovamente dalla cache esistente.
- **Sorgente esterna non supportata da `PivotCache.refresh()`.** Se la sorgente della tabella pivot proviene da una connessione esterna (database, cubo OLAP, ecc.), `PivotCache.refresh()` non può aggiornarla nella v26.7 — attualmente supporta solo i tipi di sorgente `Sheet` e `Consolidation`. Per le sorgenti esterne, riaprire la cartella di lavoro o ricostruire la cache dalla sorgente.

{{< app/cells/assistant language="nodejs-java" >}}