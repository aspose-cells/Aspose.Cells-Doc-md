---
title: Mostra valori come nella tabella pivot
linktitle: Mostra valori come nella tabella pivot
description: Visualizza i valori del campo dati della tabella pivot come percentuale del totale, una differenza rispetto a un elemento base, totali cumulativi, ranghi e altro con Aspose.Cells for Go via C++.
keywords: Aspose.Cells for Go via C++, tabella pivot, mostra valori come, formato visualizzazione dati, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C++
type: docs
weight: 145
url: /it/go-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot aggrega normalmente ciascun campo dati con una funzione di aggregazione come `Sum` o `Count`. La funzionalità **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da quell'aggregato — ad esempio, una percentuale del totale complessivo, un totale cumulativo, una differenza rispetto a un elemento base scelto o un rango — in modo da poter eseguire analisi comparative senza formule di supporto o colonne calcolate.  
Gli usi tipici includono l'analisi della quota del totale, includendo percentuali di una riga, colonna o totale complessivo; reportistica cumulativa utilizzando un totale cumulativo in un campo periodo; analisi della varianza rispetto a un elemento di riferimento usando la differenza da o la differenza percentuale da un elemento base; e la classificazione dei valori dal più piccolo al più grande o dal più grande al più piccolo.  
In Aspose.Cells for Go via C++, `PivotFieldDataDisplayFormat` seleziona il calcolo secondario. L'accessor `PivotField.GetShowValuesSetting()` restituisce un oggetto `PivotShowValuesSetting`, i cui metodi `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType` e `SetBaseItemIndex` configurano il comportamento; il metodo di convenienza `PivotField.ShowValuesAs(...)` applica le stesse quattro impostazioni in una chiamata. Applica queste impostazioni a un campo dati o valore ottenuto da `PivotTable.GetDataFields()`.

## **Membri dell'enumerazione PivotFieldDataDisplayFormat**
Il campo dati mantiene la sua funzione di aggregazione, come Sum o Count, mentre Show Values As trasforma solo il modo in cui il valore aggregato viene visualizzato.  
Oltre a impostare direttamente i valori di `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di convenienza a chiamata singola applica la stessa configurazione:

```go
func (pivotField *PivotField) ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(displayFormat PivotFieldDataDisplayFormat, baseField int32, baseItemPositionType PivotItemPositionType, baseItem int32)
```

| Parametro | Significato | Quando è richiesto |
| --- | --- | --- |
| `displayFormat` | Il calcolo secondario `PivotFieldDataDisplayFormat` da applicare. | Sempre. |
| `baseField` | Indice basato su zero del campo base tra i campi base della tabella pivot (ad esempio, l'indice del campo riga a cui appartiene l'elemento base). | Solo per i sei formati a base di riferimento riportati di seguito (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); ignorato da ogni altro formato. |
| `baseItemPositionType` | Come viene scelto l'elemento base rispetto all'elemento corrente: `PivotItemPositionType.Previous`, `.Next` o `.Custom`. | Solo per i tre formati con elemento di base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); ignorato da ogni altro formato. |
| `baseItem` | Indice basato su zero dell'elemento base. | Solo quando `baseItemPositionType` è `Custom` (l'indice dell'elemento seleziona l'elemento base esatto); ignorato per `Previous` / `Next` e da tutti i formati non basati su elemento — passare `0`. |

| Tipo di calcolo | Comportamento | Parametri elemento base |
| --- | --- | --- |
| `Normal` | Nessun calcolo secondario; il valore aggregato è visualizzato così com'è (predefinito). | — |
| `DifferenceFrom` | Visualizza il valore come differenza rispetto al valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageOf` | Visualizza il valore come percentuale del valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageDifferenceFrom` | Visualizza il valore come differenza percentuale rispetto al valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `RunningTotalIn` | Visualizza il valore come totale cumulativo per elementi successivi di un campo base. | `baseField` (il campo il cui ordine degli elementi guida l'accumulazione) |
| `PercentageOfRow` | Visualizza il valore come percentuale del totale della riga. | — |
| `PercentageOfColumn` | Visualizza il valore come percentuale del totale della colonna. | — |
| `PercentageOfTotal` | Visualizza il valore come percentuale del totale complessivo. | — |
| `Index` | Visualizza il valore usando la formula di indice di Excel ((valore * totale complessivo) / (totale riga * totale colonna)). | — |
| `PercentageOfParentRowTotal` | Visualizza il valore come percentuale del totale della riga padre (per campi riga annidati). | — |
| `PercentageOfParentColumnTotal` | Visualizza il valore come percentuale del totale della colonna padre (per campi colonna annidati). | — |
| `PercentageOfParentTotal` | Visualizza il valore come percentuale del totale padre. | `baseField` (il campo padre di riferimento) |
| `PercentageOfRunningTotalIn` | Visualizza il valore come percentuale di un totale cumulativo in un campo base. | `baseField` (il campo di accumulazione) |
| `RankSmallestToLargest` | Classifica il valore dal più piccolo (1) al più grande. | — |
| `RankLargestToSmallest` | Classifica il valore dal più grande (1) al più piccolo. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` scrive i valori `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — il metodo e l'oggetto impostazioni sono due modi per configurare lo stesso stato, rispecchiando i selettori di campo base e elemento base nella finestra di dialogo Show Values As di Excel.
{{% /alert %}}

## **Mostra valori come percentuale del totale**
Chiama il metodo `PivotField.ShowValuesAs` con `PivotFieldDataDisplayFormat.PercentageOfTotal` per convertire ogni cella del campo dati, incluso il totale complessivo, nella sua quota del totale complessivo. I numeri visualizzati sono quindi proporzioni dell'insieme completo dei risultati. Questo formato misura ogni valore rispetto solo al totale complessivo, quindi non richiede né campo base né elemento base — gli argomenti finali (`0`, `PivotItemPositionType.Previous`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri sopra.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load or create a workbook with source data
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	dataSheet, _ := worksheets.Get_Int(0)
	cells, _ := dataSheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Amount")
	fruits := []string{"Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"}
	amounts := []int{10, 20, 30, 40, 50, 60}
	for i := range fruits {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), int32(0))
		fruitCell.PutValue_String(fruits[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), int32(1))
		amountCell.PutValue_Int(int32(amounts[i]))
	}
	// Add a pivot table on a new worksheet
	pivotSheetIndex, _ := worksheets.Add()
	pivotSheet, _ := worksheets.Get_Int(pivotSheetIndex)
	pivotTables, _ := pivotSheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=Sheet1!A1:B7", 2, 2)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Show the Amount data field as a percentage of the grand total with the
	// one-call method; PercentageOfTotal takes no base item, so the trailing
	// base arguments (0, Previous, 0) are placeholders the format ignores
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_PercentageOfTotal,
		int32(0),
		PivotItemPositionType_Previous,
		int32(0),
	)
	pivotTable.CalculateData()
	// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
	workbook.Save_String("ShowValuesAsPercentageOfTotal.xlsx")
}
```

