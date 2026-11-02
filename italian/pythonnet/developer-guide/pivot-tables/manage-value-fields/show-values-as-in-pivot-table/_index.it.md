---
title: Mostra valori come nella Tabella Pivot
linktitle: Mostra valori come nella Tabella Pivot
description: Visualizza i valori dei campi dati della tabella pivot come percentuale del totale, differenza da un elemento base, totali cumulativi, classifiche e altro con Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python via .NET, tabella pivot, mostra valori come, formato di visualizzazione dei dati, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python
type: docs
weight: 145
url: /it/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot aggrega normalmente ciascun campo dati con una funzione di aggregazione come `SUM` o `COUNT`. La funzionalità **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da quell'aggregato — ad esempio, una percentuale del totale generale, un totale cumulativo, una differenza da un elemento base scelto o una classifica — in modo da poter eseguire analisi comparative senza formule di supporto o colonne calcolate.  
Gli usi tipici includono l'analisi della quota del totale, comprese le percentuali di una riga, colonna o totale generale; reportistica cumulativa usando un totale cumulativo in un campo periodo; analisi delle deviazioni rispetto a un elemento di riferimento utilizzando la differenza o la differenza percentuale da un elemento base; e la classificazione dei valori dal più piccolo al più grande o viceversa.  
In Aspose.Cells for Python via .NET, `PivotFieldDataDisplayFormat` seleziona il calcolo secondario. La proprietà di sola lettura `PivotField.show_values_setting` restituisce un oggetto `PivotShowValuesSetting`, le cui proprietà scrivibili `calculation_type`, `base_field_index`, `base_item_position_type` e `base_item_index` configurano il comportamento; il metodo di convenienza `PivotField.show_values_as(...)` applica le stesse quattro impostazioni in una singola chiamata. Applica queste impostazioni a un campo dati o di valore ottenuto da `PivotTable.data_fields`.

