---
title: Filtrare le tabelle pivot per etichetta o valore
description: Aspose.Cells for Python via .NET supporta funzionalità complete di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati di una tabella pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri primi 10 e nascondendo o mostrando gli elementi pivot.
linktitle: Filtrare le tabelle pivot per etichetta o valore
keywords: Aspose.Cells, Python via .NET libreria, foglio di calcolo, tabella pivot, filtro, filtro per etichetta, filtro per valore, filtro per data, filtro primi 10, elemento pivot, nascondere elemento pivot
type: docs
weight: 10
url: /it/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot. È possibile applicare filtri per etichetta ai campi di riga o colonna basati su testo, utilizzare filtri per data quando il campo contiene solo celle di tipo data-ora o vuote, applicare filtri per valore rispetto ai numeri aggregati, utilizzare filtri primi 10 per classificare in base a un campo valore, oppure nascondere e mostrare manualmente i singoli elementi pivot utilizzando la proprietà `is_hidden`. Ogni strategia è esposta tramite API dedicate sulle classi `PivotField` e `PivotItem`.
{{% /alert %}}

## **Introduzione**
Le tabelle pivot sono potenti strumenti analitici, ma i riepiloghi grezzi spesso contengono molte più informazioni di quelle che è necessario presentare. Il filtraggio è il meccanismo principale per ridurre una tabella pivot alle righe, colonne o valori rilevanti per un report specifico. Aspose.Cells for Python via .NET rispecchia le funzionalità di filtraggio disponibili in Microsoft Excel, esponendole a livello di codice in modo che la generazione dei report possa essere completamente automatizzata.
Le seguenti strategie di filtraggio sono trattate in questo articolo:
1. **Filtro per etichetta** — filtra gli elementi di un campo di riga o colonna in base alle etichette di testo.
2. **Filtro per data** — filtra i campi di riga o colonna che contengono solo valori di data-ora (o vuoti).
3. **Filtro per valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro primi 10** — mostra solo i primi o gli ultimi N elementi classificati in base a un campo valore.
5. **Nascondere/Mostrare elementi pivot** — controlla manualmente la visibilità di ciascun singolo elemento in un campo.
Ogni approccio utilizza un metodo diverso sulla classe `PivotField` o una proprietà sulla classe `PivotItem`. Dopo aver applicato qualsiasi filtro, è necessario chiamare `refresh_data()` e `calculate_data()` sulla tabella pivot in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Filtro per etichetta**
Un filtro per etichetta consente di filtrare gli elementi di un campo di riga o colonna confrontando le relative didascalie di testo con un modello. Ciò è utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una lettera specifica, contengono una determinata parola o soddisfano altri criteri basati sulla didascalia.
Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.filter_by_label(PivotFilterType, label_string)`. L'enumerazione `PivotFilterType` include valori come `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` e così via. Il secondo argomento fornisce la stringa di etichetta utilizzata per il confronto.
L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che rimangano visibili solo gli elementi le cui didascalie iniziano con un prefisso specificato, aggiorna la tabella pivot e salva il risultato.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFilterType
fileName = "sample.xlsx"
prefix = "B"
# Load the existing workbook containing a pivot table
workbook = ac.Workbook(fileName)
# Access the worksheet by index (first worksheet)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivot_table = worksheet.pivot_tables[0]
# Retrieve the first row PivotField
row_field = pivot_table.row_fields[0]
# Apply the label filter — show only row items whose labels begin with the supplied prefix
row_field.filter_by_label(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")
# Refresh and recalculate the pivot table data so the filter takes effect
pivot_table.pivot_cache.refresh()
# Save the workbook back to disk
workbook.save(fileName)
```

## **Filtro per data**
I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, la settimana scorsa, questo mese, il prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che funzionano solo sui campi che memorizzano informazioni di data-ora.

{{% alert color="primary" %}}
Il filtro per data funziona solo quando l'area di riga o colonna contiene esclusivamente celle di tipo data-ora o valori vuoti. Se il campo sottostante contiene altri tipi di dati come numeri o testo, il filtro per data non produrrà il risultato atteso. Assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze valide di `datetime` oppure celle vuote prima di applicare questo filtro.
Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.filter_by_date(PivotFilterType, *date_times)`. L'enumerazione `PivotFilterType` contiene valori dedicati alle date come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro scelto, si passano uno o due valori `datetime` (per `Between`, si passano la data di inizio e la data di fine).
L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un determinato intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.
{{% /alert %}}

```python
import os
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotFilterType
input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"
if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)
# Load the existing workbook that contains the pivot table
workbook = ac.Workbook(input_path)
# Access the worksheet that holds the pivot table (by index)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivot_table = worksheet.pivot_tables[0]
# Retrieve the date PivotField from the row area
# (Date filter only works when the row/column area contains only date-time cells or blanks)
date_field = pivot_table.row_fields[0]
# Define the date criterion for the Between filter
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)
# Apply the date filter on the pivot field
date_field.filter_by_date(PivotFilterType.DATE_BETWEEN, start_date, end_date)
# Refresh and recalculate the pivot table so the filter takes effect
pivot_table.pivot_cache.refresh()
# Persist the workbook
workbook.save(output_path)
```

## **Filtro per valore**
I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella propria area dati. Invece di confrontare le etichette di testo, confrontano i totali numerici rispetto a una soglia. Casi d'uso tipici includono la visualizzazione solo dei prodotti la cui somma delle vendite supera un importo target oppure solo delle regioni il cui conteggio delle transazioni rientra in un intervallo.
Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)`. Il parametro `PivotFilterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. Il parametro `value_field` specifica quale campo dati deve essere valutato, mentre gli argomenti finali forniscono il valore o i valori di soglia.
L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFilterType
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]
row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]
# Find the data field index manually since PivotFieldCollection doesn't have IndexOf
data_field_index = -1
for i in range(len(pivot_table.data_fields)):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break
if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, PivotFilterType.VALUE_GREATER_THAN, 5000.0, float('inf'))
pivot_table.pivot_cache.refresh()
workbook.save("output.xlsx")
```

