---
title: Filtrare le tabelle pivot per etichetta o valore
linktitle: Filtrare le tabelle pivot per etichetta o valore
description: Aspose.Cells for Node.js via C++ offre funzionalità complete di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati di una tabella pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri primi 10 e nascondendo o mostrando elementi pivot.
keywords: Aspose.Cells, libreria Node.js via C++, foglio di calcolo, tabella pivot, filtro, filtro per etichetta, filtro per valore, filtro per data, filtro primi 10, elemento pivot, nascondere elemento pivot
type: docs
weight: 10
url: /it/nodejs-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells offre cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot. È possibile applicare filtri per etichetta ai campi di riga o colonna basati su testo, utilizzare filtri per data quando il campo contiene solo celle di tipo data-ora o vuote, applicare filtri per valore rispetto ai numeri aggregati, utilizzare i filtri primi 10 per classificare in base a un campo valore, oppure nascondere e mostrare manualmente i singoli elementi pivot tramite la proprietà `IsHidden`. Ogni strategia è esposta tramite API dedicate sulle classi `PivotField` e `PivotItem`.

{{% /alert %}}

## **Introduzione**

Le tabelle pivot sono potenti strumenti di analisi, ma i riepiloghi grezzi spesso contengono molte più informazioni di quelle che è necessario presentare. Il filtraggio è il meccanismo principale per restringere una tabella pivot alle righe, alle colonne o ai valori che interessano per un report specifico. Aspose.Cells for Node.js via C++ rispecchia le funzionalità di filtraggio disponibili in Microsoft Excel, esponendole in modo programmatico così che la generazione dei report possa essere completamente automatizzata.

In questo articolo vengono trattate le seguenti strategie di filtraggio:

1. **Filtro per etichetta** — filtra gli elementi di un campo di riga o colonna in base alle loro etichette di testo.
2. **Filtro per data** — filtra i campi di riga o colonna che contengono solo valori di tipo data-ora (o vuoti).
3. **Filtro per valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro primi 10** — mostra solo i primi o gli ultimi N elementi classificati in base a un campo valore.
5. **Nascondere/Mostrare elementi pivot** — controlla manualmente la visibilità di ciascun singolo elemento in un campo.

Ogni approccio utilizza un metodo diverso sulla classe `PivotField` oppure una proprietà sulla classe `PivotItem`. Dopo aver applicato qualsiasi filtro, è necessario chiamare `refreshData()` e `calculateData()` sulla tabella pivot in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Filtro per etichetta**

Un filtro per etichetta consente di filtrare gli elementi di un campo di riga o colonna confrontando le loro didascalie di testo con un modello. Ciò è utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una lettera specifica, contengono una determinata parola o soddisfano un altro criterio basato sulla didascalia.

Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.filterByLabel(PivotFilterType, string)`. L'enumerazione `PivotFilterType` include valori come `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` e così via. Il secondo argomento fornisce la stringa di etichetta utilizzata per il confronto.

L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che solo gli elementi le cui didascalie iniziano con un prefisso specificato rimangano visibili, aggiorna la tabella pivot e salva il risultato.

```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// Carica la cartella di lavoro esistente contenente una tabella pivot
let workbook = new AsposeCells.Workbook(fileName);

// Accedi al foglio di lavoro tramite indice (primo foglio di lavoro)
let worksheet = workbook.getWorksheets().get(0);

// Accedi alla tabella pivot tramite indice
let pivotTable = worksheet.getPivotTables().get(0);

// Recupera il primo PivotField di riga
let rowField = pivotTable.getRowFields().get(0);

// Applica il filtro sulle etichette: mostra solo gli elementi di riga le cui etichette iniziano con il prefisso fornito
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// Aggiorna e ricalcola i dati della tabella pivot affinché il filtro abbia effetto
pivotTable.getPivotCache().refresh();

// Salva la cartella di lavoro su disco
workbook.save(fileName);
```

## **Filtro per data**

I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, la settimana scorsa, questo mese, il prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che funzionano solo con campi che memorizzano informazioni di data e ora.

{{% alert color="primary" %}}

Il filtro per data funziona solo quando l'area di riga o di colonna contiene esclusivamente celle di tipo data-ora o valori vuoti. Se il campo sottostante contiene altri tipi di dati, come numeri o testo, il filtro per data non produrrà il risultato atteso. Assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze `DateTime` valide oppure celle vuote prima di applicare questo filtro.

{{% /alert %}}

Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. L'enumerazione `PivotFilterType` contiene valori di data dedicati come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro scelto, si passano uno o due valori `DateTime` (per `Between`, si passano la data di inizio e la data di fine).

L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un particolare intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");

const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found: " + inputPath);
}

// Carica la cartella di lavoro esistente che contiene la tabella pivot
const workbook = new AsposeCells.Workbook(inputPath);

// Accedi al foglio di lavoro che contiene la tabella pivot (per indice)
const worksheet = workbook.getWorksheets().get(0);

// Accedi alla tabella pivot per indice
const pivotTable = worksheet.getPivotTables().get(0);

// Recupera il PivotField della data dall'area delle righe
// (Il filtro per data funziona solo quando l'area delle righe/colonne contiene solo celle di data-ora o vuote)
const dateField = pivotTable.getRowFields().get(0);

// Definisci il criterio della data per il filtro Between
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);

// Applica il filtro per data sul campo pivot
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// Aggiorna e ricalcola la tabella pivot affinché il filtro abbia effetto
pivotTable.getPivotCache().refresh();

// Salva la cartella di lavoro
workbook.save(outputPath);
```

## **Filtro per valore**

