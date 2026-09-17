---
title: Aggiornare Tabelle Pivot e PivotCache in Aspose.Cells for Node.js via C++
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells for Node.js via C++ utilizzando l'API di aggiornamento delle pivot introdotta dalla v26.7. Questo articolo copre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData e GetPivotTables con esempi pratici di codice.
linktitle: Aggiornare Tabelle Pivot
keywords: Aspose.Cells, Node.js via C++, tabella pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce un'API di aggiornamento a più livelli che consente di ricaricare i dati delle pivot in quattro ambiti diversi, dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for Node.js via C++ v26.7**, il metodo legacy `PivotTable.RefreshData()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.
{{% /alert %}}

## Introduzione
Aggiornare una tabella pivot è raramente un'operazione singola. Dietro le quinte, Aspose.Cells mantiene una catena di dati a più livelli che collega i dati di origine originali ai valori renderizzati che vedi nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento giusta per ogni situazione.
La catena di dati a quattro livelli è:
1. **Origine dati** — gli intervalli originali del foglio di lavoro, la query del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati di origine. Ogni tabella pivot è costruita sopra un `PivotCache`; è qui che tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto vista che definisce i campi riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dal suo `PivotCache`, mai direttamente dall'origine dati.
4. **Celle** — le `Cells` del foglio di lavoro in cui la `PivotTable` rende i suoi valori calcolati e gli stili.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire dalla v26.7, `PivotCache.Refresh()` supporta solo i tipi di origine **`Sheet`** e **`Consolidation`**, ovvero dati che risiedono in intervalli del foglio di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.
{{% /alert %}}

A causa di questa catena, in Aspose.Cells esistono due percorsi di aggiornamento fondamentali:
- **`PivotTable.CalculateData()`** — ricalcola la visualizzazione di una singola `PivotTable` dai dati già presenti nella cache, senza un ritorno all'origine dati.
Tutti gli scenari in questo articolo utilizzano dati di origine da celle del foglio di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.

## Avvio rapido
Se hai bisogno del codice più breve possibile che aggiorni ogni pivot nella cartella di lavoro, è sufficiente una singola chiamata:

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
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

Tutto il resto in questo articolo spiega quando scegliere un'API più mirata.

## Importazioni richieste
Tutti gli esempi JavaScript in questo articolo presumono che il modulo Aspose.Cells for Node.js via C++ sia stato caricato e che i tipi pivot risiedano nel namespace `Aspose.Cells.Pivot`. Una configurazione tipica è:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (oppure accedi tramite `AsposeCells.Pivot.PivotFieldType`)

## Aggiornare tutte le Tabelle Pivot nella cartella di lavoro
Quando devi garantire che ogni cache pivot e ogni tabella pivot nella cartella di lavoro riflettano i dati di origine più recenti, l'API più semplice e completa è `Workbook.RefreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla sua origine e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti generali e completi del documento quando le prestazioni non sono un problema.
L'esempio seguente crea una cartella di lavoro con un intervallo di origine Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori di origine e quindi utilizza `RefreshAll()` per portare tutto aggiornato in una singola chiamata.

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

## Aggiornare tutte le Tabelle Pivot su un singolo foglio di lavoro
A volte è necessario aggiornare solo le tabelle pivot che si trovano su uno specifico foglio di lavoro, ad esempio quando le tabelle pivot su altri fogli di lavoro sono note per essere non correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.RefreshPivotTables()`, che è limitato a una singola istanza di `Worksheet`.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Scrivi la riga di intestazione Frutto / Anno / Importo
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Scrivi 8 righe di dati (righe 2-9, adattandosi all'intervallo sorgente A1:C9)
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
// Modifica una proprietà di visualizzazione/layout — è una modifica solo di presentazione,
// quindi NON richiede la rilettura dei dati sorgente tramite PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() ri-renderizza la visualizzazione di QUESTA tabella pivot (dati + stile) dai
// dati già presenti nella PivotCache. Poiché i dati sorgente non sono cambiati,
// non viene eseguito alcun round-trip verso la sorgente — vengono ricalcolati solo i valori
// memorizzati nella cache nelle celle del foglio di lavoro.
pivotTable.calculateData();
// Salva la cartella di lavoro su disco
workbook.save("output.xlsx");
```

## Aggiornare una singola Tabella Pivot
Quando desideri un controllo granulare su una singola tabella pivot, l'API basata sulla cache ti offre due opzioni. La scelta tra esse dipende da cosa è effettivamente cambiato: i dati di origine sottostanti, oppure solo le impostazioni di vista/layout della tabella pivot stessa.