## **Filtro primi 10**
Il filtro primi 10 è una forma specializzata di filtro per valore che mantiene solo i primi o gli ultimi N elementi in base a un campo valore scelto. È comunemente utilizzato per i report di classificazione come "i 10 prodotti principali per ricavi" o "le 5 regioni con il minor numero di vendite".

{{% alert color="primary" %}}
Il filtro primi 10 è efficace solo quando la tabella pivot dispone di uno o più campi pivot di valore nell'area dati. Senza almeno un campo valore, non esiste alcuna misura aggregata rispetto alla quale classificare gli elementi e il filtro non può essere applicato.
Aspose.Cells espone il filtro Top 10 tramite il metodo `PivotField.filter_top10(value_field_index, filter_type, is_top, item_count)`. Il parametro `value_field_index` è l'indice del campo dati i cui valori aggregati ordinano gli elementi, `filter_type` seleziona l'unità di `item_count` (`PivotFilterType.COUNT` mantiene un numero fisso di elementi, `PivotFilterType.PERCENT` mantiene una percentuale di elementi, quindi `item_count` è la percentuale stessa), `is_top` indica se mantenere gli elementi in alto (True) o in basso (False), e `item_count` definisce quanti elementi, o quale percentuale, mantenere.
L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo valore, applica un filtro primi 10 per mantenere solo i 10 elementi più alti per la somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.
{{% /alert %}}

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
# Load the existing workbook that contains the pivot table
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)
# Access the worksheet that holds the pivot table (index 0)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivotTable = worksheet.pivot_tables[0]
# Confirm there is at least one value PivotField in the data area
if len(pivotTable.data_fields) == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]
# Retrieve the target row PivotField (the field we want to apply Top 10 on)
rowField = pivotTable.row_fields[0]
# The first (and only) data field is at index 0; Top 10 ranks by it.
valueFieldIndex = 0
# Apply the Top 10 filter on the row field:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.SUM
#   - isTop       = true (top N; false would mean bottom N)
#   - valueFieldIndex = the index of the data field used to rank items
rowField.filter_top10(valueFieldIndex, acp.PivotFilterType.COUNT, True, 10)
# Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.pivot_cache.refresh()
# Save the workbook
workbook.save(outputPath)
```

## **Filtrare nascondendo o mostrando gli elementi pivot**
Oltre alle API strutturate di filtraggio, Aspose.Cells consente di controllare direttamente la visibilità di ciascun singolo elemento pivot. Iterando attraverso la raccolta `PivotItems` di un `PivotField` e attivando/disattivando la proprietà `is_hidden`, è possibile sopprimere selettivamente elementi specifici senza applicare un filtro basato su formule. Impostando `is_hidden = True` l'elemento viene nascosto dalla tabella pivot; impostando `is_hidden = False` viene mostrato di nuovo e reso visibile.
Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per gli elementi, ad esempio per nascondere un piccolo numero di categorie denominate che non devono apparire in un determinato report. L'esempio seguente carica una tabella pivot, nasconde un elemento specifico per nome, mostra come ripristinarne la visibilità, aggiorna la tabella pivot e salva la cartella di lavoro.

```python
import aspose.cells as ac
# Load an existing workbook containing a pivot table
workbook = ac.Workbook("pivot_table_sample.xlsx")
# Access the first worksheet which contains the pivot table
sheet = workbook.worksheets[0]
# Access the pivot table by index (the first pivot table on the sheet)
pivot_table = sheet.pivot_tables[0]
# Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
pivot_field = pivot_table.row_fields[0]
# Iterate through the PivotItems collection of the selected PivotField
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]
    # Hide pivot items that match a specific name/criterion
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True
    # Demonstrate unhiding: re-show a previously hidden pivot item
    if item.name == "Item3":
        item.is_hidden = False
# Refresh and recalculate the pivot table so changes take effect
pivot_table.pivot_cache.refresh()
# Save the workbook — hidden items stay in the underlying data
# but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx")
```

## **Riepilogo**
Aspose.Cells for Python via .NET fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle disponibili in Microsoft Excel. I filtri per etichetta, data e valore coprono gli scenari analitici più comuni, mentre il filtro primi 10 gestisce i report di classificazione. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.is_hidden` offre un fallback flessibile a livello di elemento. Combinando queste strategie — ad esempio, applicando un filtro per etichetta e quindi nascondendo elementi specifici — è possibile creare report di tabelle pivot precisamente mirati interamente tramite codice.

{{< app/cells/assistant language="python-net" >}}