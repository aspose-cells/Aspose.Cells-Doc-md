---
title: Aggiornamento di Tabelle Pivot e cache in Aspose.Cells for Java
linktitle: Aggiornamento di Tabelle Pivot e cache
description: Scopri come aggiornare le Tabelle Pivot in Aspose.Cells for Java utilizzando l'API di aggiornamento delle Tabelle Pivot v26.7+. Questo articolo illustra refreshAll, refreshPivotTables, PivotCache.refresh, calculateData e getPivotTables con pratici esempi di codice.
keywords: Aspose.Cells, Java, Tabella Pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce un'API di aggiornamento su più livelli che consente di ricaricare i dati delle Tabelle Pivot in quattro ambiti diversi, dall'intera cartella di lavoro fino a una singola Tabella Pivot. A partire da **Aspose.Cells for Java v26.7**, il precedente metodo `PivotTable.refreshData()` è contrassegnato come obsoleto e deve essere sostituito dalle API più efficienti e basate sulla cache descritte in questo articolo.
{{% /alert %}}

## Introduction
L'aggiornamento di una Tabella Pivot raramente consiste in una singola operazione. Internamente, Aspose.Cells mantiene una catena di dati a più livelli che collega i dati di origine originali ai valori visualizzati nel foglio di lavoro. La comprensione di questa catena è essenziale per scegliere l'API di aggiornamento più adatta a ogni situazione.
La catena di dati a quattro livelli è:
1. **Origine dati** — gli intervalli originali del foglio di lavoro, la query del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — la copia istantanea in memoria dei dati di origine. Ogni Tabella Pivot si basa su un `PivotCache`, nel quale tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto di visualizzazione che definisce i campi di riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dal proprio `PivotCache`, mai direttamente dalla fonte dei dati.
4. **Cells** — il `Cells` del foglio di lavoro nel quale la `PivotTable` rende i valori calcolati e gli stili.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire dalla v26.7, `PivotCache.refresh()` supporta esclusivamente i tipi di origine **`Sheet`** e **`Consolidation`**, cioè i dati contenuti in intervalli di fogli di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.
A causa di questa catena, in Aspose.Cells esistono due percorsi fondamentali per l'aggiornamento:
- **`PivotTable.calculateData()`** — ricalcola la visualizzazione di una `PivotTable` a partire dai dati già memorizzati nella cache, senza tornare alla fonte dei dati.
Tutti gli scenari di questo articolo usano dati di origine contenuti in celle di fogli di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.
{{% /alert %}}

## Quick Start
Se devi soltanto usare il codice più breve possibile per aggiornare ogni Tabella Pivot nella cartella di lavoro, è sufficiente una singola chiamata:

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Tutto il resto di questo articolo spiega quando scegliere un'API con un ambito più ristretto.

## Required Import Statements
Tutti gli esempi Java di questo articolo iniziano con le seguenti istruzioni di importazione, poiché i tipi relativi alle Tabelle Pivot si trovano nel package `com.aspose.cells.pivot`:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Refresh All Pivot Tables in the Workbook
Quando devi assicurarti che ogni cache e ogni Tabella Pivot nella cartella di lavoro rifletta i dati di origine più recenti, l'API più semplice e completa è `Workbook.refreshAll()`. Una singola chiamata percorre l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla propria origine e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per gli aggiornamenti generali dell'intero documento quando le prestazioni non rappresentano un vincolo.
L'esempio seguente crea una cartella di lavoro con un intervallo di origine contenente frutta, anno e quantità, crea una Tabella Pivot, modifica alcuni valori di origine e quindi utilizza `refreshAll()` per aggiornare tutto con una singola chiamata.

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
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
Talvolta devi aggiornare soltanto le Tabelle Pivot presenti in un determinato foglio di lavoro, ad esempio quando è noto che quelle in altri fogli non sono correlate e non devono essere modificate. Per questo caso, Aspose.Cells fornisce `Worksheet.refreshPivotTables()`, che opera su una singola istanza di `Worksheet`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
Quando desideri un controllo dettagliato su una singola Tabella Pivot, l'API basata sulla cache offre due opzioni. La scelta tra esse dipende dall'elemento effettivamente modificato: i dati di origine sottostanti oppure soltanto le impostazioni di visualizzazione o disposizione della Tabella Pivot.

### Source Data Changed — Use `PivotCache.refresh()`
Se i dati di origine sottostanti sono stati modificati, il punto di ingresso corretto è `pivotTable.getPivotCache().refresh()`. Questa chiamata riledge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da essa.