## **Ottieni e configura PivotField.ShowValuesSetting**
Leggi la configurazione corrente tramite `PivotField.GetShowValuesSetting()`: l'accessor restituisce l'oggetto `PivotShowValuesSetting` del campo, i cui quattro metodi getter descrivono il calcolo Show Values As attivo. Per modificare la configurazione, chiama il metodo `PivotField.ShowValuesAs` — scrive tutte e quattro le impostazioni in una singola chiamata, così non è necessario impostare i valori uno per uno.  
L'oggetto `PivotShowValuesSetting` espone i quattro valori scritti da `ShowValuesAs`:
- `GetCalculationType()` / `SetCalculationType()` selezionano il calcolo secondario `PivotFieldDataDisplayFormat`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` specificano l'indice basato su zero del campo base all'interno dei campi pivot. È usato dai formati a base di riferimento.
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` determinano come l'elemento base è posizionato rispetto all'elemento corrente e accettano `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` o `PivotItemPositionType.Custom`.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` specificano l'indice basato su zero dell'elemento base e sono usati quando il tipo di posizione è `Custom`.
Dopo aver chiamato `ShowValuesAs`, chiama nuovamente `PivotTable.CalculateData()` in modo che il corpo della tabella pivot venga ricalcolato e visualizzato con la configurazione aggiornata.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("ShowValuesAsPercentageOfTotal.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	// Read the current show-values settings
	settings, _ := dataField.GetShowValuesSetting()
	calculationType, _ := settings.GetCalculationType()
	baseFieldIndex, _ := settings.GetBaseFieldIndex()
	baseItemPositionType, _ := settings.GetBaseItemPositionType()
	baseItemIndex, _ := settings.GetBaseItemIndex()
	fmt.Println("CalculationType:", calculationType)
	fmt.Println("BaseFieldIndex:", baseFieldIndex)
	fmt.Println("BaseItemPositionType:", baseItemPositionType)
	fmt.Println("BaseItemIndex:", baseItemIndex)
	// Switch to a base-item calculation with the one-call method: difference
	// from the value of the previous item in the row field
	rowFields, _ := pivotTable.GetRowFields()
	rowField, _ := rowFields.Get_Int(0)
	baseIndex, _ := rowField.GetBaseIndex()
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_DifferenceFrom,
		baseIndex,
		PivotItemPositionType_Previous,
		0,
	)
	pivotTable.CalculateData()
	// Note: the percentage number format saved by the previous example still
	// clings to the data field cells; the underlying values are now differences
	// Re-read the applied configuration
	updatedSettings, _ := dataField.GetShowValuesSetting()
	updatedCalculationType, _ := updatedSettings.GetCalculationType()
	fmt.Println("CalculationType now:", updatedCalculationType)
	workbook.Save_String("ShowValuesAsDifferenceFrom.xlsx")
}
```

## **Articoli correlati**
- [Raggruppa campi pivot nella tabella pivot](/cells/it/go-cpp/group-pivot-fields-in-the-pivot-table/)
- [Top 10 mostra o filtra nella tabella pivot](/cells/it/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [Aggiornamento dello Slicer](/cells/it/go-cpp/updating-slicer/)

{{< app/cells/assistant language="go" >}}