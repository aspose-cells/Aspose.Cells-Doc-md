---
title: Mostra i valori come in una tabella pivot
linktitle: Mostra i valori come in una tabella pivot
description: Visualizzare i valori dei campi dati di una tabella pivot come percentuale del totale, differenza rispetto a un elemento di base, totali cumulativi, classifiche e altre opzioni con Aspose.Cells for .Net.
keywords: Aspose.Cells, tabella pivot, mostra i valori come, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex, C#
type: docs
weight: 145
url: /it/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot normalmente aggrega ogni campo dati mediante una funzione di aggregazione come `Sum` o `Count`. La funzione **Mostra valori come** di Excel sostituisce ciascun risultato visualizzato con un calcolo secondario derivato da tale aggregazione, ad esempio una percentuale del totale complessivo, un totale cumulativo, una differenza rispetto a un elemento di base o una classifica, consentendo di eseguire analisi comparative senza formule ausiliarie o colonne calcolate.
Gli utilizzi tipici includono l'analisi della quota rispetto al totale, con percentuali di riga, colonna o totale complessivo; la produzione di report cumulativi mediante un totale cumulativo in un campo di periodo; l'analisi della varianza rispetto a un elemento di riferimento mediante la differenza o la differenza percentuale rispetto a un elemento di base; e la classificazione dei valori dal più piccolo al più grande o viceversa.
In Aspose.Cells for .Net, l'enumerazione `PivotShowValuesAsType` seleziona il calcolo secondario. La proprietà di sola lettura `PivotField.ShowValuesSetting` restituisce un oggetto `PivotShowValuesSetting`, le cui proprietà scrivibili `ShowValuesAs`, `BaseFieldIndex` e `BaseItemIndex` configurano il comportamento; il metodo di comodità `PivotField.ShowValuesAs(...)` applica le stesse impostazioni con una singola chiamata. Applicare queste impostazioni a un campo dati o a un campo valore ottenuto da `PivotTable.DataFields`.

## **Membri dell'enumerazione PivotShowValuesAsType**
Il campo dati mantiene la propria funzione di aggregazione, come Sum o Count, mentre Mostra valori come trasforma soltanto il modo in cui il valore aggregato viene visualizzato.
Oltre all'impostazione diretta delle proprietà di `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di comodità applica la stessa configurazione con una singola chiamata. Sono disponibili due sovraccarichi: uno che specifica il campo e l'elemento di base mediante indici, l'altro che specifica il nome del campo di base e la didascalia dell'elemento di base.

```csharp
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, string baseField, string baseItem)
```

| Parametro | Significato | Quando è necessario |
| --- | --- | --- |
| `showValuesAsType` | Il calcolo secondario `PivotShowValuesAsType` da applicare. | Sempre. |
| `baseField` | Indice a base zero del campo di base tra i campi di base della tabella pivot (ad esempio, l'indice del campo di riga a cui appartiene l'elemento di base) oppure, nel sovraccarico con stringhe, il nome del campo di base. | Gli otto formati basati sul campo di base riportati di seguito (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); per ogni altro formato, passare `0` (o `null` nel sovraccarico con stringhe). |
| `baseItem` | Indice a base zero dell'elemento di base, con due valori sentinella: `PivotShowValuesSetting.PreviousPivotItem` (-1) seleziona l'elemento precedente e `PivotShowValuesSetting.NextPivotItem` (-2) quello successivo. Nel sovraccarico con stringhe viene accettata la didascalia dell'elemento di base; utilizzare `null` quando il formato selezionato non richiede alcun elemento di base. | Solo i tre formati basati sull'elemento di base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) utilizzano l'elemento di base; i cinque formati basati sul campo (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, entrambe le classifiche) non lo utilizzano — passare `0` o `null`. |

