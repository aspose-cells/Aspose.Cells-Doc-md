---
title: Aggiornare Tabelle Pivot e Pivot Cache in Aspose.Cells for .NET
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells for .NET utilizzando l'API di aggiornamento pivot introdotta nella v26.7. Questo articolo tratta RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData e GetPivotTables con esempi pratici di codice.
linktitle: Aggiornare le Tabelle Pivot
keywords: Aspose.Cells, .NET, tabella pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce un'API di aggiornamento su più livelli che consente di ricaricare i dati pivot con quattro ambiti differenti, dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for .NET v26.7**, il metodo legacy `PivotTable.RefreshData()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.
{{% /alert %}}

## Introduzione
L'aggiornamento di una tabella pivot raramente è una singola operazione. Dietro le quinte, Aspose.Cells mantiene una catena di dati su più livelli che collega i dati di origine originali ai valori renderizzati visibili nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento più adatta a ogni situazione.
La catena di dati a quattro livelli è la seguente:
1. **Origine dati** — gli intervalli del foglio di lavoro originali, la query al database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati di origine. Ogni tabella pivot è costruita sopra un `PivotCache`; è qui che tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto vista che definisce i campi riga, colonna, valore e filtro. Una `PivotTable` legge *esclusivamente* dal proprio `PivotCache`, mai direttamente dall'origine dati.
4. **Celle** — le `Cells` del foglio di lavoro in cui la `PivotTable` rende i valori calcolati e gli stili.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire dalla v26.7, `PivotCache.Refresh()` supporta solo i tipi di origine **`Sheet`** e **`Consolidation`**, ovvero dati che risiedono in intervalli del foglio di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.
{{% /alert %}}

A causa di questa catena, esistono due percorsi fondamentali di aggiornamento in Aspose.Cells:
- **`PivotTable.CalculateData()`** — ricalcola la visualizzazione di una singola `PivotTable` a partire dai dati già presenti in cache, senza tornare all'origine dati.
Tutti gli scenari di questo articolo utilizzano dati di origine in celle del foglio di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.

## Avvio rapido
Se ti serve solo il codice più breve possibile per aggiornare ogni pivot nella cartella di lavoro, è sufficiente una singola chiamata:

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

Tutto il resto di questo articolo spiega quando scegliere un'API più specifica.

## Direttive Using richieste
Tutti gli esempi C# di questo articolo iniziano con le seguenti tre direttive using perché i tipi pivot si trovano nel namespace `Aspose.Cells.Pivot`:
- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Aggiornare tutte le Tabelle Pivot nella cartella di lavoro
Quando è necessario garantire che ogni pivot cache e ogni tabella pivot nella cartella di lavoro riflettano i dati di origine più recenti, l'API più semplice e completa è `Workbook.RefreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla propria origine e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti completi del documento, quando le prestazioni non sono un problema.
L'esempio seguente crea una cartella di lavoro con un intervallo di origine Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori di origine e quindi utilizza `RefreshAll()` per riportare tutto allo stato corrente in un'unica chiamata.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Crea una nuova cartella di lavoro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Scrivi la riga di intestazione nelle celle A1:C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Scrivi le righe di dati nelle celle A2:C9 (8 righe di dati sulla frutta per gli anni 2020 e 2021)
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(50);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(60);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(70);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(80);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(90);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(100);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(110);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(120);
// Aggiungi una tabella pivot: intervallo di origine "A1:C9", cella di destinazione "E3", nome "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// Assegna i campi pivot: Fruit alle Righe, Year alle Colonne, Amount ai Dati
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Modifica diversi valori di Amount nei dati di origine per simulare delle modifiche
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);
// Aggiorna ogni tabella pivot / cache pivot nella cartella di lavoro
workbook.RefreshAll();
// Salva la cartella di lavoro
workbook.Save("output.xlsx");
```

## Aggiornare tutte le Tabelle Pivot su un singolo foglio di lavoro
A volte è necessario aggiornare solo le tabelle pivot che si trovano su uno specifico foglio di lavoro, ad esempio quando le tabelle pivot presenti sugli altri fogli di lavoro non sono correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.RefreshPivotTables()`, che è limitato a una singola istanza di `Worksheet`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2021);
worksheet.Cells["C3"].PutValue(150);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2021);
worksheet.Cells["C5"].PutValue(120);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(180);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2020);
worksheet.Cells["C7"].PutValue(130);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(220);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2020);
worksheet.Cells["C9"].PutValue(140);
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
worksheet.Cells["C2"].PutValue(300);
worksheet.Cells["C5"].PutValue(250);
worksheet.Cells["C9"].PutValue(400);
worksheet.RefreshPivotTables();
workbook.Save("output.xlsx");
```

## Aggiornare una singola Tabella Pivot
Quando si desidera un controllo fine su una singola tabella pivot, l'API basata sulla cache offre due opzioni. La scelta tra le due dipende da cosa è effettivamente cambiato: i dati di origine sottostanti, oppure solo le impostazioni di vista/layout della tabella pivot stessa.

### Dati di origine modificati — Usa `PivotCache.Refresh()`
Se i dati di origine sottostanti sono cambiati, il punto di ingresso corretto è `pivotTable.PivotCache.Refresh()`. Questa chiamata rilegge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da quella cache.

### È cambiata solo la vista/layout — Usa `CalculateData()`
Se i dati di origine *non* sono cambiati ma sono state modificate solo le impostazioni di vista o layout della tabella pivot (ad esempio, un campo è stato spostato in un'area diversa, o un'impostazione di aggiornamento all'apertura è stata attivata/disattivata), non è necessario tornare all'origine dati. La cache contiene già i dati corretti; è sufficiente ricalcolare la `PivotTable` renderizzata. In questo caso, `pivotTable.CalculateData()` è la scelta giusta.
L'esempio seguente modifica una proprietà non legata all'origine della tabella pivot e quindi chiama `CalculateData()` per renderizzarla nuovamente dalla cache esistente.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Scrivi riga di intestazione Frutto / Anno / Importo
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Scrivi 8 righe di dati (righe 2-9, adattandosi all'intervallo sorgente A1:C9)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(150);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(250);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(350);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(450);
// Aggiungi una tabella pivot denominata "Pivot1" posizionata nella cella di destinazione E3, con origine da A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];
// Assegna i campi: Fruit a Riga, Year a Colonna, Amount a Dati
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Modifica una proprietà di visualizzazione/layout — è una modifica solo di presentazione,
// quindi NON richiede di rileggere i dati sorgente tramite PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;
// CalculateData() ridisegna la visualizzazione di QUESTA tabella pivot (dati + stile) dai
// dati già contenuti nella PivotCache. Poiché i dati sorgente non sono cambiati,
// non viene eseguito alcun round-trip verso la sorgente — vengono solo ricalcolati
// i valori memorizzati nella cache nelle celle del foglio di lavoro.
pivotTable.CalculateData();
// Salva la cartella di lavoro su disco
workbook.Save("output.xlsx");
```

