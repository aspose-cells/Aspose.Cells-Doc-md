---
title: Mostra valori come nella Tabella Pivot in Aspose.Cells for C++
linktitle: Mostra valori come nella Tabella Pivot
description: Visualizza i valori del campo dati della tabella pivot come percentuale del totale, differenza da un elemento base, totali cumulativi, ranghi e altro con Aspose.Cells for C++.
keywords: Aspose.Cells, C++, Tabella Pivot, mostra valori come, formato visualizzazione dati, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /it/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scenari di utilizzo possibili**
Una tabella pivot aggrega normalmente ogni campo dati con una funzione di aggregazione come `Sum` o `Count`. La funzionalità **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da tale aggregato — ad esempio, una percentuale del totale globale, un totale cumulativo, una differenza da un elemento base scelto o un rango — consentendo di eseguire analisi comparative senza formule di supporto o colonne calcolate.  
Gli usi tipici includono l'analisi della quota sul totale, comprese le percentuali di una riga, colonna o totale globale; reportistica cumulativa mediante totale in corso in un campo di periodo; analisi della varianza rispetto a un elemento di riferimento usando la differenza da o la differenza percentuale da un elemento base; e la classificazione dei valori dal più piccolo al più grande o viceversa.

## **Membri dell'enumerazione PivotFieldDataDisplayFormat**
Il campo dati conserva la sua funzione di aggregazione, ad esempio Sum o Count, mentre Show Values As trasforma solo il modo in cui il valore aggregato viene visualizzato.  
Oltre a impostare direttamente i valori di `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di comodità con una sola chiamata applica la stessa configurazione:

```cpp
void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int32_t baseField, PivotItemPositionType baseItemPositionType, int32_t baseItem);
```

| Parametro | Significato | Quando è obbligatorio |
| --- | --- | --- |
| `displayFormat` | Il calcolo secondario `PivotFieldDataDisplayFormat` da applicare. | Sempre. |
| `baseField` | Indice basato su zero del campo base tra i campi base della tabella pivot (ad esempio, l'indice del campo riga a cui appartiene l'elemento base). | Solo per i sei formati a base di riferimento riportati di seguito (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); ignorato da ogni altro formato. |
| `baseItemPositionType` | Come viene scelto l'elemento base rispetto all'elemento corrente: `PivotItemPositionType::Previous`, `::Next` o `::Custom`. | Solo per i tre formati con elemento di base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); ignorato da ogni altro formato. |
| `baseItem` | Indice basato su zero dell'elemento base. | Solo quando `baseItemPositionType` è `Custom` (l'indice specifica l'elemento base esatto); ignorato per `Previous` / `Next` e per tutti i formati non basati su elemento — passare `0`. |

| Tipo di calcolo | Comportamento | Parametri elemento base |
| --- | --- | --- |
| `Normal` | Nessun calcolo secondario; il valore aggregato viene visualizzato così com'è (predefinito). | — |
| `DifferenceFrom` | Visualizza il valore come differenza rispetto al valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageOf` | Visualizza il valore come percentuale del valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageDifferenceFrom` | Visualizza il valore come differenza percentuale rispetto al valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `RunningTotalIn` | Visualizza il valore come totale cumulativo per gli elementi successivi di un campo base. | `baseField` (il campo il cui ordine di elementi guida l'accumulazione) |
| `PercentageOfRow` | Visualizza il valore come percentuale del totale della riga. | — |
| `PercentageOfColumn` | Visualizza il valore come percentuale del totale della colonna. | — |
| `PercentageOfTotal` | Visualizza il valore come percentuale del totale globale. | — |
| `Index` | Visualizza il valore usando la formula di indice di Excel ((valore * totale globale) / (totale riga * totale colonna)). | — |
| `PercentageOfParentRowTotal` | Visualizza il valore come percentuale del totale della riga padre (per campi riga nidificati). | — |
| `PercentageOfParentColumnTotal` | Visualizza il valore come percentuale del totale della colonna padre (per campi colonna nidificati). | — |
| `PercentageOfParentTotal` | Visualizza il valore come percentuale del totale del padre. | `baseField` (il campo padre di riferimento) |
| `PercentageOfRunningTotalIn` | Visualizza il valore come percentuale di un totale cumulativo in un campo base. | `baseField` (il campo di accumulazione) |
| `RankSmallestToLargest` | Assegna un rango al valore dal più piccolo (1) al più grande. | — |
| `RankLargestToSmallest` | Assegna un rango al valore dal più grande (1) al più piccolo. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` scrive i valori di `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — il metodo e l'oggetto impostazioni sono due modi per configurare lo stesso stato, rispecchiando i selettori di campo base ed elemento base nella finestra di dialogo **Show Values As** di Excel.
{{% /alert %}}

## **Mostra valori come percentuale del totale**
Chiama il metodo `PivotField.ShowValuesAs` con `PivotFieldDataDisplayFormat::PercentageOfTotal` per convertire ogni cella del campo dati, incluso il totale globale, nella sua quota del totale globale. I numeri visualizzati quindi rappresentano proporzioni dell'insieme completo dei risultati. Questo formato confronta ogni valore solo con il totale globale, quindi non richiede né campo base né elemento base — gli argomenti finali (`0`, `PivotItemPositionType::Previous`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri sopra.

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
    // base arguments (0, Previous, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::PercentageOfTotal, 0, PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Ottieni e configura PivotField.ShowValuesSetting**
Leggi la configurazione corrente tramite `PivotField.GetShowValuesSetting()`: l'accessor restituisce l'oggetto `PivotShowValuesSetting` del campo, il cui quattro metodi getter descrivono il calcolo Show Values As attivo. Per modificare la configurazione, chiama il metodo `PivotField.ShowValuesAs` — scrive tutte e quattro le impostazioni in una sola chiamata, così non è necessario assegnare i valori uno per uno.  
L'oggetto `PivotShowValuesSetting` espone i quattro valori che `ShowValuesAs` scrive:
- `GetCalculationType()` / `SetCalculationType()` selezionano il calcolo secondario `PivotFieldDataDisplayFormat`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` specificano l'indice basato su zero del campo base all'interno dei campi pivot. Viene usato dai formati a base di riferimento.
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` determinano come l'elemento base è posizionato rispetto all'elemento corrente e accettano `PivotItemPositionType::Next`, `PivotItemPositionType::Previous` o `PivotItemPositionType::Custom`.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` specificano l'indice basato su zero dell'elemento base e sono usati quando il tipo di posizione è `Custom`.
Dopo aver chiamato `ShowValuesAs`, richiama nuovamente `PivotTable.CalculateData()` affinché il corpo della tabella pivot venga ricalcolato e ridisegnato con la configurazione aggiornata.

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
    std::cout << "CalculationType: " << static_cast<int32_t>(settings.GetCalculationType()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemPositionType: " << static_cast<int32_t>(settings.GetBaseItemPositionType()) << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "CalculationType now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetCalculationType()) << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Articoli correlati**
- [Gestione dei campi valore nella Tabella Pivot](/cells/it/cpp/manage-value-fields/)
- [Aggiornamento della Tabella Pivot](/cells/it/cpp/refresh-pivot-table/)
- [Applicazione di stile alla Tabella Pivot](/cells/it/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}