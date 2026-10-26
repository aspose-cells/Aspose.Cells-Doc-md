---
title: Aggiornare le Tabelle Pivot e le cache pivot in Aspose.Cells for Python via .NET
linktitle: Aggiornare le Tabelle Pivot e le cache pivot
description: Scopri come aggiornare le Tabelle Pivot in Aspose.Cells for Python via .NET usando l'API di aggiornamento delle Tabelle Pivot v26.7+. Questo articolo illustra refresh_all, _refresh_pivot_tables, PivotCache.refresh, _calculate_data e _get_pivot_tables con esempi di codice pratici.
keywords: Aspose.Cells, Python via .NET, Tabella Pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce un'API di aggiornamento a livelli che consente di ricaricare i dati delle Tabelle Pivot in quattro ambiti diversi, dall'intera cartella di lavoro fino a una singola Tabella Pivot. A partire da **Aspose.Cells for Python via .NET v26.7**, il metodo precedente `PivotTable.refresh_data()` è contrassegnato come obsoleto e deve essere sostituito dalle API più efficienti che tengono conto della cache, descritte in questo articolo.
{{% /alert %}}

## Introduction
L'aggiornamento di una Tabella Pivot raramente consiste in una singola operazione. Dietro le quinte, Aspose.Cells mantiene una catena di dati a livelli che collega i dati di origine originali ai valori visualizzati nel foglio di lavoro. Comprendere questa catena è essenziale per scegliere l'API di aggiornamento giusta in ogni situazione.
La catena di dati a quattro livelli è:
1. **Origine dati** — gli intervalli del foglio di lavoro di origine, l'interrogazione del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati di origine. Ogni Tabella Pivot è costruita su un `PivotCache`, nel quale tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto di visualizzazione che definisce i campi di riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dal proprio `PivotCache`, mai direttamente dall'origine dati.
4. **Cells** — le `Cells` del foglio di lavoro in cui la `PivotTable` trasferisce i valori calcolati e gli stili.

{{% alert color="primary" %}}
`PivotCache.source_type` (enumerazione `PivotTableSourceType`) indica da dove provengono i dati della cache. Dalla versione v26.7, `PivotCache.refresh()` supporta esclusivamente i tipi di origine **`Sheet`** e **`Consolidation`**, ovvero dati contenuti in intervalli di fogli di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.
Poiché la catena è composta da questi livelli, in Aspose.Cells esistono due percorsi fondamentali per l'aggiornamento:
- **`PivotTable.calculate_data()`** — ricalcola la visualizzazione di una `PivotTable` a partire dai dati già memorizzati nella cache, senza dover tornare all'origine dati.
Tutti gli scenari di questo articolo usano dati di origine costituiti da celle di fogli di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.
{{% /alert %}}

## Quick Start
Se serve soltanto il codice più breve possibile per aggiornare tutte le Tabelle Pivot nella cartella di lavoro, è sufficiente una singola chiamata:

```python
import aspose.cells as ac

workbook = ac.Workbook("input.xlsx")
workbook.refresh_all()
workbook.save("output.xlsx")
```

Tutto il resto di questo articolo spiega quando scegliere un'API con un ambito più ristretto.

