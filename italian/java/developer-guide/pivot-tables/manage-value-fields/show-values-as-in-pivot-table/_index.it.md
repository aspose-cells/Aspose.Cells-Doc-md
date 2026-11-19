---
title: Mostra i valori come in una tabella pivot
linktitle: Mostra i valori come in una tabella pivot
description: Visualizza i valori dei campi dati di una tabella pivot come percentuale del totale generale, differenza rispetto a un elemento di base, totali cumulativi, classifiche e altro con Aspose.Cells for Java.
keywords: Aspose.Cells, tabella pivot, mostra valori come, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Java
type: docs
weight: 145
url: /it/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot normalmente aggrega ogni campo dati mediante una funzione di aggregazione, come `Sum` o `Count`. La funzionalità **Mostra valori come** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da tale aggregazione, ad esempio una percentuale del totale generale, un totale cumulativo, una differenza rispetto a un elemento di base selezionato o una classifica. Questa funzionalità consente di eseguire analisi comparative senza formule ausiliarie o colonne calcolate.
Tra gli utilizzi tipici vi sono l'analisi della quota rispetto al totale, mediante percentuali di riga, colonna o totale generale; la generazione di report cumulativi mediante un totale cumulativo su un campo di periodo; l'analisi della varianza rispetto a un elemento di riferimento, mediante differenza o differenza percentuale rispetto a un elemento di base; e la classificazione dei valori dal più piccolo al più grande o dal più grande al più piccolo.
In Aspose.Cells for Java, l'enumerazione `PivotShowValuesAsType` seleziona il calcolo secondario. Il getter di sola lettura `PivotField.getShowValuesSetting()` restituisce un oggetto `PivotShowValuesSetting`, i cui metodi `setShowValuesAs(...)`, `setBaseFieldIndex(...)` e `setBaseItemIndex(...)` configurano il comportamento; il metodo di convenienza `PivotField.showValuesAs(...)` applica le stesse impostazioni in una singola chiamata. Applicare queste impostazioni a un campo dati o valore ottenuto da `PivotTable.getDataFields()`.

## **Membri dell'enumerazione PivotShowValuesAsType**
Il campo dati mantiene la funzione di aggregazione, come `Sum` o `Count`, mentre Mostra valori come modifica soltanto il modo in cui il valore aggregato viene visualizzato.
Oltre all'utilizzo diretto dei metodi di impostazione di `PivotShowValuesSetting` (vedere l'ultima sezione), è disponibile un metodo di convenienza che applica la stessa configurazione con una singola chiamata. Il metodo offre due varianti: una che identifica il campo di base e l'elemento di base tramite indice e una tramite nome:

```java
public class CodeRunner
{
    public void showValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
    {
    }

    public void showValuesAs(PivotShowValuesAsType showValuesAsType, String baseField, String baseItem)
    {
    }
}
```

