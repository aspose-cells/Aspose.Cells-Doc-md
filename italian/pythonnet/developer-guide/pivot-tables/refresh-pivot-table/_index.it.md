---
title: Aggiornamento delle tabelle pivot in Aspose.Cells for Python via .NET
linktitle: Aggiornamento delle tabelle pivot
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells for Python via .NET utilizzando l'API di aggiornamento pivot dalla v26.7+. Questo articolo copre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData e GetPivotTables con esempi pratici di codice.
keywords: Aspose.Cells, Python via .NET, tabella pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells fornisce un'API di aggiornamento a più livelli che consente di ricaricare i dati pivot in quattro ambiti diversi, dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for Python via .NET v26.7**, il metodo legacy `PivotTable.refresh_data()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.

{{% /alert %}}

## Introduzione

L'aggiornamento di una tabella pivot è raramente una singola operazione. Dietro le quinte, Aspose.Cells mantiene una catena di dati a più livelli che collega i dati di origine originali ai valori visualizzati nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento giusta per ogni situazione.

La catena di dati a quattro livelli è:

1. **Origine dati** — gli intervalli del foglio di lavoro originali, la query del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati di origine. Ogni tabella pivot è costruita sopra una `PivotCache`; è qui che tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto vista che definisce i campi di riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dalla propria `PivotCache`, mai direttamente dall'origine dati.
4. **Celle** — le `Cells` del foglio di lavoro in cui la `PivotTable` rende i valori calcolati e gli stili.

Un concetto particolarmente importante è la **cache condivisa**. Quando più tabelle pivot in una cartella di lavoro fanno riferimento allo stesso intervallo di origine, condividono *una* singola istanza di `PivotCache`. Una singola `PivotCache` può essere referenziata da molte tabelle pivot, e l'aggiornamento di quella cache aggiorna ogni `PivotTable` dipendente in un colpo solo.

{{% alert color="primary" %}}

`PivotCache.source_type` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire dalla v26.7, `PivotCache.refresh()` supporta solo i tipi di origine **`Sheet`** e **`Consolidation`**, ovvero dati che risiedono in intervalli del foglio di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.

{{% /alert %}}

A causa di questa catena, ci sono due percorsi di aggiornamento fondamentali in Aspose.Cells:

- **`PivotCache.refresh()`** — ricarica l'origine nella cache E ricalcola tutte le `PivotTable` dipendenti in una singola operazione.
- **`PivotTable.calculate_data()`** — ricalcola la visualizzazione di una `PivotTable` dai dati già memorizzati nella cache, senza tornare all'origine dati.

Tutti gli scenari in questo articolo utilizzano dati di origine da celle del foglio di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.

## Importazioni richieste

Tutti gli esempi Python in questo articolo iniziano con le seguenti tre istruzioni di importazione perché i tipi pivot si trovano nel namespace `aspose.cells.pivot`:

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Aggiornare tutte le tabelle pivot nella cartella di lavoro

Quando è necessario garantire che ogni cache pivot e ogni tabella pivot nella cartella di lavoro riflettano i dati di origine più recenti, l'API più semplice e completa è `Workbook.refresh_all()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla propria origine e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti generali e completi del documento in cui le prestazioni non sono un problema.

L'esempio seguente crea una cartella di lavoro con un intervallo di origine Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori di origine e quindi utilizza `refresh_all()` per aggiornare tutto in una singola chiamata.

```python
import aspose.cells as ac

# Crea una nuova cartella di lavoro
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Scrivi la riga di intestazione nelle celle A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Scrivi le righe di dati nelle celle A2:C9 (8 righe di dati sulla frutta negli anni 2020 e 2021)
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(50)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(60)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(70)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(80)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(90)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(100)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(110)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(120)

# Aggiungi una tabella pivot: intervallo sorgente "A1:C9", cella di destinazione "E3", nome "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Assegna i campi pivot: Fruit alle Righe, Year alle Colonne, Amount ai Dati
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Modifica diversi valori di Amount nei dati sorgente per simulare le modifiche
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# Aggiorna ogni tabella pivot / cache pivot nella cartella di lavoro
workbook.refresh_all()

# Salva la cartella di lavoro
workbook.save("output.xlsx")
```

## Aggiornare tutte le tabelle pivot su un singolo foglio di lavoro

