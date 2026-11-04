---
title: Visa eller filtrera topp 10 i pivottabell
linktitle: Visa eller filtrera topp 10 i pivottabell
description: Lär dig att endast visa objekten med högst eller lägst rankning i ett pivotfält med Aspose.Cells for Go via C++. Artikeln beskriver AutoShow-inställningarna för Excel 97-2003 (SetIsAutoShow och relaterade metoder), hur du läser tillbaka inställningarna och hur du använder filtret för topp 10 i Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, Go via C++, pivottabell, topp 10, AutoShow, SetIsAutoShow, SetIsAscendShow, SetAutoShowCount, SetAutoShowField, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /sv/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell som listar varje objekt i ett radfält kan vara svårläst när fältet innehåller dussintals objekt. En topp 10-rapport behåller endast objekten med högst eller lägst rankning, vilket är precis vad rankningsrapporter behöver – ”topp 5 produkter efter intäkt” eller ”de tre lägsta regionerna efter antalet försäljningar”. Aspose.Cells stöder två mekanismer för detta, som motsvarar två generationer av Microsoft Excel.
- **Excel 97-2003 AutoShow** – de fyra inställningsmetoderna i `PivotField`: `SetIsAutoShow`, `SetIsAscendShow`, `SetAutoShowCount` och `SetAutoShowField`. Detta är den klassiska inställningen ”Visa de översta/understa N objekten”, som lagras direkt på pivotfältet. Den fungerar i alla Excel-versioner, äldre och nyare, eftersom den ingår i det ursprungliga formatet för pivottabeller.
- **Excel 2007-365 topp 10-filter** – metoden `PivotField.FilterTop10()`. Detta är det moderna filtret för topp 10 som finns under Värdefiltrar i fältmenyn. Det lagras som ett `PivotFilter`-objekt som är kopplat till fältet och erbjuder antals- eller procentbaserad rankning.

## **Topp 10-visning i Excel 97-2003 (AutoShow)**
Den klassiska AutoShow-inställningen konfigureras med fyra inställningsanrop på `PivotField`:
- `SetIsAutoShow(bool)` – aktiverar eller inaktiverar AutoShow-inställningen för fältet.
- `SetIsAscendShow(bool)` – `false` behåller de översta objekten, medan `true` behåller de nedersta.
- `SetAutoShowCount(int32)` – antalet objekt som ska behållas, till exempel 10 för en klassisk topp 10-rapport.
- `SetAutoShowField(int32)` – det nollbaserade indexet för det **datafält** vars värden används för att ranka objekten. Ange -1 för att ranka objekten efter fältet självt.
Rankningen kan baseras på ett värdefält eller på fältet självt. Det finns två naturliga varianter, som visas nedan.

### **Ranka efter ett värdefält**
Ranka radfältets objekt efter ett vanligt värdefält, till exempel ”Sum of Sales”. Det följande exemplet skapar en pivottabell med ett radfält (`Sport`) och ett datafält (`Sales`) och visar sedan de två bäst rankade sporten baserat på försäljningen. `rankBy` är 0 eftersom ”Sum of Sales” är datafältet på index 0.

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
	// Visa de 2 högsta objekten rankade efter "Sum of Sales" (datfältsindex 0)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(false)
	sportField.SetAutoShowCount(int32(2))
	sportField.SetAutoShowField(int32(0))
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **Ranka efter fältet självt**
Ett fält kan också rankas efter sina egna värden – ange -1 med `SetAutoShowField`. Inget ytterligare datafält behövs för den här varianten; fältet behöver endast finnas i rad- eller kolumnområdet. Det följande exemplet visar de tre lägst rankade sporten när de rankas efter fältets egna värden. När inställningen sparas utelämnas attributet `rankBy` i pivottabellens XML eftersom -1 är formatets standardvärde, och `GetAutoShowField()` läser tillbaka -1.

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
	// Visa de 3 lägsta objekten, rankade efter fältet självt (rankBy = -1)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(true)
	sportField.SetAutoShowCount(3)
	sportField.SetAutoShowField(-1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **Läsa aktuella AutoShow-alternativ**
Metoderna `IsAutoShow()`, `IsAscendShow()`, `GetAutoShowCount()` och `GetAutoShowField()` i `PivotField` gör det möjligt att läsa de AutoShow-alternativ som för närvarande lagras på fältet. Använd dem för att undersöka hur en befintlig arbetsbok eller en nyligen konfigurerad pivottabell kommer att presentera sina objekt. Det gäller även arbetsböcker som läses in från en fil.

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
	isAutoShow, _ := sportField.IsAutoShow()
	isAscendShow, _ := sportField.IsAscendShow()
	autoShowCount, _ := sportField.GetAutoShowCount()
	autoShowField, _ := sportField.GetAutoShowField()
	direction := "Bottom"
	if !isAscendShow {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", autoShowField)
}
```

De fyra läsmetoderna motsvarar de klassiska AutoShow-attributen som skrivs till pivottabellens XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), så att de värden som läses tillbaka är de värden som gäller i alla Excel-versioner.

## **Obs**

{{% alert color="primary" %}}
- Efter att du har ändrat någon AutoShow-inställning ska du anropa `PivotTable.CalculateData()` igen. Inställningarna börjar endast gälla i pivottabellens visningslayout vid nästa omberäkning.
- AutoShow-inställningarna fungerar med rad- och kolumnfält. Ett fält som endast finns i filterområdet kan inte rankas på det här sättet, eftersom dess objekt inte placeras i pivottabellens rad- eller kolumnområde.
{{% /alert %}}

## **Excel 2007-365: topp 10-filter (FilterTop10)**
I moderna Excel-versioner finns topp 10 som ett värdefilter i fältmenyn (Värdefiltrar, Topp 10...). Aspose.Cells modellerar detta med metoden `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, som returnerar det skapade `PivotFilter`-objektet:
- `valueFieldIndex` – det nollbaserade indexet för det datafält vars aggregerade värden rankar objekten.
- `type` – vad `itemCount` betyder. `PivotFilterType.Count` behåller ett bestämt antal objekt (dialogens alternativ Objekt). `PivotFilterType.Percent` behåller en viss procentandel av objekten, så att `itemCount` själv är procentvärdet – 30 behåller de bästa 30 procenten av objekten. `PivotFilterType.Sum` rankerar efter ackumulerad värdeandel.
- `isTop` – `true` för att behålla de översta objekten och `false` för att behålla de nedersta.
- `itemCount` – N i topp N; enheten beror på `type`.

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
	// Topp 10-filter — behåll de två främsta objekten enligt "Sum of Sales" (index 0 för datafältet)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// För ett procentuellt filter i stället, behåll de 30 bästa procenten av objekten:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
AutoShow-inställningarna och `FilterTop10` är två separata funktioner. AutoShow skriver den klassiska uppsättningen av attribut, inklusive `autoShow`, till pivotfältet och gäller i alla Excel-versioner tillbaka till Excel 97. `FilterTop10` skriver en modern `PivotFilter`-post, som kräver Excel 2007 eller senare. Om en arbetsbok öppnas i en äldre Excel-version visas alla objekt i pivottabeller som använder det moderna filtret. För dokument som måste öppnas, bearbetas och sparas med äldre verktyg bör du välja AutoShow-inställningarna. För moderna arbetsböcker bör du i stället välja `FilterTop10`, eftersom filtret kan kombineras med de andra värdefiltren.
{{% /alert %}}

## **Relaterade artiklar**
- [Gruppera pivotfält i pivottabellen](/cells/sv/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}