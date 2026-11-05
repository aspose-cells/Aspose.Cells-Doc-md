---
title: Lägg till villkorlig formatering i en pivottabell
linktitle: Lägg till villkorlig formatering i en pivottabell
description: Lägg till villkorlig formatering i en pivottabell i Aspose.Cells för Go via C++ – fäst en regel på dataområdet med ApplyTo och ett PivotConditionFormatScopeType‑omfång, eller definiera målet med AddCellArea och PivotAreas, och anslut sedan regler och stilar genom FormatConditions.AddCondition.
keywords: Aspose.Cells, pivottabell, villkorsstyrd formatering, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /sv/go-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Stilarna som beskrivs på föräldrasidan och på syskonsidan är statiska – ett `PivotArea`‑ eller `CellArea`‑område målas en gång och behåller sin stil oavsett vilka värden som finns. Villkorsstyrd formatering är den regelbaserade motsvarigheten – markera varje belopp över 200, skugga de mellersta femtio procenten, eller flagga de lägst rankade objekten – och markeringen följer värdena när pivottabellen beräknas om eller uppdateras.  
I Aspose.Cells finns villkorsstyrd formatering för pivottabeller i samlingen `PivotTable.ConditionalFormats`. Varje post är en `PivotConditionalFormat` som besvarar två frågor oberoende av varandra:
- **Var tillämpas regeln?** Målområdet definieras antingen via `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, vilket speglar omfångsväljaren i Excel‑användargränssnittet, eller via `AddCellArea(CellArea)` och samlingen `PivotAreas`, som namnger området explicit.
- **Vad testar regeln?** En eller flera villkor läggs till i `FormatConditions` med `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, och varje villkor bär sin egen `Style`.

{{% alert color="primary" %}}
Anropa inte `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` eller `FormatConditionCollection.AddArea(CellArea)` på `FormatConditions`‑objektet för ett pivottabell‑villkorsformat. Dessa två överlagringar ärvs från det vanliga kalkylblads‑API‑t för villkorsstyrd formatering och fungerar inte för pivottabeller – cellområdet konverteras aldrig till ett pivot‑område, så begäran ignoreras tyst. Definiera alltid området på själva `PivotConditionalFormat` (`ApplyTo`, `AddCellArea` eller `PivotAreas`) och lägg till regeln med någon av `AddCondition`‑överlagringarna.
{{% /alert %}}

