---
title: Aggiornare le Tabelle Pivot e le Cache Pivot in Aspose.Cells for Java
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells for Java utilizzando l'API di aggiornamento delle pivot introdotta dalla v26.7. Questo articolo tratta RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData e GetPivotTables con esempi di codice pratici.
linktitle: Aggiornare le Tabelle Pivot
keywords: Aspose.Cells, Java, tabella pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre un'API di aggiornamento a più livelli che consente di ricaricare i dati pivot in quattro ambiti diversi, dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for Java v26.7**, il metodo legacy `PivotTable.refreshData()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.
{{% /alert %}}

## Introduzione
L'aggiornamento di una tabella pivot raramente è una singola operazione. Dietro le quinte, Aspose.Cells mantiene una catena di dati stratificata che collega i dati di origine originali ai valori visualizzati nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento giusta per ogni situazione.
La catena di dati a quattro livelli è:
1. **Origine dati** — gli intervalli originali del foglio di lavoro, la query del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — lo snapshot in memoria dei dati di origine. Ogni tabella pivot è costruita sopra un `PivotCache`; è qui che tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto vista che definisce i campi riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dalla propria `PivotCache`, mai direttamente dall'origine dati.
4. **Cells** — le `Cells` del foglio di lavoro in cui la `PivotTable` rende i valori calcolati e gli stili.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire dalla v26.7, `PivotCache.refresh()` supporta solo i tipi di origine **`Sheet`** e **`Consolidation`**, ovvero dati che risiedono in intervalli del foglio di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.
{{% /alert %}}

A causa di questa catena, in Aspose.Cells esistono due percorsi fondamentali di aggiornamento:
- **`PivotTable.calculateData()`** — ricalcola la visualizzazione di una singola `PivotTable` dai dati già presenti nella cache, senza un ritorno all'origine dati.
Tutti gli scenari in questo articolo utilizzano dati di origine provenienti da celle del foglio di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.

## Avvio rapido
Se ti serve solo il codice più breve possibile che aggiorni ogni pivot nella cartella di lavoro, è sufficiente una singola chiamata:

```java
import com.aspose.cells.*;
// Crea una nuova cartella di lavoro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Scrivi la riga di intestazione nelle celle A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Scrivi le righe di dati nelle celle A2:C9 (8 righe di dati sulla frutta tra il 2020 e il 2021)
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
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assegna i campi pivot: Frutta a Righe, Anno a Colonne, Importo a Dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modifica diversi valori di Importo nei dati di origine per simulare le modifiche
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Aggiorna ogni tabella pivot / cache pivot nella cartella di lavoro
workbook.refreshAll();
// Salva la cartella di lavoro
workbook.save("output.xlsx");
```

Tutto il resto di questo articolo spiega quando scegliere invece un'API più specifica.

## Istruzioni di importazione richieste
Tutti gli esempi Java in questo articolo iniziano con le seguenti istruzioni di importazione, poiché i tipi pivot risiedono nel package `com.aspose.cells.pivot`:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Aggiornare tutte le tabelle pivot nella cartella di lavoro
Quando hai bisogno di garantire che ogni cache pivot e ogni tabella pivot nella cartella di lavoro rifletta i dati di origine più recenti, l'API più semplice e completa è `Workbook.refreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla propria origine e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti completi e generali del documento in cui le prestazioni non sono un problema.
L'esempio seguente crea una cartella di lavoro con un intervallo di origine Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori di origine e quindi utilizza `RefreshAll()` per portare tutto aggiornato in una sola chiamata.

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
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Aggiornare tutte le tabelle pivot su un singolo foglio di lavoro
A volte hai bisogno di aggiornare solo le tabelle pivot che si trovano su un foglio di lavoro specifico, ad esempio quando le tabelle pivot sugli altri fogli di lavoro sono notoriamente non correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.refreshPivotTables()`, che è limitato a una singola istanza di `Worksheet`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assegna i campi: Frutto a Riga, Anno a Colonna, Importo a Dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modifica una proprietà di visualizzazione/layout -- questa è una modifica solo di presentazione,
// quindi NON richiede la rilettura dei dati sorgente tramite PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() ridisegna la visualizzazione di QUESTA tabella pivot (dati + stile) dai
// dati già presenti nella PivotCache. Poiché i dati sorgente non sono cambiati,
// non viene eseguito alcun round-trip verso l'origine -- solo i valori memorizzati nella cache vengono ricalcolati
// nelle celle del foglio di lavoro.
pivotTable.calculateData();
// Salva la cartella di lavoro su disco
workbook.save("output.xlsx");
```

