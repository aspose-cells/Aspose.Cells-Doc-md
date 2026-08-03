---
title: Filtrare le tabelle pivot per etichetta o valore
linktitle: Filtrare le tabelle pivot per etichetta o valore
description: Aspose.Cells for Node.js via Java supporta funzionalità complete di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati delle tabelle pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri primi 10 e nascondendo o mostrando gli elementi pivot.
keywords: Aspose.Cells, libreria Node.js via Java, foglio elettronico, tabella pivot, filtro, filtro per etichetta, filtro per valore, filtro per data, filtro primi 10, elemento pivot, nascondere elemento pivot
type: docs
weight: 10
url: /it/nodejs-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Alert: Aspose.Cells provides five practical strategies for filtering the data displayed in a pivot table...
-> Aspose.Cells fornisce cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot...

Introduction: Pivot tables are powerful analytical tools, but raw summaries often contain far more information than you need to present. Filtering is the primary mechanism for narrowing a pivot table down to the rows, columns, or values that matter for a specific report. Aspose.Cells for Node.js via Java mirrors the filtering capabilities that are available in Microsoft Excel, exposing them programmatically so that report generation can be fully automated.

-> Le tabelle pivot sono potenti strumenti analitici, ma i riepiloghi grezzi spesso contengono molte più informazioni di quelle che è necessario presentare. Il filtraggio è il meccanismo principale per restringere una tabella pivot alle righe, alle colonne o ai valori che interessano per un report specifico. Aspose.Cells for Node.js via Java rispecchia le funzionalità di filtraggio disponibili in Microsoft Excel, esponendole programmaticamente in modo che la generazione dei report possa essere completamente automatizzata.

The following filtering strategies are covered in this article:
-> In questo articolo sono trattate le seguenti strategie di filtraggio:

1. Label Filter -> Filtro per etichetta
2. Date Filter -> Filtro per data
3. Value Filter -> Filtro per valore
4. Top 10 Filter -> Filtro primi 10
5. Hide / Unhide Pivot Items -> Nascondere / mostrare elementi pivot


-> Ogni approccio utilizza un metodo diverso sulla classe `PivotField` o una proprietà sulla classe `PivotItem`. Dopo aver applicato qualsiasi filtro, è necessario chiamare `refreshData()` e `calculateData()` sulla tabella pivot in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Label Filter**
-> ## **Filtro per etichetta**

A label filter allows you to filter the items of a row or column field by comparing their text captions against a pattern. This is useful when you want to display only products whose names start with a specific letter, contain a particular word, or match some other caption-based criterion.

-> Un filtro per etichetta consente di filtrare gli elementi di un campo riga o colonna confrontando le relative didascalie testuali con un modello. Ciò è utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una lettera specifica, contengono una determinata parola o soddisfano qualche altro criterio basato sulle didascalie.

Aspose.Cells exposes label filtering through the `PivotField.filterByLabel(PivotFilterType, string)` method...

-> Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.filterByLabel(PivotFilterType, string)`...

The following example loads a workbook containing an existing pivot table, applies a label filter so that only items whose captions begin with a specified prefix remain visible, refreshes the pivot table, and saves the result.

-> L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che solo gli elementi le cui didascalie iniziano con un prefisso specificato rimangano visibili, aggiorna la tabella pivot e salva il risultato.

## **Date Filter**
-> ## **Filtro per data**

Date filters let you narrow a pivot table by date-based criteria such as today, last week, this month, next quarter, or a specific date range. They are specialized filters that work only against fields that store date-time information.

-> I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, settimana scorsa, questo mese, prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che funzionano solo con i campi che memorizzano informazioni di data e ora.

Alert: The date filter only works when the row or column area contains only date-time cells or blank values...

-> Il filtro per data funziona solo quando l'area riga o colonna contiene solo celle di data e ora o valori vuoti...

Aspose.Cells exposes date filtering through the `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` method...

-> Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`...

The following example loads a workbook with a pivot table whose row area contains a date field, applies a date filter that restricts the visible items to a particular date range, refreshes the pivot table, and saves the workbook.

-> L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un determinato intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.

## **Value Filter**
-> ## **Filtro per valore**

Value filters operate on the aggregated values that a pivot table calculates in its data area. Instead of matching text labels, they compare numeric totals against a threshold. Typical use cases include showing only products whose sum of sales exceeds a target amount or only regions whose count of transactions falls within a range.

-> I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella sua area dati. Invece di confrontare le etichette di testo, confrontano i totali numerici con una soglia. Casi d'uso tipici includono la visualizzazione dei soli prodotti la cui somma delle vendite supera un importo obiettivo o solo delle regioni il cui conteggio delle transazioni rientra in un intervallo.