### Only View/Layout Changed — Use `calculateData()`
Se i dati di origine *non* sono stati modificati, ma sono state modificate soltanto le impostazioni di visualizzazione o disposizione della Tabella Pivot (ad esempio, un campo è stato spostato in un'area diversa o un'impostazione di aggiornamento all'apertura è stata modificata), non è necessario tornare alla fonte dei dati. La cache contiene già i dati corretti; è necessario ricalcolare soltanto la `PivotTable` visualizzata. In questo caso, la scelta corretta è `pivotTable.calculateData()`.
L'esempio seguente modifica una proprietà della Tabella Pivot diversa dalla fonte e quindi chiama `calculateData()` per rigenerarne la visualizzazione utilizzando la cache esistente.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify a view/layout property -- this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed -- only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

Una cartella di lavoro contiene spesso molte Tabelle Pivot basate tutte su una singola cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento per lotti o di diagnosticare l'impatto di una cache condivisa, usa `PivotCache.getPivotTables()`. Questo metodo restituisce la raccolta di tutte le `PivotTable` che dipendono dalla cache specificata.

## Migrating from the Obsolete `PivotTable.refreshData()`
Prima di Aspose.Cells for Java v26.7, il metodo standard per aggiornare una Tabella Pivot consisteva nel chiamare `PivotTable.refreshData()` singolarmente per ogni Tabella Pivot. A partire dalla v26.7, questo metodo è contrassegnato come **obsoleto** e deve essere sostituito dalle API basate sulla cache descritte in precedenza.
L'approccio `refreshData()` per singola tabella presenta due problemi nelle cartelle di lavoro reali:
- Recupera nuovamente i dati dalla fonte *ogni* volta che viene chiamato, anche quando la fonte non è stata modificata.
Le sostituzioni consigliate sono:
L'esempio seguente dimostra il nuovo schema efficiente per cartelle di lavoro con più Tabelle Pivot che condividono una singola cache.

## Which Refresh API Should I Use?
La tabella seguente riepiloga le API di aggiornamento disponibili e le circostanze in cui scegliere ciascuna.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.refreshAll()` | Una singola chiamata; copre tutte le cache e le Tabelle Pivot. |
| Aggiornare soltanto le Tabelle Pivot in un singolo foglio | `Worksheet.refreshPivotTables()` | Opera su un solo foglio di lavoro. |
| Dati di origine modificati per una cache | `pivotTable.getPivotCache().refresh()` | Aggiorna TUTTE le Tabelle Pivot basate su quella cache condivisa. |
| Modificate soltanto le impostazioni di visualizzazione o disposizione | `pivotTable.calculateData()` | Evita il passaggio non necessario alla fonte. |
| Elencare tutte le Tabelle Pivot basate su una cache condivisa | `pivotCache.getPivotTables()` | Consente di enumerarle prima di un aggiornamento per lotti. |
In pratica, preferisci le API basate sulla cache rispetto al metodo obsoleto `refreshData()` per singola tabella. Sono consapevoli delle cache condivise, evitano recuperi ridondanti dalla fonte e consentono di scegliere l'ambito più ristretto che soddisfa il requisito di aggiornamento.

## Common Pitfalls
- **Dimenticare di aggiornare prima di salvare.** Una Tabella Pivot scrive i suoi valori visualizzati nel foglio di lavoro soltanto quando la sua catena di dati viene aggiornata. Se modifichi le celle di origine, chiama `PivotCache.refresh()` (o `Workbook.refreshAll()`) prima di `Workbook.save()`; in caso contrario, il file salvato conterrà ancora i vecchi valori aggregati.
- **Chiamare il metodo obsoleto `refreshData()` per ogni tabella.** In v26.7, `PivotTable.refreshData()` è contrassegnato come obsoleto e recupera nuovamente la fonte a ogni chiamata. Con più Tabelle Pivot che condividono una cache, ciò comporta N recuperi ridondanti dalla fonte. Sostituiscilo con una singola chiamata `PivotCache.refresh()` seguita da `calculateData()` per ogni tabella.
- **Aggiornare quando è cambiata soltanto la disposizione.** Se hai modificato soltanto la visualizzazione di una Tabella Pivot (ordine delle colonne, `ConsolidationFunction`, ecc.) senza toccare i dati di origine, la chiamata `PivotCache.refresh()` è inutile e lenta. Chiama `pivotTable.calculateData()` per rigenerare la visualizzazione utilizzando la cache esistente.
- **Origine esterna non supportata da `PivotCache.refresh()`.** Se l'origine della Tabella Pivot proviene da una connessione esterna (database, cubo OLAP, ecc.), `PivotCache.refresh()` non può aggiornarla in v26.7, poiché attualmente supporta soltanto i tipi di origine `Sheet` e `Consolidation`. Per le origini esterne, riapri la cartella di lavoro o ricostruisci la cache dalla fonte.

{{< app/cells/assistant language="java" >}}