---
title: Filtraggio delle Tabelle Pivot per Etichetta o Valore
description: Aspose.Cells for .NET offre funzionalità complete di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati di una tabella pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri primi 10 e nascondendo o mostrando elementi pivot.
linktitle: Filtraggio per Etichetta o Valore
keywords: Aspose.Cells, libreria .NET, foglio elettronico, tabella pivot, filtro, filtro per etichetta, filtro per valore, filtro per data, filtro primi 10, elemento pivot, nascondere elemento pivot
type: docs
weight: 10
url: /it/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot. È possibile applicare filtri per etichetta ai campi di riga o colonna basati su testo, utilizzare filtri per data quando il campo contiene solo celle di tipo data-ora o vuote, applicare filtri per valore rispetto ai numeri aggregati, utilizzare filtri primi 10 per classificare in base a un campo valore, oppure nascondere e mostrare manualmente singoli elementi pivot tramite la proprietà `IsHidden`. Ogni strategia è esposta tramite API dedicate sulle classi `PivotField` e `PivotItem`.
{{% /alert %}}

## **Introduzione**
Le tabelle pivot sono potenti strumenti analitici, ma i riepiloghi grezzi spesso contengono molte più informazioni di quelle che è necessario presentare. Il filtraggio è il meccanismo principale per restringere una tabella pivot alle righe, alle colonne o ai valori che contano per un report specifico. Aspose.Cells for .NET rispecchia le funzionalità di filtraggio disponibili in Microsoft Excel, esponendole a livello di codice in modo che la generazione di report possa essere completamente automatizzata.
In questo articolo vengono illustrate le seguenti strategie di filtraggio:
1. **Filtro per etichetta** — filtra gli elementi dei campi di riga o colonna in base alle loro etichette di testo.
2. **Filtro per data** — filtra i campi di riga o colonna che contengono solo valori di tipo data-ora (o vuoti).
3. **Filtro per valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro primi 10** — mostra solo i primi o gli ultimi N elementi classificati in base a un campo valore.
5. **Nascondi / Mostra elementi pivot** — controlla manualmente la visibilità di ogni singolo elemento in un campo.
Ogni approccio utilizza un metodo diverso sulla classe `PivotField` o una proprietà sulla classe `PivotItem`. Dopo aver applicato qualsiasi filtro, è necessario chiamare `PivotCache.Refresh()` sulla tabella pivot in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Filtro per etichetta**
Un filtro per etichetta consente di filtrare gli elementi di un campo di riga o colonna confrontando le relative didascalie di testo con un modello. Questo è utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una lettera specifica, contengono una determinata parola o soddisfano qualche altro criterio basato sulle didascalie.
Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)`. L'argomento `filterType` seleziona la modalità di confronto (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` e così via). Gli argomenti `label1` e `label2` forniscono il testo di confronto — passare `string.Empty` per `label2` quando è necessaria solo una corrispondenza a valore singolo (ad esempio inizia con o contiene).
L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che solo gli elementi le cui didascalie iniziano con un prefisso specificato rimangano visibili, aggiorna la tabella pivot e salva il risultato.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string fileName = "sample.xlsx";
string prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.Worksheets[0];
// Access the pivot table by index
PivotTable pivotTable = worksheet.PivotTables[0];
// Retrieve the first row PivotField
PivotField rowField = pivotTable.RowFields[0];
// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.PivotCache.Refresh();
// Save the workbook back to disk
workbook.Save(fileName);
```

## **Filtro per data**
I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, la settimana scorsa, questo mese, il prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che funzionano solo con i campi che memorizzano informazioni di tipo data-ora.

{{% alert color="primary" %}}
Il filtro per data funziona solo quando l'area di riga o colonna contiene esclusivamente celle di tipo data-ora o valori vuoti. Se il campo sottostante contiene altri tipi di dati come numeri o testo, il filtro per data non produrrà il risultato atteso. Assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze valide di `DateTime` o celle vuote prima di applicare questo filtro.
Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)`. L'enumerazione `PivotFilterType` contiene valori di data dedicati come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro scelto, è necessario passare uno o due valori `DateTime` (per `Between`, si passano le date di inizio e fine).
L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un determinato intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string inputPath = "sample.xlsx";
string outputPath = "output_filtered.xlsx";
if (!File.Exists(inputPath))
{
    throw new FileNotFoundException("Source workbook not found.", inputPath);
}
// Load the existing workbook that contains the pivot table
var workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.Worksheets[0];
// Access the pivot table by index
var pivotTable = worksheet.PivotTables[0];
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.RowFields[0];
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.PivotCache.Refresh();
// Persist the workbook
workbook.Save(outputPath);
```

## **Filtro per valore**
I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella sua area dati. Invece di confrontare etichette di testo, confrontano i totali numerici rispetto a una soglia. Casi d'uso tipici includono la visualizzazione solo dei prodotti la cui somma delle vendite supera un importo target o solo delle regioni il cui conteggio delle transazioni rientra in un intervallo.
Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Il parametro `valueFieldIndex` specifica quale campo dati deve essere valutato (utilizzare `pivotTable.DataFields.IndexOf(dataField)` o iterare la raccolta per trovare la posizione). Il parametro `filterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. I due argomenti `double` forniscono il valore o i valori di soglia.
L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];
var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.DataFields.Count; i++)
{
    if (pivotTable.DataFields[i] == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.FilterByValue(dataFieldIndex, PivotFilterType.ValueGreaterThan, 5000, double.MaxValue);
}
pivotTable.PivotCache.Refresh();
workbook.Save("output.xlsx");
```

## **Filtro primi 10**
Il filtro primi 10 è una forma specializzata di filtro per valore che mantiene solo gli N elementi più alti o più bassi in base a un campo valore scelto. È comunemente utilizzato per i report di classificazione come "primi 10 prodotti per fatturato" o "ultime 5 regioni per numero di vendite".

{{% alert color="primary" %}}
Il filtro primi 10 è efficace solo quando la tabella pivot dispone di uno o più campi pivot di valore nell'area dati. Senza almeno un campo valore, non c'è alcuna misura aggregata rispetto a cui classificare gli elementi e il filtro non può essere applicato.
Aspose.Cells espone il filtro Top 10 tramite il metodo `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. Il parametro `valueFieldIndex` è l'indice del campo dati i cui valori aggregati ordinano gli elementi, `filterType` seleziona l'unità di `itemCount` (`Count` mantiene un numero fisso di elementi, `Percent` mantiene una percentuale di elementi, quindi `itemCount` è la percentuale stessa), `isTop` indica se mantenere gli elementi in alto (true) o in basso (false), e `itemCount` definisce quanti elementi, o quale percentuale, mantenere.
L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo valore, applica un filtro primi 10 per mantenere solo i 10 elementi più alti per somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load the existing workbook that contains the pivot table
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.Worksheets[0];
// Access the pivot table by index
PivotTable pivotTable = worksheet.PivotTables[0];
// Confirm there is at least one value PivotField in the data area
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.RowFields[0];
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - valueFieldIndex = 0 — the data field used to rank items
//   - filterType  = PivotFilterType.Count (keep a fixed number of items;
//     PivotFilterType.Percent would interpret 10 as "top 10 percent")
//   - isTop       = true (top N; false would mean bottom N)
//   - itemCount   = 10
rowField.FilterTop10(valueFieldIndex, PivotFilterType.Count, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.PivotCache.Refresh();
// Save the workbook
workbook.Save(outputPath);
```

## **Filtro tramite nascondere o mostrare elementi pivot**
Oltre alle API di filtraggio strutturate, Aspose.Cells consente di controllare direttamente la visibilità di ogni singolo elemento pivot. Iterando la raccolta `PivotItems` di un `PivotField` e attivando/disattivando la proprietà `IsHidden`, è possibile eliminare selettivamente elementi specifici senza applicare un filtro basato su formula. Impostando `IsHidden = true` l'elemento viene nascosto dalla tabella pivot; impostando `IsHidden = false` viene mostrato nuovamente e reso visibile.
Questo approccio è utile quando la regola di filtraggio è irregolare o specifica dell'elemento, come ad esempio nascondere un piccolo numero di categorie denominate che non devono apparire in un determinato report. L'esempio seguente carica una tabella pivot, nasconde un elemento specifico per nome, mostra come mostrarlo nuovamente, aggiorna la tabella pivot e salva la cartella di lavoro.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.Worksheets[0];
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.PivotTables[0];
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.RowFields[0];
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];
    // Hide pivot items that match a specific name/criterion
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.PivotCache.Refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.Save("output_pivot_filtered.xlsx");
```

## **Riepilogo**
Aspose.Cells for .NET fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle presenti in Microsoft Excel. I filtri per etichetta, per data e per valore coprono gli scenari analitici più comuni, mentre il filtro primi 10 gestisce i report di classificazione. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.IsHidden` offre un fallback flessibile a livello di elemento. Combinare queste strategie — ad esempio applicando un filtro per etichetta e poi nascondendo elementi specifici — consente di creare report di tabelle pivot precisamente mirati interamente da codice.

## Articoli correlati
- [Aggiungere campi di riga e colonna alla tabella pivot in Aspose.Cells for .NET](/cells/it/net/pivot-table-add-row-and-column-fields/)
- [Gestire i campi valore della tabella pivot in Aspose.Cells for .NET](/cells/it/net/manage-value-fields/)
- [Aggiornare tabelle pivot e cache pivot in Aspose.Cells for .NET](/cells/it/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}