## **Applicera en regel med ett omfång (Excel‑gränssnittet)**
Det första sättet placerar regeln på samma sätt som Excel‑användargränssnittet. En cell i pivottabellen identifieras av sina nollbaserade kalkylbladskoordinater, och ett `PivotConditionFormatScopeType`‑omfång talar om för Aspose.Cells hur långt regeln ska sträcka sig från den cellen:
- `PivotConditionFormatScopeType.Data` – alla värdeceller som pivottabellen producerar, inklusive totalsummor.
- `PivotConditionFormatScopeType.Field` – de värdeceller som tillhör det fält som cellen identifierar, exklusive totalsummor. Cellen måste vara en fältcell, till exempel en radfältsetikett; att skicka in en värdecell resulterar i ett undantag.
- `PivotConditionFormatScopeType.Selection` – endast de värdeceller som finns i skärningspunkten som cellen väljer, vanligtvis en enskild värdecell.
Exemplet nedan bygger en pivottabell för fruktförsäljning där det övre vänstra hörnet är på E3, fäster en villkorsstyrd formatering på cell F4 (rad 3, kolumn 5) med `Data`‑omfånget, och markerar varje belopp som är större än 200 med fet vit text på rött. Med värdena Apple 220, Banana 330, Cherry 200 och totalsumman 750 målar regeln F4, F5 och F7 – det utvärderade området är hela datakolumnen F4:F7, och endast de celler vars värde uppfyller regeln lyser upp.

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	a1, _ := cells.Get_String("A1")
	a1.PutValue_String("Fruit")
	b1, _ := cells.Get_String("B1")
	b1.PutValue_String("Year")
	c1, _ := cells.Get_String("C1")
	c1.PutValue_String("Amount")
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	for i := range fruits {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), int32(0))
		fruitCell.PutValue_String(fruits[i])
		yearCell, _ := cells.Get_Int_Int(int32(i+1), int32(1))
		yearCell.PutValue_Int(years[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), int32(2))
		amountCell.PutValue_Int(amounts[i])
	}
	// Pivottabell med dess övre vänstra hörn på E3
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Fäst det villkorsstyrda formatet på F4 (rad 3, kolumn 5) med Data‑omfånget
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	format.ApplyTo(int32(3), int32(5), PivotConditionFormatScopeType_Data)
	// Regel – markera belopp större än 200
	formatConditions, _ := format.GetFormatConditions()
	conditionIndex, _ := formatConditions.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_GreaterThan,
		"200",
		"",
	)
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	font.SetIsBold(true)
	white, _ := Color_FromArgb(int32(-1))
	red, _ := Color_FromArgb(int32(-65536))
	font.SetColor(white)
	style.SetForegroundColor(red)
	style.SetPattern(BackgroundType_Solid)
	condition, _ := formatConditions.Get(conditionIndex)
	condition.SetStyle(style)
	workbook.Save_String("PivotConditionalFormatData.xlsx")
}
```

Om samma regel fästs på rad‑fältetiketten E4 (rad 3, kolumn 4) med `Field`‑omfånget, löser den till F4:F6 istället – samma datakolumn utan totalsummoraden – eftersom omfånget nu beskriver fältet `Fruit` snarare än hela värdeområdet. `Selection`‑omfånget som fästs på F4 löser sig till endast F4.

## **Definiera området manuellt**
Det andra sättet hoppar över omfångsväljaren och namnger området explicit på `PivotConditionalFormat`.

### **Ett kalkylbladsrektangel med AddCellArea**
`AddCellArea(CellArea)` registrerar den angivna rektangeln som målet för regeln. Koordinaterna är nollbaserade kalkylbladskoordinater, och området är exakt den levererade rektangeln – ingen expansion till datakolumnen och ingen totalsummelogik. Använd den när de intressanta cellerna är en känd fast rektangel i den aktuella pivottabellens layout.

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Year")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Amount")
	for i := range fruits {
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(0))
		cell.PutValue_String(fruits[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(1))
		cell.PutValue_Int(years[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(2))
		cell.PutValue_Int(amounts[i])
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Måla rektangeln F4:F6 (värdecellerna utan totalen)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	area, _ := NewCellArea()
	area.Set_StartRow(3)
	area.Set_EndRow(5)
	area.Set_StartColumn(5)
	area.Set_EndColumn(5)
	format.AddCellArea(area)
	// Regel – kursiv på ljusgul för belopp mellan 150 och 300
	formatConditions, _ := format.GetFormatConditions()
	conditionIndex, _ := formatConditions.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_Between,
		"150",
		"300",
	)
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	font.SetIsItalic(true)
	lightYellow, _ := Color_FromArgb(int32(0xFFFFE0))
	style.SetForegroundColor(lightYellow)
	style.SetPattern(BackgroundType_Solid)
	condition, _ := formatConditions.Get(conditionIndex)
	condition.SetStyle(style)
	workbook.Save_String("PivotConditionalFormatCellArea.xlsx")
}
```

