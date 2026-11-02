---
title: Mostra Valori Come nella Tabella Pivot
linktitle: Mostra Valori Come nella Tabella Pivot
description: Mostra i valori dei campi dati della tabella pivot come percentuale del totale, differenza rispetto a un elemento base, totali cumulativi, ranghi e altro con Aspose.Cells for Java.
keywords: Aspose.Cells, tabella pivot, mostra valori come, formato visualizzazione dati, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Java
type: docs
weight: 145
url: /it/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
Una tabella pivot aggrega normalmente ogni campo dati con una funzione di aggregazione come `Sum` o `Count`. La funzionalità **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da quell'aggregato — ad esempio, una percentuale del totale generale, un totale cumulativo, una differenza rispetto a un elemento base scelto o un rango — così è possibile eseguire analisi comparative senza formule di supporto o colonne calcolate.  
Gli usi tipici includono l'analisi della quota totale, comprese le percentuali di una riga, colonna o totale generale; reportistica cumulativa mediante un totale cumulativo in un campo di periodo; analisi delle variazioni rispetto a un elemento di riferimento mediante differenza o differenza percentuale; e classificazione dei valori dal più piccolo al più grande o viceversa.  
In Aspose.Cells for Java, `PivotFieldDataDisplayFormat` seleziona il calcolo secondario. Il metodo di sola lettura `PivotField.getShowValuesSetting()` restituisce un oggetto `PivotShowValuesSetting`, i cui metodi `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` e `setBaseItemIndex(...)` configurano il comportamento; il metodo di convenienza `PivotField.showValuesAs(...)` applica le stesse quattro impostazioni in una chiamata. Applica queste impostazioni a un campo dati o valore ottenuto da `PivotTable.getDataFields()`.

## **Membri dell'enumerazione PivotFieldDataDisplayFormat**
Il campo dati mantiene la sua funzione di aggregazione, come Somma o Conteggio, mentre Show Values As trasforma solo il modo in cui il valore aggregato viene visualizzato.  
Oltre a utilizzare direttamente i setter di `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di convenienza con una sola chiamata applica la stessa configurazione:

```java
public class CodeRunner
{
    public void showValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField,
                             PivotItemPositionType baseItemPositionType, int baseItem)
    {
    }
}
```

| Parametro | Significato | Quando è richiesto |
| --- | --- | --- |
| `displayFormat` | Il calcolo secondario `PivotFieldDataDisplayFormat` da applicare. | Sempre. |
| `baseField` | Indice a base zero del campo base tra i campi base della tabella pivot (ad esempio, l'indice del campo riga a cui appartiene l'elemento base). | Solo per i sei formati a base di riferimento riportati di seguito (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); ignorato da ogni altro formato. |
| `baseItemPositionType` | Come viene scelto l'elemento base rispetto all'elemento corrente: `PivotItemPositionType.PREVIOUS`, `NEXT`, o `CUSTOM`. | Solo per i tre formati con elemento di base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); ignorato da ogni altro formato. |
| `baseItem` | Indice a base zero dell'elemento base. | Solo quando `baseItemPositionType` è `CUSTOM` (l'indice dell'elemento sceglie l'elemento base esatto); ignorato per `PREVIOUS` / `NEXT` e da tutti i formati non basati su elemento — passare `0`. |

| Tipo di calcolo | Comportamento | Parametri elemento base |
| --- | --- | --- |
| `NORMAL` | Nessun calcolo secondario; il valore aggregato è mostrato così com'è (predefinito). | — |
| `DIFFERENCE_FROM` | Mostra il valore come differenza rispetto al valore di un elemento base in un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `PERCENTAGE_OF` | Mostra il valore come percentuale del valore di un elemento base in un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Mostra il valore come differenza percentuale rispetto al valore di un elemento base in un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Mostra il valore come totale cumulativo per gli elementi successivi di un campo base. | `baseField` (il campo il cui ordine degli elementi guida l'accumulo) |
| `PERCENTAGE_OF_ROW` | Mostra il valore come percentuale del totale della riga. | — |
| `PERCENTAGE_OF_COLUMN` | Mostra il valore come percentuale del totale della colonna. | — |
| `PERCENTAGE_OF_TOTAL` | Mostra il valore come percentuale del totale complessivo. | — |
| `INDEX` | Mostra il valore usando la formula Excel INDEX ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Mostra il valore come percentuale del totale della riga padre (per campi riga nidificati). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Mostra il valore come percentuale del totale della colonna padre (per campi colonna nidificati). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Mostra il valore come percentuale del totale padre. | `baseField` (il campo padre di riferimento) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Mostra il valore come percentuale di un totale cumulativo in un campo base. | `baseField` (il campo di accumulazione) |
| `RANK_SMALLEST_TO_LARGEST` | Classifica il valore dal più piccolo (1) al più grande. | — |
| `RANK_LARGEST_TO_SMALLEST` | Classifica il valore dal più grande (1) al più piccolo. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` imposta i valori `PivotShowValuesSetting` tramite `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` e `setBaseItemIndex(...)` — il metodo e l'oggetto delle proprietà sono due modi per configurare lo stesso stato, rispecchiando i selettori di campo base e di elemento base nella finestra di dialogo Show Values As di Excel.
{{% /alert %}}

## **Mostra Valori come Percentuale del Totale**
Chiama il metodo `PivotField.showValuesAs(...)` con `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` per convertire ogni cella del campo dati, compreso il totale complessivo, nella sua quota del totale complessivo. I numeri visualizzati sono quindi proporzioni dell'intero set di risultati. Questo formato misura ogni valore solo rispetto al totale complessivo, quindi non richiede né campo base né elemento base — gli argomenti finali (`0`, `PivotItemPositionType.PREVIOUS`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri sopra.

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
// base arguments (0, PREVIOUS, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL, 0,
        PivotItemPositionType.PREVIOUS, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Ottieni e Configura PivotField.getShowValuesSetting**
Leggi la configurazione attuale tramite `PivotField.getShowValuesSetting()`: il getter di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui quattro proprietà descrivono il calcolo Show Values As attivo. Per modificare la configurazione, chiama il metodo `PivotField.showValuesAs(...)` — scrive tutte e quattro le impostazioni in una sola chiamata, così non è mai necessario impostare le proprietà singolarmente.  
L'oggetto `PivotShowValuesSetting` espone le quattro proprietà che `showValuesAs(...)` imposta:
- `getCalculationType()` / `setCalculationType(...)` seleziona il calcolo secondario `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` specifica l'indice a base zero del campo base tra i campi pivot. Viene usato dai formati a base di riferimento.
- `getBaseItemPositionType()` / `setBaseItemPositionType(...)` determina come l'elemento base è posizionato rispetto all'elemento corrente e accetta `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` o `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` specifica l'indice a base zero dell'elemento base ed è usato quando `BaseItemPositionType` è `CUSTOM`.
Dopo aver chiamato `showValuesAs(...)`, chiama nuovamente `PivotTable.calculateData()` affinché il corpo della tabella pivot venga ricalcolato e ridisegnato con la configurazione aggiornata.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("CalculationType: " + settings.getCalculationType());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemPositionType: " + settings.getBaseItemPositionType());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("CalculationType now: " + dataField.getShowValuesSetting().getCalculationType());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Articoli correlati**
- [Gestione dei campi valore nella tabella pivot](/cells/it/java/manage-value-fields/)
- [Aggiornamento della tabella pivot](/cells/it/java/refresh-pivot-table/)
- [Applicazione di stile alla tabella pivot](/cells/it/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}