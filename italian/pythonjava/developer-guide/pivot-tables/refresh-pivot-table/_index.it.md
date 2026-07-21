---
title: Aggiornamento delle tabelle pivot in Aspose.Cells for Python via Java
linktitle: Aggiornamento delle tabelle pivot
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells for Python via Java utilizzando l'API di aggiornamento pivot v26.7+. Questo articolo copre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData e GetPivotTables con esempi pratici di codice.
keywords: Aspose.Cells, Python via Java, tabella pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells fornisce un'API di aggiornamento a livelli che consente di ricaricare i dati pivot in quattro ambiti diversi, dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for Aspose.Cells for Python via Java v26.7**, il metodo legacy `PivotTable.refreshData()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.

{{% /alert %}}

## Introduzione

L'aggiornamento di una tabella pivot è raramente una singola operazione. Dietro le quinte, Aspose.Cells mantiene una catena di dati a livelli che collega i dati sorgente originali ai valori visualizzati nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento giusta per qualsiasi situazione.

La catena di dati a quattro livelli è:

1. **Sorgente dati** — gli intervalli originali del foglio di lavoro, la query del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati sorgente. Ogni tabella pivot è costruita sopra un `PivotCache`; è qui che tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto vista che definisce i campi riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dal suo `PivotCache`, mai direttamente dalla sorgente dati.
4. **Celle** — le `Cells` del foglio di lavoro in cui il `PivotTable` rende i valori calcolati e gli stili.

Un concetto particolarmente importante è la **cache condivisa**. Quando più tabelle pivot in una cartella di lavoro fanno riferimento allo stesso intervallo sorgente, condividono *una* singola istanza di `PivotCache`. Un singolo `PivotCache` può essere referenziato da molte tabelle pivot, e l'aggiornamento di quella cache aggiorna immediatamente ogni `PivotTable` dipendente.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire dalla v26.7, `PivotCache.refresh()` supporta solo i tipi di sorgente **`SHEET`** e **`CONSOLIDATION`**, ovvero dati che risiedono negli intervalli del foglio di lavoro. Le sorgenti esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.

{{% /alert %}}

A causa di questa catena, ci sono due percorsi di aggiornamento fondamentali in Aspose.Cells:

- **`PivotCache.refresh()`** — ricarica sorgente → cache E ricalcola tutte le `PivotTable` dipendenti in una singola operazione.
- **`PivotTable.calculateData()`** — ricalcola la visualizzazione di una `PivotTable` dai dati già memorizzati nella cache, senza tornare alla sorgente dati.

Tutti gli scenari in questo articolo utilizzano dati sorgente da celle del foglio di lavoro, quindi il tipo di sorgente è `SHEET` e le operazioni di aggiornamento si comportano come descritto.

## Importazioni richieste

Tutti gli esempi Python in questo articolo si basano sulle seguenti importazioni perché i tipi pivot si trovano nel namespace `aspose.cells.pivot`:

- `import jpype`
- `import aspose.cells as cells`

Il modulo `jpype` viene utilizzato per avviare la JVM, mentre `aspose.cells` espone i tipi workbook/worksheet/cell/pivot utilizzati in tutto il documento.

## Aggiornare tutte le tabelle pivot nella cartella di lavoro

Quando è necessario garantire che ogni cache pivot e ogni tabella pivot nella cartella di lavoro riflettano i dati sorgente più recenti, l'API più semplice e completa è `Workbook.refreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla sua sorgente e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti generali e completi del documento in cui le prestazioni non sono un problema.

L'esempio seguente crea una cartella di lavoro con un intervallo sorgente Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori sorgente e quindi utilizza `refreshAll()` per aggiornare tutto in una singola chiamata.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Crea una nuova cartella di lavoro
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Scrivi la riga di intestazione nelle celle A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Scrivi le righe di dati nelle celle A2:C9 (8 righe di dati sulla frutta tra 2020 e 2021)
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

