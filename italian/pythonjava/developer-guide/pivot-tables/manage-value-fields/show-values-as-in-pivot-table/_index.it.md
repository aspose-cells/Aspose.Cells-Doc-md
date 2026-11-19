---
title: Mostra Valori Come nella Tabella Pivot
description: Visualizza i valori dei campi dati della tabella pivot come percentuale del totale, differenza da un elemento di base, totali cumulativi, classifiche e altro con Aspose.Cells for Python via Java.
linktitle: Mostra Valori Come
keywords: Aspose.Cells, tabella pivot, mostra valori come, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Python
type: docs
weight: 145
url: /it/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot aggrega normalmente ogni campo dati con una funzione di aggregazione come `SUM` o `COUNT`. La funzionalità **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da quell'aggregato — ad esempio, una percentuale del totale generale, un totale cumulativo, una differenza rispetto a un elemento di base scelto o una classifica — così è possibile eseguire analisi comparative senza formule di supporto o colonne calcolate.  
Gli usi tipici includono l'analisi della quota di parte, comprese le percentuali di una riga, colonna o totale generale; la segnalazione cumulativa mediante un totale cumulativo in un campo periodico; l'analisi della varianza rispetto a un elemento di riferimento usando la differenza o la differenza percentuale da un elemento di base; e la classificazione dei valori dal più piccolo al più grande o dal più grande al più piccolo.  
In Aspose.Cells for Python via Java, l'enumerazione `PivotShowValuesAsType` seleziona il calcolo secondario. Il metodo di sola lettura `PivotField.getShowValuesSetting()` restituisce un oggetto `PivotShowValuesSetting`, i cui metodi `setShowValuesAs(...)`, `setBaseFieldIndex(...)` e `setBaseItemIndex(...)` configurano il comportamento; il metodo di convenienza `PivotField.showValuesAs(...)` applica le stesse impostazioni in una singola chiamata. Applica queste impostazioni a un campo dati o valore ottenuto da `PivotTable.getDataFields()`.

## **Membri dell'enumerazione PivotShowValuesAsType**
Il campo dati mantiene la sua funzione di aggregazione, come `SUM` o `COUNT`, mentre Show Values As trasforma solo il modo in cui il valore aggregato viene visualizzato.  
Oltre a utilizzare direttamente i setter di `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di convenienza a chiamata singola applica la stessa configurazione. È disponibile in due forme — una che fa riferimento al campo di base e all'elemento di base per indice, l'altra per nome:

```python
from asposecells.api import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
```

| Parametro | Significato | Quando è richiesto |
| --- | --- | --- |
| `show_values_as_type` | Il calcolo secondario `PivotShowValuesAsType` da applicare. | Sempre. |
| `base_field` | Indice a base zero del campo di base tra i campi base della tabella pivot (ad esempio, l'indice del campo riga a cui appartiene l'elemento di base), oppure — nella forma per nome — il nome del campo di base. | I otto formati relativi al base elencati di seguito (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); passare `0` (o `None` nella forma per nome) per tutti gli altri formati. |
| `base_item` | Indice a base zero dell'elemento di base, con due sentinelle: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) seleziona l'elemento precedente e `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) quello successivo. La forma per nome utilizza la didascalia dell'elemento di base, e `None` quando il formato selezionato non richiede alcun elemento di base. | Solo i tre formati relativi all'elemento di base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) valutano l'elemento di base; i cinque formati relativi al campo (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, entrambi i ranghi) lo ignorano — passare `0` o `None`. |

