---
title: Filtrare le tabelle pivot per etichetta o valore
linktitle: Filtrare le tabelle pivot per etichetta o valore
description: Aspose.Cells for Java supporta funzionalità complete di filtraggio delle tabelle pivot, Questo articolo spiega come filtrare i dati delle tabelle pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri primi 10 e nascondendo o mostrando gli elementi pivot.
keywords: Aspose.Cells, libreria Java, foglio di calcolo, tabella pivot, filtro, filtro per etichetta, filtro per valore, filtro per data, filtro primi 10, elemento pivot, nascondere elemento pivot
type: docs
weight: 10
url: /it/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


Alert block 1:
{{% alert color="primary" %}}
Aspose.Cells provides five practical strategies for filtering the data displayed in a pivot table. You can apply label filters to text-based row or column fields, use date filters when the field contains only date-time cells or blanks, apply value filters against aggregated numbers, use top 10 filters to rank by a value field, or manually hide and unhide individual pivot items using the `IsHidden` property. Each strategy is exposed through dedicated APIs on the `PivotField` and `PivotItem` classes.
{{% /alert %}}

{{% alert color="primary" %}}
Aspose.Cells offre cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot. È possibile applicare filtri per etichetta ai campi di riga o colonna basati su testo, utilizzare filtri per data quando il campo contiene solo celle di tipo data-ora o vuote, applicare filtri per valore rispetto ai numeri aggregati, utilizzare filtri primi 10 per classificare in base a un campo valore, oppure nascondere e mostrare manualmente i singoli elementi pivot utilizzando la proprietà `IsHidden`. Ogni strategia è esposta tramite API dedicate sulle classi `PivotField` e `PivotItem`.
{{% /alert %}}

## **Introduction**

Pivot tables are powerful analytical tools, but raw summaries often contain far more information than you need to present. Filtering is the primary mechanism for narrowing a pivot table down to the rows, columns, or values that matter for a specific report. Aspose.Cells for Java mirrors the filtering capabilities that are available in Microsoft Excel, exposing them programmatically so that report generation can be fully automated.

The following filtering strategies are covered in this article:

1. **Label Filter** — filters row or column field items based on their text labels.
2. **Date Filter** — filters row or column fields that contain only date-time values (or blanks).
3. **Value Filter** — filters items based on the aggregated values of a data field.
4. **Top 10 Filter** — shows only the top or bottom N items ranked by a value field.
5. **Hide / Unhide Pivot Items** — manually controls the visibility of each individual item in a field.

Each approach uses a different method on the `PivotField` class or a property on the `PivotItem` class. After applying any filter, you must call `refreshData()` and `calculateData()` on the pivot table so that the cached data and calculated values reflect the new filter state.

## **Introduzione**

Le tabelle pivot sono potenti strumenti analitici, ma i riepiloghi grezzi spesso contengono molte più informazioni di quelle che è necessario presentare. Il filtraggio è il meccanismo principale per ridurre una tabella pivot alle righe, colonne o valori che interessano per un report specifico. Aspose.Cells for Java rispecchia le funzionalità di filtraggio disponibili in Microsoft Excel, esponendole a livello di codice in modo che la generazione dei report possa essere completamente automatizzata.

In questo articolo vengono trattate le seguenti strategie di filtraggio:

1. **Filtro per etichetta** — filtra gli elementi dei campi di riga o colonna in base alle loro etichette di testo.
2. **Filtro per data** — filtra i campi di riga o colonna che contengono solo valori di data-ora (o vuoti).
3. **Filtro per valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro primi 10** — mostra solo i primi o gli ultimi N elementi classificati in base a un campo valore.
5. **Nascondere/Mostrare elementi pivot** — controlla manualmente la visibilità di ogni singolo elemento in un campo.

## **Label Filter**

A label filter allows you to filter the items of a row or column field by comparing their text captions against a pattern. This is useful when you want to display only products whose names start with a specific letter, contain a particular word, or match some other caption-based criterion.