# Aggiungi una tabella pivot: intervallo sorgente "A1:C9", cella di destinazione "E3", nome "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Assegna i campi pivot: Fruit a Righe, Year a Colonne, Amount a Dati
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Modifica diversi valori di Amount nei dati sorgente per simulare delle modifiche
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# Aggiorna ogni tabella pivot / cache pivot nella cartella di lavoro
workbook.refreshAll()

# Salva la cartella di lavoro
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Aggiornare tutte le tabelle pivot su un singolo foglio di lavoro

A volte è necessario aggiornare solo le tabelle pivot che si trovano su un foglio di lavoro specifico, ad esempio quando le tabelle pivot su altri fogli di lavoro non sono correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.refreshPivotTables()`, che è limitato a una singola istanza di `Worksheet`.

Questo è più selettivo rispetto a `Workbook.refreshAll()`: solo le tabelle pivot sul foglio di lavoro selezionato vengono aggiornate, lasciando intatte le tabelle pivot sugli altri fogli di lavoro.

L'esempio seguente popola gli stessi dati sorgente Frutto/Anno/Importo, aggiunge una tabella pivot sul primo foglio di lavoro, modifica alcuni valori sorgente e quindi aggiorna solo le tabelle pivot su quel foglio di lavoro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
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

## Aggiornare una singola tabella pivot

Quando si desidera un controllo dettagliato su una singola tabella pivot, l'API basata sulla cache offre due opzioni. La scelta tra esse dipende da ciò che è effettivamente cambiato: i dati sorgente sottostanti, o solo le impostazioni di vista/layout della tabella pivot stessa.

### Dati sorgente modificati — Usare `PivotCache.refresh()`

Se i dati sorgente sottostanti sono cambiati, il punto di ingresso corretto è `pivotTable.getPivotCache().refresh()`. Questa chiamata rilegge i dati sorgente nella cache e quindi ricalcola ogni `PivotTable` che dipende da quella cache.

{{% alert color="primary" %}}

Poiché le tabelle pivot condividono una singola istanza di `PivotCache`, la chiamata a `PivotCache.refresh()` ricalcola **tutte** le tabelle pivot costruite su quella stessa cache, non solo quella a cui si fa riferimento. Se due tabelle pivot condividono lo stesso intervallo sorgente, l'aggiornamento di una cache aggiorna entrambe.

{{% /alert %}}

L'esempio seguente crea due tabelle pivot sullo stesso intervallo sorgente per dimostrare questo comportamento di cache condivisa, modifica alcuni valori sorgente e quindi aggiorna tramite un riferimento alla cache.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Crea una nuova cartella di lavoro e accedi al primo foglio di lavoro
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Scrivi la riga di intestazione: Frutto / Anno / Importo
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Scrivi circa 9 righe di dati (uva / mirtillo / kiwi / ciliegia negli anni 2020-2021)
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
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

# Aggiungi la prima tabella pivot "Pivot1" ancorata alla cella E3, con intervallo di origine A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# Assegna i campi per Pivot1
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# Aggiungi una SECONDA tabella pivot "Pivot2" ancorata in E15 utilizzando lo STESSO intervallo di origine A1:C9
# Sia Pivot1 che Pivot2 condividono un unico PivotCache perché l'intervallo di origine è identico.
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# Assegna gli stessi campi per Pivot2
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# Modifica diversi valori delle celle dell'Importo nei dati di origine per simulare una modifica dei dati
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# Aggiorna il PivotCache condiviso.
# Poiché Pivot1 e Pivot2 condividono lo stesso PivotCache, questa singola chiamata
# aggiorna ENTRAMBE le tabelle pivot (dati + stile) dall'origine aggiornata.
pivotTable1.getPivotCache().refresh()

# Salva la cartella di lavoro
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Solo vista/layout modificati — Usare `calculateData()`

Se i dati sorgente *non* sono cambiati ma solo le impostazioni di vista o layout della tabella pivot sono state modificate (ad esempio, un campo è stato spostato in un'area diversa, o un'impostazione di aggiornamento all'apertura è stata attivata/disattivata), non è necessario tornare alla sorgente dati. La cache contiene già i dati corretti; solo il `PivotTable` reso necessita di ricalcolo. In questo caso, `pivotTable.calculateData()` è la scelta giusta.

Ciò evita il recupero non necessario dalla sorgente ed è significativamente più veloce quando molte tabelle pivot condividono la stessa cache.

L'esempio seguente modifica una proprietà non sorgente della tabella pivot e quindi chiama `calculateData()` per ri-renderizzarla dalla cache esistente.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Scrivi la riga di intestazione Frutto / Anno / Importo
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Scrivi 8 righe di dati (righe 2-9, adattandosi all'intervallo sorgente A1:C9)
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

# Aggiungi una tabella pivot denominata "Pivot1" posizionata nella cella di destinazione E3, con origine da A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Assegna i campi: Frutto a Riga, Anno a Colonna, Importo a Dati
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Modifica una proprietà di visualizzazione/layout — questa è una modifica solo di presentazione,
# quindi NON richiede la rilettura dei dati sorgente tramite PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() ridisegna la visualizzazione di QUESTA tabella pivot (dati + stile) dai
# dati già contenuti nel PivotCache. Poiché i dati sorgente non sono cambiati,
# non viene eseguito alcun round-trip verso la sorgente — solo i valori memorizzati nella cache vengono ricalcolati
# nelle celle del foglio di lavoro.
pivotTable.calculateData()

# Salva la cartella di lavoro su disco
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Ottenere tutte le tabelle pivot che condividono lo stesso PivotCache

Una cartella di lavoro spesso contiene molte tabelle pivot che si trovano tutte sopra una cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento in batch o per diagnosticare l'impatto della cache condivisa, utilizzare `PivotCache.getPivotTables()`. Questo metodo restituisce la raccolta di ogni `PivotTable` che dipende dalla cache data.

Questo è anche il modo più diretto per confermare che due tabelle pivot condividono effettivamente la stessa istanza di `PivotCache`: è possibile confrontare i riferimenti della cache, o semplicemente iterare la raccolta restituita da `getPivotTables()` e osservare quali tabelle pivot appaiono in essa.

L'esempio seguente crea due tabelle pivot sullo stesso intervallo sorgente, verifica che condividano la stessa istanza di cache e quindi enumera le tabelle pivot della cache.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotFieldType

# codice portato qui
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Sheet1")

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

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
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivot1Index)
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount")

pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivot2Index)
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount")

sameCache = pivotTable1.getPivotCache() is pivotTable2.getPivotCache()
print("Pivot1 and Pivot2 share the same PivotCache: " + str(sameCache))

sharedPivotTables = pivotTable1.getPivotCache().getPivotTables()
print("Number of pivot tables sharing the cache: " + str(len(sharedPivotTables)))

for pt in sharedPivotTables:
    print("Pivot table name: " + pt.getName())

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Migrazione dall'obsoleto `PivotTable.refreshData()`

Prima di Aspose.Cells for Aspose.Cells for Python via Java v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.refreshData()` su ciascuna tabella pivot individualmente. A partire dalla v26.7, quel metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API consapevoli della cache descritte sopra.