| Tipo di calcolo | Comportamento | Parametri dell'elemento base |
| --- | --- | --- |
| `NORMAL` | Nessun calcolo secondario; il valore aggregato viene visualizzato così com'è (predefinito). | — |
| `DIFFERENCE_FROM` | Visualizza il valore come differenza dal valore di un elemento di base in un campo di base. | `base_field` + `base_item` (un indice o didascalia, o la sentinella precedente/successiva) |
| `PERCENTAGE_OF` | Visualizza il valore come percentuale del valore di un elemento di base in un campo di base. | `base_field` + `base_item` (un indice o didascalia, o la sentinella precedente/successiva) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visualizza il valore come differenza percentuale dal valore di un elemento di base in un campo di base. | `base_field` + `base_item` (un indice o didascalia, o la sentinella precedente/successiva) |
| `RUNNING_TOTAL_IN` | Visualizza il valore come totale cumulativo per gli elementi successivi di un campo di base. | `base_field` (il campo il cui ordine degli elementi guida l'accumulo) |
| `PERCENTAGE_OF_ROW` | Visualizza il valore come percentuale del totale della riga. | — |
| `PERCENTAGE_OF_COLUMN` | Visualizza il valore come percentuale del totale della colonna. | — |
| `PERCENTAGE_OF_TOTAL` | Visualizza il valore come percentuale del totale generale. | — |
| `INDEX` | Visualizza il valore usando la formula di indice di Excel ((valore * totale generale) / (totale riga * totale colonna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visualizza il valore come percentuale del totale della riga padre (per campi riga annidati). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visualizza il valore come percentuale del totale della colonna padre (per campi colonna annidati). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visualizza il valore come percentuale del totale del padre. | `base_field` (il campo padre il cui totale è il riferimento) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visualizza il valore come percentuale di un totale cumulativo in un campo di base. | `base_field` (il campo di accumulazione) |
| `RANK_SMALLEST_TO_LARGEST` | Classifica il valore dal più piccolo (1) al più grande. | `base_field` (il campo i cui elementi definiscono l'ambito di classificazione) |
| `RANK_LARGEST_TO_SMALLEST` | Classifica il valore dal più grande (1) al più piccolo. | `base_field` (il campo i cui elementi definiscono l'ambito di classificazione) |

{{% alert color="primary" %}}
`showValuesAs(...)` scrive i valori di `PivotShowValuesSetting` tramite `setShowValuesAs`, `setBaseFieldIndex` e `setBaseItemIndex` — il metodo e l'oggetto di impostazione sono due modi per configurare lo stesso stato, rispecchiando i selettori di campo base e elemento base nella finestra di dialogo Show Values As di Excel.
{{% /alert %}}

## **Mostra Valori Come Percentuale del Totale**
Chiama il metodo `PivotField.showValuesAs` con `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` per convertire ogni cella del campo dati, incluso il totale generale, nella sua quota del totale generale. I numeri visualizzati rappresentano quindi proporzioni dell'intero set di risultati. Questo formato misura ogni valore solo rispetto al totale generale, quindi non richiede né campo base né elemento base — gli argomenti finali (`0`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri sopra.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotShowValuesAsType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
# float literals keep putValue on the double overload (an untyped Python int is ambiguous between putValue(boolean/int/Object) overloads)
amounts = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
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
# one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Ottieni e Configura PivotField.getShowValuesSetting()**
Leggi la configurazione corrente tramite `PivotField.getShowValuesSetting()`: il metodo di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui proprietà descrivono il calcolo Show Values As attivo. Per modificare la configurazione, chiama il metodo `PivotField.showValuesAs` — scrive tutte le impostazioni in una singola chiamata, così non è necessario impostare le proprietà una per una.  
L'oggetto `PivotShowValuesSetting` espone lo stato che `showValuesAs` scrive:
- `getShowValuesAs()` restituisce il calcolo secondario `PivotShowValuesAsType`, mentre `setShowValuesAs(...)` lo modifica.
- `getBaseFieldIndex()` e `setBaseFieldIndex(...)` specificano l'indice a base zero del campo di base tra i campi pivot. È usato dai formati relativi al campo base.
- `getBaseItemIndex()` e `setBaseItemIndex(...)` specificano l'elemento di base: un indice a base zero di uno specifico elemento pivot, o una delle due sentinelle — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) per l'elemento precedente, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) per quello successivo. È usato dai formati relativi all'elemento di base.
- `getBaseFieldName()` e `getBaseItemCaption()` sono visualizzazioni di sola lettura che riportano il nome del campo di base e la didascalia dell'elemento di base risolti; ad esempio, dopo aver selezionato la sentinella dell'elemento precedente, `getBaseItemCaption()` restituisce `(previous)`.
Dopo aver chiamato `showValuesAs`, chiama nuovamente `PivotTable.calculateData()` affinché il corpo della tabella pivot venga ricalcolato e ridisegnato con la configurazione aggiornata.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotShowValuesAsType,
    PivotShowValuesSetting,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"ShowValuesAs: {settings.getShowValuesAs()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
print(f"BaseFieldName: {settings.getBaseFieldName()}")
print(f"BaseItemCaption: {settings.getBaseItemCaption()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.getShowValuesSetting().getShowValuesAs()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Articoli correlati**
- [Gestione dei Campi Valore nella Tabella Pivot](/cells/it/python-java/manage-value-fields/)
- [Aggiornamento della Tabella Pivot](/cells/it/python-java/refresh-pivot-table/)
- [Applicazione di Stile alla Tabella Pivot](/cells/it/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}