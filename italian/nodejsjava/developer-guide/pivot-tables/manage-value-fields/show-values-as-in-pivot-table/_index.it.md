---
title: Mostra Valori Come nella Tabella Pivot
linktitle: Mostra Valori Come nella Tabella Pivot
description: Visualizza i valori dei campi dati della tabella pivot come percentuale del totale, differenza da un elemento base, totali cumulativi, classifiche e altro con Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, tabella pivot, mostra valori come, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /it/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
Una tabella pivot aggrega normalmente ciascun campo dati con una funzione di aggregazione come `SUM` o `COUNT`. La funzione **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da tale aggregato — ad esempio, una percentuale del totale complessivo, un totale cumulativo, una differenza rispetto a un elemento base scelto o una classifica — così è possibile eseguire analisi comparative senza formule di supporto o colonne calcolate.  
Gli usi tipici includono l'analisi della quota di totale, comprese le percentuali di una riga, colonna o totale complessivo; la reportistica cumulativa usando un totale cumulativo in un campo periodo; l'analisi della varianza rispetto a un elemento di riferimento usando differenza da o differenza percentuale da un elemento base; e la classificazione dei valori dal più piccolo al più grande o dal più grande al più piccolo.  
In Aspose.Cells for Node.js via Java, l'enumerazione `PivotShowValuesAsType` seleziona il calcolo secondario. Il metodo di sola lettura `PivotField.getShowValuesSetting()` restituisce un oggetto `PivotShowValuesSetting`, i cui metodi `setShowValuesAs()`, `setBaseFieldIndex()` e `setBaseItemIndex()` configurano il comportamento; il metodo di convenienza `PivotField.showValuesAs(...)` applica le stesse impostazioni in una sola chiamata. Applicare queste impostazioni a un campo dati o valore ottenuto da `PivotTable.getDataFields()`.

## **Membri dell'Enumerazione PivotShowValuesAsType**
Il campo dati mantiene la sua funzione di aggregazione, come SUM o COUNT, mentre Show Values As trasforma solo il modo in cui il valore aggregato viene visualizzato.  
Oltre a utilizzare direttamente i setter di `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di convenienza con una sola chiamata applica la stessa configurazione. È disponibile in due forme — una che specifica il campo base e l'elemento base tramite indice, l'altra tramite nome:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF, "Fruit", "Apple"
```

| Parameter | Significato | Quando è richiesto |
| --- | --- | --- |
| `showValuesAsType` | Il calcolo secondario `PivotShowValuesAsType` da applicare. | Sempre. |
| `baseField` | Indice basato su zero del campo base tra i campi base della tabella pivot (ad esempio, l'indice del campo riga a cui appartiene l'elemento base), o — nella forma per nome — il nome del campo base. | Gli otto formati relativi al base di seguito (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); passare `0` (o `null` nella forma per nome) per tutti gli altri formati. |
| `baseItem` | Indice basato su zero dell'elemento base, con due sentinelle: -1 seleziona l'elemento precedente e -2 quello successivo (la radice del pacchetto non esporta le costanti `PivotShowValuesSetting` — passare i valori letterali). La forma per nome prende la didascalia dell'elemento base, e `null` quando il formato selezionato non richiede un elemento base. | Solo i tre formati basati su elemento (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) valutano l'elemento base; i cinque formati relativi al campo (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, entrambi i ranghi) lo ignorano — passare `0` o `null`. |