I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella propria area dati. Invece di confrontare etichette di testo, confrontano i totali numerici rispetto a una soglia. Casi d'uso tipici includono la visualizzazione solo dei prodotti la cui somma delle vendite supera un importo target oppure solo delle regioni il cui conteggio di transizioni rientra in un intervallo.

Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. Il parametro `filterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. Il parametro `valueField` specifica quale campo dati deve essere valutato, mentre il/i valore/i finale/i fornisce la soglia o le soglie.

L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

```javascript
let dataFieldIndex = -1;
for (let i = 0; i < pivotTable.getDataFields().getCount(); i++) {
    if (pivotTable.getDataFields().get(i) === dataField) {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0) {
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");
```

## **Filtro primi 10**

Il filtro primi 10 è una forma specializzata di filtro per valore che mantiene solo i primi o gli ultimi N elementi in base a un campo valore scelto. È comunemente utilizzato per report di classificazione, come "i primi 10 prodotti per ricavi" o "le ultime 5 regioni per conteggio delle vendite".

{{% alert color="primary" %}}

Il filtro primi 10 è efficace solo quando la tabella pivot dispone di uno o più campi pivot di valore nell'area dati. Senza almeno un campo valore, non esiste una misura aggregata rispetto alla quale classificare gli elementi e il filtro non può essere applicato.

{{% /alert %}}

Aspose.Cells espone il filtraggio primi 10 tramite il metodo `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. Il parametro `itemCount` definisce quanti elementi mantenere, `isTop` indica se mantenere gli elementi superiori (true) o inferiori (false), `valueField` fa riferimento al campo dati utilizzato per la classificazione e `filterType` controlla come viene calcolato il valore (tipicamente `Sum`, ma anche `Count` e `Percent`).

L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo valore, applica un filtro primi 10 per mantenere solo i 10 elementi più alti in base alla somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.

```javascript
const AsposeCells = require("aspose.cells");

// Carica la cartella di lavoro esistente che contiene la tabella pivot
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);

// Accedi al foglio di lavoro che contiene la tabella pivot (indice 0)
const worksheet = workbook.getWorksheets().get(0);

// Accedi alla tabella pivot tramite indice
const pivotTable = worksheet.getPivotTables().get(0);

// Verifica che ci sia almeno un PivotField di valore nell'area dati
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("Pivot table has no value (data) PivotField.");
}
const valueField = pivotTable.getDataFields().get(0);

// Recupera il PivotField di riga di destinazione (il campo a cui vogliamo applicare Top 10)
const rowField = pivotTable.getRowFields().get(0);

// Il primo (e unico) campo dati è all'indice 0; Top 10 classifica in base ad esso.
const valueFieldIndex = 0;

// Applica il filtro Top 10 sul campo di riga:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N; false significherebbe bottom N)
//   - valueFieldIndex = l'indice del campo dati utilizzato per classificare gli elementi
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// Aggiorna i dati della tabella pivot e ricalcolala affinché il filtro abbia effetto
pivotTable.getPivotTableCache().refresh();

// Salva la cartella di lavoro
workbook.save(outputPath);
```

## **Filtrare nascondendo o mostrando elementi pivot**

Oltre alle API di filtraggio strutturato, Aspose.Cells consente di controllare direttamente la visibilità di ciascun singolo elemento pivot. Iterando attraverso la raccolta `PivotItems` di un `PivotField` e attivando/disattivando la proprietà `IsHidden`, è possibile eliminare selettivamente elementi specifici senza applicare un filtro basato su formule. Impostando `IsHidden = true` l'elemento viene nascosto nella tabella pivot; impostando `IsHidden = false` l'elemento viene mostrato nuovamente.

Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per un elemento, come nascondere un numero limitato di categorie denominate che non devono apparire in un determinato report. L'esempio seguente carica una tabella pivot, nasconde un elemento specifico per nome, mostra come mostrarlo nuovamente, aggiorna la tabella pivot e salva la cartella di lavoro.

```javascript
Cells = require("aspose.cells");

// Carica una cartella di lavoro esistente contenente una tabella pivot
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// Accedi al primo foglio di lavoro che contiene la tabella pivot
const sheet = workbook.getWorksheets().get(0);

// Accedi alla tabella pivot per indice (la prima tabella pivot nel foglio)
const pivotTable = sheet.getPivotTables().get(0);

// Recupera il PivotField di destinazione (il primo campo etichetta di riga in cui nasconderemo/mostreremo gli elementi)
const pivotField = pivotTable.getRowFields().get(0);

// Itera attraverso la raccolta PivotItems del PivotField selezionato
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);

    // Nascondi gli elementi pivot che corrispondono a un nome/criterio specifico
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }

    // Dimostra come mostrare nuovamente: rivisualizza un elemento pivot precedentemente nascosto
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}

// Aggiorna e ricalcola la tabella pivot in modo che le modifiche abbiano effetto
pivotTable.getPivotCache().refreshData();

// Salva la cartella di lavoro — gli elementi nascosti rimangono nei dati sottostanti
// ma sono esclusi dall'output della tabella pivot visualizzata
workbook.save("output_pivot_filtered.xlsx");
```

## **Riepilogo**

Aspose.Cells for Node.js via C++ fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle disponibili in Microsoft Excel. I filtri per etichetta, per data e per valore coprono gli scenari analitici più comuni, mentre il filtro primi 10 gestisce i report di classificazione. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.IsHidden` offre un fallback flessibile a livello di elemento. Combinando queste strategie, ad esempio applicando un filtro per etichetta e poi nascondendo elementi specifici, è possibile creare report di tabelle pivot mirati con precisione interamente da codice.
{{< app/cells/assistant language="nodejs-cpp" >}}