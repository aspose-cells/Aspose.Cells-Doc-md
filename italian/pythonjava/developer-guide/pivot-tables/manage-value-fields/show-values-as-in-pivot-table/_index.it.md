---
title: Mostra valori come nella tabella pivot
description: Visualizza i valori dei campi dati di una tabella pivot come percentuale del totale, differenza da un elemento di base, totali cumulativi, ranghi e altro con Aspose.Cells for Python via Java.
linktitle: Show Values As
keywords: Aspose.Cells, tabella pivot, mostra valori come, formato di visualizzazione dati, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python via Java
type: docs
weight: 145
url: /it/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot normalmente aggrega ciascun campo dati con una funzione di aggregazione come `Sum` o `Count`. La funzionalità **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da tale aggregato — ad esempio, una percentuale del totale generale, un totale cumulativo, una differenza da un elemento di base scelto o un rango — così è possibile eseguire analisi comparative senza formule di supporto o colonne calcolate.
Gli usi tipici includono l'analisi della quota rispetto al totale, comprese le percentuali di una riga, colonna o totale generale; la rendicontazione cumulativa usando un totale cumulativo in un campo periodo; l'analisi delle variazioni rispetto a un elemento di riferimento mediante differenza da o differenza percentuale da un elemento di base; e la classificazione dei valori dal più piccolo al più grande o dal più grande al più piccolo.
In Aspose.Cells for Python via Java, `PivotFieldDataDisplayFormat` seleziona il calcolo secondario. Il metodo di sola lettura `PivotField.getShowValuesSetting()` restituisce un oggetto `PivotShowValuesSetting`, i cui metodi scrivibili `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` e `setBaseItemIndex` configurano il comportamento; il metodo di convenienza `PivotField.showValuesAs(...)` applica le stesse quattro impostazioni in una sola chiamata. Applica queste impostazioni a un campo dati o valore ottenuto da `PivotTable.getDataFields()`.

## **Membri dell'enumerazione PivotFieldDataDisplayFormat**
Il campo dati conserva la propria funzione di aggregazione, come Sum o Count, mentre Show Values As trasforma solo il modo in cui il valore aggregato viene visualizzato.  
Oltre a impostare direttamente le proprietà di `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di convenienza a chiamata unica applica la stessa configurazione:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    PivotField,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.showValuesAs(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
jpype.shutdownJVM()
```

| Parameter | Meaning | When It Is Required |
| --- | --- | --- |
| `displayFormat` | Il calcolo secondario `PivotFieldDataDisplayFormat` da applicare. | Sempre. |
| `baseField` | Indice basato su zero del campo base tra i campi base della tabella pivot (ad esempio, l'indice del campo riga a cui appartiene l'elemento base). | Solo per i sei formati a base di riferimento riportati di seguito (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); ignorato da ogni altro formato. |
| `baseItemPositionType` | Come viene scelto l'elemento base rispetto all'elemento corrente: `PivotItemPositionType.Previous`, `.Next` o `.Custom`. | Solo per i tre formati con elemento di base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); ignorato da ogni altro formato. |
| `baseItem` | Indice basato su zero dell'elemento base. | Solo quando `baseItemPositionType` è `Custom` (l'indice dell'elemento sceglie l'elemento base esatto); ignorato per `Previous` / `Next` e da tutti i formati non basati su elemento — passare `0`. |

