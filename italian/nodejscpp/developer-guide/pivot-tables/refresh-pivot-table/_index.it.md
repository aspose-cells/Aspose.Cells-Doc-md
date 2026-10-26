---
title: Aggiornare tabelle pivot e cache pivot in Aspose.Cells for Node.js via C++
linktitle: Aggiornare tabelle pivot e cache pivot
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells for Node.js via C++ usando l'API di aggiornamento pivot v26.7+. Questo articolo descrive refreshAll, refreshPivotTables, PivotCache.refresh, calculateData e getPivotTables con esempi di codice pratici.
keywords: Aspose.Cells, Node.js via C++, tabella pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce un'API di aggiornamento su più livelli che consente di ricaricare i dati pivot in quattro ambiti diversi, dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for Node.js via C++ v26.7**, il metodo tradizionale `PivotTable.RefreshData()` è contrassegnato come obsoleto e deve essere sostituito dalle API più efficienti e che tengono conto della cache descritte in questo articolo.
{{% /alert %}}

## Introduction
L'aggiornamento di una tabella pivot raramente consiste in una singola operazione. Dietro le quinte, Aspose.Cells mantiene una catena di dati su più livelli che collega i dati di origine originali ai valori visualizzati nel foglio di lavoro. La comprensione di questa catena è essenziale per scegliere l'API di aggiornamento giusta in ogni situazione.
La catena di dati a quattro livelli è:
1. **Origine dati** — gli intervalli di origine del foglio di lavoro, la query del database o l'intervallo di consolidamento in cui sono presenti i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati di origine. Ogni tabella pivot è costruita su un `PivotCache`; qui tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto visuale che definisce i campi riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dal proprio `PivotCache`, mai direttamente dalla fonte dati.
4. **Cells** — le `Cells` del foglio di lavoro in cui la `PivotTable` rende i valori calcolati e applica gli stili.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) indica l'origine dei dati della cache. A partire da v26.7, `PivotCache.refresh()` supporta soltanto i tipi di origine **`Sheet`** e **`Consolidation`**, ovvero i dati contenuti in intervalli di foglio di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non possono ancora essere aggiornate tramite l'API della cache.
Poiché esiste questa catena, in Aspose.Cells sono disponibili due percorsi fondamentali di aggiornamento:
- **`PivotTable.calculateData()`** — ricalcola la visualizzazione di una singola `PivotTable` usando i dati già presenti nella cache, senza dover tornare alla fonte dati.
Tutti gli scenari di questo articolo utilizzano dati di origine contenuti nelle celle del foglio di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.
{{% /alert %}}

## Quick Start
Se basta aggiornare tutte le tabelle pivot della cartella di lavoro con il codice più breve possibile, è sufficiente una singola chiamata:

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Il resto di questo articolo spiega quando conviene scegliere un'API con un ambito più ristretto.

## Required Imports
Tutti gli esempi JavaScript di questo articolo presuppongono che il modulo Aspose.Cells for Node.js via C++ sia stato caricato e che i tipi pivot si trovino nel namespace `Aspose.Cells.Pivot`. Una configurazione tipica è:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (oppure accedere tramite `AsposeCells.Pivot.PivotFieldType`)

## Refresh All Pivot Tables in the Workbook
Quando è necessario garantire che tutte le cache pivot e tutte le tabelle pivot della cartella di lavoro riflettano i dati di origine più aggiornati, l'API più semplice e completa è `Workbook.refreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla propria origine e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per gli aggiornamenti generali dell'intero documento quando le prestazioni non costituiscono un problema.
L'esempio seguente costruisce una cartella di lavoro con un intervallo di origine Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori di origine e quindi utilizza `refreshAll()` per aggiornare tutto con una singola chiamata.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
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
// Add a pivot table: source range "A1:C9", destination cell "E3"
let pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
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
Talvolta è necessario aggiornare soltanto le tabelle pivot presenti in un determinato foglio di lavoro, ad esempio quando quelle in altri fogli sono note come non correlate e non devono essere modificate. Per questo caso, Aspose.Cells fornisce `Worksheet.refreshPivotTables()`, che opera nell'ambito di una singola istanza di `Worksheet`.

