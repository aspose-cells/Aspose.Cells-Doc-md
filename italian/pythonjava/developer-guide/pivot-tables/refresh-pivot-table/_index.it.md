---
title: Aggiornare Tabelle Pivot e Cache Pivot in Aspose.Cells for Python via Java
linktitle: Aggiornare Tabelle Pivot e Cache Pivot
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells for Python via Java utilizzando l'API di aggiornamento delle pivot v26.7+. Questo articolo tratta RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData e GetPivotTables con esempi pratici di codice.
keywords: Aspose.Cells, Python via Java, tabella pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce un'API di aggiornamento a più livelli che consente di ricaricare i dati delle pivot in quattro ambiti diversi, dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for Python via Java v26.7**, il metodo legacy `PivotTable.refreshData()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.
{{% /alert %}}

## Introduction
Aggiornare una tabella pivot raramente è un'operazione singola. Dietro le quinte, Aspose.Cells mantiene una catena di dati a più livelli che collega i dati di origine originali ai valori renderizzati visibili nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento giusta per ogni situazione.
La catena di dati a quattro livelli è:
1. **Origine dati** — gli intervalli originali del foglio di lavoro, la query del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — lo snapshot in memoria dei dati di origine. Ogni tabella pivot è costruita sopra un `PivotCache`; è qui che tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto vista che definisce i campi riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dal proprio `PivotCache`, mai direttamente dall'origine dati.
4. **Cells** — le `Cells` del foglio di lavoro in cui la `PivotTable` rende i valori calcolati e gli stili.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire da v26.7, `PivotCache.refresh()` supporta solo i tipi di origine **`SHEET`** e **`CONSOLIDATION`**, ovvero dati che risiedono negli intervalli del foglio di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.
A causa di questa catena, in Aspose.Cells esistono due percorsi fondamentali di aggiornamento:
- **`PivotTable.calculateData()`** — ricalcola la visualizzazione di una `PivotTable` a partire dai dati già presenti nella cache, senza effettuare un round-trip verso l'origine dati.
Tutti gli scenari in questo articolo utilizzano dati di origine provenienti da celle del foglio di lavoro, quindi il tipo di origine è `SHEET` e le operazioni di aggiornamento si comportano come descritto.
{{% /alert %}}

## Quick Start
Se hai bisogno solo del codice più breve possibile che aggiorni ogni pivot nella cartella di lavoro, è sufficiente una singola chiamata:

```python
import jpype
from asposecells.api import Workbook

workbook = Workbook("input.xlsx")
workbook.refreshAll()
workbook.save("output.xlsx")
```

Tutto il resto in questo articolo spiega quando scegliere invece un'API più specifica.

## Required Imports
Tutti gli esempi Python in questo articolo si basano sulle seguenti importazioni perché i tipi pivot risiedono nel namespace `aspose.cells.pivot`:
- `import jpype`
- `import aspose.cells as cells`
Il modulo `jpype` viene utilizzato per avviare la JVM, mentre `aspose.cells` espone i tipi workbook/worksheet/cell/pivot usati in tutto il codice.