## Required Imports
Tutti gli esempi Python di questo articolo iniziano con le seguenti tre istruzioni di import, poiché i tipi relativi alle Tabelle Pivot si trovano nel namespace `aspose.cells.pivot`:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Refresh All Pivot Tables in the Workbook
Quando devi garantire che ogni cache pivot e ogni Tabella Pivot nella cartella di lavoro riflettano i dati di origine più recenti, l'API più semplice e completa è `Workbook.refresh_all()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla propria origine e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per gli aggiornamenti generali dell'intero documento quando le prestazioni non costituiscono un problema.
L'esempio seguente costruisce una cartella di lavoro con un intervallo di origine per frutta, anno e importo, crea una Tabella Pivot, modifica alcuni valori di origine e usa `refresh_all()` per aggiornare tutto in una singola chiamata.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
# Create a new workbook
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write header row into cells A1:C1
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(50)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(60)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(70)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(80)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(90)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(100)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(110)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(120)
# Add a pivot table: source range "A1:C9", destination cell "E3"
pivot_table = worksheet.pivot_tables.add("A1:C9", 2, 4)
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.cells.get("C2").put_value(55)
worksheet.cells.get("C5").put_value(85)
worksheet.cells.get("C9").put_value(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refresh_all()
# Save the workbook
workbook.save("output.xlsx")
```

## Refresh All Pivot Tables on a Single Worksheet
Talvolta occorre aggiornare soltanto le Tabelle Pivot presenti in un determinato foglio di lavoro, ad esempio quando quelle in altri fogli sono note come non correlate e non devono essere modificate. Per questo caso, Aspose.Cells fornisce `Worksheet.refresh_pivot_tables()`, che opera nell'ambito di una singola istanza di `Worksheet`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2021)
worksheet.cells.get("C3").put_value(150)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(200)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2021)
worksheet.cells.get("C5").put_value(120)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(180)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2020)
worksheet.cells.get("C7").put_value(130)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(220)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2020)
worksheet.cells.get("C9").put_value(140)
pivot_table = worksheet.pivot_tables.add("A1:C9", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
worksheet.cells.get("C2").put_value(300)
worksheet.cells.get("C5").put_value(250)
worksheet.cells.get("C9").put_value(400)
worksheet.refresh_pivot_tables()
workbook.save("output.xlsx")
```

## Refresh a Single Pivot Table
Quando è necessario un controllo dettagliato su una singola Tabella Pivot, l'API basata sulla cache offre due opzioni. La scelta dipende da ciò che è effettivamente cambiato: i dati di origine sottostanti oppure solo le impostazioni di visualizzazione e disposizione della Tabella Pivot stessa.

### Source Data Changed — Use `PivotCache.refresh()`
Se i dati di origine sottostanti sono stati modificati, il punto di ingresso corretto è `pivot_table.pivot_cache.refresh()`. Questa chiamata rilegge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da essa.

### Only View/Layout Changed — Use `calculate_data()`
Se i dati di origine *non* sono stati modificati, ma sono cambiate solo le impostazioni di visualizzazione o disposizione della Tabella Pivot, ad esempio quando un campo è stato spostato in un'area diversa o quando un'impostazione di aggiornamento all'apertura è stata attivata o disattivata, non è necessario tornare all'origine dati. La cache contiene già i dati corretti; occorre ricalcolare solo la `PivotTable` così come viene visualizzata. In questo caso, `pivot_table.calculate_data()` è la scelta corretta.
L'esempio seguente modifica una proprietà della Tabella Pivot non correlata all'origine e quindi chiama `calculate_data()` per rigenerarne la visualizzazione dalla cache esistente.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write Fruit / Year / Amount header row
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(200)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(300)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(400)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(150)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(250)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(350)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(450)
# Add a pivot table placed at destination cell E3, sourcing from A1:C9
pivot_table = worksheet.pivot_tables.add("A1:C9", 2, 4)
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivot_table.refresh_data_on_opening_file = False
# calculate_data() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivot_table.calculate_data()
# Save the workbook to disk
workbook.save("output.xlsx")
```

Una cartella di lavoro contiene spesso molte Tabelle Pivot basate tutte sulla stessa cache. Per enumerarle, ad esempio prima di eseguire un aggiornamento massivo o per diagnosticare l'impatto di una cache condivisa, usa `PivotCache.get_pivot_tables()`. Questo metodo restituisce la raccolta di tutte le `PivotTable` che dipendono dalla cache specificata.

## Migrating from the Obsolete `PivotTable.refresh_data()`
Prima di Aspose.Cells for Python via .NET v26.7, il metodo standard per aggiornare una Tabella Pivot era chiamare `PivotTable.refresh_data()` singolarmente su ogni tabella. A partire da v26.7, tale metodo è contrassegnato come **obsoleto** e deve essere sostituito dalle API che tengono conto della cache descritte in precedenza.
Esistono due motivi per cui l'approccio `refresh_data()` per singola tabella risulta problematico nelle cartelle di lavoro reali:
- Recupera i dati dall'origine *ogni* volta che viene chiamato, anche quando l'origine non è cambiata.
Le sostituzioni consigliate sono:
L'esempio seguente dimostra il nuovo schema efficiente per cartelle di lavoro con più Tabelle Pivot che condividono una singola cache.

## Which Refresh API Should I Use?
La tabella seguente riepiloga le API di aggiornamento disponibili e le circostanze in cui scegliere ciascuna di esse.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.refresh_all()` | Una singola chiamata; include tutte le cache e le tabelle. |
| Aggiornare solo le Tabelle Pivot in un singolo foglio | `Worksheet.refresh_pivot_tables()` | Limitata a un solo foglio di lavoro. |
| Dati di origine modificati per una cache | `pivot_table.pivot_cache.refresh()` | Aggiorna TUTTE le Tabelle Pivot basate su quella cache condivisa. |
| Modificate solo le impostazioni di vista e disposizione | `pivot_table.calculate_data()` | Evita il ritorno non necessario all'origine. |
| Elencare tutte le Tabelle Pivot associate a una cache condivisa | `pivot_cache.get_pivot_tables()` | Da utilizzare per enumerarle prima di un aggiornamento massivo. |
Nella pratica, è preferibile utilizzare le API basate sulla cache rispetto al metodo obsoleto `refresh_data()` per singola tabella. Tali API tengono conto delle cache condivise, evitano recuperi ridondanti dall'origine e consentono di scegliere l'ambito più piccolo che soddisfa il requisito di aggiornamento.

## Common Pitfalls
- **Dimenticare di aggiornare prima di salvare.** Una Tabella Pivot scrive i valori visualizzati nel foglio di lavoro solo quando la catena di dati viene aggiornata. Se modifichi le celle di origine, chiama `PivotCache.refresh()` (o `Workbook.refresh_all()`) prima di `Workbook.save()`; in caso contrario, il file salvato conterrà ancora i precedenti valori aggregati.
- **Chiamare il metodo obsoleto `refresh_data()` per ogni tabella.** In v26.7, `PivotTable.refresh_data()` è contrassegnato come obsoleto e recupera nuovamente l'origine a ogni chiamata. Con più Tabelle Pivot che condividono una cache, ciò comporta N recuperi ridondanti dall'origine. Sostituiscilo con una singola chiamata a `PivotCache.refresh()`, seguita da `calculate_data()` per ogni tabella.
- **Aggiornare quando è cambiata solo la disposizione.** Se hai modificato solo la visualizzazione di una Tabella Pivot, come l'ordine delle colonne o `ConsolidationFunction`, senza toccare i dati di origine, `PivotCache.refresh()` non è necessario ed è lento. Chiama `pivotTable.calculate_data()` per rigenerare la visualizzazione dalla cache esistente.
- **Origine esterna non supportata da `PivotCache.refresh()`.** Se l'origine della Tabella Pivot proviene da una connessione esterna, come un database o un cubo OLAP, `PivotCache.refresh()` non può aggiornarla in v26.7 perché attualmente supporta solo i tipi di origine `Sheet` e `Consolidation`. Per le origini esterne, riapri la cartella di lavoro o ricostruisci la cache dall'origine.

{{< app/cells/assistant language="python-net" >}}