---
title: Mostra Valori Come in Tabella Pivot
linktitle: Mostra Valori Come in Tabella Pivot
description: Visualizza i valori dei campi dati della tabella pivot come percentuale del totale, differenza da un elemento di base, totali cumulativi, ranghi e altro con Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, tabella pivot, mostra valori come, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, show_values_as, base_field_index, base_item_index, Python
type: docs
weight: 145
url: /it/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili Scenari d'Uso**
Una tabella pivot aggrega normalmente ogni campo dati con una funzione di aggregazione come `SUM` o `COUNT`. La funzionalità **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da quell'aggregato — ad esempio, una percentuale del totale generale, un totale cumulativo, una differenza da un elemento di base scelto o un rango — così è possibile eseguire analisi comparative senza formule di supporto o colonne calcolate.  
Gli utilizzi tipici includono l'analisi della quota del totale, comprese le percentuali di riga, colonna o totale generale; la reportistica cumulativa usando un totale cumulativo in un campo di periodo; l'analisi della variazione rispetto a un elemento di riferimento usando differenza o differenza percentuale da un elemento di base; e la classifica dei valori dal più piccolo al più grande o viceversa.  
In Aspose.Cells for Python via .NET, l'enumerazione `PivotShowValuesAsType` seleziona il calcolo secondario. La proprietà di sola lettura `PivotField.show_values_setting` restituisce un oggetto `PivotShowValuesSetting`, le cui proprietà scrivibili `show_values_as`, `base_field_index` e `base_item_index` configurano il comportamento; il metodo di convenienza `PivotField.show_values_as(...)` applica le stesse impostazioni in una sola chiamata. Applica queste impostazioni a un campo dati o valore ottenuto da `PivotTable.data_fields`.

## **Membri dell'Enumerazione PivotShowValuesAsType**
Il campo dati mantiene la sua funzione di aggregazione, come `SUM` o `COUNT`, mentre Show Values As trasforma solo il modo in cui il valore aggregato viene mostrato.  
Oltre a scrivere direttamente le proprietà di `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di convenienza a chiamata singola applica la stessa configurazione. Esso è disponibile in due forme — una che fa riferimento al campo base e all'elemento base per indice, l'altra per nome:

```python
from aspose.cells.pivot import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
```

| Parametro | Significato | Quando È Necessario |
| --- | --- | --- |
| `show_values_as_type` | Il calcolo secondario `PivotShowValuesAsType` da applicare. | Sempre. |
| `base_field` | Indice zero‑based del campo base tra i campi base della tabella pivot (ad esempio, l'indice del campo riga a cui appartiene l'elemento base), o — nella forma per nome — il nome del campo base. | Gli otto formati relativi al base elencati sotto (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); passare `0` (o `None` nella forma per nome) per tutti gli altri formati. |
| `base_item` | Indice zero‑based dell'elemento base, con due valori sentinella: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) seleziona l'elemento precedente e `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) quello successivo. Nella forma per nome si fornisce la didascalia dell'elemento base, e `None` quando il formato selezionato non richiede un elemento base. | Solo i tre formati basati su elemento (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) valutano l'elemento base; i cinque formati relativi al campo (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, entrambi i ranghi) lo ignorano — passare `0` o `None`. |