Una cartella di lavoro spesso contiene molte tabelle pivot che poggiano tutte su una cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento in batch o per diagnosticare l'impatto di una cache condivisa, usa `PivotCache.GetPivotTables()`. Questo metodo restituisce la collezione di tutte le `PivotTable` che dipendono dalla cache specificata.

## Migrazione dall'obsoleto `PivotTable.RefreshData()`
Prima di Aspose.Cells for .NET v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.RefreshData()` su ciascuna tabella pivot singolarmente. A partire dalla v26.7, tale metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API consapevoli della cache descritte sopra.
Per due motivi l'approccio `RefreshData()` per singola tabella è problematico nelle cartelle di lavoro reali:
- Recupera i dati dall'origine *ogni* volta che viene chiamato, anche quando l'origine non è cambiata.
Le sostituzioni consigliate sono le seguenti:
L'esempio seguente mostra il nuovo pattern efficiente per cartelle di lavoro con più tabelle pivot che condividono una singola cache.

## Quale API di aggiornamento devo usare?
La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna di esse.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.RefreshAll()` | Una sola chiamata; copre tutte le cache e le tabelle. |
| Aggiornare solo le tabelle pivot di un singolo foglio | `Worksheet.RefreshPivotTables()` | Limitato a un singolo foglio di lavoro. |
| Dati di origine modificati per una cache | `pivotTable.PivotCache.Refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Modificata solo la vista/layout | `pivotTable.CalculateData()` | Evita un inutile ritorno all'origine. |
| Elencare tutte le tabelle pivot su una cache condivisa | `pivotCache.GetPivotTables()` | Da usare per enumerare prima di un aggiornamento massivo. |
In pratica, preferisci le API basate sulla cache rispetto all'obsoleto `RefreshData()` per singola tabella. Esse tengono conto delle cache condivise, evitano recuperi ridondanti dall'origine e consentono di scegliere l'ambito più ridotto che soddisfi la tua esigenza di aggiornamento.

## Errori comuni
- **Dimenticare di aggiornare prima del salvataggio.** Una tabella pivot scrive i propri valori renderizzati nel foglio di lavoro solo quando la sua catena di dati viene aggiornata. Se modifichi le celle di origine, chiama `PivotCache.Refresh()` (o `Workbook.RefreshAll()`) prima di `Workbook.Save()`, altrimenti il file salvato conterrà ancora i vecchi valori aggregati.
- **Chiamare l'obsoleto `RefreshData()` per ogni tabella.** Dalla v26.7, `PivotTable.RefreshData()` è obsoleto e recupera l'origine a ogni chiamata. Con più tabelle pivot che condividono una cache, questo significa N recuperi ridondanti dall'origine. Sostituisci con una singola `PivotCache.Refresh()` seguita da `CalculateData()` per ogni tabella.
- **Aggiornare quando è cambiato solo il layout.** Se hai modificato solo la vista di una tabella pivot (ordine delle colonne, `ConsolidationFunction`, ecc.) senza toccare i dati di origine, `PivotCache.Refresh()` è inutile e lento. Chiama `pivotTable.CalculateData()` per renderizzare nuovamente dalla cache esistente.
- **Origine esterna non supportata da `PivotCache.Refresh()`.** Se l'origine della tabella pivot proviene da una connessione esterna (database, cubo OLAP, ecc.), `PivotCache.Refresh()` non può aggiornarla nella v26.7, poiché attualmente supporta solo i tipi di origine `Sheet` e `Consolidation`. Per le origini esterne, riapri la cartella di lavoro o ricostruisci la cache dall'origine.

{{< app/cells/assistant language="csharp" >}}