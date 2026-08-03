---
title: Filtraggio delle tabelle pivot per etichetta o valore
linktitle: Filtraggio delle tabelle pivot per etichetta o valore
description: Aspose.Cells for .NET supporta funzionalità complete di filtraggio delle tabelle pivot, questo articolo spiega come filtrare i dati delle tabelle pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri dei primi 10 e nascondendo o mostrando gli elementi pivot.
keywords: Aspose.Cells, libreria .NET, foglio di calcolo, tabella pivot, filtro, filtro per etichetta, filtro per valore, filtro per data, filtro primi 10, elemento pivot, nascondere elemento pivot
type: docs
weight: 10
url: /it/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---



## **Introduzione**

Le tabelle pivot sono potenti strumenti analitici, ma i riepiloghi grezzi spesso contengono molte più informazioni di quelle necessarie per la presentazione. Il filtraggio è il meccanismo principale per restringere una tabella pivot alle righe, colonne o valori che contano per un report specifico. Aspose.Cells for .NET rispecchia le funzionalità di filtraggio disponibili in Microsoft Excel, esponendole a livello di codice in modo che la generazione dei report possa essere completamente automatizzata.

Le seguenti strategie di filtraggio sono trattate in questo articolo:

1. **Filtro per etichetta** — filtra gli elementi dei campi di riga o colonna in base alle loro etichette di testo.
2. **Filtro per data** — filtra i campi di riga o colonna che contengono solo valori data-ora (o vuoti).
3. **Filtro per valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro primi 10** — mostra solo i primi o gli ultimi N elementi classificati in base a un campo valore.
5. **Nascondi / Mostra elementi pivot** — controlla manualmente la visibilità di ciascun singolo elemento in un campo.

Ogni approccio utilizza un metodo diverso sulla classe `PivotField` o una proprietà sulla classe `PivotItem`. Dopo aver applicato qualsiasi filtro, è necessario chiamare `RefreshData()` e `CalculateData()` sulla tabella pivot in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Filtro per etichetta**

Un filtro per etichetta consente di filtrare gli elementi di un campo di riga o colonna confrontando le loro didascalie di testo con un criterio. Ciò è utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una lettera specifica, contengono una particolare parola o soddisfano un altro criterio basato sulla didascalia.

Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)`. L'enumerazione `PivotFilterType` include valori come `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` e così via. Il secondo argomento fornisce la stringa di etichetta utilizzata per il confronto.

L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che rimangano visibili solo gli elementi le cui didascalie iniziano con un prefisso specificato, aggiorna la tabella pivot e salva il risultato.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string fileName = "sample.xlsx";
string prefix = "B";

// Carica la cartella di lavoro esistente contenente una tabella pivot
Workbook workbook = new Workbook(fileName);

// Accedi al foglio di lavoro tramite indice (primo foglio di lavoro)
Worksheet worksheet = workbook.Worksheets[0];

// Accedi alla tabella pivot tramite indice
PivotTable pivotTable = worksheet.PivotTables[0];

// Recupera il primo PivotField di riga
PivotField rowField = pivotTable.RowFields[0];

// Applica il filtro delle etichette: mostra solo gli elementi di riga le cui etichette iniziano con il prefisso fornito
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);

// Aggiorna e ricalcola i dati della tabella pivot in modo che il filtro abbia effetto
pivotTable.PivotCache.Refresh();

// Salva la cartella di lavoro sul disco
workbook.Save(fileName);
```

## **Filtro per data**

I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, la settimana scorsa, questo mese, il prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che funzionano solo sui campi che memorizzano informazioni di data e ora.

{{% alert color="primary" %}}

Il filtro per data funziona solo quando l'area di riga o colonna contiene solo celle data-ora o valori vuoti. Se il campo sottostante contiene altri tipi di dati come numeri o testo, il filtro per data non produrrà il risultato atteso. Assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze `DateTime` valide o celle vuote prima di applicare questo filtro.

{{% /alert %}}

Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)`. L'enumerazione `PivotFilterType` contiene valori dedicati per le date come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro scelto, si passano uno o due valori `DateTime` (per `Between`, si passano le date di inizio e fine).

L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un determinato intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.

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

// Carica la cartella di lavoro esistente che contiene la tabella pivot
var workbook = new Workbook(inputPath);

// Accedi al foglio di lavoro che contiene la tabella pivot (per indice)
var worksheet = workbook.Worksheets[0];

// Accedi alla tabella pivot per indice
var pivotTable = worksheet.PivotTables[0];

// Recupera il PivotField della data dall'area delle righe
// (Il filtro per data funziona solo quando l'area di riga/colonna contiene solo celle di tipo data-ora o vuote)
PivotField dateField = pivotTable.RowFields[0];

// Definisci il criterio di data per il filtro Between
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// Applica il filtro per data sul campo pivot
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);

// Aggiorna e ricalcola la tabella pivot affinché il filtro abbia effetto
pivotTable.PivotCache.Refresh();

// Salva la cartella di lavoro
workbook.Save(outputPath);
```

## **Filtro per valore**

