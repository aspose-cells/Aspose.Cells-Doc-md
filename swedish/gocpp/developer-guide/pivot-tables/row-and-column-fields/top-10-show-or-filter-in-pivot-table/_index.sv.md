---
title: Visa eller filtrera topp 10 i pivottabell
linktitle: Visa eller filtrera topp 10 i pivottabell
description: Läs om hur du endast visar de högst eller lägst rangordnade objekten i ett pivotfält med Aspose.Cells for Go via C++. Artikeln beskriver metoden Top10AutoShow i Excel 97-2003, hur du läser tillbaka alternativen med Top10AutoShowSettings och filtret Top 10 i Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, Go via C++, pivottabell, topp 10, automatisk visning, Top10AutoShow, GetTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /sv/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell som listar varje objekt i ett radfält kan vara svårläst när fältet har flera tiotal medlemmar. En topp 10-rapport behåller endast de högst eller lägst rangordnade objekten, vilket är precis det som rangordningsrapporter behöver – ”de 5 produkterna med högst intäkt” eller ”de 3 regionerna med lägst antal försäljningar”. Aspose.Cells stöder två mekanismer för detta, och de motsvarar två generationer av Microsoft Excel.
- **Excel 97-2003 AutoShow** – metoden `PivotField.Top10AutoShow()`. Detta är den klassiska inställningen ”Visa de högst/lägst N objekten” som lagras direkt i pivotfältet. Den fungerar i alla Excel-versioner, både äldre och nyare, eftersom den ingår i det ursprungliga pivottabellformatet.
- **Excel 2007-365 Top 10 Filter** – metoden `PivotField.FilterTop10()`. Detta är det moderna topp 10-värdefiltret i fältmenyns värdefilter. Det lagras som ett `PivotFilter`-objekt som är kopplat till fältet och möjliggör rangordning efter antal objekt eller procent.

## **Visa topp 10 i Excel 97-2003 (Top10AutoShow)**
Den klassiska AutoShow-funktionen konfigureras med ett enda anrop till `PivotField.Top10AutoShow(isAutoShow bool, isTop bool, count int32, rankBy int32)`:
- `isAutoShow` – aktiverar eller inaktiverar AutoShow-inställningen på fältet.
- `isTop` – `true` behåller de högst rangordnade objekten (topp), `false` behåller de lägst rangordnade objekten (botten).
- `count` – hur många objekt som ska behållas, till exempel 10 för en klassisk topp 10-rapport.
- `rankBy` – det nollbaserade indexet för det **datafält** vars värden används för att rangordna objekten. Ange -1 för att rangordna objekten efter fältet självt.
Rangordningen kan baseras på ett värdefält eller på fältet självt. Det finns två naturliga varianter, som visas nedan.

### **Rangordna efter ett värdefält**
Rangordna radfältets objekt efter ett vanligt värdefält, till exempel ”Sum of Sales”. Följande exempel skapar en pivottabell med ett radfält (`Sport`) och ett datafält (`Sales`) och visar sedan de två mest säljande sporten. `rankBy` är 0 eftersom ”Sum of Sales” är datafältet på index 0.

```go
package main
import (
	"strconv"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String("Qtr" + strconv.Itoa(int(quarter)))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
	sportField.Top10AutoShow(true, true, 2, 0)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **Rangordna efter fältet självt**
Ett fält kan också rangordnas efter sig självt – ange -1 till `rankBy`. För den här varianten behövs inget extra datafält; fältet behöver bara finnas i rad- eller kolumnområdet. Följande exempel visar de tre lägst rangordnade sporten när de rangordnas efter fältet självt. När inställningen sparas utelämnas attributet `rankBy` från pivottabellens XML eftersom -1 är formatets standardvärde, och `GetRankBy()` returnerar -1.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Show the bottom 3 items ranked by the field itself (rankBy = -1)
	sportField.Top10AutoShow(true, false, 3, -1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **Läsa aktuella AutoShow-alternativ**
Metoden `PivotField.GetTop10AutoShowSettings()` returnerar ett `PivotFieldTop10AutoShowSettings`-objekt som exponerar de AutoShow-alternativ som för närvarande lagras på fältet. Använd metoden för att undersöka hur objekt visas i en befintlig arbetsbok eller i en pivottabell som du nyligen har konfigurerat, inklusive arbetsböcker som har lästs in från en fil.

```go
package main

import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)

func main() {
	workbook, _ := NewWorkbook_String("output-top10-by-value-field.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	settings, _ := sportField.GetTop10AutoShowSettings()
	isAutoShow, _ := settings.IsAutoShow()
	isTop, _ := settings.IsTop()
	autoShowCount, _ := settings.GetAutoShowCount()
	rankBy, _ := settings.GetRankBy()
	direction := "Bottom"
	if isTop {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", rankBy)
}
```

Inställningarna motsvarar de klassiska AutoShow-attributen som skrivs till pivottabellens XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), så värdena som läses tillbaka är de värden som alla Excel-versioner tillämpar.

## **Obs**

{{% alert color="primary" %}}
- Efter att du har anropat `Top10AutoShow()` ska du anropa `PivotTable.CalculateData()` igen – inställningarna börjar endast gälla i den visade pivottabellen vid nästa omberäkning.
- AutoShow-inställningarna fungerar med rad- och kolumnfält. Ett fält som endast finns i sidområdet (filterområdet) kan inte rangordnas på det här sättet eftersom dess objekt inte placeras i pivottabellens dataområde.
{{% /alert %}}

## **Excel 2007-365: topp 10-filter (FilterTop10)**
Moderna Excel-versioner visar topp 10 som ett värdefilter i fältmenyn (Värdefilter, Topp 10…). Aspose.Cells modellerar det med metoden `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, som returnerar det skapade `PivotFilter`-objektet:
- `valueFieldIndex` – det nollbaserade indexet för det datafält vars aggregerade värden används för att rangordna objekten.
- `type` – vad `itemCount` betyder. `PivotFilterType.Count` behåller ett bestämt antal objekt (alternativet ”Objekt” i dialogrutan). `PivotFilterType.Percent` behåller en procentandel av objekten, så `itemCount` anger procentandelen i sig – 30 behåller de 30 procent av objekten som rangordnats högst. `PivotFilterType.Sum` rangordnar objekten efter hur stor del av det totala värdet de täcker.
- `isTop` – `true` för topp, `false` för botten.
- `itemCount` – N-värdet i Topp N; enheten beror på `type`.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	wss, _ := workbook.GetWorksheets()
	worksheet, _ := wss.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// For a percentage-based filter instead, keep the top 30 percent of the items:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
AutoShow-inställningarna och `FilterTop10` är två separata funktioner. AutoShow skriver den klassiska `autoShow`-attributuppsättningen på pivotfältet, och den tillämpas av alla Excel-versioner tillbaka till Excel 97. `FilterTop10` skriver en modern `PivotFilter`-post, som kräver Excel 2007 eller senare. När en arbetsbok med en pivottabell som använder det moderna filtret öppnas i en äldre Excel-version visas alla objekt. För dokument som måste överföras fram och tillbaka via äldre verktyg bör du använda `Top10AutoShow`; för moderna arbetsböcker bör du använda `FilterTop10` eftersom det kan kombineras med de andra värdefiltren.
{{% /alert %}}

## **Relaterade artiklar**
- [Gruppera pivotfält i pivottabellen](/cells/sv/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}