Ci sono due motivi per cui l'approccio `refreshData()` per tabella è problematico nelle cartelle di lavoro reali:

- Recupera i dati dalla sorgente *ogni* volta che viene chiamato, anche quando la sorgente non è cambiata.
- Ogni chiamata aggiorna l'intera cache condivisa. Quando molte tabelle pivot condividono una cache, chiamare ripetutamente `refreshData()` per tabella pivot fa sì che la stessa cache venga recuperata più e più volte, il che è molto lento.

Le sostituzioni consigliate sono:

- **Aggiorna TUTTE le tabelle pivot nella cartella di lavoro** → usa `workbook.refreshAll();`
- **Aggiorna ALCUNE di esse** → usa `pivotTable.getPivotCache().refresh();` per una cache. Poiché la cache è condivisa, questa singola chiamata aggiorna ogni tabella pivot costruita sopra quella cache. Altre tabelle pivot che si trovano su una cache già aggiornata possono essere tranquillamente saltate.
- **Solo la vista/layout pivot è cambiata** → usa `pivotTable.calculateData();` per ri-renderizzare dalla cache esistente senza alcun ritorno alla sorgente.

L'esempio seguente dimostra il nuovo schema efficiente per cartelle di lavoro con più tabelle pivot che condividono una singola cache.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Crea una nuova cartella di lavoro e accedi al primo foglio di lavoro
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- Costruisci i dati di origine: Frutto / Anno / Importo (intestazione + 9 righe) ---
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000)
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000)
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500)
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500)
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000)
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800)
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200)
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700)

