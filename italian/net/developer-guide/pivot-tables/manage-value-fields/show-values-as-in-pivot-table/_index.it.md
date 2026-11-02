---
title: Mostra valori come nella tabella pivot
linktitle: Mostra valori come nella tabella pivot
description: Visualizza i valori dei campi dati della tabella pivot come percentuale del totale, differenza da un elemento base, totali cumulativi, classifiche e altro con Aspose.Cells per .NET.
keywords: Aspose.Cells, tabella pivot, mostra valori come, formato di visualizzazione dei dati, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C#
type: docs
weight: 145
url: /it/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
Una tabella pivot aggrega normalmente ciascun campo dati con una funzione di aggregazione come `Sum` o `Count`. La funzionalità **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da tale aggregato — ad esempio, una percentuale del totale complessivo, un totale cumulativo, una differenza rispetto a un elemento base scelto o una classifica — in modo da poter eseguire analisi comparative senza formule di supporto o colonne calcolate.  
Gli usi tipici includono l'analisi della quota rispetto al totale, comprese le percentuali di riga, colonna o totale complessivo; la reportistica cumulativa utilizzando un totale cumulativo in un campo periodico; l'analisi della varianza rispetto a un elemento di riferimento tramite differenza da o differenza percentuale da un elemento base; e la classificazione dei valori dal più piccolo al più grande o viceversa.  
In Aspose.Cells per .NET, `PivotFieldDataDisplayFormat` seleziona il calcolo secondario. La proprietà in sola lettura `PivotField.ShowValuesSetting` restituisce un oggetto `PivotShowValuesSetting`, le cui proprietà modificabili `CalculationType`, `BaseFieldIndex`, `BaseItemPositionType` e `BaseItemIndex` configurano il comportamento; il metodo di comodità `PivotField.ShowValuesAs(...)` applica le stesse quattro impostazioni in una singola chiamata. Applica queste impostazioni a un campo dati o valore ottenuto da `PivotTable.DataFields`.