Aspose.Cells exposes value filtering through the `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)` method...

-> Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`...

The following example loads a workbook with a pivot table, applies a value filter that keeps only items whose aggregated sales exceed a numeric threshold, refreshes the pivot table, and saves the workbook.

-> L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

## **Top 10 Filter**
-> ## **Filtro primi 10**

The top 10 filter is a specialized form of value filter that retains only the highest or lowest N items based on a chosen value field. It is commonly used for ranking reports such as "top 10 products by revenue" or "bottom 5 regions by sales count".

-> Il filtro primi 10 è una forma specializzata di filtro per valore che mantiene solo gli N elementi più alti o più bassi in base a un campo valore scelto. È comunemente utilizzato per i report di classificazione come "i primi 10 prodotti per ricavo" o "le 5 regioni peggiori per numero di vendite".

Alert: The top 10 filter is only effective when the pivot table has one or more value pivot fields in the data area...

-> Il filtro primi 10 è efficace solo quando la tabella pivot ha uno o più campi pivot di valore nell'area dati...

Aspose.Cells exposes top 10 filtering through the `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` method...

-> Aspose.Cells espone il filtraggio primi 10 tramite il metodo `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`...

The following example loads a workbook with a pivot table that contains a value field, applies a top 10 filter to keep only the highest 10 items by the sum of sales, refreshes the pivot table, and saves the workbook.

-> L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo valore, applica un filtro primi 10 per mantenere solo i 10 elementi più alti in base alla somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.

## **Filter by Hiding or Unhiding Pivot Items**
-> ## **Filtro tramite nascondere o mostrare elementi pivot**

In addition to the structured filter APIs, Aspose.Cells allows you to control the visibility of each individual pivot item directly...

-> Oltre alle API di filtraggio strutturate, Aspose.Cells consente di controllare direttamente la visibilità di ciascun singolo elemento pivot...

This approach is useful when the filtering rule is irregular or item-specific...

-> Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per l'elemento...

## **Summary**
-> ## **Riepilogo**

Aspose.Cells for Node.js via Java provides a complete set of pivot table filtering capabilities that match those found in Microsoft Excel...

-> Aspose.Cells for Node.js via Java fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle disponibili in Microsoft Excel...

Related Articles - keep the titles but they are part of the link, I'll keep them as-is.

1. Translate every prose paragraph
2. Keep all technical terms (API names, class names, methods, etc.)
3. Keep code blocks as-is
4. Keep CODE_BLOCK placeholders as-is
5. Keep YAML frontmatter keys as-is, translate values
6. Make sure the description doesn't have a colon

"Aspose.Cells for Node.js via Java supports comprehensive pivot table filtering capabilities. This article explains how to filter pivot table data using label filters, date filters, value filters, top 10 filters, and by hiding or unhiding pivot items."


{{% alert color="primary" %}}

Aspose.Cells fornisce cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot. È possibile applicare filtri per etichetta ai campi di riga o colonna basati su testo, utilizzare filtri per data quando il campo contiene solo celle di data e ora o vuote, applicare filtri per valore rispetto ai numeri aggregati, utilizzare filtri primi 10 per classificare in base a un campo valore oppure nascondere e mostrare manualmente i singoli elementi pivot tramite la proprietà `IsHidden`. Ogni strategia è esposta tramite API dedicate sulle classi `PivotField` e `PivotItem`.

{{% /alert %}}

## **Introduzione**

Le tabelle pivot sono potenti strumenti analitici, ma i riepiloghi grezzi spesso contengono molte più informazioni di quelle che è necessario presentare. Il filtraggio è il meccanismo principale per restringere una tabella pivot alle righe, alle colonne o ai valori che interessano per un report specifico. Aspose.Cells for Node.js via Java rispecchia le funzionalità di filtraggio disponibili in Microsoft Excel, esponendole a livello di codice in modo che la generazione dei report possa essere completamente automatizzata.

In questo articolo sono trattate le seguenti strategie di filtraggio:

1. **Filtro per etichetta** — filtra gli elementi dei campi di riga o colonna in base alle relative etichette di testo.
2. **Filtro per data** — filtra i campi di riga o colonna che contengono solo valori di data e ora (oppure vuoti).
3. **Filtro per valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro primi 10** — mostra solo i primi o gli ultimi N elementi classificati in base a un campo valore.
5. **Nascondere / mostrare elementi pivot** — controlla manualmente la visibilità di ciascun singolo elemento in un campo.

Ogni approccio utilizza un metodo diverso sulla classe `PivotField` oppure una proprietà sulla classe `PivotItem`. Dopo aver applicato qualsiasi filtro, è necessario chiamare `refreshData()` e `calculateData()` sulla tabella pivot in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Filtro per etichetta**

Un filtro per etichetta consente di filtrare gli elementi di un campo di riga o colonna confrontando le relative didascalie testuali con un modello. Ciò è utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una lettera specifica, contengono una determinata parola oppure soddisfano qualche altro criterio basato sulle didascalie.

Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.filterByLabel(PivotFilterType, string)`. L'enumerazione `PivotFilterType` include valori come `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` e così via. Il secondo argomento fornisce la stringa dell'etichetta utilizzata per il confronto.