Aspose.Cells exposes label filtering through the `PivotField.filterByLabel(PivotFilterType, String)` method. The `PivotFilterType` enumeration includes values such as `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, and so on. The second argument supplies the label string used for comparison.

The following example loads a workbook containing an existing pivot table, applies a label filter so that only items whose captions begin with a specified prefix remain visible, refreshes the pivot table, and saves the result.

## **Filtro per etichetta**

Un filtro per etichetta consente di filtrare gli elementi di un campo di riga o colonna confrontando le loro didascalie di testo con un modello. Ciò è utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una lettera specifica, contengono una determinata parola o corrispondono a un altro criterio basato sulle didascalie.

Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.filterByLabel(PivotFilterType, String)`. L'enumerazione `PivotFilterType` include valori come `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` e così via. Il secondo argomento fornisce la stringa di etichetta utilizzata per il confronto.

L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che solo gli elementi le cui didascalie iniziano con un prefisso specificato rimangano visibili, aggiorna la tabella pivot e salva il risultato.

## **Date Filter**

Date filters let you narrow a pivot table by date-based criteria such as today, last week, this month, next quarter, or a specific date range. They are specialized filters that work only against fields that store date-time information.

Alert 2:
{{% alert color="primary" %}}
The date filter only works when the row or column area contains only date-time cells or blank values. If the underlying field contains other data types such as numbers or text, the date filter will not produce the expected result. Make sure the field is formatted as a date and that all values are valid `DateTime` instances or empty cells before applying this filter.
{{% /alert %}}

Aspose.Cells exposes date filtering through the `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` method. The `PivotFilterType` enumeration contains dedicated date values such as `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear`, and `Between`. Depending on the chosen filter type, you pass one or two `DateTime` values (for `Between`, you pass the start and end dates).

The following example loads a workbook with a pivot table whose row area contains a date field, applies a date filter that restricts the visible items to a particular date range, refreshes the pivot table, and saves the workbook.

## **Filtro per data**

I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, la settimana scorsa, questo mese, il prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che funzionano solo con i campi che memorizzano informazioni di data-ora.

{{% alert color="primary" %}}
Il filtro per data funziona solo quando l'area di riga o colonna contiene solo celle di tipo data-ora o valori vuoti. Se il campo sottostante contiene altri tipi di dati come numeri o testo, il filtro per data non produrrà il risultato previsto. Assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze valide di `DateTime` oppure celle vuote prima di applicare questo filtro.
{{% /alert %}}

Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. L'enumerazione `PivotFilterType` contiene valori dedicati alla data come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro scelto, si passano uno o due valori `DateTime` (per `Between`, si passano le date di inizio e fine).

L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un determinato intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.

## **Value Filter**

Value filters operate on the aggregated values that a pivot table calculates in its data area. Instead of matching text labels, they compare numeric totals against a threshold. Typical use cases include showing only products whose sum of sales exceeds a target amount or only regions whose count of transactions falls within a range.

Aspose.Cells exposes value filtering through the `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)` method. The `filterType` parameter uses values such as `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual`, and `ValueLessThanOrEqual`. The `valueField` parameter specifies which data field should be evaluated, and the final argument(s) supply the threshold value(s).

The following example loads a workbook with a pivot table, applies a value filter that keeps only items whose aggregated sales exceed a numeric threshold, refreshes the pivot table, and saves the workbook.

## **Filtro per valore**

