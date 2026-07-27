---
title: Aggiornamento delle tabelle pivot in Aspose.Cells for Java
linktitle: Aggiornamento delle tabelle pivot
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells for Java utilizzando l'API di aggiornamento delle pivot introdotta nella v26.7+. Questo articolo illustra RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData e GetPivotTables con esempi pratici di codice.
keywords: Aspose.Cells, Java, tabella pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells offre un'API di aggiornamento a più livelli che consente di ricaricare i dati delle pivot in quattro ambiti diversi, dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for Java v26.7**, il metodo legacy `PivotTable.refreshData()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.

{{% /alert %}}

## Introduzione

L'aggiornamento di una tabella pivot raramente è una singola operazione. Dietro le quinte, Aspose.Cells mantiene una catena di dati a più livelli che collega i dati di origine originali ai valori visualizzati nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento giusta per ogni situazione.

La catena di dati a quattro livelli è:

1. **Origine dati** — gli intervalli del foglio di lavoro originali, la query del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati di origine. Ogni tabella pivot è costruita sopra un `PivotCache`; è qui che tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto vista che definisce i campi riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dal suo `PivotCache`, mai direttamente dall'origine dati.
4. **Celle** — le `Cells` del foglio di lavoro in cui la `PivotTable` rende i valori calcolati e gli stili.

Un concetto particolarmente importante è la **cache condivisa**. Quando più tabelle pivot in una cartella di lavoro fanno riferimento allo stesso intervallo di origine, condividono *una* sola istanza di `PivotCache`. Una singola `PivotCache` può essere referenziata da molte tabelle pivot e l'aggiornamento di tale cache aggiorna ogni `PivotTable` dipendente contemporaneamente.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire dalla v26.7, `PivotCache.refresh()` supporta solo i tipi di origine **`Sheet`** e **`Consolidation`**, ovvero dati che risiedono in intervalli di fogli di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.

{{% /alert %}}

A causa di questa catena, in Aspose.Cells esistono due percorsi di aggiornamento fondamentali:

- **`PivotCache.refresh()`** — ricarica l'origine → cache E ricalcola tutte le `PivotTable` dipendenti in un'unica operazione.
- **`PivotTable.calculateData()`** — ricalcola la visualizzazione di una `PivotTable` dai dati già memorizzati nella cache, senza tornare all'origine dati.

Tutti gli scenari di questo articolo utilizzano dati di origine provenienti da celle del foglio di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.

## Istruzioni di importazione necessarie

Tutti gli esempi Java in questo articolo iniziano con le seguenti istruzioni di importazione perché i tipi pivot si trovano nel package `com.aspose.cells.pivot`:

- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Aggiornare tutte le tabelle pivot nella cartella di lavoro

Quando è necessario garantire che ogni cache pivot e ogni tabella pivot nella cartella di lavoro rifletta i dati di origine più recenti, l'API più semplice e completa è `Workbook.refreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla propria origine e poi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti generali e completi del documento, laddove le prestazioni non siano un problema.

L'esempio seguente crea una cartella di lavoro con un intervallo di origine Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori di origine e quindi utilizza `refreshAll()` per portare tutto aggiornato in un'unica chiamata.

```java
import com.aspose.cells.*;

// Crea una nuova cartella di lavoro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Scrivi la riga di intestazione nelle celle A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Scrivi le righe di dati nelle celle A2:C9 (8 righe di dati sulla frutta per gli anni 2020 e 2021)
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

// Assegna i campi pivot: Fruit alle Righe, Year alle Colonne, Amount ai Dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Modifica diversi valori di Amount nei dati di origine per simulare delle modifiche
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Aggiorna ogni tabella pivot / cache pivot nella cartella di lavoro
workbook.refreshAll();

// Salva la cartella di lavoro
workbook.save("output.xlsx");
```

## Aggiornare tutte le tabelle pivot su un singolo foglio di lavoro