L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che solo gli elementi le cui didascalie iniziano con un prefisso specificato rimangano visibili, aggiorna la tabella pivot e salva il risultato.

```javascript
prefix = "B";

// Carica la cartella di lavoro esistente contenente una tabella pivot
let workbook = new AsposeCells.Workbook(fileName);

// Accedi al foglio di lavoro tramite indice (primo foglio di lavoro)
let worksheet = workbook.getWorksheets().get(0);

// Accedi alla tabella pivot tramite indice
let pivotTable = worksheet.getPivotTables().get(0);

// Recupera il primo PivotField di riga
let rowField = pivotTable.getRowFields().get(0);

// Applica il filtro etichetta — mostra solo gli elementi di riga le cui etichette iniziano con il prefisso fornito
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// Aggiorna e ricalcola i dati della tabella pivot affinché il filtro abbia effetto
pivotTable.getPivotCache().refresh();

// Salva la cartella di lavoro sul disco
workbook.save(fileName);
```

## **Filtro per data**

I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, settimana scorsa, questo mese, prossimo trimestre oppure un intervallo di date specifico. Sono filtri specializzati che funzionano solo con i campi che memorizzano informazioni di data e ora.

{{% alert color="primary" %}}

Il filtro per data funziona solo quando l'area riga o colonna contiene solo celle di data e ora oppure valori vuoti. Se il campo sottostante contiene altri tipi di dati come numeri o testo, il filtro per data non produrrà il risultato atteso. Assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze valide di `DateTime` oppure celle vuote prima di applicare questo filtro.

{{% /alert %}}

Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. L'enumerazione `PivotFilterType` contiene valori dedicati alle date come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro scelto, si passano uno o due valori `DateTime` (per `Between`, si passano le date di inizio e fine).

L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un determinato intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.

```javascript
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}

// Carica la cartella di lavoro esistente che contiene la tabella pivot
var workbook = new AsposeCells.Workbook(inputPath);

// Accedi al foglio di lavoro che contiene la tabella pivot (per indice)
var worksheet = workbook.getWorksheets().get(0);

// Accedi alla tabella pivot per indice
var pivotTable = worksheet.getPivotTables().get(0);

// Recupera il PivotField della data dall'area delle righe
// (Il filtro per data funziona solo quando l'area delle righe/colonne contiene solo celle di tipo data-ora o vuote)
let dateField = pivotTable.getRowFields().get(0);

// Definisce il criterio di data per il filtro Between
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);

// Applica il filtro per data sul campo pivot
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// Aggiorna e ricalcola la tabella pivot affinché il filtro abbia effetto
pivotTable.getPivotCache().refresh();

// Salva la cartella di lavoro
workbook.save(outputPath);
```

## **Filtro per valore**

I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella propria area dati. Invece di confrontare etichette di testo, confrontano i totali numerici con una soglia. Casi d'uso tipici includono la visualizzazione dei soli prodotti la cui somma delle vendite supera un importo obiettivo oppure delle sole regioni il cui conteggio delle transazioni rientra in un intervallo.

Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. Il parametro `filterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. Il parametro `valueField` specifica quale campo dati deve essere valutato, mentre l'ultimo argomento (o gli ultimi argomenti) fornisce i valori di soglia.

L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

```javascript
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);

var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);

