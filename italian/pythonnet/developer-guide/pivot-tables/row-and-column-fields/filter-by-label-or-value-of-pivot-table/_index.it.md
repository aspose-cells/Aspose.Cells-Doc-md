---
title: Filtrare le tabelle pivot per etichetta o valore
linktitle: Filtrare le tabelle pivot per etichetta o valore
description: Aspose.Cells for Python via .NET supporta funzionalità complete di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati di una tabella pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri primi 10 e nascondendo o mostrando gli elementi pivot.
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

fileName = "sample.xlsx"
prefix = "B"

# Carica la cartella di lavoro esistente contenente una tabella pivot
workbook = ac.Workbook(fileName)

# Accedi al foglio di lavoro tramite indice (primo foglio di lavoro)
worksheet = workbook.worksheets[0]

# Accedi alla tabella pivot tramite indice
pivot_table = worksheet.pivot_tables[0]

# Recupera il primo PivotField di riga
row_field = pivot_table.row_fields[0]

# Applica il filtro sulle etichette — mostra solo gli elementi di riga le cui etichette iniziano con il prefisso fornito
row_field.filter_by_label(ac.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")

# Aggiorna e ricalcola i dati della tabella pivot in modo che il filtro abbia effetto
pivot_table.pivot_cache.refresh()

# Salva la cartella di lavoro su disco
workbook.save(fileName)
```
## **Filtro per data**
I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, la settimana scorsa, questo mese, il prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che funzionano solo sui campi che memorizzano informazioni di data-ora.
{{% alert color="primary" %}}
Il filtro per data funziona solo quando l'area di riga o colonna contiene esclusivamente celle di tipo data-ora o valori vuoti. Se il campo sottostante contiene altri tipi di dati come numeri o testo, il filtro per data non produrrà il risultato atteso. Assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze valide di `DateTime` oppure celle vuote prima di applicare questo filtro.
{{% /alert %}}
Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.filter_by_date(PivotFilterType, *date_times)`. L'enumerazione `PivotFilterType` contiene valori dedicati alle date come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro scelto, si passano uno o due valori `DateTime` (per `Between`, si passano la data di inizio e la data di fine).
L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un determinato intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.
```python
from datetime import datetime

input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"

if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)

# Carica la cartella di lavoro esistente che contiene la tabella pivot
workbook = ac.Workbook(input_path)

# Accedi al foglio di lavoro che contiene la tabella pivot (per indice)
worksheet = workbook.worksheets[0]

# Accedi alla tabella pivot per indice
pivot_table = worksheet.pivot_tables[0]

# Recupera il PivotField della data dall'area delle righe
# (Il filtro per data funziona solo quando l'area di riga/colonna contiene solo celle data-ora o vuote)
date_field = pivot_table.row_fields[0]

# Definisci il criterio di data per il filtro Between (Tra)
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

# Applica il filtro per data sul campo pivot
date_field.filter_by_date(ac.PivotFilterType.DATE_BETWEEN, start_date, end_date)

# Aggiorna e ricalcola la tabella pivot affinché il filtro abbia effetto
pivot_table.pivot_cache.refresh()

# Salva la cartella di lavoro
workbook.save(output_path)
```
## **Filtro per valore**
I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella propria area dati. Invece di confrontare le etichette di testo, confrontano i totali numerici rispetto a una soglia. Casi d'uso tipici includono la visualizzazione solo dei prodotti la cui somma delle vendite supera un importo target oppure solo delle regioni il cui conteggio delle transazioni rientra in un intervallo.
Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)`. Il parametro `PivotFilterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. Il parametro `value_field` specifica quale campo dati deve essere valutato, mentre gli argomenti finali forniscono il valore o i valori di soglia.
L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.
```python
import aspose.cells as ac

workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]

row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]

# Trova l'indice del campo dati manualmente poiché PivotFieldCollection non ha IndexOf
data_field_index = -1
for i in range(pivot_table.data_fields.count):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break

if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, ac.PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivot_table.pivot_cache.refresh()

workbook.save("output.xlsx")
```
## **Filtro primi 10**
Il filtro primi 10 è una forma specializzata di filtro per valore che mantiene solo i primi o gli ultimi N elementi in base a un campo valore scelto. È comunemente utilizzato per i report di classificazione come "i 10 prodotti principali per ricavi" o "le 5 regioni con il minor numero di vendite".
{{% alert color="primary" %}}
Il filtro primi 10 è efficace solo quando la tabella pivot dispone di uno o più campi pivot di valore nell'area dati. Senza almeno un campo valore, non esiste alcuna misura aggregata rispetto alla quale classificare gli elementi e il filtro non può essere applicato.
{{% /alert %}}
Aspose.Cells espone il filtraggio primi 10 tramite il metodo `PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)`. Il parametro `item_count` definisce quanti elementi mantenere, `is_top` indica se mantenere gli elementi superiori (True) o inferiori (False), `value_field` fa riferimento al campo dati utilizzato per la classificazione e `PivotFilterType` controlla come viene calcolato il valore (in genere `Sum`, ma anche `Count` e `Percent`).
L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo valore, applica un filtro primi 10 per mantenere solo i 10 elementi più alti per la somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.
```python
import aspose.cells as ac
import aspose.cells.pivot as acp

# Carica il workbook esistente che contiene la tabella pivot
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)

# Accedi al foglio di lavoro che contiene la tabella pivot (indice 0)
worksheet = workbook.worksheets[0]

# Accedi alla tabella pivot tramite indice
pivotTable = worksheet.pivot_tables[0]

# Verifica che ci sia almeno un PivotField di valori nell'area dati
if pivotTable.data_fields.count == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]

# Ottieni il PivotField di riga target (il campo su cui vogliamo applicare il filtro Top 10)
rowField = pivotTable.row_fields[0]

# Il primo (e unico) campo dati è all'indice 0; il filtro Top 10 classifica in base ad esso.
valueFieldIndex = 0

# Applica il filtro Top 10 sul campo di riga:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (top N; false significherebbe bottom N)
#   - valueFieldIndex = l'indice del campo dati utilizzato per classificare gli elementi
rowField.filter_top10(10, acp.PivotFilterType.Sum, True, valueFieldIndex)

# Aggiorna i dati della tabella pivot e ricalcolala affinché il filtro abbia effetto
pivotTable.pivot_cache.refresh()

# Salva il workbook
workbook.save(outputPath)
```
## **Filtrare nascondendo o mostrando gli elementi pivot**
Oltre alle API strutturate di filtraggio, Aspose.Cells consente di controllare direttamente la visibilità di ciascun singolo elemento pivot. Iterando attraverso la raccolta `PivotItems` di un `PivotField` e attivando/disattivando la proprietà `is_hidden`, è possibile sopprimere selettivamente elementi specifici senza applicare un filtro basato su formule. Impostando `is_hidden = True` l'elemento viene nascosto dalla tabella pivot; impostando `is_hidden = False` viene mostrato di nuovo e reso visibile.
Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per gli elementi, ad esempio per nascondere un piccolo numero di categorie denominate che non devono apparire in un determinato report. L'esempio seguente carica una tabella pivot, nasconde un elemento specifico per nome, mostra come ripristinarne la visibilità, aggiorna la tabella pivot e salva la cartella di lavoro.
```python
import aspose.cells as ac

# Carica una cartella di lavoro esistente contenente una tabella pivot
workbook = ac.Workbook("pivot_table_sample.xlsx")

# Accedi al primo foglio di lavoro che contiene la tabella pivot
sheet = workbook.worksheets[0]

# Accedi alla tabella pivot tramite indice (la prima tabella pivot nel foglio)
pivot_table = sheet.pivot_tables[0]

# Recupera il PivotField di destinazione (il primo campo etichetta di riga in cui nasconderemo/mostreremo gli elementi)
pivot_field = pivot_table.row_fields[0]

# Itera attraverso la collezione PivotItems del PivotField selezionato
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]

    # Nascondi gli elementi pivot che corrispondono a un nome/criterio specifico
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True

    # Dimostra come mostrare nuovamente un elemento pivot precedentemente nascosto
    if item.name == "Item3":
        item.is_hidden = False

# Aggiorna e ricalcola la tabella pivot affinché le modifiche abbiano effetto
pivot_table.pivot_cache.refresh()

# Salva la cartella di lavoro — gli elementi nascosti rimangono nei dati sottostanti
# ma sono esclusi dall'output della tabella pivot visualizzata
workbook.save("output_pivot_filtered.xlsx")
```
## **Riepilogo**
Aspose.Cells for Python via .NET fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle disponibili in Microsoft Excel. I filtri per etichetta, data e valore coprono gli scenari analitici più comuni, mentre il filtro primi 10 gestisce i report di classificazione. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.is_hidden` offre un fallback flessibile a livello di elemento. Combinando queste strategie — ad esempio, applicando un filtro per etichetta e quindi nascondendo elementi specifici — è possibile creare report di tabelle pivot precisamente mirati interamente tramite codice.
{{< app/cells/assistant language="python-net" >}}