## Aggiornare una singola tabella pivot
Quando desideri un controllo capillare su una singola tabella pivot, l'API basata sulla cache ti offre due opzioni. La scelta tra esse dipende da ciò che è effettivamente cambiato: i dati di origine sottostanti o solo le impostazioni di vista/layout della tabella pivot stessa.

### Dati di origine modificati — Usa `PivotCache.refresh()`
Se i dati di origine sottostanti sono cambiati, il punto di ingresso corretto è `pivotTable.getPivotCache().refresh()`. Questa chiamata rilegge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da quella cache.

### Solo vista/layout cambiato — Usa `calculateData()`
Se i dati di origine *non* sono cambiati ma solo le impostazioni di vista o layout della tabella pivot sono state modificate (ad esempio, un campo è stato spostato in un'area diversa, o un'impostazione di aggiornamento all'apertura è stata attivata/disattivata), non è necessario tornare all'origine dati. La cache contiene già i dati corretti; deve essere ricalcolata solo la `PivotTable` resa. In questo caso, `pivotTable.calculateData()` è la scelta giusta.
L'esempio seguente modifica una proprietà non di origine della tabella pivot e quindi chiama `calculateData()` per ridisegnarla dalla cache esistente.
Una cartella di lavoro spesso contiene molte tabelle pivot che poggiano tutte su una cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento in batch o per diagnosticare l'impatto della cache condivisa, usa `PivotCache.getPivotTables()`. Questo metodo restituisce la raccolta di ogni `PivotTable` che dipende dalla cache specificata.

## Migrazione dall'obsoleto `PivotTable.refreshData()`
Prima di Aspose.Cells for Java v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.refreshData()` su ciascuna tabella pivot individualmente. Dalla v26.7, tale metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API consapevoli della cache descritte sopra.
Ci sono due motivi per cui l'approccio `refreshData()` per tabella è problematico nelle cartelle di lavoro reali:
- Recupera i dati dall'origine *ogni* volta che viene chiamato, anche quando l'origine non è cambiata.
Le sostituzioni consigliate sono:
L'esempio seguente dimostra il nuovo schema efficiente per cartelle di lavoro con più tabelle pivot che condividono una singola cache.

## Quale API di aggiornamento dovrei usare?
La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna di esse.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.refreshAll()` | Una sola chiamata; copre tutte le cache e le tabelle. |
| Aggiornare solo le tabelle pivot su un singolo foglio | `Worksheet.refreshPivotTables()` | Limitato a un singolo foglio di lavoro. |
| Dati di origine modificati per una cache | `pivotTable.getPivotCache().refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Solo impostazioni di vista/layout modificate | `pivotTable.calculateData()` | Evita il round-trip non necessario all'origine. |
| Elencare tutte le tabelle pivot su una cache condivisa | `pivotCache.getPivotTables()` | Da usare per enumerare prima di un aggiornamento in massa. |
In pratica, preferisci le API basate sulla cache rispetto all'obsoleto `refreshData()` per tabella. Sono consapevoli delle cache condivise, evitano recuperi ridondanti dall'origine e ti permettono di scegliere l'ambito più ristretto che soddisfa la tua esigenza di aggiornamento.

## Errori comuni
- **Dimenticare di aggiornare prima di salvare.** Una tabella pivot scrive i suoi valori resi nel foglio di lavoro solo quando la sua catena di dati viene aggiornata. Se modifichi le celle di origine, chiama `PivotCache.Refresh()` (o `Workbook.RefreshAll()`) prima di `Workbook.save()`, altrimenti il file salvato conterrà ancora i vecchi valori aggregati.
- **Chiamare l'obsoleto `RefreshData()` per tabella.** Dalla v26.7, `PivotTable.RefreshData()` è contrassegnato come obsoleto e recupera l'origine per ogni chiamata. Con più tabelle pivot che condividono una cache, ciò significa N recuperi ridondanti dall'origine. Sostituisci con una singola `PivotCache.Refresh()` seguita da `CalculateData()` per ogni tabella.
- **Aggiornare quando è cambiato solo il layout.** Se hai modificato solo la vista di una tabella pivot (ordine delle colonne, `ConsolidationFunction`, ecc.) senza toccare i dati di origine, `PivotCache.Refresh()` è inutile e lento. Chiama `pivotTable.CalculateData()` per ridisegnare dalla cache esistente.
- **Origine esterna non supportata da `PivotCache.Refresh()`.** Se l'origine della tabella pivot proviene da una connessione esterna (database, cubo OLAP, ecc.), `PivotCache.Refresh()` non può aggiornarla nella v26.7 — attualmente supporta solo i tipi di origine `Sheet` e `Consolidation`. Per le origini esterne, riapri la cartella di lavoro o ricostruisci la cache dall'origine.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="java" >}}