### Dati di origine modificati — Usa `PivotCache.Refresh()`
Se i dati di origine sottostanti sono cambiati, il punto di ingresso corretto è `pivotTable.PivotCache.Refresh()`. Questa chiamata rilegge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da quella cache.

### Solo vista/layout modificati — Usa `CalculateData()`
Se i dati di origine *non* sono cambiati ma sono state modificate solo le impostazioni di vista o layout della tabella pivot (ad esempio, un campo è stato spostato in un'area diversa, o un'impostazione di aggiornamento all'apertura è stata attivata/disattivata), non è necessario tornare all'origine dati. La cache contiene già i dati corretti; deve essere ricalcolata solo la `PivotTable` renderizzata. In questo caso, `pivotTable.CalculateData()` è la scelta giusta.
L'esempio seguente modifica una proprietà non di origine della tabella pivot e quindi chiama `CalculateData()` per renderizzarla nuovamente dalla cache esistente.
Una cartella di lavoro spesso contiene molte tabelle pivot che poggiano tutte su una cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento in blocco o per diagnosticare l'impatto della cache condivisa, usa `PivotCache.GetPivotTables()`. Questo metodo restituisce la raccolta di ogni `PivotTable` che dipende dalla cache specificata.

## Migrazione dall'obsoleto `PivotTable.RefreshData()`
Prima di Aspose.Cells for Node.js via C++ v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.RefreshData()` su ogni tabella pivot singolarmente. Dalla v26.7, quel metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API consapevoli della cache descritte sopra.
Ci sono due motivi per cui l'approccio `RefreshData()` per tabella è problematico nelle cartelle di lavoro reali:
- Recupera i dati dall'origine *ogni* volta che viene chiamato, anche quando l'origine non è cambiata.
Le sostituzioni consigliate sono:
L'esempio seguente mostra il nuovo schema efficiente per cartelle di lavoro con più tabelle pivot che condividono una singola cache.

## Quale API di aggiornamento devo usare?
La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna di esse.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.RefreshAll()` | Una chiamata; copre tutte le cache e tabelle. |
| Aggiornare solo le tabelle pivot su un singolo foglio | `Worksheet.RefreshPivotTables()` | Limitato a un singolo foglio di lavoro. |
| Dati di origine modificati per una cache | `pivotTable.PivotCache.Refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Solo impostazioni di vista/layout modificate | `pivotTable.CalculateData()` | Salta l'inutile round-trip verso l'origine. |
| Elencare tutte le tabelle pivot su una cache condivisa | `pivotCache.GetPivotTables()` | Da usare per enumerare prima di un aggiornamento in blocco. |
In pratica, preferisci le API basate sulla cache rispetto all'obsoleto `RefreshData()` per tabella. Sono consapevoli delle cache condivise, evitano recuperi ridondanti dall'origine e ti permettono di scegliere l'ambito più piccolo che soddisfa la tua esigenza di aggiornamento.

## Errori comuni
- **Dimenticare di aggiornare prima di salvare.** Una tabella pivot scrive i suoi valori renderizzati nel foglio di lavoro solo quando la sua catena di dati viene aggiornata. Se modifichi le celle di origine, chiama `PivotCache.Refresh()` (oppure `Workbook.RefreshAll()`) prima di `Workbook.save()`, altrimenti il file salvato conterrà ancora i vecchi valori aggregati.
- **Chiamare l'obsoleto `RefreshData()` per ogni tabella.** Nella v26.7, `PivotTable.RefreshData()` è contrassegnato come obsoleto e recupera l'origine per ogni chiamata. Con più tabelle pivot che condividono una cache, ciò significa N recuperi ridondanti dall'origine. Sostituiscilo con una singola `PivotCache.Refresh()` seguita da `CalculateData()` per ogni tabella.
- **Aggiornare quando è cambiato solo il layout.** Se hai modificato solo la vista di una tabella pivot (ordine delle colonne, `ConsolidationFunction`, ecc.) senza toccare i dati di origine, `PivotCache.Refresh()` non è necessario ed è lento. Chiama `pivotTable.CalculateData()` per renderizzare nuovamente dalla cache esistente.
- **Origine esterna non supportata da `PivotCache.Refresh()`.** Se l'origine della tabella pivot proviene da una connessione esterna (database, cubo OLAP, ecc.), `PivotCache.Refresh()` non può aggiornarla nella v26.7: attualmente supporta solo i tipi di origine `Sheet` e `Consolidation`. Per le origini esterne, riapri la cartella di lavoro o ricostruisci la cache dall'origine.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}