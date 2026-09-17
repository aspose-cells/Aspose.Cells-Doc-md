---
title: Refresh Pivot Tables and Pivot Caches in Aspose.Cells for Node.js via Java
description: Learn how to refresh pivot tables in Aspose.Cells for Node.js via Java using the v26.7+ pivot-refresh API. This article covers RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData, and GetPivotTables with practical code examples.
linktitle: Refresh Pivot Tables
keywords: Aspose.Cells, Node.js, Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce un'API di aggiornamento a più livelli che consente di ricaricare i dati delle tabelle pivot in quattro ambiti diversi, dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for Node.js via Java v26.7**, il metodo legacy `PivotTable.RefreshData()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.
{{% /alert %}}

## Introduzione
Aggiornare una tabella pivot raramente è un'operazione singola. Dietro le quinte, Aspose.Cells mantiene una catena dati a più livelli che collega i dati sorgente originali ai valori renderizzati che si vedono nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento giusta per ogni situazione.
La catena dati a quattro livelli è:
1. **Data Source** — gli intervalli originali del foglio di lavoro, la query del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati sorgente. Ogni tabella pivot è costruita sopra una `PivotCache`; è qui che tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto vista che definisce i campi riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dalla sua `PivotCache`, mai direttamente dalla fonte dati.
4. **Cells** — le `Cells` del foglio di lavoro in cui la `PivotTable` rende i valori calcolati e gli stili.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire dalla v26.7, `PivotCache.Refresh()` supporta solo i tipi di sorgente **`Sheet`** e **`Consolidation`**, ovvero dati che risiedono negli intervalli del foglio di lavoro. Le sorgenti esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.
{{% /alert %}}

A causa di questa catena, ci sono due percorsi di aggiornamento fondamentali in Aspose.Cells:
- **`PivotTable.CalculateData()`** — ricalcola la visualizzazione di una `PivotTable` dai dati già in cache, senza tornare alla fonte dati.
Tutti gli scenari in questo articolo utilizzano dati sorgente da celle del foglio di lavoro, quindi il tipo di sorgente è `Sheet` e le operazioni di aggiornamento si comportano come descritto.

## Avvio rapido
Se hai bisogno solo del codice più breve possibile che aggiorni ogni pivot nella cartella di lavoro, una singola chiamata è sufficiente:

```javascript
const aspose = require('aspose.cells');
const workbook = new aspose.cells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Tutto il resto in questo articolo spiega quando scegliere invece un'API più ristretta.

## Importazioni richieste
- `const aspose = require('aspose.cells');`
- Oppure per importazioni specifiche: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Aggiornare tutte le tabelle pivot nella cartella di lavoro
Quando è necessario garantire che ogni pivot cache e ogni tabella pivot nella cartella di lavoro riflettano i dati sorgente più recenti, l'API più semplice e completa è `Workbook.RefreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla sua sorgente e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti generali e completi del documento in cui le prestazioni non sono un problema.
L'esempio seguente crea una cartella di lavoro con un intervallo sorgente Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori sorgente e quindi utilizza `RefreshAll()` per portare tutto aggiornato in una singola chiamata.

```javascript
const AsposeCells = require("aspose.cells");
// Crea una nuova cartella di lavoro
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
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
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assegna i campi pivot: Frutta a Righe, Anno a Colonne, Importo a Dati
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
A volte è necessario aggiornare solo le tabelle pivot che si trovano su un foglio di lavoro specifico, ad esempio quando le tabelle pivot su altri fogli di lavoro sono note per non essere correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.RefreshPivotTables()`, che è limitato a una singola istanza di `Worksheet`.

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
Quando si desidera un controllo granulare su una singola tabella pivot, l'API basata sulla cache offre due opzioni. La scelta tra esse dipende da ciò che è effettivamente cambiato: i dati sorgente sottostanti, o solo le impostazioni di vista/layout della tabella pivot stessa.

### Dati sorgente cambiati — Usa `PivotCache.Refresh()`
Se i dati sorgente sottostanti sono cambiati, il punto di ingresso corretto è `pivotTable.PivotCache.Refresh()`. Questa chiamata rilegge i dati sorgente nella cache e quindi ricalcola ogni `PivotTable` che dipende da quella cache.

