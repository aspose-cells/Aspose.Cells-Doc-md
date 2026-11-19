---
title: Mostra valori come in Tabella Pivot
linktitle: Mostra valori come in Tabella Pivot
description: Visualizza i valori dei campi dati della tabella pivot come percentuale del totale, differenza da un elemento base, totali cumulativi, classifiche e altro con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, tabella pivot, mostra valori come, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /it/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot aggrega normalmente ogni campo dati con una funzione di aggregazione come `SUM` o `COUNT`. La funzionalità **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da quell'aggregato — ad esempio, una percentuale del totale complessivo, un totale cumulativo, una differenza rispetto a un elemento base scelto o una classifica dei valori — così è possibile eseguire analisi comparative senza formule di supporto o colonne calcolate.  
Gli usi tipici includono l'analisi della quota rispetto al totale complessivo, comprese le percentuali di una riga, colonna o totale generale; la rendicontazione cumulativa usando un totale cumulativo in un campo temporale; l'analisi delle variazioni rispetto a un elemento di riferimento mediante differenza o differenza percentuale da un elemento base; e la classificazione dei valori dal più piccolo al più grande o viceversa.  
In Aspose.Cells for Node.js via C++, l'enumerazione `PivotShowValuesAsType` seleziona il calcolo secondario. L'accessor di sola lettura `PivotField.getShowValuesSetting()` restituisce un oggetto `PivotShowValuesSetting`, i cui metodi `setShowValuesAs()`, `setBaseFieldIndex()` e `setBaseItemIndex()` configurano il comportamento; il metodo di convenienza `PivotField.showValuesAs(...)` applica le stesse impostazioni in una sola chiamata. Applica queste impostazioni a un campo dati o valore ottenuto da `PivotTable.getDataFields()`.