I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella sua area dati. Invece di confrontare le etichette di testo, confrontano i totali numerici con una soglia. Casi d'uso tipici includono la visualizzazione solo dei prodotti la cui somma delle vendite supera un importo obiettivo o solo delle regioni il cui conteggio delle transazioni rientra in un intervallo.

Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. Il parametro `filterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. Il parametro `valueField` specifica quale campo dati deve essere valutato e gli ultimi argomenti forniscono i valori di soglia.

L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

## **Top 10 Filter**

The top 10 filter is a specialized form of value filter that retains only the highest or lowest N items based on a chosen value field. It is commonly used for ranking reports such as "top 10 products by revenue" or "bottom 5 regions by sales count".

Alert 3:
{{% alert color="primary" %}}
The top 10 filter is only effective when the pivot table has one or more value pivot fields in the data area. Without at least one value field, there is no aggregated measure to rank the items against, and the filter cannot be applied.
{{% /alert %}}

Aspose.Cells exposes top 10 filtering through the `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)` method. The `itemCount` parameter defines how many items to retain, `isTop` indicates whether to keep the top items (true) or the bottom items (false), `valueField` references the data field used for ranking, and `filterType` controls how the value is computed (typically `Sum`, but also `Count` and `Percent`).

The following example loads a workbook with a pivot table that contains a value field, applies a top 10 filter to keep only the highest 10 items by the sum of sales, refreshes the pivot table, and saves the workbook.

## **Filtro primi 10**

Il filtro primi 10 è una forma specializzata di filtro per valore che mantiene solo i primi o gli ultimi N elementi in base a un campo valore scelto. È comunemente utilizzato per report di classifica come "i primi 10 prodotti per ricavi" o "le ultime 5 regioni per numero di vendite".

{{% alert color="primary" %}}
Il filtro primi 10 è efficace solo quando la tabella pivot dispone di uno o più campi pivot di valore nell'area dati. Senza almeno un campo di valore, non esiste alcuna misura aggregata rispetto a cui classificare gli elementi e il filtro non può essere applicato.
{{% /alert %}}

Aspose.Cells espone il filtraggio primi 10 tramite il metodo `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)`. Il parametro `itemCount` definisce quanti elementi mantenere, `isTop` indica se mantenere i primi elementi (true) o gli ultimi elementi (false), `valueField` fa riferimento al campo dati utilizzato per la classifica e `filterType` controlla come viene calcolato il valore (tipicamente `Sum`, ma anche `Count` e `Percent`).

L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo di valore, applica un filtro primi 10 per mantenere solo i primi 10 elementi in base alla somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.

## **Filter by Hiding or Unhiding Pivot Items**

In addition to the structured filter APIs, Aspose.Cells allows you to control the visibility of each individual pivot item directly. By iterating through the `PivotItems` collection of a `PivotField` and toggling the `IsHidden` property, you can selectively suppress specific items without applying a formula-based filter. Setting `IsHidden = true` hides the item from the pivot table; setting `IsHidden = false` unhides it and makes it visible again.

This approach is useful when the filtering rule is irregular or item-specific, such as hiding a small number of named categories that should not appear in a particular report. The example below loads a pivot table, hides a specific item by name, demonstrates how to unhide it, refreshes the pivot table, and saves the workbook.

## **Filtrare nascondendo o mostrando elementi pivot**

Oltre alle API di filtraggio strutturate, Aspose.Cells consente di controllare direttamente la visibilità di ogni singolo elemento pivot. Iterando attraverso la raccolta `PivotItems` di un `PivotField` e attivando/disattivando la proprietà `IsHidden`, è possibile sopprimere selettivamente elementi specifici senza applicare un filtro basato su formula. Impostando `IsHidden = true` l'elemento viene nascosto dalla tabella pivot; impostando `IsHidden = false` viene mostrato nuovamente e reso visibile.

Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per elemento, come nascondere un piccolo numero di categorie denominate che non devono apparire in un determinato report. L'esempio seguente carica una tabella pivot, nasconde un elemento specifico per nome, mostra come mostrarlo nuovamente, aggiorna la tabella pivot e salva la cartella di lavoro.

## **Summary**

Aspose.Cells for Java provides a complete set of pivot table filtering capabilities that match those found in Microsoft Excel. Label, date, and value filters cover the most common analytical scenarios, while the top 10 filter handles ranking reports. When the filtering rule is irregular, the `PivotItem.IsHidden` property offers a flexible, item-level fallback. Combining these strategies — for example, applying a label filter and then hiding specific items — allows you to build precisely targeted pivot table reports entirely from code.

## **Riepilogo**

Aspose.Cells for Java fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle disponibili in Microsoft Excel. I filtri per etichetta, per data e per valore coprono gli scenari analitici più comuni, mentre il filtro primi 10 gestisce i report di classifica. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.IsHidden` offre un fallback flessibile a livello di elemento. Combinando queste strategie, ad esempio applicando un filtro per etichetta e poi nascondendo elementi specifici, è possibile creare report di tabelle pivot mirati con precisione interamente da codice.


