---
title: Mostra Valori Come nella Tabella Pivot
linktitle: Mostra Valori Come nella Tabella Pivot
description: Visualizza i valori del campo dati della tabella pivot come percentuale del totale, differenza rispetto a un elemento di base, totali progressivi, ranghi e altro con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, tabella pivot, mostra valori come, formato visualizzazione dati, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /it/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot aggrega normalmente ogni campo dati con una funzione di aggregazione come `SUM` o `COUNT`. La funzionalità **Mostra valori come** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da quell'aggregato — ad esempio, una percentuale del totale complessivo, un totale progressivo, una differenza rispetto a un elemento di base scelto o un rango — consentendo analisi comparative senza formule di supporto o colonne calcolate.  
Gli usi tipici includono l'analisi della quota del totale, comprese le percentuali di una riga, colonna o totale complessivo; reporting cumulativo mediante un totale progressivo in un campo periodo; analisi delle variazioni rispetto a un elemento di riferimento usando la differenza o la differenza percentuale; e classificazione dei valori dal più piccolo al più grande o viceversa.  
In Aspose.Cells for Node.js via C++, `PivotFieldDataDisplayFormat` seleziona il calcolo secondario. L'accessor di sola lettura `PivotField.getShowValuesSetting()` restituisce un oggetto `PivotShowValuesSetting`, i cui metodi scrivibili `setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` e `setBaseItemIndex()` configurano il comportamento; il metodo di convenienza `PivotField.showValuesAs(...)` applica le stesse quattro impostazioni in una sola chiamata. Applica queste impostazioni a un campo dati o valore ottenuto da `PivotTable.getDataFields()`.

## **Membri dell'enumerazione PivotFieldDataDisplayFormat**
Il campo dati mantiene la sua funzione di aggregazione, ad esempio SUM o COUNT, mentre **Mostra valori come** trasforma solo il modo in cui il valore aggregato viene visualizzato.  
Oltre a scrivere direttamente le proprietà di `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di convenienza a chiamata singola applica la stessa configurazione:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
function pickEnum(enumType, candidates, fallback) {
    const type = enumType || {};
    for (const name of candidates) {
        if (type[name] !== undefined && type[name] !== null) {
            return type[name];
        }
    }
    return fallback;
}
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().add("PivotData");
const cells = sheet.getCells();
// --- Source data -----------------------------------------------------------
const headers = ["Region", "Product", "Sales"];
for (const [c, header] of headers.entries()) {
    cells.get(0, c).putValue(header);
}
const rows = [
    ["East", "Apple", 100],
    ["East", "Banana", 120],
    ["West", "Apple", 90],
    ["West", "Banana", 60],
    ["North", "Apple", 75],
    ["North", "Banana", 45]
];
for (const [r, row] of rows.entries()) {
    for (const [c, value] of row.entries()) {
        cells.get(r + 1, c).putValue(value);
    }
}
// --- Pivot table ------------------------------------------------------------
const pivotTables = sheet.getPivotTables();
const pivotTableIndex = pivotTables.add("A1:C7", 0, 4);
const pivotTable = pivotTables.get(pivotTableIndex);
pivotTable.getRowFields().add("Region");
pivotTable.getDataFields().add("Sales");
const salesField = pivotTable.getDataFields().get(0);
// --- ShowValuesAs -----------------------------------------------------------
const displayFormat = pickEnum(
    AsposeCells.PivotFieldDataDisplayFormat,
    ["PERCENT_OF_TOTAL", "PercentOfTotal", "PERCENTAGE_OF_TOTAL", "PercentageOfTotal"],
    7
);
const baseItemPositionType = pickEnum(
    AsposeCells.PivotItemPositionType,
    ["DEFAULT", "Default"],
    0
);
showValuesAs(salesField, displayFormat, -1, baseItemPositionType, -1);
// --- Save -------------------------------------------------------------------
workbook.save("ShowValuesAs.xlsx");
console.log("ShowValuesAs applied and workbook saved.");
```

| Parameter | Meaning | When It Is Required |
| --- | --- | --- |
| `displayFormat` | The `PivotFieldDataDisplayFormat` secondary calculation to apply. | Always. |
| `baseField` | Zero-based index of the base field among the pivot table's base fields (for example, the index of the row field the base item belongs to). | Solo per i sei formati a base di riferimento riportati di seguito (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); ignorato da ogni altro formato. |
| `baseItemPositionType` | How the base item is chosen relative to the current item: `PivotItemPositionType.PREVIOUS`, `.NEXT`, or `.CUSTOM`. | Solo per i tre formati con elemento di base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); ignorato da ogni altro formato. |
| `baseItem` | Zero-based index of the base item. | Only when `baseItemPositionType` is `CUSTOM` (the item index picks the exact base item); ignored for `PREVIOUS` / `NEXT` and by every non-base format — pass `0`. |