## **Membri dell'enumerazione PivotShowValuesAsType**
Il campo dati mantiene la sua funzione di aggregazione, come SUM o COUNT, mentre Show Values As trasforma solo il modo in cui il valore aggregato viene visualizzato.  
Oltre a impostare direttamente le impostazioni `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di convenienza a chiamata singola applica la stessa configurazione. Viene fornito in due forme — una che indirizza il campo base e l'elemento base per indice, l'altra per nome:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Parametro | Significato | Quando è richiesto |
| --- | --- | --- |
| `showValuesAsType` | Il calcolo secondario `PivotShowValuesAsType` da applicare. | Sempre. |
| `baseField` | Indice basato su zero del campo di base tra i campi di base della tabella pivot (ad esempio, l'indice del campo di riga a cui appartiene l'elemento di base), oppure — nella forma per nome — il nome del campo di base. | I otto formati relativi al base elencati di seguito (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); per tutti gli altri formati passare `0` (o `null` nella forma per nome). |
| `baseItem` | Indice basato su zero dell'elemento di base, con due valori sentinella: -1 seleziona l'elemento precedente e -2 quello successivo (il binding Node.js via C++ non esporta le costanti denominate — passare i valori letterali). La forma per nome utilizza invece la didascalia dell'elemento di base, e `null` quando il formato selezionato non richiede un elemento di base. | Solo i tre formati basati su elemento (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) valutano l'elemento di base; i cinque formati relativi al campo (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, entrambe le classifiche) lo ignorano — passare `0` o `null`. |

| Tipo di calcolo | Comportamento | Parametri dell'elemento base |
| --- | --- | --- |
| `Normal` | Nessun calcolo secondario; il valore aggregato viene visualizzato così com'è (predefinito). | — |
| `DifferenceFrom` | Visualizza il valore come differenza dal valore di un elemento base in un campo base. | `baseField` + `baseItem` (indice o didascalia, oppure la sentinella precedente/seguente) |
| `PercentageOf` | Visualizza il valore come percentuale del valore di un elemento base in un campo base. | `baseField` + `baseItem` (indice o didascalia, oppure la sentinella precedente/seguente) |
| `PercentageDifferenceFrom` | Visualizza il valore come differenza percentuale dal valore di un elemento base in un campo base. | `baseField` + `baseItem` (indice o didascalia, oppure la sentinella precedente/seguente) |
| `RunningTotalIn` | Visualizza il valore come totale cumulativo per gli elementi successivi di un campo base. | `baseField` (il campo il cui ordine degli elementi guida l'accumulo) |
| `PercentageOfRow` | Visualizza il valore come percentuale del totale della riga. | — |
| `PercentageOfColumn` | Visualizza il valore come percentuale del totale della colonna. | — |
| `PercentageOfTotal` | Visualizza il valore come percentuale del totale generale. | — |
| `Index` | Visualizza il valore usando la formula indice di Excel ((valore * totale generale) / (totale riga * totale colonna)). | — |
| `PercentageOfParentRowTotal` | Visualizza il valore come percentuale del totale della riga padre (per campi riga nidificati). | — |
| `PercentageOfParentColumnTotal` | Visualizza il valore come percentuale del totale della colonna padre (per campi colonna nidificati). | — |
| `PercentageOfParentTotal` | Visualizza il valore come percentuale del totale del campo padre. | `baseField` (il campo padre il cui totale è il riferimento) |
| `PercentageOfRunningTotalIn` | Visualizza il valore come percentuale di un totale cumulativo in un campo base. | `baseField` (il campo di accumulo) |
| `RankSmallestToLargest` | Classifica il valore dal più piccolo (1) al più grande. | `baseField` (il campo i cui elementi definiscono l'ambito di classificazione) |
| `RankLargestToSmallest` | Classifica il valore dal più grande (1) al più piccolo. | `baseField` (il campo i cui elementi definiscono l'ambito di classificazione) |

{{% alert color="primary" %}}
`showValuesAs(...)` scrive le impostazioni di `PivotShowValuesSetting` (`getShowValuesAs()`/`setShowValuesAs()`, `getBaseFieldIndex()`/`setBaseFieldIndex()`, e `getBaseItemIndex()`/`setBaseItemIndex()`) — il metodo e l'oggetto proprietà sono due modi per configurare lo stesso stato, rispecchiando i selettori di campo base e elemento base nella finestra di dialogo Show Values As di Excel.
{{% /alert %}}

## **Mostra valori come percentuale del totale**
Chiama il metodo `PivotField.showValuesAs()` con `PivotShowValuesAsType.PercentageOfTotal` per convertire ogni cella del campo dati, incluso il totale generale, nella sua quota del totale complessivo. I numeri visualizzati rappresentano quindi proporzioni dell'insieme completo di risultati. Questo formato confronta ogni valore solo con il totale complessivo, quindi non richiede né campo base né elemento base — gli argomenti finali (`0`, `0`) sono segnaposto ignorati dal formato, come indicato nella tabella dei parametri sopra.

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
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Ottieni e configura PivotField.getShowValuesSetting()**
Leggi la configurazione corrente attraverso `PivotField.getShowValuesSetting()`: l'accessor di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui impostazioni descrivono il calcolo Show Values As attivo. Per modificare la configurazione, chiama il metodo `PivotField.showValuesAs()` — scrive tutte le impostazioni in una sola chiamata, così non è necessario impostarle una per una.  
L'oggetto `PivotShowValuesSetting` espone lo stato scritto da `showValuesAs()`:
- `getShowValuesAs()` e `setShowValuesAs()` selezionano il calcolo secondario `PivotShowValuesAsType`.
- `getBaseFieldIndex()` e `setBaseFieldIndex()` specificano l'indice basato su zero del campo base all'interno dei campi pivot. È utilizzato dai formati relativi al base.
- `getBaseItemIndex()` e `setBaseItemIndex()` specificano l'elemento base: un indice basato su zero di uno specifico elemento pivot, o uno dei due valori sentinella — -1 per l'elemento precedente, -2 per quello successivo (il binding non esporta le costanti denominate). È utilizzato dai formati basati su elemento.
- `getBaseFieldName()` e `getBaseItemCaption()` sono visualizzazioni di sola lettura che riportano il nome del campo base risolto e la didascalia dell'elemento base; ad esempio, dopo aver selezionato la sentinella dell'elemento precedente, `getBaseItemCaption()` restituisce `(previous)`.
Dopo aver chiamato `showValuesAs()`, chiama nuovamente `PivotTable.calculateData()` affinché il corpo della tabella pivot venga ricalcolato e renderizzato con la configurazione aggiornata.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`ShowValuesAs: ${settings.getShowValuesAs()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
console.log(`BaseFieldName: ${settings.getBaseFieldName()}`);
console.log(`BaseItemCaption: ${settings.getBaseItemCaption()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
// -1 is the previous-item sentinel (the binding does not export the named constant)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    -1
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`ShowValuesAs now: ${dataField.getShowValuesSetting().getShowValuesAs()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Articoli correlati**
- [Gestione dei campi valore nella Tabella Pivot](/cells/it/nodejs-cpp/manage-value-fields/)
- [Aggiornamento della Tabella Pivot](/cells/it/nodejs-cpp/refresh-pivot-table/)
- [Applicazione di stile alla Tabella Pivot](/cells/it/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}