These links are: pivot-tables/, row-and-column-fields/, add-page-field-in-pivot-table/, manage-value-fields/, refresh-pivot-table/. All pivot-table related. 

- The 5 code block placeholders are preserved exactly
- All alert blocks are balanced
- No additional code blocks

- Frontmatter description: "Aspose.Cells for Java supporta funzionalità complete..." - 1 occurrence
- Body: "Aspose.Cells for Java rispecchia le funzionalità..." - 1 occurrence
- Summary: "Aspose.Cells for Java fornisce..." - 1 occurrence

Total: 3 separate occurrences, each correct.

- "Aggiungere campi di riga e colonna della tabella pivot in Aspose.Cells for Java" - 1 occurrence ✓
- "Aggiungere campi filtro a una tabella pivot in Aspose.Cells for Java" - 1 occurrence ✓
- "Gestire i campi di valore della tabella pivot in Aspose.Cells for Java" - 1 occurrence ✓
- "Aggiornare tabelle pivot e cache pivot in Aspose.Cells for Java" - 1 occurrence ✓

All good.

So it has two sentences separated by a period. I'll use a period in Italian too.

description: Aspose.Cells for Java supporta funzionalità complete di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati delle tabelle pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri primi 10 e nascondendo o mostrando gli elementi pivot.


And "before applying this filter" - "prima di applicare questo filtro" - good.

For the top 10 filter alert: "there is no aggregated measure to rank the items against" - "non esiste alcuna misura aggregata rispetto a cui classificare gli elementi" - good.

"Aspose.Cells for Java supports comprehensive pivot table filtering capabilities. This article explains how to filter pivot table data using label filters, date filters, value filters, top 10 filters, and by hiding or unhiding pivot items."

"Aspose.Cells for Java supporta funzionalità complete di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati delle tabelle pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri primi 10 e nascondendo o mostrando gli elementi pivot."

This looks good. No colons, just periods and commas.

1. Start with ---
2. Have the frontmatter
3. Then immediately have a blank line or first content
4. Have all the body content
5. Preserve all code block placeholders
6. End with the Hugo shortcode


{{% alert color="primary" %}}

Aspose.Cells offre cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot. È possibile applicare filtri per etichetta ai campi di riga o colonna basati su testo, utilizzare filtri per data quando il campo contiene solo celle di tipo data-ora o vuote, applicare filtri per valore rispetto ai numeri aggregati, utilizzare filtri primi 10 per classificare in base a un campo valore, oppure nascondere e mostrare manualmente i singoli elementi pivot utilizzando la proprietà `IsHidden`. Ogni strategia è esposta tramite API dedicate sulle classi `PivotField` e `PivotItem`.

{{% /alert %}}

## **Introduzione**

Le tabelle pivot sono potenti strumenti analitici, ma i riepiloghi grezzi spesso contengono molte più informazioni di quelle che è necessario presentare. Il filtraggio è il meccanismo principale per ridurre una tabella pivot alle righe, colonne o valori che interessano per un report specifico. Aspose.Cells for Java rispecchia le funzionalità di filtraggio disponibili in Microsoft Excel, esponendole a livello di codice in modo che la generazione dei report possa essere completamente automatizzata.

In questo articolo vengono trattate le seguenti strategie di filtraggio:

1. **Filtro per etichetta** — filtra gli elementi dei campi di riga o colonna in base alle loro etichette di testo.
2. **Filtro per data** — filtra i campi di riga o colonna che contengono solo valori di data-ora (o vuoti).
3. **Filtro per valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro primi 10** — mostra solo i primi o gli ultimi N elementi classificati in base a un campo valore.
5. **Nascondere/Mostrare elementi pivot** — controlla manualmente la visibilità di ogni singolo elemento in un campo.

Ogni approccio utilizza un metodo diverso sulla classe `PivotField` o una proprietà sulla classe `PivotItem`. Dopo aver applicato un filtro, è necessario chiamare `refreshData()` e `calculateData()` sulla tabella pivot in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Filtro per etichetta**