| Calculation Type | Behavior | Base Item Parameters |
| --- | --- | --- |
| `NORMAL` | No secondary calculation; the aggregated value is displayed as is (default). | — |
| `DIFFERENCE_FROM` | Displays the value as a difference from the value of a base item in a base field. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` only with `CUSTOM`) |
| `PERCENTAGE_OF` | Displays the value as a percentage of the value of a base item in a base field. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` only with `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Displays the value as the percentage difference from the value of a base item in a base field. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` only with `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Displays the value as a running total for successive items of a base field. | `baseField` (the field whose item order drives the accumulation) |
| `PERCENTAGE_OF_ROW` | Displays the value as a percentage of the row total. | — |
| `PERCENTAGE_OF_COLUMN` | Displays the value as a percentage of the column total. | — |
| `PERCENTAGE_OF_TOTAL` | Displays the value as a percentage of the grand total. | — |
| `INDEX` | Displays the value using the Excel index formula ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Displays the value as a percentage of its parent row total (for nested row fields). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Displays the value as a percentage of its parent column total (for nested column fields). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Displays the value as a percentage of its parent total. | `baseField` (il campo padre di riferimento) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Displays the value as a percentage of a running total in a base field. | `baseField` (the accumulation field) |
| `RANK_SMALLEST_TO_LARGEST` | Ranks the value from smallest (1) to largest. | — |
| `RANK_LARGEST_TO_SMALLEST` | Ranks the value from largest (1) to smallest. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` scrive le impostazioni di `PivotShowValuesSetting` (`getCalculationType()`/`setCalculationType()`, `getBaseFieldIndex()`/`setBaseFieldIndex()`, `getBaseItemPositionType()`/`setBaseItemPositionType()`, e `getBaseItemIndex()`/`setBaseItemIndex()`) — il metodo e l'oggetto impostazioni sono due modi per configurare lo stesso stato, replicando i selettori di campo base e elemento base nella finestra di dialogo **Mostra valori come** di Excel.  
{{% /alert %}}

## **Mostra valori come percentuale del totale**
Chiama il metodo `PivotField.showValuesAs()` con `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` per convertire ogni cella del campo dati, incluso il totale generale, nella sua quota del totale generale. I numeri visualizzati quindi rappresentano proporzioni dell'intero set di risultati. Questo formato confronta ogni valore solo con il totale generale, quindi non richiede né campo base né elemento base — gli argomenti finali (`0`, `PivotItemPositionType.PREVIOUS`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri sopra.

```javascript
const AsposeCells = require("aspose.cells.node");
// Load or create a workbook with source data
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
const amounts = [10, 20, 30, 40, 50, 60];
for (let i = 0; i < fruits.length; i++) {
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
const pivotSheetIndex = workbook.getWorksheets().add();
const pivotTable = workbook
    .getWorksheets()
    .get(pivotSheetIndex)
    .getPivotTables()
    .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
    0,
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Ottieni e configura PivotField.getShowValuesSetting()**
Leggi la configurazione corrente tramite `PivotField.getShowValuesSetting()`: l'accessor di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui quattro proprietà descrivono il calcolo **Mostra valori come** attivo. Per modificare la configurazione, chiama il metodo `PivotField.showValuesAs()` — esso scrive tutte e quattro le impostazioni in una singola chiamata, così non è necessario assegnare le proprietà una per una.  
L'oggetto `PivotShowValuesSetting` espone le quattro impostazioni che `showValuesAs()` scrive:
- `getCalculationType()` e `setCalculationType()` selezionano il calcolo secondario `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` e `setBaseFieldIndex()` specificano l'indice zero‑based del campo base all'interno dei campi pivot. È usato nei formati a base di riferimento.
- `getBaseItemPositionType()` e `setBaseItemPositionType()` determinano come l'elemento base è posizionato rispetto all'elemento corrente e accettano `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` o `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` e `setBaseItemIndex()` specificano l'indice zero‑based dell'elemento base e sono usati quando `getBaseItemPositionType()` è `CUSTOM`.  
Dopo aver chiamato `showValuesAs()`, richiama nuovamente `PivotTable.calculateData()` affinché il corpo della tabella pivot venga ricalcolato e ridisegnato con la configurazione aggiornata.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`CalculationType: ${settings.getCalculationType()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemPositionType: ${settings.getBaseItemPositionType()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    AsposeCells.Pivot.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.Pivot.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`CalculationType now: ${dataField.getShowValuesSetting().getCalculationType()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Articoli correlati**
- [Gestione dei campi valore nella tabella pivot](/cells/it/nodejs-cpp/manage-value-fields/)
- [Aggiornamento della tabella pivot](/cells/it/nodejs-cpp/refresh-pivot-table/)
- [Applicazione di uno stile alla tabella pivot](/cells/it/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}