| Parametro | Significato | Quando è obbligatorio |
| --- | --- | --- |
| `showValuesAsType` | Il calcolo secondario di tipo `PivotShowValuesAsType` da applicare. | Sempre. |
| `baseField` | Indice in base zero del campo di base tra i campi di base della tabella pivot (ad esempio, l'indice del campo di riga a cui appartiene l'elemento di base) oppure, nella variante `String`, il nome del campo di base. | Gli otto formati relativi alla base elencati di seguito (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); passare `0` (oppure `null` nella variante `String`) per tutti gli altri formati. |
| `baseItem` | Indice in base zero dell'elemento di base, con due valori sentinella: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) seleziona l'elemento precedente e `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) quello successivo. La variante `String` accetta invece la didascalia dell'elemento di base oppure `null` quando il formato selezionato non richiede un elemento di base. | Solo i tre formati basati sull'elemento di base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) prendono in considerazione l'elemento di base; i cinque formati relativi al campo (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, entrambe le classifiche) lo ignorano: passare `0` o `null`. |

| Tipo di calcolo | Comportamento | Parametri dell'elemento di base |
| --- | --- | --- |
| `NORMAL` | Nessun calcolo secondario; il valore aggregato viene visualizzato invariato (predefinito). | — |
| `DIFFERENCE_FROM` | Visualizza il valore come differenza rispetto al valore di un elemento di base in un campo di base. | `baseField` + `baseItem` (un indice o una didascalia, oppure il valore sentinella per l'elemento precedente/successivo) |
| `PERCENTAGE_OF` | Visualizza il valore come percentuale del valore di un elemento di base in un campo di base. | `baseField` + `baseItem` (un indice o una didascalia, oppure il valore sentinella per l'elemento precedente/successivo) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visualizza il valore come differenza percentuale rispetto al valore di un elemento di base in un campo di base. | `baseField` + `baseItem` (un indice o una didascalia, oppure il valore sentinella per l'elemento precedente/successivo) |
| `RUNNING_TOTAL_IN` | Visualizza il valore come totale cumulativo per gli elementi successivi di un campo di base. | `baseField` (il campo il cui ordine degli elementi determina l'accumulo) |
| `PERCENTAGE_OF_ROW` | Visualizza il valore come percentuale del totale di riga. | — |
| `PERCENTAGE_OF_COLUMN` | Visualizza il valore come percentuale del totale di colonna. | — |
| `PERCENTAGE_OF_TOTAL` | Visualizza il valore come percentuale del totale generale. | — |
| `INDEX` | Visualizza il valore usando la formula dell'indice di Excel ((valore * totale generale) / (totale di riga * totale di colonna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visualizza il valore come percentuale del totale della riga padre (per campi di riga annidati). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visualizza il valore come percentuale del totale della colonna padre (per campi di colonna annidati). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visualizza il valore come percentuale del totale del livello padre. | `baseField` (il campo padre il cui totale costituisce il riferimento) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visualizza il valore come percentuale di un totale cumulativo in un campo di base. | `baseField` (il campo di accumulo) |
| `RANK_SMALLEST_TO_LARGEST` | Classifica il valore dal più piccolo (1) al più grande. | `baseField` (il campo i cui elementi definiscono l'ambito della classifica) |
| `RANK_LARGEST_TO_SMALLEST` | Classifica il valore dal più grande (1) al più piccolo. | `baseField` (il campo i cui elementi definiscono l'ambito della classifica) |

{{% alert color="primary" %}}
`showValuesAs(...)` imposta esattamente lo stato `PivotShowValuesSetting` tramite `setShowValuesAs(...)`, `setBaseFieldIndex(...)` e `setBaseItemIndex(...)`: il metodo e l'oggetto `PivotShowValuesSetting` sono due modi per configurare lo stesso stato, in analogia con i controlli di selezione del campo di base e dell'elemento di base nella finestra di dialogo Mostra valori come di Excel.
{{% /alert %}}

## **Mostra valori come percentuale del totale generale**
Chiamare il metodo `PivotField.showValuesAs(...)` con `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` per rappresentare ogni cella del campo dati, inclusa quella del totale generale, come quota del totale generale. I numeri visualizzati rappresentano quindi proporzioni dell'insieme completo dei risultati. Il formato confronta ogni valore soltanto con il totale generale e pertanto non richiede né un campo di base né un elemento di base: gli argomenti finali (`0`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri riportata sopra.

```java
import com.aspose.cells.*;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
String[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.length; i++)
{
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.getWorksheets().add();
PivotTable pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables()
        .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Ottenere e configurare PivotField.getShowValuesSetting**
Leggere la configurazione corrente tramite `PivotField.getShowValuesSetting()`: il getter di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui proprietà descrivono il calcolo secondario attivo nella modalità Mostra valori come. Per modificare la configurazione, chiamare il metodo `PivotField.showValuesAs(...)`, che imposta tutte le impostazioni in una singola chiamata; non è quindi necessario impostare le proprietà singolarmente.
L'oggetto `PivotShowValuesSetting` espone lo stato impostato da `showValuesAs(...)`:
- `getShowValuesAs()` / `setShowValuesAs(...)` consentono di selezionare il calcolo secondario `PivotShowValuesAsType`.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` consentono di specificare l'indice in base zero del campo di base tra i campi della tabella pivot. Vengono utilizzati dai formati relativi alla base.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` consentono di specificare l'elemento di base: un indice in base zero di un elemento specifico della tabella pivot oppure uno dei due valori sentinella, `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) per l'elemento precedente e `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) per quello successivo. Vengono utilizzati dai formati basati sull'elemento di base.
- `getBaseFieldName()` e `getBaseItemCaption()` restituiscono, in sola lettura, il nome risolto del campo di base e la didascalia dell'elemento di base; ad esempio, dopo aver selezionato il valore sentinella per l'elemento precedente, `getBaseItemCaption()` restituisce `(previous)`.
Dopo aver chiamato `showValuesAs(...)`, chiamare nuovamente `PivotTable.calculateData()` affinché il corpo della tabella pivot venga ricalcolato e ridisegnato con la configurazione aggiornata.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("ShowValuesAs: " + settings.getShowValuesAs());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
System.out.println("BaseFieldName: " + settings.getBaseFieldName());
System.out.println("BaseItemCaption: " + settings.getBaseItemCaption());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("ShowValuesAs now: " + dataField.getShowValuesSetting().getShowValuesAs());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Articoli correlati**
- [Gestione dei campi valore nella tabella pivot](/cells/it/java/manage-value-fields/)
- [Aggiornamento della tabella pivot](/cells/it/java/refresh-pivot-table/)
- [Applicazione di uno stile alla tabella pivot](/cells/it/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}