Un filtro per etichetta consente di filtrare gli elementi di un campo di riga o colonna confrontando le loro didascalie di testo con un modello. Ciò è utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una lettera specifica, contengono una determinata parola o corrispondono a un altro criterio basato sulle didascalie.

Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.filterByLabel(PivotFilterType, String)`. L'enumerazione `PivotFilterType` include valori come `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` e così via. Il secondo argomento fornisce la stringa di etichetta utilizzata per il confronto.

L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che solo gli elementi le cui didascalie iniziano con un prefisso specificato rimangano visibili, aggiorna la tabella pivot e salva il risultato.

```java
import com.aspose.cells.*;

String fileName = "sample.xlsx";
String prefix = "B";

// Carica la cartella di lavoro esistente contenente una tabella pivot
Workbook workbook = new Workbook(fileName);

// Accedi al foglio di lavoro tramite indice (primo foglio di lavoro)
Worksheet worksheet = workbook.getWorksets().get(0);

// Accedi alla tabella pivot tramite indice
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Recupera il primo PivotField delle righe
PivotField rowField = pivotTable.getRowFields().get(0);

// Applica il filtro sulle etichette - mostra solo gli elementi di riga le cui etichette iniziano con il prefisso fornito
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");

// Aggiorna e ricalcola i dati della tabella pivot affinché il filtro abbia effetto
pivotTable.refreshData();

// Salva la cartella di lavoro su disco
workbook.save(fileName);
```

## **Filtro per data**

I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, la settimana scorsa, questo mese, il prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che funzionano solo con i campi che memorizzano informazioni di data-ora.

{{% alert color="primary" %}}

Il filtro per data funziona solo quando l'area di riga o colonna contiene solo celle di tipo data-ora o valori vuoti. Se il campo sottostante contiene altri tipi di dati come numeri o testo, il filtro per data non produrrà il risultato previsto. Assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze valide di `DateTime` oppure celle vuote prima di applicare questo filtro.

{{% /alert %}}

Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. L'enumerazione `PivotFilterType` contiene valori dedicati alla data come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro scelto, si passano uno o due valori `DateTime` (per `Between`, si passano le date di inizio e fine).

L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un determinato intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.

```java
import java.io.File;
import java.io.FileNotFoundException;

String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";

if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}

// Carica la cartella di lavoro esistente che contiene la tabella pivot
Workbook workbook = new Workbook(inputPath);

// Accedi al foglio di lavoro che contiene la tabella pivot (per indice)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Accedi alla tabella pivot per indice
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Recupera il PivotField della data dall'area delle righe
// (Il filtro per data funziona solo quando l'area di riga/colonna contiene solo celle data-ora o vuote)
PivotField dateField = pivotTable.getRowFields().get(0);

// Definisce il criterio di data per il filtro Between
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// Applica il filtro per data sul campo pivot
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);

// Aggiorna e ricalcola la tabella pivot affinché il filtro abbia effetto
pivotTable.refreshData();

// Salva la cartella di lavoro
workbook.save(outputPath);
```

## **Filtro per valore**

I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella sua area dati. Invece di confrontare le etichette di testo, confrontano i totali numerici con una soglia. Casi d'uso tipici includono la visualizzazione solo dei prodotti la cui somma delle vendite supera un importo obiettivo o solo delle regioni il cui conteggio delle transazioni rientra in un intervallo.

Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. Il parametro `filterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. Il parametro `valueField` specifica quale campo dati deve essere valutato e gli ultimi argomenti forniscono i valori di soglia.

L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);

PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);

// Trova manualmente l'indice del campo dati poiché PivotFieldCollection non ha IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, Double.MAX_VALUE);
}

pivotTable.refreshData();