| Tipo di Calcolo | Comportamento | Parametri dell'Elemento Base |
| --- | --- | --- |
| `NORMAL` | Nessun calcolo secondario; il valore aggregato è mostrato così com'è (predefinito). | — |
| `DIFFERENCE_FROM` | Visualizza il valore come differenza dal valore di un elemento base in un campo base. | `base_field` + `base_item` (indice, didascalia o sentinella precedente/successiva) |
| `PERCENTAGE_OF` | Visualizza il valore come percentuale del valore di un elemento base in un campo base. | `base_field` + `base_item` (indice, didascalia o sentinella precedente/successiva) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visualizza il valore come differenza percentuale dal valore di un elemento base in un campo base. | `base_field` + `base_item` (indice, didascalia o sentinella precedente/successiva) |
| `RUNNING_TOTAL_IN` | Visualizza il valore come totale cumulativo per gli elementi successivi di un campo base. | `base_field` (campo il cui ordine di elementi guida l'accumulazione) |
| `PERCENTAGE_OF_ROW` | Visualizza il valore come percentuale del totale della riga. | — |
| `PERCENTAGE_OF_COLUMN` | Visualizza il valore come percentuale del totale della colonna. | — |
| `PERCENTAGE_OF_TOTAL` | Visualizza il valore come percentuale del totale generale. | — |
| `INDEX` | Visualizza il valore usando la formula di indice di Excel ((valore * totale generale) / (totale riga * totale colonna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visualizza il valore come percentuale del totale della riga padre (per campi riga nidificati). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visualizza il valore come percentuale del totale della colonna padre (per campi colonna nidificati). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visualizza il valore come percentuale del suo totale padre. | `base_field` (campo padre il cui totale è il riferimento) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visualizza il valore come percentuale di un totale cumulativo in un campo base. | `base_field` (campo di accumulazione) |
| `RANK_SMALLEST_TO_LARGEST` | Assegna un rango al valore dal più piccolo (1) al più grande. | `base_field` (campo i cui elementi definiscono l'ambito del ranking) |
| `RANK_LARGEST_TO_SMALLEST` | Assegna un rango al valore dal più grande (1) al più piccolo. | `base_field` (campo i cui elementi definiscono l'ambito del ranking) |

{{% alert color="primary" %}}
`show_values_as(...)` scrive le proprietà di `PivotShowValuesSetting` (`show_values_as`, `base_field_index`, `base_item_index`) — il metodo e l'oggetto proprietà sono due modi per configurare lo stesso stato, rispecchiando i selettori di campo base ed elemento base nella finestra di dialogo Show Values As di Excel.  
{{% /alert %}}

## **Mostra Valori come Percentuale del Totale**
Chiama il metodo `PivotField.show_values_as` con `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` per convertire ogni cella del campo dati, incluso il totale generale, nella sua quota del totale generale. I numeri visualizzati, dunque, rappresentano proporzioni del set di risultati completo. Questo formato confronta ogni valore solo con il totale generale, quindi non richiede né campo base né elemento base — gli argomenti finali (`0`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri sopra.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType
# Load or create a workbook with source data
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.cells.get(i + 1, 0).put_value(fruits[i])
    data_sheet.cells.get(i + 1, 1).put_value(amounts[i])
# Add a pivot table on a new worksheet (worksheets.add() returns the sheet index)
pivot_sheet_index = workbook.worksheets.add()
pivot_table = workbook.worksheets[pivot_sheet_index].pivot_tables.add("=Sheet1!A1:B7", 2, 2)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Ottieni e Configura PivotField.show_values_setting**
Leggi la configurazione corrente tramite `PivotField.show_values_setting`: la proprietà di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui proprietà descrivono il calcolo Show Values As attivo. Per modificare la configurazione, chiama il metodo `PivotField.show_values_as` — scrive tutte le impostazioni in una sola chiamata, così non è necessario assegnare le proprietà una per una.  
L'oggetto `PivotShowValuesSetting` espone lo stato che `show_values_as` scrive:
- `show_values_as` seleziona il calcolo secondario `PivotShowValuesAsType`.
- `base_field_index` specifica l'indice zero‑based del campo base all'interno dei campi pivot. È usato dai formati relativi al campo base.
- `base_item_index` specifica l'elemento base: un indice zero‑based di uno specifico elemento pivot, o una delle due sentinelle — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) per l'elemento precedente, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) per quello successivo. È usato dai formati basati su elemento.
- `base_field_name` e `base_item_caption` sono viste di sola lettura che riportano il nome del campo base risolto e la didascalia dell'elemento base; ad esempio, dopo aver selezionato la sentinella dell'elemento precedente, `base_item_caption` restituisce `(previous)`.  
Dopo aver chiamato `show_values_as`, invoca nuovamente `PivotTable.calculate_data()` affinché il corpo della pivot venga ricalcolato e ridisegnato con la configurazione aggiornata.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType, PivotShowValuesSetting
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"ShowValuesAs: {settings.show_values_as}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemIndex: {settings.base_item_index}")
print(f"BaseFieldName: {settings.base_field_name}")
print(f"BaseItemCaption: {settings.base_item_caption}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.show_values_setting.show_values_as}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Articoli Correlati**
- [Gestione dei Campi Valore nella Tabella Pivot](/cells/it/python-net/manage-value-fields/)
- [Aggiornamento della Tabella Pivot](/cells/it/python-net/refresh-pivot-table/)
- [Applicazione di Stile alla Tabella Pivot](/cells/it/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}