A volte è necessario aggiornare solo le tabelle pivot che si trovano su un foglio di lavoro specifico, ad esempio quando le tabelle pivot su altri fogli di lavoro non sono correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.refreshPivotTables()`, che è limitato a una singola istanza di `Worksheet`.

Questo è più selettivo rispetto a `Workbook.refreshAll()`: vengono aggiornate solo le tabelle pivot sul foglio di lavoro di destinazione, lasciando intatte le tabelle pivot sugli altri fogli di lavoro.

L'esempio seguente popola gli stessi dati di origine Frutto/Anno/Importo, aggiunge una tabella pivot sul primo foglio di lavoro, modifica alcuni valori di origine e quindi aggiorna solo le tabelle pivot su quel foglio di lavoro.

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

## Aggiornare una singola tabella pivot

Quando si desidera un controllo capillare su una singola tabella pivot, l'API basata sulla cache offre due opzioni. La scelta tra di esse dipende da ciò che è effettivamente cambiato: i dati di origine sottostanti, oppure solo le impostazioni di vista/layout della tabella pivot stessa.

### Dati di origine modificati — Usare `PivotCache.refresh()`

Se i dati di origine sottostanti sono cambiati, il punto di ingresso corretto è `pivotTable.getPivotCache().refresh()`. Questa chiamata rilegge i dati di origine nella cache e poi ricalcola ogni `PivotTable` che dipende da quella cache.

{{% alert color="primary" %}}

Poiché le tabelle pivot condividono una singola istanza di `PivotCache`, chiamare `PivotCache.refresh()` ricalcola **tutte** le tabelle pivot costruite su quella stessa cache, non solo quella a cui si fa riferimento. Se due tabelle pivot condividono lo stesso intervallo di origine, l'aggiornamento di una cache aggiorna entrambe.

{{% /alert %}}

L'esempio seguente crea due tabelle pivot sullo stesso intervallo di origine per dimostrare questo comportamento di cache condivisa, modifica alcuni valori di origine e quindi aggiorna tramite un riferimento alla cache.

```java
import com.aspose.cells.*;

// Crea una nuova cartella di lavoro e accedi al primo foglio di lavoro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Scrivi la riga di intestazione: Frutto / Anno / Importo
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Scrivi circa 9 righe di dati (uva / mirtillo / kiwi / ciliegia negli anni 2020-2021)
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
int pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Assegna i campi per Pivot1
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount");

// Aggiungi una SECONDA tabella pivot "Pivot2" ancorata a E15 utilizzando lo STESSO intervallo di origine A1:C9
// Sia Pivot1 che Pivot2 condividono un unico PivotCache perché l'intervallo di origine è identico.
int pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Assegna gli stessi campi per Pivot2
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount");

// Modifica diversi valori delle celle Importo nei dati di origine per simulare una modifica dei dati
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Aggiorna il PivotCache condiviso.
// Poiché Pivot1 e Pivot2 condividono lo stesso PivotCache, questa singola chiamata
// aggiorna ENTRAMBE le tabelle pivot (dati + stile) dall'origine aggiornata.
pivotTable1.refreshData();

// Salva la cartella di lavoro
workbook.save("output.xlsx");
```

### Solo vista/layout modificati — Usare `calculateData()`

Se i dati di origine *non* sono cambiati ma sono state modificate solo le impostazioni di vista o di layout della tabella pivot (ad esempio, un campo è stato spostato in un'area diversa, o è stata attivata/disattivata un'impostazione di aggiornamento all'apertura), non è necessario tornare all'origine dati. La cache contiene già i dati corretti; deve essere ricalcolata solo la `PivotTable` visualizzata. In questo caso, `pivotTable.calculateData()` è la scelta giusta.

Ciò evita il recupero non necessario dei dati di origine ed è significativamente più veloce quando molte tabelle pivot condividono la stessa cache.

L'esempio seguente modifica una proprietà non relativa all'origine della tabella pivot e quindi chiama `calculateData()` per ridisegnarla dalla cache esistente.

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
worksheet.getCells().get("B2").putValue(2020);.
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);.
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);.
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);.
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);.
worksheet.getCells().get("C6").putValue(150);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);.
worksheet.getCells().get("C7").putValue(250);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);.
worksheet.getCells().get("C8").putValue(350);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);.
worksheet.getCells().get("C9").putValue(450);

// Aggiungi una tabella pivot denominata "Pivot1" posizionata nella cella di destinazione E3, con origine da A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assegna i campi: Fruit a Riga, Year a Colonna, Amount a Dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Modifica una proprietà di visualizzazione/layout -- questa è una modifica solo di presentazione.
// quindi NON richiede la rilettura dei dati sorgente tramite PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() ri-renderizza la visualizzazione di QUESTA tabella pivot (dati + stile) dai dati
// già presenti nella PivotCache. Poiché i dati sorgente non sono cambiati.
// non viene eseguito alcun round-trip verso la sorgente -- vengono solo ricalcolati i valori memorizzati nella cache
// nelle celle del foglio di lavoro.
pivotTable.calculateData();

// Salva la cartella di lavoro su disco
workbook.save("output.xlsx");
```