| Tipo di calcolo | Comportamento | Parametri relativi all'elemento di base |
| --- | --- | --- |
| `Normal` | Nessun calcolo secondario; il valore aggregato viene visualizzato invariato (predefinito). | — |
| `DifferenceFrom` | Visualizza il valore come differenza rispetto al valore di un elemento di base in un campo di base. | `baseField` + `baseItem` (un indice o una didascalia, oppure il valore sentinella per l'elemento precedente o successivo) |
| `PercentageOf` | Visualizza il valore come percentuale del valore di un elemento di base in un campo di base. | `baseField` + `baseItem` (un indice o una didascalia, oppure il valore sentinella per l'elemento precedente o successivo) |
| `PercentageDifferenceFrom` | Visualizza il valore come differenza percentuale rispetto al valore di un elemento di base in un campo di base. | `baseField` + `baseItem` (un indice o una didascalia, oppure il valore sentinella per l'elemento precedente o successivo) |
| `RunningTotalIn` | Visualizza il valore come totale cumulativo per i successivi elementi di un campo di base. | `baseField` (il campo il cui ordine degli elementi determina l'accumulamento) |
| `PercentageOfRow` | Visualizza il valore come percentuale del totale di riga. | — |
| `PercentageOfColumn` | Visualizza il valore come percentuale del totale di colonna. | — |
| `PercentageOfTotal` | Visualizza il valore come percentuale del totale complessivo. | — |
| `Index` | Visualizza il valore usando la formula dell'indice di Excel ((valore * totale complessivo) / (totale di riga * totale di colonna)). | — |
| `PercentageOfParentRowTotal` | Visualizza il valore come percentuale del totale della riga padre (per campi di riga nidificati). | — |
| `PercentageOfParentColumnTotal` | Visualizza il valore come percentuale del totale della colonna padre (per campi di colonna nidificati). | — |
| `PercentageOfParentTotal` | Visualizza il valore come percentuale del totale dell'elemento padre. | `baseField` (il campo padre il cui totale funge da riferimento) |
| `PercentageOfRunningTotalIn` | Visualizza il valore come percentuale di un totale cumulativo in un campo di base. | `baseField` (il campo di accumulo) |
| `RankSmallestToLargest` | Classifica il valore dal più piccolo (1) al più grande. | `baseField` (il campo i cui elementi definiscono l'ambito della classifica) |
| `RankLargestToSmallest` | Classifica il valore dal più grande (1) al più piccolo. | `baseField` (il campo i cui elementi definiscono l'ambito della classifica) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` scrive lo stato rappresentato da `PivotShowValuesSetting` (`ShowValuesAs`, `BaseFieldIndex`, `BaseItemIndex`): il metodo e l'oggetto restituito dalla proprietà sono due modi per configurare lo stesso stato, in modo analogo ai controlli di selezione del campo e dell'elemento di base nella finestra di dialogo Mostra valori come di Excel.
{{% /alert %}}

## **Mostra i valori come percentuale del totale**
Chiamare il metodo `PivotField.ShowValuesAs` con `PivotShowValuesAsType.PercentageOfTotal` per trasformare ogni cella relativa a un campo dati, incluso il totale complessivo, nella rispettiva quota del totale complessivo. I numeri visualizzati rappresentano quindi proporzioni dell'intero insieme di risultati. Questo formato confronta ogni valore soltanto con il totale complessivo; pertanto non richiede alcun campo di base né alcun elemento di base. Gli argomenti finali (`0`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri riportata sopra.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Amount");
string[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.Length; i++)
{
    dataSheet.Cells[i + 1, 0].PutValue(fruits[i]);
    dataSheet.Cells[i + 1, 1].PutValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.Worksheets.Add();
PivotTable pivotTable = workbook.Worksheets[pivotSheetIndex].PivotTables.Add("=Sheet1!A1:B7", 2, 2);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Ottenere e configurare PivotField.ShowValuesSetting**
Per leggere la configurazione corrente, utilizzare `PivotField.ShowValuesSetting`: la proprietà di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui proprietà descrivono il calcolo attualmente applicato tramite Mostra valori come. Per modificare la configurazione, chiamare il metodo `PivotField.ShowValuesAs`: il metodo scrive tutte le impostazioni con una singola chiamata, quindi non è necessario assegnare le proprietà singolarmente.
L'oggetto `PivotShowValuesSetting` espone lo stato impostato da `ShowValuesAs`:
- `ShowValuesAs` seleziona il calcolo secondario `PivotShowValuesAsType`.
- `BaseFieldIndex` specifica l'indice a base zero del campo di base tra i campi della tabella pivot. Viene utilizzato dai formati basati sul campo di base.
- `BaseItemIndex` specifica l'elemento di base: un indice a base zero di un elemento specifico della tabella pivot oppure uno dei due valori sentinella, `PivotShowValuesSetting.PreviousPivotItem` (-1) per l'elemento precedente e `PivotShowValuesSetting.NextPivotItem` (-2) per quello successivo. Viene utilizzato dai formati basati sull'elemento di base.
- `BaseFieldName` e `BaseItemCaption` sono proprietà di sola lettura che espongono i valori risolti per il nome del campo di base e per la didascalia dell'elemento di base; ad esempio, dopo la selezione del valore sentinella per l'elemento precedente, `BaseItemCaption` restituisce `(previous)`.
Dopo aver chiamato `ShowValuesAs`, chiamare nuovamente `PivotTable.CalculateData()` affinché il corpo della tabella pivot venga ricalcolato e ridisegnato con la configurazione aggiornata.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"ShowValuesAs: {settings.ShowValuesAs}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
Console.WriteLine($"BaseFieldName: {settings.BaseFieldName}");
Console.WriteLine($"BaseItemCaption: {settings.BaseItemCaption}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotShowValuesAsType.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotShowValuesSetting.PreviousPivotItem);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"ShowValuesAs now: {dataField.ShowValuesSetting.ShowValuesAs}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Articoli correlati**
- [Gestione dei campi valore in una tabella pivot](/cells/it/net/manage-value-fields/)
- [Utilizzo dei formati di visualizzazione dei dati di DataField in una tabella pivot](/cells/it/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Aggiornamento di una tabella pivot](/cells/it/net/refresh-pivot-table/)
- [Applicazione di uno stile a una tabella pivot](/cells/it/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}