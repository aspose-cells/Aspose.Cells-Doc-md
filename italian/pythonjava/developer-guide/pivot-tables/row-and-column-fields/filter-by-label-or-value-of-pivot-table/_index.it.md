---
title: Filtrare le tabelle pivot per etichetta o valore
description: Aspose.Cells for Python via Java supporta funzionalità complete di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati di una tabella pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri primi 10 e nascondendo o rendendo visibili singoli elementi pivot.
linktitle: Filtrare le tabelle pivot per etichetta o valore
keywords: Aspose.Cells, libreria Python via Java, foglio di calcolo, tabella pivot, filtro, filtro per etichetta, filtro per valore, filtro per data, filtro primi 10, elemento pivot, nascondere elemento pivot
type: docs
weight: 10
url: /it/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot. È possibile applicare filtri per etichetta ai campi di riga o colonna basati su testo, utilizzare filtri per data quando il campo contiene solo celle di tipo data-ora o vuote, applicare filtri per valore rispetto ai numeri aggregati, utilizzare filtri primi 10 per classificare in base a un campo valore, oppure nascondere e rendere visibili manualmente singoli elementi pivot tramite la proprietà `is_hidden`. Ogni strategia è esposta attraverso API dedicate sulle classi `PivotField` e `PivotItem`.
{{% /alert %}}

## **Introduzione**
Le tabelle pivot sono potenti strumenti analitici, ma i riepiloghi grezzi spesso contengono molte più informazioni di quelle necessarie da presentare. Il filtraggio è il meccanismo principale per restringere una tabella pivot alle righe, colonne o valori rilevanti per un report specifico. Aspose.Cells for Python via Java rispecchia le funzionalità di filtraggio disponibili in Microsoft Excel, esponendole a livello di codice in modo che la generazione dei report possa essere completamente automatizzata.
Le seguenti strategie di filtraggio sono trattate in questo articolo:
1. **Filtro per etichetta** — filtra gli elementi dei campi di riga o colonna in base alle loro etichette di testo.
2. **Filtro per data** — filtra i campi di riga o colonna che contengono solo valori data-ora (o vuoti).
3. **Filtro per valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro primi 10** — mostra solo i primi o gli ultimi N elementi classificati in base a un campo valore.
5. **Nascondere / Rendere visibile gli elementi pivot** — controlla manualmente la visibilità di ciascun singolo elemento in un campo.
Ogni approccio utilizza un metodo diverso sulla classe `PivotField` o una proprietà sulla classe `PivotItem`. Dopo aver applicato qualsiasi filtro, è necessario chiamare `refresh_data()` e `calculate_data()` sulla tabella pivot in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Filtro per etichetta**
Un filtro per etichetta consente di filtrare gli elementi di un campo di riga o colonna confrontando le relative didascalie di testo con un modello. Questo è utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una lettera specifica, contengono una determinata parola o soddisfano un altro criterio basato sulla didascalia.
Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.filter_by_label(PivotFilterType, str)`. L'enumerazione `PivotFilterType` include valori come `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` e così via. Il secondo argomento fornisce la stringa dell'etichetta utilizzata per il confronto.
L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che solo gli elementi le cui didascalie iniziano con un prefisso specificato rimangano visibili, aggiorna la tabella pivot e salva il risultato.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
fileName = "sample.xlsx"
prefix = "B"
# Load the existing workbook containing a pivot table
workbook = Workbook(fileName)
# Access the worksheet by index (first worksheet)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Retrieve the first row PivotField
rowField = pivotTable.getRowFields().get(0)
# Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")
# Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh()
# Save the workbook back to disk
workbook.save(fileName)
jpype.shutdownJVM()
```

## **Filtro per data**
I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, settimana scorsa, questo mese, prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che funzionano solo con campi che memorizzano informazioni di data-ora.

{{% alert color="primary" %}}
Il filtro per data funziona solo quando l'area di riga o colonna contiene solo celle di tipo data-ora o valori vuoti. Se il campo sottostante contiene altri tipi di dati come numeri o testo, il filtro per data non produrrà il risultato atteso. Assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze valide di `DateTime` o celle vuote prima di applicare questo filtro.
Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.filter_by_date(PivotFilterType, values)`. L'enumerazione `PivotFilterType` contiene valori dedicati alle date come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro scelto, si passano uno o due valori `DateTime` (per `Between`, si passano le date di inizio e fine).
L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un determinato intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.
{{% /alert %}}

```python
import jpype
import os
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"
if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")
# Load the existing workbook that contains the pivot table
workbook = Workbook(inputPath)
# Access the worksheet that holds the pivot table (by index)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Retrieve the date PivotField from the row area
# (Date filter only works when the row/column area contains only date-time cells or blanks)
dateField = pivotTable.getRowFields().get(0)
# Define the date criterion for the Between filter
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)
# Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate)
# Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh()
# Persist the workbook
workbook.save(outputPath)
jpype.shutdownJVM()
```

## **Filtro per valore**
I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella sua area dati. Invece di confrontare etichette di testo, confrontano totali numerici con una soglia. Casi d'uso tipici includono la visualizzazione solo dei prodotti la cui somma delle vendite supera un importo target o solo delle regioni il cui conteggio delle transazioni rientra in un intervallo.
Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.filter_by_value(value_field, filter_type, values)`. Il parametro `filter_type` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. Il parametro `value_field` specifica quale campo dati deve essere valutato e gli argomenti finali forniscono i valori di soglia.
L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)
rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)
# Find the data field index manually since PivotFieldCollection doesn't have IndexOf
dataFieldIndex = -1
for i in range(pivotTable.getDataFields().getCount()):
    if pivotTable.getDataFields().get(i) == dataField:
        dataFieldIndex = i
        break