A volte è necessario aggiornare solo le tabelle pivot che si trovano su un foglio di lavoro specifico, ad esempio quando le tabelle pivot su altri fogli di lavoro non sono correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.refresh_pivot_tables()`, che ha come ambito una singola istanza di `Worksheet`.

Questo è più selettivo rispetto a `Workbook.refresh_all()`: vengono aggiornate solo le tabelle pivot sul foglio di lavoro di destinazione, lasciando intatte le tabelle pivot sugli altri fogli di lavoro.

L'esempio seguente popola gli stessi dati di origine Frutto/Anno/Importo, aggiunge una tabella pivot sul primo foglio di lavoro, modifica alcuni valori di origine e quindi aggiorna solo le tabelle pivot su quel foglio di lavoro.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2021)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2021)
worksheet.cells["C5"].put_value(120)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(180)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2020)
worksheet.cells["C7"].put_value(130)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(220)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2020)
worksheet.cells["C9"].put_value(140)

pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

worksheet.cells["C2"].put_value(300)
worksheet.cells["C5"].put_value(250)
worksheet.cells["C9"].put_value(400)

worksheet.refresh_pivot_tables()

workbook.save("output.xlsx")
```

## Aggiornare una singola tabella pivot

Quando si desidera un controllo preciso su una singola tabella pivot, l'API basata su cache offre due opzioni. La scelta tra esse dipende da cosa è effettivamente cambiato: i dati di origine sottostanti o solo le impostazioni di vista/layout della tabella pivot stessa.

### Dati di origine cambiati — Usa `PivotCache.refresh()`

Se i dati di origine sottostanti sono cambiati, il punto di ingresso corretto è `pivot_table.pivot_cache.refresh()`. Questa chiamata rilegge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da quella cache.

{{% alert color="primary" %}}

Poiché le tabelle pivot condividono una singola istanza di `PivotCache`, la chiamata di `PivotCache.refresh()` ricalcola **tutte** le tabelle pivot costruite su quella stessa cache, non solo quella a cui si fa riferimento. Se due tabelle pivot condividono lo stesso intervallo di origine, l'aggiornamento di una cache aggiorna entrambe.

{{% /alert %}}

L'esempio seguente crea due tabelle pivot sullo stesso intervallo di origine per dimostrare questo comportamento di cache condivisa, modifica alcuni valori di origine e quindi aggiorna attraverso un riferimento a una cache.

```python
import aspose.cells as ac

# Crea una nuova cartella di lavoro e accedi al primo foglio di lavoro
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Scrivi la riga di intestazione: Frutta / Anno / Importo
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Scrivi circa 9 righe di dati (uva / mirtillo / kiwi / ciliegia nel periodo 2020-2021)
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

# Aggiungi la prima tabella pivot "Pivot1" ancorata alla cella E3, con intervallo di origine A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# Assegna i campi per Pivot1
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Aggiungi una SECONDA tabella pivot "Pivot2" ancorata a E15 utilizzando lo STESSO intervallo di origine A1:C9
# Sia Pivot1 che Pivot2 condividono un unico PivotCache perché l'intervallo di origine è identico.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Assegna gli stessi campi per Pivot2
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Modifica diversi valori delle celle Importo nei dati di origine per simulare una modifica dei dati
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# Aggiorna il PivotCache condiviso.
# Poiché Pivot1 e Pivot2 condividono lo stesso PivotCache, questa singola chiamata
# aggiorna ENTRAMBE le tabelle pivot (dati + stile) dall'origine aggiornata.
pivotTable1.pivot_cache.refresh()

# Salva la cartella di lavoro
workbook.save("output.xlsx")
```

### Solo vista/layout cambiato — Usa `calculate_data()`

