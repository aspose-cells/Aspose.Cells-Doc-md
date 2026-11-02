---
title: Visualizzazione o filtro dei primi 10 in una tabella pivot
linktitle: Visualizzazione o filtro dei primi 10 in una tabella pivot
description: Scopri come visualizzare in Aspose.Cells for .Net soltanto gli elementi classificati tra i primi o gli ultimi di un campo pivot. Questo articolo illustra il metodo Top10AutoShow di Excel 97-2003, la lettura delle opzioni tramite Top10AutoShowSettings e il filtro dei primi 10 di Excel 2007-365 tramite FilterTop10.
keywords: Aspose.Cells, .NET, tabella pivot, primi 10, visualizzazione automatica, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, C#
type: docs
weight: 20
url: /it/net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot che elenca tutti gli elementi di un campo di riga può essere difficile da leggere quando il campo contiene decine di elementi. Un report dei primi 10 conserva soltanto gli elementi che occupano le posizioni più alte o più basse della classifica, ossia esattamente ciò di cui hanno bisogno i report di classifica: "i 5 prodotti con il fatturato più alto" o "le 3 regioni con il minor numero di vendite". Aspose.Cells supporta due meccanismi a questo scopo, corrispondenti a due generazioni di Microsoft Excel.
- **AutoShow di Excel 97-2003** — il metodo `PivotField.Top10AutoShow()`. Questa è l'impostazione classica "Mostra i primi/ultimi N elementi", memorizzata direttamente sul campo pivot. Funziona in tutte le versioni di Excel, sia precedenti sia recenti, perché fa parte del formato originale della tabella pivot.
- **Filtro dei primi 10 di Excel 2007-365** — il metodo `PivotField.FilterTop10()`. Questo è il moderno filtro Top 10 disponibile nella sezione Filtri valori del menu del campo. Viene memorizzato come oggetto `PivotFilter` associato al campo e supporta la selezione in base al numero di elementi o alla percentuale.

## **Visualizzazione dei primi 10 in Excel 97-2003 (Top10AutoShow)**
L'AutoShow classico viene configurato con una singola chiamata a `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int count, int rankBy)`:
- `isAutoShow` — abilita o disabilita l'impostazione AutoShow sul campo.
- `isTop` — `true` mantiene gli elementi che occupano le posizioni più alte nella classifica (Primi), `false` mantiene quelli che occupano le posizioni più basse (Ultimi).
- `count` — il numero di elementi da mantenere, ad esempio 10 per un classico report dei primi 10.
- `rankBy` — l'indice in base zero del **campo di dati** i cui valori determinano la classifica degli elementi. Passare il valore -1 per classificare gli elementi in base al campo stesso.
La classifica può essere determinata da un campo di valore o dal campo stesso. Di seguito sono illustrate due varianti.

### **Classifica in base a un campo di valore**
È possibile classificare gli elementi del campo di riga in base a un normale campo di valore, come Somma di vendite. L'esempio seguente crea una tabella pivot con un campo di riga (`Sport`) e un campo di dati (`Sales`), quindi mostra i 2 sport con le vendite più alte. `rankBy` è 0 perché "Somma di vendite" è il campo di dati all'indice 0.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Mostra i primi 2 elementi ordinati per "Sum of Sales" (indice del campo dati 0)
sportField.Top10AutoShow(true, true, 2, 0);
pivotTable.CalculateData();
workbook.Save("output-top10-by-value-field.xlsx");
```

### **Classifica in base al campo stesso**
Un campo può anche essere classificato in base a sé stesso: passare -1 come `rankBy`. Per questa variante non è necessario alcun campo di dati aggiuntivo; il campo deve semplicemente trovarsi nell'area delle righe (o delle colonne). L'esempio seguente mostra gli ultimi 3 sport classificati in base al campo stesso. Quando questa impostazione viene salvata, l'attributo `rankBy` viene omesso dal XML della tabella pivot perché -1 è il valore predefinito del formato e `Top10AutoShowSettings.RankBy` legge nuovamente il valore -1.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Mostra i 3 elementi inferiori classificati in base al campo stesso (rankBy = -1)
sportField.Top10AutoShow(true, false, 3, -1);
pivotTable.CalculateData();
workbook.Save("output-top10-by-field-itself.xlsx");
```