## **Membri dell'enumerazione PivotFieldDataDisplayFormat**
Il campo dati conserva la sua funzione di aggregazione, come `SUM` o `COUNT`, mentre Show Values As trasforma solo il modo in cui il valore aggregato viene visualizzato.  
Oltre a impostare direttamente le proprietà `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di convenienza a chiamata singola applica la stessa configurazione:

```python
from aspose.cells.pivot import PivotField, PivotFieldDataDisplayFormat, PivotItemPositionType
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
```

| Parametro | Significato | Quando è richiesto |
| --- | --- | --- |
| `display_format` | Il calcolo secondario `PivotFieldDataDisplayFormat` da applicare. | Sempre. |
| `base_field` | Indice basato su zero del campo base tra i campi base della tabella pivot (ad esempio, l'indice del campo riga a cui appartiene l'elemento base). | Solo per i sei formati a base di riferimento riportati di seguito (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); ignorato da ogni altro formato. |
| `base_item_position_type` | Come viene scelto l'elemento base rispetto all'elemento corrente: `PivotItemPositionType.PREVIOUS`, `.NEXT` o `.CUSTOM`. | Solo per i tre formati con elemento di base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); ignorato da ogni altro formato. |
| `base_item` | Indice basato su zero dell'elemento base. | Solo quando `base_item_position_type` è `CUSTOM` (l'indice dell'elemento seleziona l'elemento base esatto); ignorato per `PREVIOUS` / `NEXT` e da ogni formato non basato su elemento — passare `0`. |

| Tipo di calcolo | Comportamento | Parametri elemento base |
| --- | --- | --- |
| `NORMAL` | Nessun calcolo secondario; il valore aggregato viene visualizzato così com'è (predefinito). | — |
| `DIFFERENCE_FROM` | Visualizza il valore come differenza dal valore di un elemento base in un campo base. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` solo con `CUSTOM`) |
| `PERCENTAGE_OF` | Visualizza il valore come percentuale del valore di un elemento base in un campo base. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` solo con `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visualizza il valore come la differenza percentuale dal valore di un elemento base in un campo base. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` solo con `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Visualizza il valore come totale cumulativo per gli elementi successivi di un campo base. | `base_field` (il campo il cui ordine degli elementi guida l'accumulazione) |
| `PERCENTAGE_OF_ROW` | Visualizza il valore come percentuale del totale di riga. | — |
| `PERCENTAGE_OF_COLUMN` | Visualizza il valore come percentuale del totale di colonna. | — |
| `PERCENTAGE_OF_TOTAL` | Visualizza il valore come percentuale del totale generale. | — |
| `INDEX` | Visualizza il valore usando la formula Excel INDEX ((valore * totale generale) / (totale riga * totale colonna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visualizza il valore come percentuale del totale della riga padre (per campi riga nidificati). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visualizza il valore come percentuale del totale della colonna padre (per campi colonna nidificati). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visualizza il valore come percentuale del totale del padre. | `baseField` (il campo padre di riferimento) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visualizza il valore come percentuale di un totale cumulativo in un campo base. | `base_field` (il campo di accumulo) |
| `RANK_SMALLEST_TO_LARGEST` | Classifica il valore dal più piccolo (1) al più grande. | — |
| `RANK_LARGEST_TO_SMALLEST` | Classifica il valore dal più grande (1) al più piccolo. | — |

{{% alert color="primary" %}}
`show_values_as(...)` scrive le proprietà `PivotShowValuesSetting` (`calculation_type`, `base_field_index`, `base_item_position_type`, `base_item_index`) — il metodo e l'oggetto proprietà sono due modi per configurare lo stesso stato, rispecchiando i selettori di campo base e elemento base nella finestra di dialogo Show Values As di Excel.
{{% /alert %}}

## **Mostra valori come percentuale del totale**
Chiama il metodo `PivotField.show_values_as` con `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` per convertire ogni cella del campo dati, compreso il totale generale, nella sua quota del totale generale. I numeri visualizzati quindi rappresentano proporzioni dell'intero set di risultati. Questo formato confronta ogni valore solo con il totale generale, quindi non richiede alcun campo base o elemento base — gli argomenti finali (`0`, `PivotItemPositionType.PREVIOUS`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri sopra.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
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
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Recupera e configura PivotField.show_values_setting**
Leggi la configurazione corrente tramite `PivotField.show_values_setting`: la proprietà di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui quattro proprietà descrivono il calcolo Show Values As attivo. Per modificare la configurazione, chiama il metodo `PivotField.show_values_as` — scrive tutte e quattro le impostazioni in una singola chiamata, così non è necessario assegnare le proprietà una per una.  
L'oggetto `PivotShowValuesSetting` espone le quattro proprietà che `show_values_as` scrive:
- `calculation_type` seleziona il calcolo secondario `PivotFieldDataDisplayFormat`.
- `base_field_index` specifica l'indice basato su zero del campo base all'interno dei campi pivot. È utilizzato dai formati a base di riferimento.
- `base_item_position_type` determina come l'elemento base è posizionato rispetto all'elemento corrente e accetta `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` o `PivotItemPositionType.CUSTOM`.
- `base_item_index` specifica l'indice basato su zero dell'elemento base ed è utilizzato quando `base_item_position_type` è `CUSTOM`.
Dopo aver chiamato `show_values_as`, chiama nuovamente `PivotTable.calculate_data()` affinché il corpo della tabella pivot venga ricalcolato e ridisegnato con la configurazione aggiornata.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"CalculationType: {settings.calculation_type}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemPositionType: {settings.base_item_position_type}")
print(f"BaseItemIndex: {settings.base_item_index}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotItemPositionType.PREVIOUS,
    0
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.show_values_setting.calculation_type}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Articoli correlati**
- [Gestione dei campi valore nella Tabella Pivot](/cells/it/python-net/manage-value-fields/)
- [Aggiornamento della Tabella Pivot](/cells/it/python-net/refresh-pivot-table/)
- [Applicare lo stile alla Tabella Pivot](/cells/it/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}