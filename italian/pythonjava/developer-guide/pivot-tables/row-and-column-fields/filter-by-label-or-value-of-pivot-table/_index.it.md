---
title: Filtrare le tabelle pivot per etichetta o valore
linktitle: Filtrare le tabelle pivot per etichetta o valore
description: Aspose.Cells for Python via Java supporta funzionalità complete di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati di una tabella pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri primi 10 e nascondendo o rendendo visibili singoli elementi pivot.
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
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

fileName = "sample.xlsx"
prefix = "B"

# Carica la cartella di lavoro esistente contenente una tabella pivot
workbook = Workbook(fileName)

# Accedi al foglio di lavoro tramite indice (primo foglio di lavoro)
worksheet = workbook.getWorksheets().get(0)

# Accedi alla tabella pivot tramite indice
pivotTable = worksheet.getPivotTables().get(0)

# Recupera il primo PivotField di riga
rowField = pivotTable.getRowFields().get(0)

# Applica il filtro etichetta: mostra solo gli elementi di riga le cui etichette iniziano con il prefisso fornito
rowField.filterByLabel(PivotFilterType.CaptionBeginsWith, prefix, "")

# Aggiorna e ricalcola i dati della tabella pivot affinché il filtro abbia effetto
pivotTable.getPivotCache().refresh()

# Salva la cartella di lavoro su disco
workbook.save(fileName)

jpype.shutdownJVM()
```
## **Filtro per data**
I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, settimana scorsa, questo mese, prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che funzionano solo con campi che memorizzano informazioni di data-ora.
{{% alert color="primary" %}}
Il filtro per data funziona solo quando l'area di riga o colonna contiene solo celle di tipo data-ora o valori vuoti. Se il campo sottostante contiene altri tipi di dati come numeri o testo, il filtro per data non produrrà il risultato atteso. Assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze valide di `DateTime` o celle vuote prima di applicare questo filtro.
{{% /alert %}}
Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.filter_by_date(PivotFilterType, values)`. L'enumerazione `PivotFilterType` contiene valori dedicati alle date come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro scelto, si passano uno o due valori `DateTime` (per `Between`, si passano le date di inizio e fine).
L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un determinato intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"

if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")

# Carica la cartella di lavoro esistente che contiene la tabella pivot
workbook = Workbook(inputPath)

# Accedi al foglio di lavoro che contiene la tabella pivot (per indice)
worksheet = workbook.getWorksheets().get(0)

# Accedi alla tabella pivot per indice
pivotTable = worksheet.getPivotTables().get(0)

# Recupera il PivotField della data dall'area delle righe
# (Il filtro per data funziona solo quando l'area delle righe/colonne contiene solo celle data-ora o vuote)
dateField = pivotTable.getRowFields().get(0)

# Definisci il criterio di data per il filtro Between
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)

# Applica il filtro per data sul campo pivot
dateField.filterByDate(PivotFilterType.DateBetween, startDate, endDate)

# Aggiorna e ricalcola la tabella pivot affinché il filtro abbia effetto
pivotTable.getPivotCache().refresh()

# Salva la cartella di lavoro
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
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)

rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)

# Trova l'indice del campo dati manualmente poiché PivotFieldCollection non ha IndexOf
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
{{% /alert %}}
Aspose.Cells espone il filtraggio primi 10 tramite il metodo `PivotField.filter_top10(item_count, is_top, value_field, filter_type)`. Il parametro `item_count` definisce quanti elementi mantenere, `is_top` indica se mantenere gli elementi superiori (true) o inferiori (false), `value_field` fa riferimento al campo dati utilizzato per la classificazione e `filter_type` controlla come viene calcolato il valore (tipicamente `Sum`, ma anche `Count` e `Percent`).
L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo valore, applica un filtro primi 10 per mantenere solo i 10 elementi più alti in base alla somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType

# Carica la cartella di lavoro esistente che contiene la tabella pivot
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)

# Accedi al foglio di lavoro che contiene la tabella pivot (indice 0)
worksheet = workbook.getWorksheets().get(0)

# Accedi alla tabella pivot tramite indice
pivotTable = worksheet.getPivotTables().get(0)

# Conferma che ci sia almeno un PivotField di valore nell'area dati
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)

# Recupera il PivotField di riga di destinazione (il campo su cui vogliamo applicare Top 10)
rowField = pivotTable.getRowFields().get(0)

# Il primo (e unico) campo dati è all'indice 0; Top 10 classifica in base ad esso.
valueFieldIndex = 0

# Applica il filtro Top 10 sul campo riga:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (top N; false significherebbe bottom N)
#   - valueFieldIndex = l'indice del campo dati utilizzato per classificare gli elementi
rowField.filterTop10(10, PivotFilterType.Sum, True, valueFieldIndex)

# Aggiorna i dati della tabella pivot e ricalcolala in modo che il filtro abbia effetto
pivotTable.getPivotCache().refresh()

# Salva la cartella di lavoro
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
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem

# Carica una cartella di lavoro esistente contenente una tabella pivot
workbook = Workbook("pivot_table_sample.xlsx")

# Accedi al primo foglio di lavoro che contiene la tabella pivot
sheet = workbook.getWorksheets().get(0)

# Accedi alla tabella pivot tramite indice (la prima tabella pivot nel foglio)
pivotTable = sheet.getPivotTables().get(0)

# Recupera il PivotField di destinazione (il primo campo etichetta di riga in cui nasconderemo/mostreremo gli elementi)
pivotField = pivotTable.getRowFields().get(0)

# Itera attraverso la collezione di PivotItems del PivotField selezionato
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)

    # Nascondi gli elementi pivot che corrispondono a un nome/criterio specifico
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setIsHidden(True)

    # Dimostra come mostrare nuovamente un elemento pivot precedentemente nascosto
    if item.getName() == "Item3":
        item.setIsHidden(False)

# Aggiorna e ricalcola la tabella pivot affinché le modifiche abbiano effetto
pivotTable.getPivotCache().refresh()

# Salva la cartella di lavoro: gli elementi nascosti rimangono nei dati sottostanti
# ma vengono esclusi dall'output visualizzato della tabella pivot
workbook.save("output_pivot_filtered.xlsx")

jpype.shutdownJVM()
```
## **Riepilogo**
Aspose.Cells for Python via Java fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle presenti in Microsoft Excel. I filtri per etichetta, data e valore coprono gli scenari analitici più comuni, mentre il filtro primi 10 gestisce i report di classificazione. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.is_hidden` offre un fallback flessibile a livello di elemento. Combinando queste strategie, ad esempio applicando un filtro per etichetta e poi nascondendo elementi specifici, è possibile creare report di tabelle pivot mirati interamente tramite codice.
{{< app/cells/assistant language="python" >}}