## Ottenere tutte le tabelle pivot che condividono la stessa PivotCache

Una cartella di lavoro spesso contiene molte tabelle pivot che poggiano tutte su una cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento in batch o per diagnosticare l'impatto della cache condivisa, utilizzare `PivotCache.getPivotTables()`. Questo metodo restituisce la raccolta di tutte le `PivotTable` che dipendono dalla cache specificata.

Questo è anche il modo più diretto per verificare che due tabelle pivot condividano effettivamente la stessa istanza di `PivotCache`: è possibile confrontare i riferimenti alla cache (usando l'operatore `==`) oppure semplicemente scorrere la raccolta restituita da `getPivotTables()` e osservare quali tabelle pivot vi compaiono.

L'esempio seguente crea due tabelle pivot sullo stesso intervallo di origine, verifica che condividano la stessa istanza di cache e quindi enumera le tabelle pivot della cache.


## Migrazione dal metodo obsoleto `PivotTable.refreshData()`

Prima di Aspose.Cells for Java v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.refreshData()` su ciascuna tabella pivot individualmente. A partire dalla v26.7, tale metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API consapevoli della cache descritte sopra.

Ci sono due motivi per cui l'approccio `refreshData()` per tabella è problematico nelle cartelle di lavoro reali:

- Recupera i dati dall'origine *ogni* volta che viene chiamato, anche quando l'origine non è cambiata.
- Ogni chiamata aggiorna l'intera cache condivisa. Quando molte tabelle pivot condividono una cache, chiamare ripetutamente `refreshData()` per ogni tabella pivot fa sì che la stessa cache venga recuperata più e più volte, il che è molto lento.

Le sostituzioni consigliate sono:

- **Aggiornare TUTTE le tabelle pivot nella cartella di lavoro** → utilizzare `workbook.refreshAll();`
- **Aggiornarne ALCUNE** → utilizzare `pivotTable.getPivotCache().refresh();` per una cache. Poiché la cache è condivisa, questa singola chiamata aggiorna ogni tabella pivot costruita sopra quella cache. Altre tabelle pivot che poggiano su una cache già aggiornata possono essere tranquillamente saltate.
- **Solo la vista/layout della pivot è cambiato** → utilizzare `pivotTable.calculateData();` per ridisegnare dalla cache esistente senza alcun round-trip verso l'origine.

L'esempio seguente mostra il nuovo schema efficiente per le cartelle di lavoro con più tabelle pivot che condividono una singola cache.

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// --- Costruisci i dati di origine: Frutta / Anno / Importo (intestazione + 9 righe) ---
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

// --- Aggiungi la prima tabella pivot (Pivot1) nella cella di destinazione E3 ---
int idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

// --- Aggiungi la SECONDA tabella pivot (Pivot2) sullo STESSO intervallo di origine ---
int idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

// --- Modifica diversi valori di Importo nei dati di origine ---
sheet.getCells().get("C2").putValue(5000);   // Uva 2020
sheet.getCells().get("C5").putValue(7500);   // Ciliegia 2020
sheet.getCells().get("C9").putValue(9500);   // Ciliegia 2021

// --- NUOVO schema v26.7+: aggiorna la cache UNA VOLTA, quindi rirenderizza secondo necessità ---
pivotTable1.getPivotCache().refresh();

// Rirenderizza la vista/layout della seconda tabella pivot senza toccare l'origine
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Quale API di aggiornamento dovrei usare?

La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna di esse.

| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.refreshAll()` | Una sola chiamata; copre tutte le cache e le tabelle. |
| Aggiornare solo le tabelle pivot su un singolo foglio | `Worksheet.refreshPivotTables()` | Limitato a un singolo foglio di lavoro. |
| Dati di origine cambiati per una cache | `pivotTable.getPivotCache().refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Sono cambiate solo le impostazioni di vista/layout | `pivotTable.calculateData()` | Evita il round-trip non necessario verso l'origine. |
| Elencare tutte le tabelle pivot su una cache condivisa | `pivotCache.getPivotTables()` | Utilizzare per enumerare prima dell'aggiornamento in blocco. |

In pratica, preferire le API basate sulla cache rispetto al metodo obsoleto `refreshData()` per tabella. Sono consapevoli delle cache condivise, evitano recuperi ridondanti dall'origine e consentono di scegliere l'ambito più piccolo che soddisfa il requisito di aggiornamento.

{{< app/cells/assistant language="java" >}}