# --- Aggiungi la prima tabella pivot (Pivot1) nella cella di destinazione E3 ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Aggiungi la SECONDA tabella pivot (Pivot2) sullo STESSO intervallo di origine ---
# Sia Pivot1 che Pivot2 condividono UN unico PivotCache sottostante.
# Questo è esattamente lo scenario in cui l'approccio legacy per tabella
# RefreshData() diventa inefficiente: aggiornare una tabella recupera l'intera
# cache condivisa, quindi aggiornare N tabelle esegue la stessa operazione
# costosa N volte.
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Modifica diversi valori di Importo nei dati di origine ---
sheet.getCells().get("C2").putValue(5000)   # Grape  2020
sheet.getCells().get("C5").putValue(7500)   # Cherry 2020
sheet.getCells().get("C9").putValue(9500)   # Cherry 2021

# --- Schema OBSOLETO (pre-26.7) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // recupera di nuovo dall'origine, aggiorna l'intera cache
# pivotTable2.RefreshData();  // recupera di NUOVO — la cache è già aggiornata!
# Ogni chiamata ricostruisce la cache condivisa, quindi N tabelle = N recuperi ridondanti.

# --- NUOVO schema v26.7+: aggiorna la cache UNA volta, quindi ridisegna se necessario ---
# Una sola chiamata a PivotCache.Refresh() recupera i valori modificati nella cache
# condivisa E ricalcola la visualizzazione di OGNI tabella pivot che vi fa riferimento.
# Poiché Pivot1 e Pivot2 condividono un PivotCache, questa singola chiamata
# aggiorna entrambe le tabelle — non è richiesto un secondo round-trip all'origine.
pivotTable1.getPivotCache().refresh()

# CalculateData() ridisegna solo la visualizzazione di una tabella pivot (dati + stile)
# dai dati già presenti nella cache — NON tocca l'origine.
# Lo chiamiamo su Pivot2 qui solo per dimostrare l'API: dopo che la cache
# è stata aggiornata una volta, qualsiasi tabella dipendente può essere ridisegnata
# senza tornare all'origine. Usa CalculateData() da solo quando sono cambiate solo
# le impostazioni di vista/layout della tabella pivot e la cache è aggiornata.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Quale API di aggiornamento dovrei usare?

La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna.

| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiorna tutto nella cartella di lavoro | `Workbook.refreshAll()` | Una sola chiamata; copre tutte le cache e tabelle. |
| Aggiorna solo le tabelle pivot su un singolo foglio | `Worksheet.refreshPivotTables()` | Limitato a un foglio di lavoro. |
| Dati sorgente cambiati per una cache | `pivotTable.getPivotCache().refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Solo le impostazioni di vista/layout sono cambiate | `pivotTable.calculateData()` | Evita il ritorno non necessario alla sorgente. |
| Elenca tutte le tabelle pivot su una cache condivisa | `pivotCache.getPivotTables()` | Usare per enumerare prima dell'aggiornamento in batch. |

In pratica, preferire le API basate sulla cache rispetto all'obsoleto `refreshData()` per tabella. Esse sono consapevoli delle cache condivise, evitano recuperi ridondanti dalla sorgente e consentono di scegliere l'ambito più piccolo che soddisfi il requisito di aggiornamento.

{{< app/cells/assistant language="python" >}}