## **Membri dell'enumerazione PivotFieldDataDisplayFormat**
Il campo dati mantiene la sua funzione di aggregazione, come Sum o Count, mentre Show Values As trasforma solo il modo in cui il valore aggregato viene visualizzato. Oltre a scrivere direttamente le proprietà `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di comodità a chiamata singola applica la stessa configurazione:

```csharp
public void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField, PivotItemPositionType baseItemPositionType, int baseItem)
```

| Parametro | Significato | Quando è richiesto |
| --- | --- | --- |
| `displayFormat` | Il calcolo secondario `PivotFieldDataDisplayFormat` da applicare. | Sempre. |
| `baseField` | Indice basato su zero del campo base tra i campi base della tabella pivot (ad es., l'indice del campo di riga a cui appartiene l'elemento base). | Solo per i sei formati a base di riferimento riportati di seguito (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); ignorato da ogni altro formato. |
| `baseItemPositionType` | Come viene scelto l'elemento base rispetto all'elemento corrente: `PivotItemPositionType.Previous`, `.Next` o `.Custom`. | Solo per i tre formati con elemento di base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); ignorato da ogni altro formato. |
| `baseItem` | Indice basato su zero dell'elemento base. | Solo quando `baseItemPositionType` è `Custom` (l'indice dell'elemento sceglie l'elemento base esatto); ignorato per `Previous` / `Next` e da tutti i formati non basati su elemento — passare `0`. |

| Tipo di calcolo | Comportamento | Parametri dell'elemento base |
| --- | --- | --- |
| `Normal` | Nessun calcolo secondario; il valore aggregato viene visualizzato così com'è (predefinito). | — |
| `DifferenceFrom` | Visualizza il valore come differenza dal valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageOf` | Visualizza il valore come percentuale del valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageDifferenceFrom` | Visualizza il valore come differenza percentuale dal valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `RunningTotalIn` | Visualizza il valore come totale cumulativo per gli elementi successivi di un campo base. | `baseField` (il campo il cui ordine degli elementi guida l'accumulazione) |
| `PercentageOfRow` | Visualizza il valore come percentuale del totale della riga. | — |
| `PercentageOfColumn` | Visualizza il valore come percentuale del totale della colonna. | — |
| `PercentageOfTotal` | Visualizza il valore come percentuale del totale complessivo. | — |
| `Index` | Visualizza il valore usando la formula indice di Excel ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Visualizza il valore come percentuale del totale della riga padre (per campi riga annidati). | — |
| `PercentageOfParentColumnTotal` | Visualizza il valore come percentuale del totale della colonna padre (per campi colonna annidati). | — |
| `PercentageOfParentTotal` | Visualizza il valore come percentuale del totale padre. | `baseField` (il campo padre di riferimento) |
| `PercentageOfRunningTotalIn` | Visualizza il valore come percentuale di un totale cumulativo in un campo base. | `baseField` (il campo di accumulazione) |
| `RankSmallestToLargest` | Classifica il valore dal più piccolo (1) al più grande. | — |
| `RankLargestToSmallest` | Classifica il valore dal più grande (1) al più piccolo. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` scrive le proprietà `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — il metodo e l'oggetto proprietà sono due modi per configurare lo stesso stato, replicando i selettori di campo base e di elemento base nella finestra di dialogo Show Values As di Excel.
{{% /alert %}}

## **Mostra valori come percentuale del totale**
Chiama il metodo `PivotField.ShowValuesAs` con `PivotFieldDataDisplayFormat.PercentageOfTotal` per convertire ogni cella del campo dati, incluso il totale complessivo, nella sua quota del totale complessivo. I numeri visualizzati quindi rappresentano proporzioni dell'intero set di risultati. Questo formato misura ogni valore solo rispetto al totale complessivo, quindi non richiede né campo base né elemento base — gli argomenti finali (`0`, `PivotItemPositionType.Previous`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri sopra.

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
// base arguments (0, Previous, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.PercentageOfTotal, 0, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Recupera e configura PivotField.ShowValuesSetting**
Leggi la configurazione attuale tramite `PivotField.ShowValuesSetting`: la proprietà in sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui quattro proprietà descrivono il calcolo Show Values As attivo. Per modificare la configurazione, chiama il metodo `PivotField.ShowValuesAs` — scrive tutte e quattro le impostazioni in una singola chiamata, così non è necessario assegnare le proprietà una per una.  
L'oggetto `PivotShowValuesSetting` espone le quattro proprietà scritte da `ShowValuesAs`:
- `CalculationType` seleziona il calcolo secondario `PivotFieldDataDisplayFormat`.
- `BaseFieldIndex` specifica l'indice basato su zero del campo base all'interno dei campi pivot. Viene utilizzato dai formati a base di riferimento.
- `BaseItemPositionType` determina come l'elemento base è posizionato rispetto all'elemento corrente e accetta `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` o `PivotItemPositionType.Custom`.
- `BaseItemIndex` specifica l'indice basato su zero dell'elemento base ed è usato quando `BaseItemPositionType` è `Custom`.
Dopo aver chiamato `ShowValuesAs`, chiama nuovamente `PivotTable.CalculateData()` affinché il corpo della pivot venga ricalcolato e ridisegnato con la configurazione aggiornata.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"CalculationType: {settings.CalculationType}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemPositionType: {settings.BaseItemPositionType}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"CalculationType now: {dataField.ShowValuesSetting.CalculationType}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Articoli correlati**
- [Gestione dei campi valore nella tabella pivot](/cells/it/net/manage-value-fields/)
- [Lavorare con i formati di visualizzazione dei dati di DataField nella tabella pivot](/cells/it/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Aggiornare la tabella pivot](/cells/it/net/refresh-pivot-table/)
- [Applicare lo stile alla tabella pivot](/cells/it/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}