### **Ett semantiskt pivot‑område med PivotAreas**
`PivotAreas` är samma semantiska‑områdesmodell som syskonsidan använder för statiska stilar. Bygg ett `PivotArea`, välj ett fält eller område med `Select` eller `SelectField`, och lägg till det med `PivotAreas.AddPivotArea(PivotArea)`. Ett semantiskt område förblir kopplat till sitt fält, så den villkorsstyrda formateringen följer fältet när pivottabellen uppdateras och layouten förändras. `PivotAreas.Add(PivotArea)`‑överlagringen kompilerar fortfarande men är markerad som föråldrad – föredra `AddPivotArea`.

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Skapa en ny arbetsbok
	workbook, _ := NewWorkbook()
	// Hämta det första kalkylbladet
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	// Hämta cellsamlingen
	cells, _ := sheet.GetCells()
	// Dataarrayer
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	// Skriv rubriker
	cellA1, _ := cells.Get_String("A1")
	cellA1.PutValue_String("Fruit")
	cellB1, _ := cells.Get_String("B1")
	cellB1.PutValue_String("Year")
	cellC1, _ := cells.Get_String("C1")
	cellC1.PutValue_String("Amount")
	// Skriv datarader
	for i := 0; i < len(fruits); i++ {
		row := int32(i + 1)
		c0, _ := cells.Get_Int_Int(row, 0)
		c0.PutValue_String(fruits[i])
		c1, _ := cells.Get_Int_Int(row, 1)
		c1.PutValue_Int(years[i])
		c2, _ := cells.Get_Int_Int(row, 2)
		c2.PutValue_Int(amounts[i])
	}
	// Skapa pivottabell
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	// Lägg till fält i pivottabellen
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Fäst villkorsformat på Amount‑datafältet
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	cfIdx, _ := conditionalFormats.Add()
	condFormat, _ := conditionalFormats.Get(cfIdx)
	// Definiera pivotområdet som täcker Amount‑datafältet
	area, _ := NewPivotArea(pivotTable)
	area.SelectField_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotAreas, _ := condFormat.GetPivotAreas()
	pivotAreas.AddPivotArea(area)
	// Lägg till ett villkor: grå text för mängder under 150
	formatConds, _ := condFormat.GetFormatConditions()
	condIdx, _ := formatConds.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_LessThan,
		"150",
		"", // null andra formeln
	)
	// Skapa stil med grå teckensnittsfärg
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	grayColor, _ := Color_Gray()
	font.SetColor(grayColor)
	// Tillämpa stil på villkoret
	cond, _ := formatConds.Get(condIdx)
	cond.SetStyle(style)
	// Spara arbetsboken
	_ = workbook.Save_String("PivotConditionalFormatPivotArea.xlsx")
	fmt.Println("Workbook saved.")
}
```

## **Var reglerna lagras och hur de överlever en omladdning**
Varje anrop av `ConditionalFormats.Add()` lägger till en `PivotConditionalFormat` i pivottabellen. Villkoren, deras formler och deras stilar sparas med arbetsboken – att öppna filen igen i exemplet nedan visar samma regel med sin typ, operator och formel intakt, och `GetCellAreas()` rapporterar samma områden. Poster som aldrig fick ett villkor tas bort när arbetsboken sparas, på samma sätt som Excel tar bort en villkorsstyrd formatering som saknar regel.

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("PivotConditionalFormatData.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	conditionalFormatCount, _ := conditionalFormats.GetCount()
	fmt.Printf("Conditional formats: %d\n", conditionalFormatCount)
	for i := int32(0); i < conditionalFormatCount; i++ {
		format, _ := conditionalFormats.Get(i)
		formatConditions, _ := format.GetFormatConditions()
		formatConditionCount, _ := formatConditions.GetCount()
		for j := int32(0); j < formatConditionCount; j++ {
			condition, _ := formatConditions.Get(j)
			conditionType, _ := condition.GetType()
			operatorType, _ := condition.GetOperator()
			formula1, _ := condition.GetFormula1()
			conditionTypeName := fmt.Sprintf("%v", conditionType)
			if int32(conditionType) == int32(FormatConditionType_CellValue) {
				conditionTypeName = "CellValue"
			}
			operatorTypeName := fmt.Sprintf("%v", operatorType)
			if int32(operatorType) == int32(OperatorType_GreaterThan) {
				operatorTypeName = "GreaterThan"
			}
			fmt.Printf("Format %d: %s %s formula1=%s\n",
				i, conditionTypeName, operatorTypeName, formula1)
		}
		areas, _ := format.GetCellAreas()
		for _, area := range areas {
			startRow, _ := area.Get_StartRow()
			endRow, _ := area.Get_EndRow()
			startColumn, _ := area.Get_StartColumn()
			endColumn, _ := area.Get_EndColumn()
			fmt.Printf("    rows %d-%d, columns %d-%d\n",
				startRow+1, endRow+1, startColumn+1, endColumn+1)
		}
	}
	// Detta skriver ut:
	// Villkorsformat: 1
	// Format 0: CellValue GreaterThan formula1==200
	//     rader 4-7, kolumner 6-6        (F4:F7, det avklarade dataintervallet)
}
```

## **Relaterade artiklar**
- [Formatera del av en pivottabell](/cells/sv/go-cpp/format-part-of-pivot-table/)
- [Topp 10 Visa eller filtrera i pivottabell](/cells/sv/go-cpp/top-10-show-or-filter-in-pivot-table/)

{{< app/cells/assistant language="go" >}}