I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella sua area dati. Invece di confrontare etichette di testo, confrontano i totali numerici con una soglia. I casi d'uso tipici includono la visualizzazione solo dei prodotti la cui somma delle vendite supera un importo target o solo delle regioni il cui conteggio delle transazioni rientra in un intervallo.

Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Il parametro `filterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. Il parametro `valueField` specifica quale campo dati deve essere valutato, e gli argomenti finali forniscono il valore o i valori soglia.

L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];

var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];

// Trova l'indice del campo dati manualmente poiché PivotFieldCollection non ha IndexOf
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

Il filtro primi 10 è una forma specializzata di filtro per valore che mantiene solo i primi o gli ultimi N elementi in base a un campo valore scelto. È comunemente utilizzato per i report di classifica come "i 10 prodotti principali per ricavi" o "le 5 regioni peggiori per numero di vendite".

{{% alert color="primary" %}}

Il filtro primi 10 è efficace solo quando la tabella pivot ha uno o più campi pivot valore nell'area dati. Senza almeno un campo valore, non c'è alcuna misura aggregata rispetto a cui classificare gli elementi e il filtro non può essere applicato.

{{% /alert %}}

Aspose.Cells espone il filtraggio primi 10 tramite il metodo `PivotField.FilterTop10(int itemCount, PivotFilterType filterType, bool isTop, int valueFieldIndex)`. Il parametro `itemCount` definisce quanti elementi mantenere, `isTop` indica se mantenere gli elementi superiori (true) o inferiori (false), `valueField` fa riferimento al campo dati utilizzato per la classifica e `filterType` controlla come viene calcolato il valore (tipicamente `Sum`, ma anche `Count` e `Percent`).

L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo valore, applica un filtro primi 10 per mantenere solo i 10 elementi più alti per la somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Carica la cartella di lavoro esistente che contiene la tabella pivot
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// Accedi al foglio di lavoro che contiene la tabella pivot (indice 0)
Worksheet worksheet = workbook.Worksheets[0];

// Accedi alla tabella pivot tramite indice
PivotTable pivotTable = worksheet.PivotTables[0];

// Verifica che ci sia almeno un PivotField di valore nell'area dati
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];

// Recupera il PivotField riga di destinazione (il campo su cui applicare Top 10)
PivotField rowField = pivotTable.RowFields[0];

// Il primo (e unico) campo dati è all'indice 0; Top 10 classifica in base ad esso.
int valueFieldIndex = 0;

// Applica il filtro Top 10 sul campo riga:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N; false significherebbe bottom N)
//   - valueFieldIndex = l'indice del campo dati utilizzato per classificare gli elementi
rowField.FilterTop10(10, PivotFilterType.Sum, true, valueFieldIndex);

// Aggiorna i dati della tabella pivot e ricalcola affinché il filtro abbia effetto
pivotTable.PivotCache.Refresh();

// Salva la cartella di lavoro
workbook.Save(outputPath);
```

## **Filtro tramite nascondere o mostrare elementi pivot**

Oltre alle API strutturate di filtraggio, Aspose.Cells consente di controllare direttamente la visibilità di ciascun singolo elemento pivot. Iterando attraverso la raccolta `PivotItems` di un `PivotField` e attivando/disattivando la proprietà `IsHidden`, è possibile eliminare selettivamente elementi specifici senza applicare un filtro basato su formula. Impostando `IsHidden = true` si nasconde l'elemento dalla tabella pivot; impostando `IsHidden = false` lo si mostra nuovamente rendendolo visibile.

Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per un elemento, come nascondere un piccolo numero di categorie denominate che non devono apparire in un particolare report. L'esempio seguente carica una tabella pivot, nasconde un elemento specifico per nome, dimostra come mostrarlo nuovamente, aggiorna la tabella pivot e salva la cartella di lavoro.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Carica una cartella di lavoro esistente contenente una tabella pivot
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// Accedi al primo foglio di lavoro che contiene la tabella pivot
Worksheet sheet = workbook.Worksheets[0];

// Accedi alla tabella pivot tramite indice (la prima tabella pivot nel foglio)
PivotTable pivotTable = sheet.PivotTables[0];

// Recupera il PivotField di destinazione (il primo campo etichetta di riga in cui nasconderemo/mostreremo gli elementi)
PivotField pivotField = pivotTable.RowFields[0];

// Itera attraverso la raccolta PivotItems del PivotField selezionato
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];

    // Nascondi gli elementi pivot che corrispondono a un nome/criterio specifico
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }

    // Dimostra come mostrare nuovamente un elemento pivot precedentemente nascosto
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}

// Aggiorna e ricalcola la tabella pivot affinché le modifiche abbiano effetto
pivotTable.PivotCache.Refresh();

// Salva la cartella di lavoro — gli elementi nascosti rimangono nei dati sottostanti
// ma sono esclusi dall'output della tabella pivot visualizzata
workbook.Save("output_pivot_filtered.xlsx");
```

## **Riepilogo**

Aspose.Cells for .NET fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle presenti in Microsoft Excel. I filtri per etichetta, data e valore coprono gli scenari analitici più comuni, mentre il filtro primi 10 gestisce i report di classifica. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.IsHidden` offre un fallback flessibile a livello di elemento. Combinando queste strategie — ad esempio, applicando un filtro per etichetta e poi nascondendo elementi specifici — è possibile creare report di tabelle pivot mirati con precisione interamente da codice.
{{< app/cells/assistant language="csharp" >}}
