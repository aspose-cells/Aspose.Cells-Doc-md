---
title: Aggiorna Tabelle Pivot e Cache Pivot in Aspose.Cells for Python via .NET
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells for Python via .NET utilizzando l'API di aggiornamento pivot v26.7+. Questo articolo tratta RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData e GetPivotTables con esempi pratici di codice.
linktitle: Aggiorna Tabelle Pivot
keywords: Aspose.Cells, Python via .NET, tabella pivot, aggiorna, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce un'API di aggiornamento a più livelli che consente di ricaricare i dati pivot in quattro ambiti diversi, dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for Python via .NET v26.7**, il metodo legacy `PivotTable.refresh_data()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.
{{% /alert %}}

## Introduction
Aggiornare una tabella pivot è raramente una singola operazione. Dietro le quinte, Aspose.Cells mantiene una catena di dati a più livelli che collega i dati di origine originali ai valori resi visibili nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento giusta in qualsiasi situazione.
La catena di dati a quattro livelli è:
1. **Data Source (Origine dati)** — gli intervalli originali del foglio di lavoro, la query del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati di origine. Ogni tabella pivot è costruita sopra un `PivotCache`; qui tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto vista che definisce i campi di riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dal suo `PivotCache`, mai direttamente dall'origine dati.
4. **Cells** — le `Cells` del foglio di lavoro in cui la `PivotTable` rende i valori calcolati e gli stili.

{{% alert color="primary" %}}
`PivotCache.source_type` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire dalla v26.7, `PivotCache.refresh()` supporta solo i tipi di origine **`Sheet`** e **`Consolidation`**, ovvero dati che risiedono negli intervalli del foglio di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.
{{% /alert %}}

A causa di questa catena, in Aspose.Cells esistono due percorsi di aggiornamento fondamentali:
- **`PivotTable.calculate_data()`** — ricalcola la visualizzazione di una `PivotTable` dai dati già presenti nella cache, senza tornare all'origine dati.
Tutti gli scenari di questo articolo utilizzano dati di origine da celle del foglio di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.

## Quick Start
Se hai bisogno solo del codice più breve possibile che aggiorni ogni tabella pivot nella cartella di lavoro, è sufficiente una singola chiamata:

```python
import aspose.cells as ac
# Crea una nuova cartella di lavoro
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Scrivi la riga di intestazione nelle celle A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# Scrivi le righe di dati nelle celle A2:C9 (8 righe di dati sulla frutta per 2020 e 2021)
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
# Aggiungi una tabella pivot: intervallo di origine "A1:C9", cella di destinazione "E3", nome "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Assegna i campi pivot: Fruit a Righe, Year a Colonne, Amount a Dati
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# Modifica diversi valori di Amount nei dati di origine per simulare delle modifiche
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)
# Aggiorna tutte le tabelle pivot / cache pivot nella cartella di lavoro
workbook.refresh_all()
# Salva la cartella di lavoro
workbook.save("output.xlsx")
```

Tutto il resto di questo articolo spiega quando scegliere invece un'API più ristretta.

## Required Imports
Tutti gli esempi Python in questo articolo iniziano con le seguenti tre istruzioni di importazione perché i tipi pivot risiedono nel namespace `aspose.cells.pivot`:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Refresh All Pivot Tables in the Workbook
Quando è necessario garantire che ogni cache pivot e ogni tabella pivot nella cartella di lavoro riflettano i dati di origine più recenti, l'API più semplice e completa è `Workbook.refresh_all()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla sua origine e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti generali e completi del documento in cui le prestazioni non sono un problema.
L'esempio seguente crea una cartella di lavoro con un intervallo di origine Fruit/Year/Amount, crea una tabella pivot, modifica alcuni valori di origine e quindi utilizza `refresh_all()` per portare tutto aggiornato in una singola chiamata.

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

## Refresh All Pivot Tables on a Single Worksheet
A volte è necessario aggiornare solo le tabelle pivot che si trovano su uno specifico foglio di lavoro, ad esempio quando le tabelle pivot su altri fogli di lavoro sono note per essere non correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.refresh_pivot_tables()`, che è limitato a una singola istanza di `Worksheet`.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Scrivi la riga di intestazione Frutto / Anno / Importo
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# Scrivi 8 righe di dati (righe 2-9, adattandosi all'intervallo di origine A1:C9)
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
# Assegna i campi: Frutto a Riga, Anno a Colonna, Importo a Dati
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# Modifica una proprietà di visualizzazione/layout — questa è una modifica solo di presentazione,
# quindi NON richiede la rilettura dei dati di origine tramite PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False
# CalculateData() ridisegna la visualizzazione di QUESTA tabella pivot (dati + stile) dai
# dati già presenti nella PivotCache. Poiché i dati di origine non sono cambiati,
# non viene eseguito alcun round-trip verso l'origine — solo i valori memorizzati nella cache vengono ricalcolati
# nelle celle del foglio di lavoro.
pivot_table.calculate_data()
# Salva la cartella di lavoro su disco
workbook.save("output.xlsx")
```

