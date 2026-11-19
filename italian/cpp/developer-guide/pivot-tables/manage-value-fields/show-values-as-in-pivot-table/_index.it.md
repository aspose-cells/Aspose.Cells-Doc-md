---
title: Mostra valori come in una tabella pivot in Aspose.Cells for C++
linktitle: Mostra valori come in una tabella pivot
description: Visualizza i valori dei campi dati di una tabella pivot in varie forme, ad esempio come percentuale del totale, come differenza da un elemento di base, come totale progressivo o come classifica, con Aspose.Cells for C++.
keywords: Aspose.Cells, C++, tabella pivot, mostra valori come, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /it/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot normalmente aggrega ogni campo dati mediante una funzione di aggregazione come `Sum` o `Count`. La funzione **Mostra valori come** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da tale aggregazione, ad esempio una percentuale del totale complessivo, un totale progressivo, una differenza da un elemento di base selezionato o una classificazione, consentendo di eseguire analisi comparative senza formule ausiliarie o colonne calcolate.
Gli utilizzi tipici includono l'analisi della quota del totale, comprese le percentuali di riga, di colonna o del totale complessivo; la generazione di report cumulativi mediante un totale progressivo in un campo di periodo; l'analisi della varianza rispetto a un elemento di riferimento mediante differenza o differenza percentuale da un elemento di base; e la classificazione dei valori dal più piccolo al più grande o dal più grande al più piccolo.
In Aspose.Cells for C++, l'enumerazione `PivotShowValuesAsType` seleziona il calcolo secondario. Il metodo di accesso `PivotField.GetShowValuesSetting()` restituisce un oggetto `PivotShowValuesSetting`, i cui metodi `SetShowValuesAs`, `SetBaseFieldIndex` e `SetBaseItemIndex` configurano il comportamento. Il metodo `PivotField.ShowValuesAs(...)` costituisce un'alternativa per applicare le stesse impostazioni in una singola chiamata. Le impostazioni devono essere applicate a un campo dati o a un campo valore ottenuto da `PivotTable.GetDataFields()`.

## **Membri dell'enumerazione PivotShowValuesAsType**
Il campo dati mantiene la propria funzione di aggregazione, come `Sum` o `Count`, mentre Mostra valori come modifica esclusivamente la modalità di visualizzazione del valore aggregato.
Oltre all'impostazione diretta dei valori `PivotShowValuesSetting` (vedere l'ultima sezione), è disponibile un metodo di convenienza che applica la stessa configurazione con una singola chiamata. Sono disponibili due forme: una che identifica il campo di base e l'elemento di base mediante indice e l'altra mediante nome:

```cpp
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int32_t baseField, int32_t baseItem);
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, const U16String& baseField, const U16String& baseItem);
// index form: PivotShowValuesAsType::PercentageOfTotal, 0, 0
// name form:  PivotShowValuesAsType::PercentageOf, u"Fruit", u"Apple"
```