| Tipo di calcolo | Comportamento | Parametri elemento base |
| --- | --- | --- |
| `Normal` | Nessun calcolo secondario; il valore aggregato è visualizzato così com'è (predefinito). | — |
| `DifferenceFrom` | Visualizza il valore come differenza rispetto al valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageOf` | Visualizza il valore come percentuale del valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageDifferenceFrom` | Visualizza il valore come differenza percentuale dal valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `RunningTotalIn` | Visualizza il valore come totale cumulativo per gli elementi successivi di un campo base. | `baseField` (il campo il cui ordine degli elementi guida l'accumulazione) |
| `PercentageOfRow` | Visualizza il valore come percentuale del totale della riga. | — |
| `PercentageOfColumn` | Visualizza il valore come percentuale del totale della colonna. | — |
| `PercentageOfTotal` | Visualizza il valore come percentuale del totale generale. | — |
| `Index` | Visualizza il valore usando la formula di indice di Excel ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Visualizza il valore come percentuale del totale della riga padre (per campi riga nidificati). | — |
| `PercentageOfParentColumnTotal` | Visualizza il valore come percentuale del totale della colonna padre (per campi colonna nidificati). | — |
| `PercentageOfParentTotal` | Visualizza il valore come percentuale del totale del padre. | `baseField` (il campo padre di riferimento) |
| `PercentageOfRunningTotalIn` | Visualizza il valore come percentuale di un totale cumulativo in un campo base. | `baseField` (il campo di accumulazione) |
| `RankSmallestToLargest` | Classifica il valore dal più piccolo (1) al più grande. | — |
| `RankLargestToSmallest` | Classifica il valore dal più grande (1) al più piccolo. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` scrive i valori di `PivotShowValuesSetting` tramite `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` e `setBaseItemIndex` — il metodo e l'oggetto impostazione sono due modi per configurare lo stesso stato, rispecchiando i selettori di campo base e elemento base nella finestra di dialogo Show Values As di Excel.
{{% /alert %}}

## **Mostra valori come percentuale del totale**
Chiama il metodo `PivotField.showValuesAs` con `PivotFieldDataDisplayFormat.PercentageOfTotal` per convertire ogni cella di campo dati, inclusa la totalizzazione generale, nella sua quota del totale generale. I numeri visualizzati sono quindi letti come proporzioni dell'intero insieme di risultati. Questo formato misura ogni valore solo rispetto al totale generale, quindi non richiede né campo base né elemento base — gli argomenti finali (`0`, `PivotItemPositionType.Previous`, `0`) sono segnaposti che il formato ignora, come indicato nella tabella dei parametri sopra.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotTable,
    PivotField,
    PivotFieldType,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.getCells().get(i + 1, 0).putValue(fruits[i])
    data_sheet.getCells().get(i + 1, 1).putValue(amounts[i])
# Add a pivot table on a new worksheet (getWorksheets().add() returns the sheet index)
pivot_sheet_index = workbook.getWorksheets().add()
pivot_table = workbook.getWorksheets().get(pivot_sheet_index).getPivotTables().add("=Sheet1!A1:B7", 2, 2)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Ottieni e configura PivotField.getShowValuesSetting()**
Leggi la configurazione corrente tramite `PivotField.getShowValuesSetting()`: il metodo di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui quattro proprietà descrivono il calcolo Show Values As attivo. Per modificare la configurazione, chiama il metodo `PivotField.showValuesAs` — scrive tutte e quattro le impostazioni in una sola chiamata, così non è necessario assegnare le proprietà una per una.
L'oggetto `PivotShowValuesSetting` espone le quattro proprietà che `showValuesAs` scrive:
- `getCalculationType()` restituisce il calcolo secondario `PivotFieldDataDisplayFormat`, mentre `setCalculationType(...)` lo cambia.
- `getBaseFieldIndex()` e `setBaseFieldIndex(...)` specificano l'indice basato su zero del campo base all'interno dei campi pivot. È usato dai formati a base di riferimento.
- `getBaseItemPositionType()` e `setBaseItemPositionType(...)` determinano come l'elemento base è posizionato rispetto all'elemento corrente e accettano `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` o `PivotItemPositionType.Custom`.
- `getBaseItemIndex()` e `setBaseItemIndex(...)` specificano l'indice basato su zero dell'elemento base e sono usati quando `BaseItemPositionType` è `Custom`.
Dopo aver chiamato `showValuesAs`, richiama nuovamente `PivotTable.calculateData()` affinché il corpo della tabella pivot venga ricalcolato e renderizzato con la configurazione aggiornata.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"CalculationType: {settings.getCalculationType()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemPositionType: {settings.getBaseItemPositionType()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.getShowValuesSetting().getCalculationType()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Articoli correlati**
- [Gestire i campi valore nella Tabella Pivot](/cells/it/python-java/manage-value-fields/)
- [Aggiornare la Tabella Pivot](/cells/it/python-java/refresh-pivot-table/)
- [Applicare lo stile alla Tabella Pivot](/cells/it/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}