Se i dati di origine *non* sono cambiati ma solo le impostazioni di vista o layout della tabella pivot sono state modificate (ad esempio, un campo è stato spostato in un'area diversa, o un'impostazione di aggiornamento all'apertura è stata attivata), non è necessario tornare all'origine dati. La cache contiene già i dati corretti; deve essere ricalcolata solo la `PivotTable` visualizzata. In questo caso, `pivot_table.calculate_data()` è la scelta giusta.

Ciò evita il recupero non necessario dall'origine ed è significativamente più veloce quando molte tabelle pivot condividono la stessa cache.

L'esempio seguente modifica una proprietà non di origine della tabella pivot e quindi chiama `calculate_data()` per ridisegnarla dalla cache esistente.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Scrivi riga di intestazione Frutta / Anno / Importo
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Scrivi 8 righe di dati (righe 2-9, corrispondenti all'intervallo sorgente A1:C9)
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(150)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(250)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(350)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(450)

# Aggiungi una tabella pivot denominata "Pivot1" posizionata nella cella di destinazione E3, con origine da A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Assegna i campi: Frutta a Riga, Anno a Colonna, Importo a Dati
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Modifica una proprietà di visualizzazione/layout — è una modifica solo di presentazione,
# quindi NON richiede la rilettura dei dati sorgente tramite PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False

# CalculateData() ridisegna la visualizzazione di QUESTA tabella pivot (dati + stile) dai
# dati già contenuti nella PivotCache. Poiché i dati sorgente non sono cambiati,
# non viene eseguito alcun round-trip verso la sorgente — solo i valori memorizzati nella cache vengono ricalcolati
# nelle celle del foglio di lavoro.
pivot_table.calculate_data()

# Salva la cartella di lavoro su disco
workbook.save("output.xlsx")
```

## Ottenere tutte le tabelle pivot che condividono la stessa PivotCache

Una cartella di lavoro spesso contiene molte tabelle pivot che si trovano tutte sopra una cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento in batch o per diagnosticare l'impatto della cache condivisa, utilizzare `PivotCache.get_pivot_tables()`. Questo metodo restituisce la raccolta di ogni `PivotTable` che dipende dalla cache data.

Questo è anche il modo più diretto per confermare che due tabelle pivot condividono effettivamente la stessa istanza di `PivotCache`: è possibile confrontare i riferimenti alla cache, o semplicemente iterare la raccolta restituita da `get_pivot_tables()` e osservare quali tabelle pivot vi appaiono.

L'esempio seguente crea due tabelle pivot sullo stesso intervallo di origine, verifica che condividano la stessa istanza di cache e quindi enumera le tabelle pivot della cache.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Sheet1"

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

pivot1_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = worksheet.pivot_tables[pivot1_index]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

pivot2_index = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = worksheet.pivot_tables[pivot2_index]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

same_cache = pivot_table1.pivot_cache is pivot_table2.pivot_cache
print("Pivot1 and Pivot2 share the same PivotCache: " + str(same_cache))

shared_pivot_tables = pivot_table1.pivot_cache.get_pivot_tables()
print("Number of pivot tables sharing the cache: " + str(len(shared_pivot_tables)))

for pt in shared_pivot_tables:
    print("Pivot table name: " + pt.name)

workbook.save("output.xlsx")
```

## Migrazione dall'obsoleto `PivotTable.refresh_data()`

Prima di Aspose.Cells for Python via .NET v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.refresh_data()` su ciascuna tabella pivot individualmente. A partire dalla v26.7, tale metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API consapevoli della cache descritte sopra.

Ci sono due motivi per cui l'approccio `refresh_data()` per tabella è problematico nelle cartelle di lavoro reali:

- Recupera i dati dall'origine *ogni* volta che viene chiamato, anche quando l'origine non è cambiata.
- Ogni chiamata aggiorna l'intera cache condivisa. Quando molte tabelle pivot condividono una cache, chiamare ripetutamente `refresh_data()` per ogni tabella pivot fa sì che la stessa cache venga recuperata più e più volte, il che è molto lento.

Le sostituzioni consigliate sono:

- **Aggiornare TUTTE le tabelle pivot nella cartella di lavoro** → utilizzare `workbook.refresh_all();`
- **Aggiornarne ALCUNE** → utilizzare `pivot_table.pivot_cache.refresh();` per una cache. Poiché la cache è condivisa, questa singola chiamata aggiorna ogni tabella pivot costruita sopra quella cache. Altre tabelle pivot che si trovano su una cache già aggiornata possono essere tranquillamente saltate.
- **Solo la vista/layout della pivot è cambiato** → utilizzare `pivot_table.calculate_data();` per ridisegnare dalla cache esistente senza alcun round-trip all'origine.

L'esempio seguente dimostra il nuovo pattern efficiente per cartelle di lavoro con più tabelle pivot che condividono una singola cache.

```python
import aspose.cells as ac

# Crea una nuova cartella di lavoro e accedi al primo foglio di lavoro
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- Costruisci i dati di origine: Frutto / Anno / Importo (intestazione + 9 righe) ---
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

sheet.cells["A2"].put_value("Grape")      ; sheet.cells["B2"].put_value(2020); sheet.cells["C2"].put_value(1000)
sheet.cells["A3"].put_value("Blueberry")  ; sheet.cells["B3"].put_value(2020); sheet.cells["C3"].put_value(2000)
sheet.cells["A4"].put_value("Kiwi")       ; sheet.cells["B4"].put_value(2020); sheet.cells["C4"].put_value(1500)
sheet.cells["A5"].put_value("Cherry")     ; sheet.cells["B5"].put_value(2020); sheet.cells["C5"].put_value(2500)
sheet.cells["A6"].put_value("Grape")      ; sheet.cells["B6"].put_value(2021); sheet.cells["C6"].put_value(3000)
sheet.cells["A7"].put_value("Blueberry")  ; sheet.cells["B7"].put_value(2021); sheet.cells["C7"].put_value(1800)
sheet.cells["A8"].put_value("Kiwi")       ; sheet.cells["B8"].put_value(2021); sheet.cells["C8"].put_value(2200)
sheet.cells["A9"].put_value("Cherry")     ; sheet.cells["B9"].put_value(2021); sheet.cells["C9"].put_value(2700)

# --- Aggiungi la prima tabella pivot (Pivot1) alla cella di destinazione E3 ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Aggiungi la SECONDA tabella pivot (Pivot2) sullo STESSO intervallo di origine ---
# Sia Pivot1 che Pivot2 condividono UN unico PivotCache sottostante.
# Questo è esattamente lo scenario in cui il vecchio approccio RefreshData()
# per tabella diventa inefficiente: aggiornare una tabella recupera nuovamente l'intero
# cache condiviso, quindi aggiornare N tabelle esegue la stessa costosa operazione N volte.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Modifica diversi valori di Importo nei dati di origine ---
sheet.cells["C2"].put_value(5000)   # Uva      2020
sheet.cells["C5"].put_value(7500)   # Ciliegia 2020
sheet.cells["C9"].put_value(9500)   # Ciliegia 2021

# --- Schema OBSOLETO (pre-26.7) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # recupera dall'origine, aggiorna l'intero cache
# pivot_table2.refresh_data();  # recupera DI NUOVO — il cache è già aggiornato!
# Ogni chiamata ricostruisce il cache condiviso, quindi N tabelle = N recuperi ridondanti.

# --- NUOVO schema v26.7+: aggiorna il cache UNA VOLTA, quindi rirenderizza se necessario ---
# Una sola chiamata a PivotCache.Refresh() porta i valori modificati nel cache condiviso
# E ricalcola la visualizzazione di OGNI tabella pivot che lo referenzia.
# Poiché Pivot1 e Pivot2 condividono un PivotCache, questa singola chiamata aggiorna
# entrambe le tabelle — non è richiesto un secondo round-trip verso l'origine.
pivot_table1.pivot_cache.refresh()

# CalculateData() rirenderizza solo la visualizzazione di una tabella pivot (dati + stile)
# dai dati già presenti nel cache — NON tocca l'origine.
# La chiamiamo su Pivot2 qui puramente per dimostrare l'API: dopo che il cache
# è stato aggiornato una volta, qualsiasi tabella dipendente può essere rirenderizzata senza
# tornare all'origine. Usa CalculateData() da solo quando solo le impostazioni di
# visualizzazione/layout della tabella pivot sono cambiate e il cache è aggiornato.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## Quale API di aggiornamento dovrei usare?

La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna di esse.

| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.refresh_all()` | Una sola chiamata; copre tutte le cache e tabelle. |
| Aggiornare solo le tabelle pivot su un singolo foglio | `Worksheet.refresh_pivot_tables()` | Ambito limitato a un foglio di lavoro. |
| Dati di origine cambiati per una cache | `pivot_table.pivot_cache.refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Solo le impostazioni di vista/layout sono cambiate | `pivot_table.calculate_data()` | Evita il round-trip non necessario all'origine. |
| Elencare tutte le tabelle pivot su una cache condivisa | `pivot_cache.get_pivot_tables()` | Da usare per enumerare prima dell'aggiornamento in blocco. |

In pratica, preferire le API basate sulla cache rispetto all'obsoleto `refresh_data()` per tabella. Sono consapevoli delle cache condivise, evitano recuperi ridondanti dall'origine e consentono di scegliere l'ambito più piccolo che soddisfa il proprio requisito di aggiornamento.

## Articoli correlati

- [Sparkline in Aspose.Cells for Python via .NET](/cells/it/python-net/sparkline/)

{{< app/cells/assistant language="python" >}}