workbook.save("output.xlsx");
```

## **Filtro primi 10**

Il filtro primi 10 è una forma specializzata di filtro per valore che mantiene solo i primi o gli ultimi N elementi in base a un campo valore scelto. È comunemente utilizzato per report di classifica come "i primi 10 prodotti per ricavi" o "le ultime 5 regioni per numero di vendite".

{{% alert color="primary" %}}

Il filtro primi 10 è efficace solo quando la tabella pivot dispone di uno o più campi pivot di valore nell'area dati. Senza almeno un campo di valore, non esiste alcuna misura aggregata rispetto a cui classificare gli elementi e il filtro non può essere applicato.

{{% /alert %}}

Aspose.Cells espone il filtraggio primi 10 tramite il metodo `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)`. Il parametro `itemCount` definisce quanti elementi mantenere, `isTop` indica se mantenere i primi elementi (true) o gli ultimi elementi (false), `valueField` fa riferimento al campo dati utilizzato per la classifica e `filterType` controlla come viene calcolato il valore (tipicamente `Sum`, ma anche `Count` e `Percent`).

L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo di valore, applica un filtro primi 10 per mantenere solo i primi 10 elementi in base alla somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.

```java
import com.aspose.cells.*;

// Carica la cartella di lavoro esistente che contiene la tabella pivot
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// Accedi al foglio di lavoro che contiene la tabella pivot (indice 0)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Accedi alla tabella pivot tramite indice
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Verifica che ci sia almeno un PivotField di valore nell'area dati
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);

// Recupera il PivotField di riga di destinazione (il campo su cui vogliamo applicare Top 10)
PivotField rowField = pivotTable.getRowFields().get(0);

// Il primo (e unico) campo dati è all'indice 0; Top 10 classifica in base ad esso.
int valueFieldIndex = 0;

// Applica il filtro Top 10 sul campo di riga:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false significherebbe bottom N)
//   - valueFieldIndex = l'indice del campo dati utilizzato per classificare gli elementi
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);

// Aggiorna i dati della tabella pivot e ricalcolala affinché il filtro abbia effetto
pivotTable.refreshData();

// Salva la cartella di lavoro
workbook.save(outputPath);
```

## **Filtrare nascondendo o mostrando elementi pivot**

Oltre alle API di filtraggio strutturate, Aspose.Cells consente di controllare direttamente la visibilità di ogni singolo elemento pivot. Iterando attraverso la raccolta `PivotItems` di un `PivotField` e attivando/disattivando la proprietà `IsHidden`, è possibile sopprimere selettivamente elementi specifici senza applicare un filtro basato su formula. Impostando `IsHidden = true` l'elemento viene nascosto dalla tabella pivot; impostando `IsHidden = false` viene mostrato nuovamente e reso visibile.

Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per elemento, come nascondere un piccolo numero di categorie denominate che non devono apparire in un determinato report. L'esempio seguente carica una tabella pivot, nasconde un elemento specifico per nome, mostra come mostrarlo nuovamente, aggiorna la tabella pivot e salva la cartella di lavoro.

```java
import com.aspose.cells.*;

// Carica una cartella di lavoro esistente contenente una tabella pivot
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// Accedi al primo foglio di lavoro che contiene la tabella pivot
Worksheet sheet = workbook.getWorksheets().get(0);

// Accedi alla tabella pivot per indice (la prima tabella pivot nel foglio)
PivotTable pivotTable = sheet.getPivotTables().get(0);

// Recupera il PivotField di destinazione (il primo campo etichetta di riga in cui nasconderemo/mostreremo gli elementi)
PivotField pivotField = pivotTable.getRowFields().get(0);

// Itera attraverso la raccolta PivotItems del PivotField selezionato
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);

    // Nascondi gli elementi pivot che corrispondono a un nome/criterio specifico
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }

    // Dimostra come mostrare nuovamente un elemento pivot precedentemente nascosto
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}

// Aggiorna e ricalcola la tabella pivot affinché le modifiche abbiano effetto
pivotTable.refreshData();

// Salva la cartella di lavoro - gli elementi nascosti rimangono nei dati sottostanti
// ma sono esclusi dall'output della tabella pivot visualizzata
workbook.save("output_pivot_filtered.xlsx");
```

## **Riepilogo**

Aspose.Cells for Java fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle disponibili in Microsoft Excel. I filtri per etichetta, per data e per valore coprono gli scenari analitici più comuni, mentre il filtro primi 10 gestisce i report di classifica. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.IsHidden` offre un fallback flessibile a livello di elemento. Combinando queste strategie, ad esempio applicando un filtro per etichetta e poi nascondendo elementi specifici, è possibile creare report di tabelle pivot mirati con precisione interamente da codice.
{{< app/cells/assistant language="java" >}}




