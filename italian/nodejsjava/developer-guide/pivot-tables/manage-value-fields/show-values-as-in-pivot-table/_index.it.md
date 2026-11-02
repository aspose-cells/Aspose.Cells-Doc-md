---
title: Mostra valori come nella tabella pivot
linktitle: Mostra valori come nella tabella pivot
description: Visualizza i valori dei campi dati della tabella pivot come percentuale del totale, differenza da un elemento base, totali cumulativi, classifiche e altro con Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, tabella pivot, mostra valori come, formato visualizzazione dati, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Node.js via Java
type: docs
weight: 145
url: /it/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
Una tabella pivot aggrega normalmente ogni campo dati con una funzione di aggregazione come `SUM` o `COUNT`. La funzionalità **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da quell'aggregato—ad esempio una percentuale del totale complessivo, un totale cumulativo, una differenza da un elemento base scelto o una classifica—così è possibile eseguire analisi comparative senza formule di supporto o colonne calcolate.  
Gli utilizzi tipici includono analisi della quota di mercato, comprese le percentuali per riga, colonna o totale complessivo; reportistica cumulativa usando un totale cumulativo in un campo di periodo; analisi della varianza rispetto a un elemento di riferimento mediante differenza o differenza percentuale da un elemento base; e classificazione dei valori dal più piccolo al più grande o viceversa.  
In Aspose.Cells for Node.js via Java, `PivotFieldDataDisplayFormat` seleziona il calcolo secondario. Il metodo di sola lettura `PivotField.getShowValuesSetting()` restituisce un oggetto `PivotShowValuesSetting`. I suoi metodi `setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` e `setBaseItemIndex()` configurano il comportamento; il metodo di comodità `PivotField.showValuesAs(...)` applica le stesse quattro impostazioni in una sola chiamata. Applica queste impostazioni a un campo dati o valore ottenuto da `PivotTable.getDataFields()`.

## **Membri dell'enumerazione PivotFieldDataDisplayFormat**
Il campo dati mantiene la sua funzione di aggregazione, ad esempio SUM o COUNT, mentre Show Values As trasforma solo il modo in cui il valore aggregato viene visualizzato.  
Oltre a scrivere direttamente le impostazioni `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di comodità a chiamata singola applica la stessa configurazione:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
module.exports = { showValuesAs };
```

| Parametro | Significato | Quando è richiesto |
| --- | --- | --- |
| `displayFormat` | Il calcolo secondario `PivotFieldDataDisplayFormat` da applicare. | Sempre. |
| `baseField` | Indice base‑zero del campo base tra i campi base della tabella pivot (ad esempio, l'indice del campo riga a cui appartiene l'elemento base). | Solo per i sei formati a base di riferimento riportati di seguito (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); ignorato da ogni altro formato. |
| `baseItemPositionType` | Come viene scelto l'elemento base rispetto all'elemento corrente: `PivotItemPositionType.PREVIOUS`, `.NEXT` o `.CUSTOM`. | Solo per i tre formati con elemento di base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); ignorato da ogni altro formato. |
| `baseItem` | Indice base‑zero dell'elemento base. | Solo quando `baseItemPositionType` è `CUSTOM` (l'indice dell'elemento indica l'elemento base esatto); ignorato per `PREVIOUS` / `NEXT` e per tutti i formati non basati su elemento — passare `0`. |

| Tipo di Calcolo | Comportamento | Parametri elemento base |
| --- | --- | --- |
| `NORMAL` | Nessun calcolo secondario; il valore aggregato viene visualizzato così com'è (predefinito). | — |
| `DIFFERENCE_FROM` | Visualizza il valore come differenza dal valore di un elemento base in un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `PERCENTAGE_OF` | Visualizza il valore come percentuale del valore di un elemento base in un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visualizza il valore come differenza percentuale dal valore di un elemento base in un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Visualizza il valore come totale cumulativo per gli elementi successivi di un campo base. | `baseField` (il campo il cui ordine degli elementi guida l'accumulo) |
| `PERCENTAGE_OF_ROW` | Visualizza il valore come percentuale del totale della riga. | — |
| `PERCENTAGE_OF_COLUMN` | Visualizza il valore come percentuale del totale della colonna. | — |
| `PERCENTAGE_OF_TOTAL` | Visualizza il valore come percentuale del totale complessivo. | — |
| `INDEX` | Visualizza il valore usando la formula di indice di Excel ((valore * totale complessivo) / (totale riga * totale colonna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visualizza il valore come percentuale del totale della riga genitore (per campi riga nidificati). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visualizza il valore come percentuale del totale della colonna genitore (per campi colonna nidificati). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visualizza il valore come percentuale del totale del genitore. | `baseField` (il campo padre di riferimento) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visualizza il valore come percentuale di un totale cumulativo in un campo base. | `baseField` (il campo di accumulo) |
| `RANK_SMALLEST_TO_LARGEST` | Classifica il valore dal più piccolo (1) al più grande. | — |
| `RANK_LARGEST_TO_SMALLEST` | Classifica il valore dal più grande (1) al più piccolo. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` scrive le impostazioni `PivotShowValuesSetting` (`setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()`, e `setBaseItemIndex()`) — il metodo e l'oggetto impostazione sono due modi per configurare lo stesso stato, replicando i selettori di campo base e elemento base nella finestra di dialogo **Show Values As** di Excel.
{{% /alert %}}

## **Mostra valori come percentuale del totale**
Chiama il metodo `PivotField.showValuesAs()` con `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` per convertire ogni cella del campo dati, incluso il totale complessivo, nella sua quota del totale complessivo. I numeri visualizzati saranno quindi proporzioni del risultato completo. Questo formato confronta ogni valore solo con il totale complessivo, quindi non richiede né campo base né elemento base — gli argomenti finali (`0`, `PivotItemPositionType.PREVIOUS`, `0`) sono segnaposti che il formato ignora, come indicato nella tabella dei parametri sopra.

```javascript
const AsposeCells = require("aspose.cells");
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
const pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables().add("=Sheet1!A1:B7", 2, 2);
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
Leggi la configurazione corrente tramite `PivotField.getShowValuesSetting()`: il metodo di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, i cui quattro settaggi descrivono il calcolo Show Values As attivo. Per modificare la configurazione, chiama il metodo `PivotField.showValuesAs()` — scrive tutti e quattro i settaggi in una sola chiamata, così non è necessario assegnarli uno per volta.  
L'oggetto `PivotShowValuesSetting` espone le quattro impostazioni che `showValuesAs()` scrive:
- `getCalculationType()` / `setCalculationType()` seleziona il calcolo secondario `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` specifica l'indice base‑zero del campo base all'interno dei campi pivot. È usato dai formati a base di riferimento.
- `getBaseItemPositionType()` / `setBaseItemPositionType()` determina come l'elemento base è posizionato rispetto all'elemento corrente e accetta `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` o `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` / `setBaseItemIndex()` specifica l'indice base‑zero dell'elemento base ed è usato quando `getBaseItemPositionType()` è `CUSTOM`.
Dopo aver chiamato `showValuesAs()`, invoca nuovamente `PivotTable.calculateData()` affinché il corpo della tabella pivot venga ricalcolato e ridisegnato con la nuova configurazione.

```javascript
const AsposeCells = require("aspose.cells");
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
    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.PivotItemPositionType.Previous,
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
- [Gestione dei campi valore nella Tabella Pivot](/cells/it/nodejs-java/manage-value-fields/)
- [Aggiornamento della Tabella Pivot](/cells/it/nodejs-java/refresh-pivot-table/)
- [Applicazione di stile alla Tabella Pivot](/cells/it/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}