if dataFieldIndex >= 0:
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))
pivotTable.getPivotCache().refresh()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Filtro primi 10**
Il filtro primi 10 è una forma specializzata di filtro per valore che mantiene solo gli N elementi più alti o più bassi in base a un campo valore scelto. È comunemente utilizzato per i report di classificazione come "i primi 10 prodotti per fatturato" o "le ultime 5 regioni per numero di vendite".

{{% alert color="primary" %}}
Il filtro primi 10 è efficace solo quando la tabella pivot dispone di uno o più campi pivot di valore nell'area dati. Senza almeno un campo valore, non esiste una misura aggregata rispetto a cui classificare gli elementi e il filtro non può essere applicato.
Aspose.Cells espone il filtro Top 10 tramite il metodo `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)`. Il parametro `valueFieldIndex` è l'indice del campo dati i cui valori aggregati ordinano gli elementi, `filterType` seleziona l'unità di `itemCount` (`PivotFilterType.COUNT` mantiene un numero fisso di elementi, `PivotFilterType.PERCENT` mantiene una percentuale di elementi, quindi `itemCount` è la percentuale stessa), `isTop` indica se mantenere gli elementi in alto (true) o in basso (false), e `itemCount` definisce quanti elementi, o quale percentuale, mantenere.
L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo valore, applica un filtro primi 10 per mantenere solo i 10 elementi più alti in base alla somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType
# Load the existing workbook that contains the pivot table
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)
# Access the worksheet that holds the pivot table (index 0)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Confirm there is at least one value PivotField in the data area
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)
# Retrieve the target row PivotField (the field we want to apply Top 10 on)
rowField = pivotTable.getRowFields().get(0)
# The first (and only) data field is at index 0; Top 10 ranks by it.
valueFieldIndex = 0
# Apply the Top 10 filter on the row field:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.SUM
#   - isTop       = true (top N; false would mean bottom N)
#   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, True, 10)
# Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh()
# Save the workbook
workbook.save(outputPath)
jpype.shutdownJVM()
```

## **Filtrare nascondendo o rendendo visibili gli elementi pivot**
Oltre alle API di filtraggio strutturate, Aspose.Cells consente di controllare direttamente la visibilità di ciascun singolo elemento pivot. Iterando attraverso la raccolta `PivotItems` di un `PivotField` e attivando la proprietà `is_hidden`, è possibile sopprimere selettivamente elementi specifici senza applicare un filtro basato su formula. Impostando `is_hidden = True` si nasconde l'elemento dalla tabella pivot; impostando `is_hidden = False` lo si rende nuovamente visibile.
Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per l'elemento, come nascondere un piccolo numero di categorie denominate che non devono apparire in un determinato report. L'esempio seguente carica una tabella pivot, nasconde un elemento specifico per nome, dimostra come renderlo nuovamente visibile, aggiorna la tabella pivot e salva la cartella di lavoro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem
# Load an existing workbook containing a pivot table
workbook = Workbook("pivot_table_sample.xlsx")
# Access the first worksheet which contains the pivot table
sheet = workbook.getWorksheets().get(0)
# Access the pivot table by index (the first pivot table on the sheet)
pivotTable = sheet.getPivotTables().get(0)
# Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
pivotField = pivotTable.getRowFields().get(0)
# Iterate through the PivotItems collection of the selected PivotField
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)
    # Hide pivot items that match a specific name/criterion
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setHidden(True)
    # Demonstrate unhiding: re-show a previously hidden pivot item
    if item.getName() == "Item3":
        item.setHidden(False)
# Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh()
# Save the workbook — hidden items stay in the underlying data
# but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx")
jpype.shutdownJVM()
```

## **Riepilogo**
Aspose.Cells for Python via Java fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle presenti in Microsoft Excel. I filtri per etichetta, data e valore coprono gli scenari analitici più comuni, mentre il filtro primi 10 gestisce i report di classificazione. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.is_hidden` offre un fallback flessibile a livello di elemento. Combinando queste strategie, ad esempio applicando un filtro per etichetta e poi nascondendo elementi specifici, è possibile creare report di tabelle pivot mirati interamente tramite codice.

{{< app/cells/assistant language="python" >}}