| Parametro | Significato | Quando è obbligatorio |
| --- | --- | --- |
| `showValuesAsType` | Il tipo di calcolo secondario `PivotShowValuesAsType` da applicare. | Sempre. |
| `baseField` | Indice a base zero del campo di base tra i campi di base della tabella pivot (ad esempio, l'indice del campo di riga a cui appartiene l'elemento di base) oppure, nella forma basata sul nome, il nome del campo di base. | Per gli otto formati relativi alla base elencati di seguito (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); per tutti gli altri formati, passare `0` (o un `U16String` vuoto nella forma basata sul nome). |
| `baseItem` | Indice a base zero dell'elemento di base, con due valori sentinella: -1 seleziona l'elemento precedente e -2 quello successivo (l'API C++ non definisce costanti nominate per i valori sentinella, pertanto occorre passare i valori letterali). Nella forma basata sul nome, il parametro accetta la didascalia dell'elemento di base; occorre passare un `U16String` vuoto quando il formato selezionato non richiede alcun elemento di base. | Solo per i tre formati basati sull'elemento di base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`), che valutano l'elemento di base; i cinque formati relativi al campo (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, entrambe le classificazioni) lo ignorano, pertanto occorre passare `0` o un `U16String` vuoto. |

| Tipo di calcolo | Comportamento | Parametri relativi alla base |
| --- | --- | --- |
| `Normal` | Nessun calcolo secondario; il valore aggregato viene visualizzato invariato (predefinito). | — |
| `DifferenceFrom` | Visualizza il valore come differenza rispetto al valore di un elemento di base in un campo di base. | `baseField` + `baseItem` (un indice o una didascalia, oppure il valore sentinella dell'elemento precedente o successivo) |
| `PercentageOf` | Visualizza il valore come percentuale del valore di un elemento di base in un campo di base. | `baseField` + `baseItem` (un indice o una didascalia, oppure il valore sentinella dell'elemento precedente o successivo) |
| `PercentageDifferenceFrom` | Visualizza il valore come differenza percentuale rispetto al valore di un elemento di base in un campo di base. | `baseField` + `baseItem` (un indice o una didascalia, oppure il valore sentinella dell'elemento precedente o successivo) |
| `RunningTotalIn` | Visualizza il valore come totale progressivo per gli elementi successivi di un campo di base. | `baseField` (il campo il cui ordine degli elementi determina l'accumulamento) |
| `PercentageOfRow` | Visualizza il valore come percentuale del totale della riga. | — |
| `PercentageOfColumn` | Visualizza il valore come percentuale del totale della colonna. | — |
| `PercentageOfTotal` | Visualizza il valore come percentuale del totale complessivo. | — |
| `Index` | Visualizza il valore utilizzando la formula dell'indice di Excel ((valore * totale complessivo) / (totale della riga * totale della colonna)). | — |
| `PercentageOfParentRowTotal` | Visualizza il valore come percentuale del totale della riga padre (per campi di riga annidati). | — |
| `PercentageOfParentColumnTotal` | Visualizza il valore come percentuale del totale della colonna padre (per campi di colonna annidati). | — |
| `PercentageOfParentTotal` | Visualizza il valore come percentuale del totale del campo padre. | `baseField` (il campo padre il cui totale viene utilizzato come riferimento) |
| `PercentageOfRunningTotalIn` | Visualizza il valore come percentuale di un totale progressivo in un campo di base. | `baseField` (il campo di accumulo) |
| `RankSmallestToLargest` | Classifica il valore dal più piccolo (1) al più grande. | `baseField` (il campo i cui elementi definiscono l'ambito della classificazione) |
| `RankLargestToSmallest` | Classifica il valore dal più grande (1) al più piccolo. | `baseField` (il campo i cui elementi definiscono l'ambito della classificazione) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` imposta i valori `PivotShowValuesSetting` (`ShowValuesAs`, `BaseFieldIndex` e `BaseItemIndex`); il metodo e l'oggetto delle impostazioni sono due modi per configurare lo stesso stato, corrispondenti ai selettori del campo di base e dell'elemento di base nella finestra Mostra valori come di Excel.
{{% /alert %}}

## **Mostra valori come percentuale del totale**
Chiamare il metodo `PivotField.ShowValuesAs` con `PivotShowValuesAsType::PercentageOfTotal` per rappresentare ogni cella del campo dati, compreso il totale complessivo, come quota del totale complessivo. I numeri visualizzati rappresentano quindi proporzioni dell'insieme completo dei risultati. Questo formato confronta ogni valore esclusivamente con il totale complessivo; pertanto non richiede né un campo di base né un elemento di base. I segnaposto finali (`0`, `0`) vengono ignorati dal formato, come indicato nella tabella dei parametri.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load or create a workbook with source data
    Workbook workbook;
    Worksheet dataSheet = workbook.GetWorksheets().Get(0);
    Cells cells = dataSheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Fruit"));
    cells.Get(0, 1).PutValue(U16String("Amount"));
    const char* fruits[6] = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
    int32_t amounts[6] = { 10, 20, 30, 40, 50, 60 };
    for (int32_t i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(amounts[i]);
    }
    // Add a pivot table on a new worksheet
    int32_t pivotSheetIndex = workbook.GetWorksheets().Add();
    PivotTable pivotTable = workbook.GetWorksheets().Get(pivotSheetIndex).GetPivotTables().Add(u"=Sheet1!A1:B7", 2, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Show the Amount data field as a percentage of the grand total with the
    // one-call method; PercentageOfTotal takes no base item, so the trailing
    // base arguments (0, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotShowValuesAsType::PercentageOfTotal, 0, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Ottenere e configurare PivotField.ShowValuesSetting**
Leggere la configurazione corrente tramite `PivotField.GetShowValuesSetting()`: il metodo restituisce l'oggetto `PivotShowValuesSetting` del campo, i cui metodi di lettura descrivono il calcolo secondario Mostra valori come attivo. Per modificare la configurazione, chiamare il metodo `PivotField.ShowValuesAs`, che imposta tutte le opzioni in una singola chiamata e consente di evitare di impostarle singolarmente.
L'oggetto `PivotShowValuesSetting` espone lo stato impostato da `ShowValuesAs`:
- `GetShowValuesAs()` / `SetShowValuesAs()` selezionano il calcolo secondario `PivotShowValuesAsType`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` specificano l'indice a base zero del campo di base tra i campi della tabella pivot. L'indice è utilizzato dai formati relativi alla base.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` specificano l'elemento di base: l'indice a base zero di un elemento specifico della tabella pivot oppure uno dei due valori sentinella, -1 per l'elemento precedente e -2 per quello successivo (l'API C++ non definisce costanti nominate per i valori sentinella). L'elemento è utilizzato dai formati basati sull'elemento di base.
- `GetBaseFieldName()` e `GetBaseItemCaption()` forniscono viste di sola lettura del nome risolto del campo di base e della didascalia dell'elemento di base; ad esempio, dopo aver selezionato il valore sentinella dell'elemento precedente, `GetBaseItemCaption()` restituisce `(previous)`.
Dopo aver chiamato `ShowValuesAs`, chiamare nuovamente `PivotTable.CalculateData()` affinché il corpo della tabella pivot venga ricalcolato e ridisegnato con la configurazione aggiornata.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"ShowValuesAsPercentageOfTotal.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(1).GetPivotTables().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    // Read the current show-values settings
    PivotShowValuesSetting settings = dataField.GetShowValuesSetting();
    std::cout << "ShowValuesAs: " << static_cast<int32_t>(settings.GetShowValuesAs()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    std::cout << "BaseFieldName: " << settings.GetBaseFieldName().ToUtf8() << std::endl;
    std::cout << "BaseItemCaption: " << settings.GetBaseItemCaption().ToUtf8() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    // (-1 is the previous-item sentinel; no named constant exists in C++)
    dataField.ShowValuesAs(PivotShowValuesAsType::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), -1);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "ShowValuesAs now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetShowValuesAs()) << std::endl;
    std::cout << "BaseItemCaption now: " << dataField.GetShowValuesSetting().GetBaseItemCaption().ToUtf8() << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Articoli correlati**
- [Gestione dei campi valore nella tabella pivot](/cells/it/cpp/manage-value-fields/)
- [Aggiornamento della tabella pivot](/cells/it/cpp/refresh-pivot-table/)
- [Applicazione di uno stile alla tabella pivot](/cells/it/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}