## Refresh a Single Pivot Table
Quando si desidera un controllo dettagliato su una singola tabella pivot, l'API basata sulla cache offre due opzioni. La scelta tra di esse dipende da cosa è effettivamente cambiato: i dati di origine sottostanti o solo le impostazioni di vista/layout della tabella pivot stessa.

### Source Data Changed — Use `PivotCache.refresh()`
Se i dati di origine sottostanti sono cambiati, il giusto punto di ingresso è `pivot_table.pivot_cache.refresh()`. Questa chiamata rilegge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da quella cache.

### Only View/Layout Changed — Use `calculate_data()`
Se i dati di origine *non* sono cambiati ma sono state modificate solo le impostazioni di vista o layout della tabella pivot (ad esempio, un campo è stato spostato in un'area diversa, o un'impostazione di aggiornamento all'apertura è stata attivata), non è necessario tornare all'origine dati. La cache contiene già i dati corretti; solo la `PivotTable` resa necessita di ricalcolo. In questo caso, `pivot_table.calculate_data()` è la scelta giusta.
L'esempio seguente modifica una proprietà non di origine della tabella pivot e quindi chiama `calculate_data()` per renderizzarla nuovamente dalla cache esistente.
Una cartella di lavoro spesso contiene molte tabelle pivot che poggiano tutte su un'unica cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento in batch o per diagnosticare l'impatto della cache condivisa, utilizzare `PivotCache.get_pivot_tables()`. Questo metodo restituisce la raccolta di ogni `PivotTable` che dipende dalla cache data.

## Migrating from the Obsolete `PivotTable.refresh_data()`
Prima di Aspose.Cells for Python via .NET v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.refresh_data()` su ciascuna tabella pivot individualmente. A partire dalla v26.7, quel metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API consapevoli della cache descritte sopra.
Ci sono due motivi per cui l'approccio `refresh_data()` per tabella è problematico nelle cartelle di lavoro reali:
- Recupera i dati dall'origine *ogni* volta che viene chiamato, anche quando l'origine non è cambiata.
Le sostituzioni consigliate sono:
L'esempio seguente dimostra il nuovo modello efficiente per cartelle di lavoro con più tabelle pivot che condividono un'unica cache.

## Which Refresh API Should I Use?
La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiorna tutto nella cartella di lavoro | `Workbook.refresh_all()` | Una sola chiamata; copre tutte le cache e le tabelle. |
| Aggiorna solo le tabelle pivot in un singolo foglio | `Worksheet.refresh_pivot_tables()` | Limitato a un foglio di lavoro. |
| Dati di origine modificati per una cache | `pivot_table.pivot_cache.refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Solo le impostazioni di vista/layout sono cambiate | `pivot_table.calculate_data()` | Evita un viaggio inutile verso l'origine. |
| Elenca tutte le tabelle pivot su una cache condivisa | `pivot_cache.get_pivot_tables()` | Usare per enumerare prima dell'aggiornamento in blocco. |
In pratica, preferire le API basate sulla cache rispetto all'obsoleto `refresh_data()` per tabella. Sono consapevoli delle cache condivise, evitano recuperi ridondanti dall'origine e consentono di scegliere l'ambito più piccolo che soddisfa il requisito di aggiornamento.

## Common Pitfalls
- **Dimenticare di aggiornare prima del salvataggio.** Una tabella pivot scrive i suoi valori resi nel foglio di lavoro solo quando la sua catena di dati viene aggiornata. Se si modificano le celle di origine, chiamare `PivotCache.Refresh()` (o `Workbook.RefreshAll()`) prima di `Workbook.save()`, altrimenti il file salvato contiene ancora i vecchi valori aggregati.
- **Chiamare l'obsoleto `RefreshData()` per tabella.** Nella v26.7, `PivotTable.RefreshData()` è contrassegnato come obsoleto e recupera l'origine per ogni chiamata. Con più tabelle pivot che condividono una cache, ciò significa N recuperi ridondanti dall'origine. Sostituire con un singolo `PivotCache.Refresh()` seguito da `CalculateData()` per tabella.
- **Aggiornare quando è cambiato solo il layout.** Se è stata modificata solo la vista di una tabella pivot (ordine delle colonne, `ConsolidationFunction`, ecc.) senza toccare i dati di origine, `PivotCache.Refresh()` non è necessario ed è lento. Chiamare `pivotTable.CalculateData()` per renderizzare nuovamente dalla cache esistente.
- **Origine esterna non supportata da `PivotCache.Refresh()`.** Se l'origine della tabella pivot proviene da una connessione esterna (database, cubo OLAP, ecc.), `PivotCache.Refresh()` non può aggiornarla nella v26.7 — attualmente supporta solo i tipi di origine `Sheet` e `Consolidation`. Per le origini esterne, riaprire la cartella di lavoro o ricostruire la cache dall'origine.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python-net" >}}