| Tipo di Calcolo | Comportamento | Parametri dell'Elemento Base |
| --- | --- | --- |
| `NORMAL` | Nessun calcolo secondario; il valore aggregato è visualizzato così com'è (predefinito). | — |
| `DIFFERENCE_FROM` | Visualizza il valore come differenza dal valore di un elemento base in un campo base. | `baseField` + `baseItem` (un indice o una didascalia, o la sentinella precedente/successiva) |
| `PERCENTAGE_OF` | Visualizza il valore come percentuale del valore di un elemento base in un campo base. | `baseField` + `baseItem` (un indice o una didascalia, o la sentinella precedente/successiva) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visualizza il valore come differenza percentuale dal valore di un elemento base in un campo base. | `baseField` + `baseItem` (un indice o una didascalia, o la sentinella precedente/successiva) |
| `RUNNING_TOTAL_IN` | Visualizza il valore come totale cumulativo per gli elementi successivi di un campo base. | `baseField` (il campo il cui ordine degli elementi guida l'accumulazione) |
| `PERCENTAGE_OF_ROW` | Visualizza il valore come percentuale del totale della riga. | — |
| `PERCENTAGE_OF_COLUMN` | Visualizza il valore come percentuale del totale della colonna. | — |
| `PERCENTAGE_OF_TOTAL` | Visualizza il valore come percentuale del totale complessivo. | — |
| `INDEX` | Visualizza il valore usando la formula indice di Excel ((valore * totale complessivo) / (totale riga * totale colonna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visualizza il valore come percentuale del totale della riga padre (per campi riga annidati). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visualizza il valore come percentuale del totale della colonna padre (per campi colonna annidati). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visualizza il valore come percentuale del totale del campo padre. | `baseField` (il campo padre il cui totale è il riferimento) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visualizza il valore come percentuale di un totale cumulativo in un campo base. | `baseField` (il campo di accumulazione) |
| `RANK_SMALLEST_TO_LARGEST` | Classifica il valore dal più piccolo (1) al più grande. | `baseField` (il campo i cui elementi definiscono l'ambito del ranking) |
| `RANK_LARGEST_TO_SMALLEST` | Classifica il valore dal più grande (1) al più piccolo. | `baseField` (il campo i cui elementi definiscono l'ambito del ranking) |

{{% alert color="primary" %}}
`showValuesAs(...)` scrive lo stato `PivotShowValuesSetting` tramite `setShowValuesAs()`, `setBaseFieldIndex()` e `setBaseItemIndex()` — il metodo e l'oggetto proprietà sono due modi per configurare lo stesso stato, rispecchiando i selettori di campo base e di elemento base nella finestra di dialogo **Show Values As** di Excel.  
{{% /alert %}}

## **Mostra Valori come Percentuale del Totale**
Chiama il metodo `PivotField.showValuesAs()` con `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` per convertire ogni cella del campo dati, incluso il totale complessivo, nella sua quota del totale complessivo. I numeri visualizzati sono quindi proporzioni dell'intero set di risultati. Questo formato misura ogni valore solo rispetto al totale complessivo, quindi non necessita di un campo base o di un elemento base — gli argomenti finali (`0`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri sopra.

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Ottieni e Configura PivotField.getShowValuesSetting()**
Leggi la configurazione corrente tramite `PivotField.getShowValuesSetting()`: il metodo di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui impostazioni descrivono il calcolo Show Values As attivo. Per modificare la configurazione, chiama il metodo `PivotField.showValuesAs()` — scrive tutte le impostazioni in una sola chiamata, così non è necessario impostarle una per una.  
L'oggetto `PivotShowValuesSetting` espone lo stato scritto da `showValuesAs()`:
- `getShowValuesAs()` / `setShowValuesAs()` seleziona il calcolo secondario `PivotShowValuesAsType`.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` specifica l'indice basato su zero del campo base all'interno dei campi pivot. È usato dai formati relativi al campo.
- `getBaseItemIndex()` / `setBaseItemIndex()` specifica l'elemento base: un indice basato su zero di uno specifico elemento pivot, oppure uno dei due valori sentinella — -1 per l'elemento precedente, -2 per quello successivo (la radice del pacchetto non esporta le costanti denominate). È usato dai formati basati su elemento.
- `getBaseFieldName()` e `getBaseItemCaption()` sono visualizzazioni di sola lettura che riportano il nome del campo base risolto e la didascalia dell'elemento base; ad esempio, dopo aver selezionato la sentinella dell'elemento precedente, `getBaseItemCaption()` restituisce `(previous)`.

Dopo aver chiamato `showValuesAs()`, richiama nuovamente `PivotTable.calculateData()` affinché il corpo della pivot venga ricalcolato e visualizzato con la configurazione aggiornata.

```javascript
const AsposeCells = require("aspose.cells");
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
// (-1 is the previous-item sentinel; the constants are not exported here)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DIFFERENCE_FROM,
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
- [Gestione dei campi valore nella tabella pivot](/cells/it/nodejs-java/manage-value-fields/)
- [Aggiornamento della tabella pivot](/cells/it/nodejs-java/refresh-pivot-table/)
- [Applicazione di uno stile alla tabella pivot](/cells/it/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}