```javascript
const AsposeCells = require("aspose.cells.node");
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
let pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
Quando si desidera un controllo dettagliato di una singola tabella pivot, l'API basata sulla cache offre due opzioni. La scelta dipende da ciò che è effettivamente cambiato: i dati di origine sottostanti oppure solo le impostazioni di visualizzazione o layout della tabella pivot.

### Source Data Changed — Use `PivotCache.refresh()`
Se i dati di origine sottostanti sono cambiati, il punto di ingresso corretto è `pivotTable.PivotCache.refresh()`. Questa chiamata rilegge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da essa.

### Only View/Layout Changed — Use `calculateData()`
Se i dati di origine *non* sono cambiati, ma sono state modificate soltanto le impostazioni di visualizzazione o layout della tabella pivot, ad esempio quando un campo è stato spostato in un'area diversa o quando è stata attivata o disattivata un'impostazione di aggiornamento all'apertura, non è necessario tornare alla fonte dati. La cache contiene già i dati corretti; occorre soltanto ricalcolare la `PivotTable` visualizzata. In questo caso, `pivotTable.calculateData()` è la scelta appropriata.
L'esempio seguente modifica una proprietà della tabella pivot che non riguarda la fonte e quindi chiama `calculateData()` per rigenerarne il rendering dalla cache esistente.

```javascript
const AsposeCells = require("aspose.cells.node");
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
// Add a pivot table placed at destination cell E3, sourcing from A1:C9
var pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
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

Una cartella di lavoro contiene spesso molte tabelle pivot, tutte basate sulla stessa cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento massivo o per diagnosticare l'impatto di una cache condivisa, usare `PivotCache.getPivotTables()`. Questo metodo restituisce la raccolta di tutte le `PivotTable` che dipendono dalla cache specificata.

## Migrating from the Obsolete `PivotTable.RefreshData()`
Prima di Aspose.Cells for Node.js via C++ v26.7, il modo standard di aggiornare una tabella pivot era chiamare `PivotTable.RefreshData()` per ogni tabella pivot. A partire da v26.7, il metodo è contrassegnato come **obsoleto** e deve essere sostituito dalle API basate sulla cache descritte in precedenza.
Esistono due motivi per cui l'approccio basato su `RefreshData()` per singola tabella presenta problemi nelle cartelle di lavoro reali:
- Riescarica i dati dalla fonte *a ogni chiamata*, anche quando la fonte non è cambiata.
Le API sostitutive consigliate sono:
L'esempio seguente dimostra il nuovo schema efficiente per cartelle di lavoro con più tabelle pivot che condividono una singola cache.

## Which Refresh API Should I Use?
La tabella seguente riepiloga le API di aggiornamento disponibili e indica quando scegliere ciascuna di esse.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto il contenuto della cartella di lavoro | `Workbook.refreshAll()` | Una singola chiamata; copre tutte le cache e le tabelle. |
| Aggiornare solo le tabelle pivot di un singolo foglio | `Worksheet.refreshPivotTables()` | Limitato a un foglio di lavoro. |
| Modifica dei dati di origine per una cache | `pivotTable.PivotCache.refresh()` | Aggiorna TUTTE le tabelle pivot che utilizzano la cache condivisa. |
| Modifica delle sole impostazioni di visualizzazione o layout | `pivotTable.calculateData()` | Evita il ritorno non necessario alla fonte. |
| Elenco di tutte le tabelle pivot basate su una cache condivisa | `pivotCache.getPivotTables()` | Utilizzare per enumerarle prima di un aggiornamento massivo. |
In pratica, è preferibile utilizzare le API basate sulla cache anziché il metodo obsoleto `RefreshData()` per singola tabella. Queste API tengono conto delle cache condivise, evitano recuperi ridondanti dalla fonte e consentono di scegliere l'ambito più ristretto che soddisfa l'esigenza di aggiornamento.

## Common Pitfalls
- **Dimenticare di aggiornare prima di salvare.** Una tabella pivot scrive i valori visualizzati nel foglio di lavoro solo quando la sua catena di dati viene aggiornata. Se si modificano celle di origine, chiamare `PivotCache.refresh()` (o `Workbook.refreshAll()`) prima di `Workbook.save()`; in caso contrario, il file salvato conterrà ancora i precedenti valori aggregati.
- **Chiamare il metodo obsoleto `RefreshData()` per ogni tabella.** In v26.7, `PivotTable.RefreshData()` è contrassegnato come obsoleto e ricarica la fonte a ogni chiamata. Quando più tabelle pivot condividono una cache, ciò comporta N recuperi ridondanti dalla fonte. Sostituirlo con una singola chiamata `PivotCache.refresh()` seguita da `calculateData()` per ogni tabella.
- **Aggiornare quando è cambiato solo il layout.** Se è stata modificata soltanto la visualizzazione di una tabella pivot (ordine delle colonne, `ConsolidationFunction`, ecc.) senza intervenire sui dati di origine, l'operazione `PivotCache.refresh()` non è necessaria e risulta lenta. Chiamare `pivotTable.calculateData()` per rigenerare la tabella dalla cache esistente.
- **Origine esterna non supportata da `PivotCache.refresh()`.** Se la fonte della tabella pivot proviene da una connessione esterna (database, cubo OLAP, ecc.), `PivotCache.refresh()` non può aggiornarla in v26.7: attualmente supporta soltanto i tipi di origine `Sheet` e `Consolidation`. Per le origini esterne, riaprire la cartella di lavoro oppure ricostruire la cache dalla fonte.

{{< app/cells/assistant language="nodejs-cpp" >}}