// Trova manualmente l'indice del campo dati poiché PivotFieldCollection non ha IndexOf
var dataFieldIndex = -1;
for (var i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, AsposeCells.Pivot.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");
```

## **Filtro primi 10**

Il filtro primi 10 è una forma specializzata di filtro per valore che mantiene solo gli N elementi più alti o più bassi in base a un campo valore scelto. È comunemente utilizzato per i report di classificazione come "i primi 10 prodotti per ricavo" oppure "le 5 regioni peggiori per numero di vendite".

{{% alert color="primary" %}}

Il filtro primi 10 è efficace solo quando la tabella pivot ha uno o più campi pivot di valore nell'area dati. Senza almeno un campo valore, non esiste una misura aggregata rispetto alla quale classificare gli elementi e il filtro non può essere applicato.

{{% /alert %}}

Aspose.Cells espone il filtraggio primi 10 tramite il metodo `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. Il parametro `itemCount` definisce quanti elementi mantenere, `isTop` indica se mantenere gli elementi superiori (true) o inferiori (false), `valueField` fa riferimento al campo dati utilizzato per la classificazione e `filterType` controlla come viene calcolato il valore (in genere `Sum`, ma anche `Count` e `Percent`).

L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo valore, applica un filtro primi 10 per mantenere solo i 10 elementi più alti in base alla somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.

```javascript
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);

// Accedi al foglio di lavoro che contiene la tabella pivot (indice 0)
let worksheet = workbook.getWorksheets().get(0);

// Accedi alla tabella pivot tramite indice
let pivotTable = worksheet.getPivotTables().get(0);

// Verifica che ci sia almeno un PivotField di valore nell'area dati
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("La tabella pivot non ha PivotField di valore (dati).");
}
let valueField = pivotTable.getDataFields().get(0);

// Recupera il PivotField della riga di destinazione (il campo su cui vogliamo applicare Top 10)
let rowField = pivotTable.getRowFields().get(0);

// Il primo (e unico) campo dati si trova all'indice 0; Top 10 classifica in base ad esso.
let valueFieldIndex = 0;

// Applica il filtro Top 10 sul campo riga:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N; false significherebbe bottom N)
//   - valueFieldIndex = l'indice del campo dati usato per classificare gli elementi
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// Aggiorna i dati della tabella pivot e ricalcola per applicare il filtro
pivotTable.getPivotCache().refresh();

// Salva la cartella di lavoro
workbook.save(outputPath);
```

## **Filtro tramite nascondere o mostrare elementi pivot**

Oltre alle API di filtraggio strutturate, Aspose.Cells consente di controllare direttamente la visibilità di ciascun singolo elemento pivot. Iterando nella raccolta `PivotItems` di un `PivotField` e attivando/disattivando la proprietà `IsHidden`, è possibile sopprimere selettivamente elementi specifici senza applicare un filtro basato su formule. Impostando `IsHidden = true`, l'elemento viene nascosto dalla tabella pivot; impostando `IsHidden = false`, viene mostrato nuovamente e torna visibile.

Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per l'elemento, ad esempio per nascondere un piccolo numero di categorie con nome che non devono apparire in un determinato report. L'esempio seguente carica una tabella pivot, nasconde un elemento specifico per nome, mostra come ripristinarne la visibilità, aggiorna la tabella pivot e salva la cartella di lavoro.

```javascript
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// Accedi al primo foglio di lavoro che contiene la tabella pivot
let sheet = workbook.getWorksheets().get(0);

// Accedi alla tabella pivot per indice (la prima tabella pivot nel foglio)
let pivotTable = sheet.getPivotTables().get(0);

// Recupera il PivotField di destinazione (il primo campo etichetta di riga in cui nascondere/mostrare gli elementi)
let pivotField = pivotTable.getRowFields().get(0);

// Itera attraverso la collezione PivotItems del PivotField selezionato
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);

    // Nascondi gli elementi pivot che corrispondono a un nome/criterio specifico
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setIsHidden(true);
    }

    // Dimostra come mostrare nuovamente: ri-visualizza un elemento pivot precedentemente nascosto
    if (item.getName() == "Item3") {
        item.setIsHidden(false);
    }
}

// Aggiorna e ricalcola la tabella pivot affinché le modifiche abbiano effetto
pivotTable.getPivotCache().refreshData();

// Salva la cartella di lavoro — gli elementi nascosti rimangono nei dati sottostanti
// ma sono esclusi dall'output visualizzato della tabella pivot
workbook.save("output_pivot_filtered.xlsx");
```

## **Riepilogo**

Aspose.Cells for Node.js via Java fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle disponibili in Microsoft Excel. I filtri per etichetta, per data e per valore coprono gli scenari analitici più comuni, mentre il filtro primi 10 gestisce i report di classificazione. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.IsHidden` offre un fallback flessibile a livello di elemento. Combinando queste strategie, ad esempio applicando un filtro per etichetta e quindi nascondendo elementi specifici, è possibile creare report di tabelle pivot mirati con precisione interamente da codice.
{{< app/cells/assistant language="nodejs-java" >}}