## Refresh All Pivot Tables in the Workbook
Quando hai bisogno di assicurarti che ogni cache pivot e ogni tabella pivot nella cartella di lavoro riflettano i dati di origine più recenti, l'API più semplice e completa è `Workbook.refreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla propria origine e poi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per gli aggiornamenti generali e completi del documento, quando le prestazioni non rappresentano un problema.
L'esempio seguente costruisce una cartella di lavoro con un intervallo di origine Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori di origine e poi utilizza `refreshAll()` per allineare il tutto in una singola chiamata.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create a new workbook
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)
# Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll()
# Save the workbook
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh All Pivot Tables on a Single Worksheet
A volte è necessario aggiornare solo le tabelle pivot che si trovano su un determinato foglio di lavoro, ad esempio quando le tabelle pivot presenti su altri fogli non sono correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.refreshPivotTables()`, che è limitato a una singola istanza di `Worksheet`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)
worksheet.refreshPivotTables()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh a Single Pivot Table
Quando si desidera un controllo dettagliato su una singola tabella pivot, l'API basata sulla cache offre due opzioni. La scelta tra esse dipende da cosa è effettivamente cambiato: i dati di origine sottostanti oppure solo le impostazioni di vista/layout della tabella pivot stessa.

### Source Data Changed — Use `PivotCache.refresh()`
Se i dati di origine sottostanti sono cambiati, il punto di ingresso corretto è `pivotTable.getPivotCache().refresh()`. Questa chiamata rilegge i dati di origine nella cache e poi ricalcola ogni `PivotTable` che dipende da quella cache.

### Only View/Layout Changed — Use `calculateData()`
Se i dati di origine *non* sono cambiati ma sono state modificate solo le impostazioni di vista o layout della tabella pivot (ad esempio, un campo è stato spostato in un'area diversa oppure è stata attivata/disattivata un'opzione di aggiornamento all'apertura), non è necessario tornare all'origine dati. La cache contiene già i dati corretti; solo la `PivotTable` renderizzata deve essere ricalcolata. In questo caso, `pivotTable.calculateData()` è la scelta giusta.
L'esempio seguente modifica una proprietà non legata all'origine della tabella pivot e poi chiama `calculateData()` per renderizzarla nuovamente dalla cache esistente.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)
# Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# calculateData() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivotTable.calculateData()
# Save the workbook to disk
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

Una cartella di lavoro spesso contiene molte tabelle pivot che poggiano tutte su una cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento in batch o per diagnosticare l'impatto della cache condivisa, usa `PivotCache.getPivotTables()`. Questo metodo restituisce la raccolta di tutte le `PivotTable` che dipendono dalla cache indicata.

## Migrating from the Obsolete `PivotTable.refreshData()`
Prima di Aspose.Cells for Python via Java v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.refreshData()` su ciascuna tabella pivot singolarmente. A partire da v26.7, quel metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API consapevoli della cache descritte sopra.
Ci sono due motivi per cui l'approccio `refreshData()` per singola tabella è problematico nelle cartelle di lavoro reali:
- Rilegge i dati dall'origine *ogni* volta che viene chiamato, anche quando l'origine non è cambiata.
Le sostituzioni consigliate sono:
L'esempio seguente mostra il nuovo pattern efficiente per cartelle di lavoro con più tabelle pivot che condividono una singola cache.

## Which Refresh API Should I Use?
La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna di esse.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.refreshAll()` | Una sola chiamata; copre tutte le cache e le tabelle. |
| Aggiornare solo le tabelle pivot su un singolo foglio | `Worksheet.refreshPivotTables()` | Limitato a un foglio di lavoro. |
| Dati di origine cambiati per una cache | `pivotTable.getPivotCache().refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Sono cambiate solo le impostazioni di vista/layout | `pivotTable.calculateData()` | Evita il round-trip non necessario verso l'origine. |
| Elencare tutte le tabelle pivot su una cache condivisa | `pivotCache.getPivotTables()` | Da usare per enumerare prima dell'aggiornamento in blocco. |
In pratica, è preferibile usare le API basate sulla cache rispetto all'obsoleto `refreshData()` per tabella. Esse sono consapevoli delle cache condivise, evitano recuperi ridondanti dall'origine e consentono di scegliere l'ambito più piccolo che soddisfa il requisito di aggiornamento.

## Common Pitfalls
- **Dimenticare di aggiornare prima di salvare.** Una tabella pivot scrive i propri valori renderizzati nel foglio di lavoro solo quando la catena di dati viene aggiornata. Se modifichi le celle di origine, chiama `PivotCache.refresh()` (oppure `Workbook.refreshAll()`) prima di `Workbook.save()`, altrimenti il file salvato conterrà ancora i vecchi valori aggregati.
- **Chiamare l'obsoleto `RefreshData()` per tabella.** In v26.7, `PivotTable.RefreshData()` è contrassegnato come obsoleto e rilegge l'origine a ogni chiamata. Con più tabelle pivot che condividono una cache, ciò significa N recuperi ridondanti dall'origine. Sostituiscilo con una singola `PivotCache.refresh()` seguita da `calculateData()` per ogni tabella.
- **Aggiornare quando è cambiato solo il layout.** Se hai modificato solo la vista di una tabella pivot (ordine delle colonne, `ConsolidationFunction`, ecc.) senza toccare i dati di origine, `PivotCache.refresh()` non è necessario ed è lento. Chiama `pivotTable.calculateData()` per renderizzare nuovamente dalla cache esistente.
- **Origine esterna non supportata da `PivotCache.refresh()`.** Se l'origine della tabella pivot proviene da una connessione esterna (database, cubo OLAP, ecc.), `PivotCache.refresh()` non può aggiornarla in v26.7: attualmente supporta solo i tipi di origine `Sheet` e `Consolidation`. Per le origini esterne, riapri la cartella di lavoro oppure ricostruisci la cache dall'origine.

{{< app/cells/assistant language="python" >}}