### Solo vista/layout cambiati — Usa `CalculateData()`
Se i dati sorgente *non* sono cambiati ma sono state modificate solo le impostazioni di vista o layout della tabella pivot (ad esempio, un campo è stato spostato in un'area diversa, o un'impostazione di aggiornamento all'apertura è stata attivata), non è necessario tornare alla fonte dati. La cache contiene già i dati corretti; solo la `PivotTable` renderizzata deve essere ricalcolata. In questo caso, `pivotTable.CalculateData()` è la scelta giusta.
L'esempio seguente modifica una proprietà non sorgente della tabella pivot e quindi chiama `CalculateData()` per renderizzarla nuovamente dalla cache esistente.

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modifica una proprietà di visualizzazione/layout — si tratta di una modifica solo di presentazione,
// quindi NON richiede una rilettura dei dati sorgente tramite PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() ri-renderizza la visualizzazione di QUESTA tabella pivot (dati + stile)
// dai dati già presenti nella PivotCache. Poiché i dati sorgente non sono cambiati,
// non viene eseguito alcun round-trip verso la sorgente — vengono ricalcolati solo i valori memorizzati nella cache
// nelle celle del foglio di lavoro.
pivotTable.calculateData();
// Salva la cartella di lavoro su disco
workbook.save("output.xlsx");
```

Una cartella di lavoro spesso contiene molte tabelle pivot che si trovano tutte sopra una cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento in batch, o per diagnosticare l'impatto della cache condivisa, utilizzare `PivotCache.GetPivotTables()`. Questo metodo restituisce la raccolta di ogni `PivotTable` che dipende dalla cache data.

## Migrazione dall'obsoleto `PivotTable.RefreshData()`
Prima di Aspose.Cells for Node.js via Java v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.RefreshData()` su ogni tabella pivot individualmente. Dalla v26.7, quel metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API consapevoli della cache descritte sopra.
Ci sono due motivi per cui l'approccio `RefreshData()` per tabella è problematico nelle cartelle di lavoro reali:
- Recupera nuovamente i dati dalla sorgente *ogni* volta che viene chiamato, anche quando la sorgente non è cambiata.
Le sostituzioni consigliate sono:
L'esempio seguente dimostra il nuovo schema efficiente per cartelle di lavoro con più tabelle pivot che condividono una singola cache.

## Quale API di aggiornamento devo usare?
La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.RefreshAll()` | Una chiamata; copre tutte le cache e le tabelle. |
| Aggiornare solo le tabelle pivot su un singolo foglio | `Worksheet.RefreshPivotTables()` | Limitato a un foglio di lavoro. |
| Dati sorgente cambiati per una cache | `pivotTable.PivotCache.Refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Solo impostazioni di vista/layout cambiate | `pivotTable.CalculateData()` | Evita il round-trip non necessario alla sorgente. |
| Elencare tutte le tabelle pivot su una cache condivisa | `pivotCache.GetPivotTables()` | Da usare per enumerare prima dell'aggiornamento in blocco. |
In pratica, preferisci le API basate sulla cache rispetto all'obsoleto `RefreshData()` per tabella. Sono consapevoli delle cache condivise, evitano recuperi sorgente ridondanti e ti consentono di scegliere il più piccolo ambito che soddisfa il tuo requisito di aggiornamento.

## Insidie comuni
- **Dimenticare di aggiornare prima di salvare.** Una tabella pivot scrive i suoi valori renderizzati nel foglio di lavoro solo quando la sua catena dati viene aggiornata. Se modifichi le celle sorgente, chiama `PivotCache.Refresh()` (o `Workbook.RefreshAll()`) prima di `Workbook.save()`, altrimenti il file salvato contiene ancora i vecchi valori aggregati.
- **Chiamare l'obsoleto `RefreshData()` per tabella.** Nella v26.7, `PivotTable.RefreshData()` è contrassegnato come obsoleto e recupera la sorgente per ogni chiamata. Con più tabelle pivot che condividono una cache, questo significa N recuperi sorgente ridondanti. Sostituisci con una singola `PivotCache.Refresh()` seguita da `CalculateData()` per tabella.
- **Aggiornare quando è cambiato solo il layout.** Se hai cambiato solo la vista di una tabella pivot (ordine delle colonne, `ConsolidationFunction`, ecc.) senza toccare i dati sorgente, `PivotCache.Refresh()` è inutile e lento. Chiama `pivotTable.CalculateData()` per renderizzare nuovamente dalla cache esistente.
- **Sorgente esterna non supportata da `PivotCache.Refresh()`.** Se la sorgente della tabella pivot proviene da una connessione esterna (database, cubo OLAP, ecc.), `PivotCache.Refresh()` non può aggiornarla nella v26.7 — attualmente supporta solo i tipi di sorgente `Sheet` e `Consolidation`. Per le sorgenti esterne, riaprire la cartella di lavoro o ricostruire la cache dalla sorgente.

{{< app/cells/assistant language="nodejs-java" >}}