---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa värden för pivottabellens datafält som en procentandel av totalen, en differens från ett grundobjekt, löpande summor, rankningar och mer med Aspose.Cells for Go via C++.
keywords: Aspose.Cells for Go via C++, pivottabell, visa värden som, dataformat för visning, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C++
type: docs
weight: 145
url: /sv/go-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datafält med en aggregationsfunktion såsom `Sum` eller `Count`. Excels **Show Values As**‑funktion ersätter varje visat resultat med en sekundär beräkning som härleds från aggregatet – till exempel en procentandel av totalsumman, en löpande total, en differens från ett valt grundobjekt eller en rankning – så att du kan göra jämförande analyser utan hjälpförmler eller beräknade kolumner. Vanliga användningsområden inkluderar andelsanalys av totalen, inklusive procent för rad, kolumn eller totalsumma; kumulativ rapportering med löpande total i ett periodfält; variansanalys mot ett referensobjekt med differens eller procentuell differens från ett grundobjekt; samt rangordning av värden från minst till störst eller omvänt. I Aspose.Cells for Go via C++ väljer `PivotFieldDataDisplayFormat` den sekundära beräkningen. Metoden `PivotField.GetShowValuesSetting()` returnerar ett `PivotShowValuesSetting`‑objekt, vars `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType` och `SetBaseItemIndex`‑metoder konfigurerar beteendet; bekvämlighetsmetoden `PivotField.ShowValuesAs(...)` tillämpar samma fyra inställningar i ett anrop. Tillämpa dessa inställningar på ett data‑ eller värdefält som erhållits från `PivotTable.GetDataFields()`.

## **PivotFieldDataDisplayFormat‑uppräkningens medlemmar**
Datafältet behåller sin aggregationsfunktion, såsom Sum eller Count, medan Show Values As endast förändrar hur det aggregerade värdet visas. Förutom att skriva `PivotShowValuesSetting`‑värdena direkt (se sista avsnittet) kan en enstaka bekvämlighetsmetod applicera samma konfiguration:

```go
func (pivotField *PivotField) ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(displayFormat PivotFieldDataDisplayFormat, baseField int32, baseItemPositionType PivotItemPositionType, baseItem int32)
```

| Parameter | Betydelse | När den krävs |
| --- | --- | --- |
| `displayFormat` | Den sekundära beräkningen av typen `PivotFieldDataDisplayFormat` som ska tillämpas. | Alltid. |
| `baseField` | Nollbaserat index för grundfältet bland pivottabellens grundfält (t.ex. indexet för radfältet som grundobjektet tillhör). | Endast för de sex basrelaterade formaten nedan (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); ignoreras av alla andra format. |
| `baseItemPositionType` | Hur grundobjektet väljs i förhållande till det aktuella objektet: `PivotItemPositionType.Previous`, `.Next` eller `.Custom`. | Endast för de tre basobjektformaten (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); ignoreras av alla andra format. |
| `baseItem` | Nollbaserat index för grundobjektet. | Endast när `baseItemPositionType` är `Custom` (objektindexet anger exakt grundobjekt); ignoreras för `Previous` / `Next` och av alla icke‑grundformat – skicka `0`. |

| Beräkningstyp | Beteende | Parametrar för grundobjekt |
| --- | --- | --- |
| `Normal` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DifferenceFrom` | Visar värdet som en differens från värdet i ett grundobjekt i ett grundfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` endast med `Custom`) |
| `PercentageOf` | Visar värdet som en procentandel av värdet i ett grundobjekt i ett grundfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` endast med `Custom`) |
| `PercentageDifferenceFrom` | Visar värdet som den procentuella differensen från värdet i ett grundobjekt i ett grundfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` endast med `Custom`) |
| `RunningTotalIn` | Visar värdet som en löpande total för på varandra följande objekt i ett grundfält. | `baseField` (fältet vars objektordning driver ackumuleringen) |
| `PercentageOfRow` | Visar värdet som en procentandel av radtotalen. | — |
| `PercentageOfColumn` | Visar värdet som en procentandel av kolumntotalen. | — |
| `PercentageOfTotal` | Visar värdet som en procentandel av totalsumman. | — |
| `Index` | Visar värdet med Excels index‑formel ((värde * totalsumma) / (radtotal * kolumntotal)). | — |
| `PercentageOfParentRowTotal` | Visar värdet som en procentandel av sin föräldraradtotal (för nästlade radfält). | — |
| `PercentageOfParentColumnTotal` | Visar värdet som en procentandel av sin föräldrakolumntotal (för nästlade kolumnfält). | — |
| `PercentageOfParentTotal` | Visar värdet som en procentandel av sin föräldratotal. | `baseField` (det överordnade referensfältet) |
| `PercentageOfRunningTotalIn` | Visar värdet som en procentandel av en löpande total i ett grundfält. | `baseField` (ackumuleringsfältet) |
| `RankSmallestToLargest` | Rangordnar värdet från minst (1) till störst. | — |
| `RankLargestToSmallest` | Rangordnar värdet från störst (1) till minst. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` skriver de `PivotShowValuesSetting`‑värdena (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — metoden och inställningsobjektet är två sätt att konfigurera samma tillstånd, vilket speglar grundfält‑ och grundobjekt‑väljarna i Excels **Show Values As**‑dialog.
{{% /alert %}}

## **Visa värden som procent av totalen**
Anropa `PivotField.ShowValuesAs`‑metoden med `PivotFieldDataDisplayFormat.PercentageOfTotal` för att konvertera varje datafältcell, inklusive totalsumman, till dess andel av totalsumman. De visade siffrorna blir därför proportioner av hela resultatmängden. Detta format mäter varje värde endast mot totalsumman, så det kräver inget grundfält eller grundobjekt — de efterföljande argumenten (`0`, `PivotItemPositionType.Previous`, `0`) är platshållare som formatet ignorerar, enligt tabellen ovan.

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

## **Hämta och konfigurera PivotField.ShowValuesSetting**
Läs den aktuella konfigurationen via `PivotField.GetShowValuesSetting()`: metoden returnerar fältets `PivotShowValuesSetting`‑objekt, vars fyra getter‑metoder beskriver den aktiva **Show Values As**‑beräkningen. För att ändra konfigurationen, anropa `PivotField.ShowValuesAs`‑metoden — den skriver alla fyra inställningar i ett anrop, så du behöver aldrig sätta värdena enskilt. `PivotShowValuesSetting`‑objektet exponerar de fyra värden som `ShowValuesAs` skriver:
- `GetCalculationType()` / `SetCalculationType()` väljer den sekundära beräkningen av typen `PivotFieldDataDisplayFormat`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` anger nollbaserat index för grundfältet inom pivottabellens fält. Det används av de basrelaterade formaten.
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` bestämmer hur grundobjektet placeras relativt till det aktuella objektet och accepterar `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` eller `PivotItemPositionType.Custom`.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` anger nollbaserat index för grundobjektet och används när positionstypen är `Custom`.
Efter att ha anropat `ShowValuesAs`, anropa `PivotTable.CalculateData()` igen så att pivottabellens kropp beräknas om och renderas med den uppdaterade konfigurationen.

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

## **Relaterade artiklar**
- [Gruppera pivottabellsfält i pivottabellen](/cells/sv/go-cpp/group-pivot-fields-in-the-pivot-table/)
- [Topp 10 Visa eller filtrera i pivottabell](/cells/sv/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [Uppdatera slicer](/cells/sv/go-cpp/updating-slicer/)

{{< app/cells/assistant language="go" >}}