## **Lettura delle opzioni correnti (Top10AutoShowSettings)**
La proprietà `PivotField.Top10AutoShowSettings` restituisce un oggetto `PivotFieldTop10AutoShowSettings` che espone le opzioni AutoShow attualmente memorizzate sul campo. Utilizzarlo per controllare come verranno presentati gli elementi di una cartella di lavoro esistente o di una tabella pivot appena configurata. Il controllo è possibile anche per le cartelle di lavoro caricate da un file.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
PivotField sportField = pivotTable.RowFields[0];
PivotFieldTop10AutoShowSettings settings = sportField.Top10AutoShowSettings;
Console.WriteLine("AutoShow enabled: " + settings.IsAutoShow);
Console.WriteLine("Direction: " + (settings.IsTop ? "Top" : "Bottom"));
Console.WriteLine("Item count: " + settings.AutoShowCount);
Console.WriteLine("Ranking data field index: " + settings.RankBy);
```

Le quattro proprietà corrispondono agli attributi classici di AutoShow memorizzati nel XML della tabella pivot (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`); pertanto, i valori letti sono quelli che verranno rispettati da tutte le versioni di Excel.

## **Nota**

{{% alert color="primary" %}}
- Le proprietà dirette `IsAutoShow`, `IsAscendShow`, `AutoShowCount` e `AutoShowField` di `PivotField` sono contrassegnate come obsolete. Utilizzare invece l'oggetto `Top10AutoShowSettings`: `IsAutoShow` corrisponde a `Top10AutoShowSettings.IsAutoShow`, `IsAscendShow` corrisponde a `Top10AutoShowSettings.IsTop`, `AutoShowCount` corrisponde a `Top10AutoShowSettings.AutoShowCount` e `AutoShowField` corrisponde a `Top10AutoShowSettings.RankBy`. Il metodo `Top10AutoShow()` è il metodo supportato per modificare le impostazioni.
- `Top10AutoShow` funziona con campi di riga e di colonna. Un campo situato soltanto nell'area della pagina (filtro) non può essere classificato in questo modo perché i suoi elementi non sono organizzati nel corpo della tabella pivot.
{{% /alert %}}

## **Excel 2007-365: filtro dei primi 10 (FilterTop10)**
Le versioni moderne di Excel presentano i primi 10 come filtro di valori nel menu del campo (Filtri valori, Primi 10...). Aspose.Cells rappresenta questa funzionalità con il metodo `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, che restituisce l'oggetto `PivotFilter` creato:
- `valueFieldIndex` — l'indice in base zero del campo di dati i cui valori aggregati determinano la classifica degli elementi.
- `type` — il significato di `itemCount`. `PivotFilterType.Count` mantiene un numero fisso di elementi (opzione Elementi della finestra di dialogo). `PivotFilterType.Percent` mantiene una percentuale degli elementi, quindi `itemCount` è la percentuale stessa: il valore 30 mantiene il 30% degli elementi in cima alla classifica. `PivotFilterType.Sum` classifica in base alla copertura cumulativa dei valori.
- `isTop` — `true` per Primi, `false` per Ultimi.
- `itemCount` — il valore N in "Primi N"; l'unità dipende da `type`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Filtro Top 10 — mantieni i 2 elementi migliori in base a "Sum of Sales" (indice del campo dati 0)
PivotFilter filter = sportField.FilterTop10(0, PivotFilterType.Count, true, 2);
// Per un filtro basato sulla percentuale, mantieni invece i primi 30 percento degli elementi:
// sportField.FilterTop10(0, PivotFilterType.Percent, true, 30);
pivotTable.PivotCache.Refresh();
pivotTable.CalculateData();
workbook.Save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`Top10AutoShow` e `FilterTop10` sono due funzionalità distinte. AutoShow scrive l'attributo classico `autoShow` sul campo pivot ed è supportato da tutte le versioni di Excel, a partire da Excel 97. `FilterTop10` scrive una voce moderna di tipo `PivotFilter`, che richiede Excel 2007 o versione successiva. Quando una cartella di lavoro viene aperta in una versione precedente di Excel, la tabella pivot che utilizza il filtro moderno torna a mostrare tutti gli elementi. Per i documenti che devono essere elaborati da strumenti di versioni precedenti, preferire `Top10AutoShow`; per le cartelle di lavoro moderne, preferire `FilterTop10`, poiché può essere combinato con gli altri filtri sui valori.
{{% /alert %}}

## **Articoli correlati**
- [Filtraggio delle tabelle pivot per etichetta o valore](/cells/it/net/filter-by-label-or-value-of-pivot-table/)
- [Aggiunta di campi di riga e colonna alla tabella pivot](/cells/it/net/pivot-table-add-row-and-column-fields/)
- [Raggruppamento dei campi pivot nella tabella pivot](/cells/it/net/group-pivot-fields-in-the-pivot-table/)
- [Aggiornamento della tabella pivot](/cells/it/net/refresh-pivot-table/)
- [Aggiunta di un campo pagina alla tabella pivot](/cells/it/net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="csharp" >}}